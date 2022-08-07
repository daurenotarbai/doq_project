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