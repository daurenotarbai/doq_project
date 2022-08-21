server {
    listen 8000;
    listen [::]:8000;
    listen 443 ssl;
    server_name docfinder.kz;
    ssl_certificate_key /home/ubuntu/ssl/private/docfinder.key;



    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }

}