server {
    listen ${LISTEN_PORT};

    location /static {
        alias /vol/static;
    }
    location ~ /.well-known/acme-challenge {
        allow all;
        root /var/www/html;
    }
    location / {
        rewrite ^ https://$host$request_uri? permanent;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }
}