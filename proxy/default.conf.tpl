server {
    listen 8000;
    listen [::]:8000;
    server_name onmenu.site;
    location ~ /.well-known/acme-challenge {
        allow all;
        root /var/www/html;
    }

    location / {
        rewrite https://$host$request_uri? permanent;
    }

}

server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name onmenu.site;

    root /var/www/html;

    server_tokens off;

    ssl_certificate /etc/letsencrypt/live/onmenu.site/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/onmenu.site/privkey.pem;

    include /etc/nginx/conf.d/options-ssl-nginx.conf;

    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;
    add_header Content-Security-Policy "default-src * data: 'unsafe-eval' 'unsafe-inline'" always;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }

}