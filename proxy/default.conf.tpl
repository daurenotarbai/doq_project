server {
    listen 8000;
    listen [::]:8000;
    listen 443 ssl;
    ssl_certificate /etc/ssl/certs/private/ssl-bundle.crt;
    ssl_certificate_key /etc/ssl/certs/private/docfinder_kz.key;
    ssl_prefer_server_ciphers on;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }

}