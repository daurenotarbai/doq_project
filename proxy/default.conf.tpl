server {
    listen 81;
    listen 443 ssl;
    server_name docfinder.kz;
    ssl_certificate_key /home/ubuntu/ssl/private/docfinder.key;

    location /static {
        alias /vol/static;
        }

    location / {
        proxy_pass http://docfinder.kz;
        proxy_set_header Host \$host:$server_port;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}