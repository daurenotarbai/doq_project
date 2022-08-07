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

    ssl_certificate /etc/letsencrypt/live/onmenu.site/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/onmenu.site/privkey.pem;

    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }

}