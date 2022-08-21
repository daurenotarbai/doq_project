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

    location /admin {
        proxy_set_header X-Forwarded-Host $host;
        proxy_set_header X-Forwarded-Server $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass http://localhost:81/api/admin;
    }

}