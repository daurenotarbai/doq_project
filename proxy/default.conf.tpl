server {
    listen 80;
    listen [::]:80;
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

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }

}