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

    location /adminn {
        proxy_pass https://doq.kz;
        proxy_set_header   Host             medicne-admin.vercel.app;
        proxy_set_header   X-Real-IP        \$remote_addr;
        proxy_set_header   X-Forwarded-For  \$proxy_add_x_forwarded_for;
    }
}