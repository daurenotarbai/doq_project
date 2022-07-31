server {
    listen ${LISTEN_PORT} ssl;

    ssl                         on;
    ssl_certificate             /doq_project/certificate/certificate.crt;
    ssl_certificate_key         /doq_project/certificate/private.key;

    server_name                 onmenu.site;
    access_log                  /var/log/nginx/nginx.vhost.access.log;
    error_log                   /var/log/nginx/nginx.vhost.error.log;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
        root                    /home/www/public_html/onmenu.site/public/;
        index                   index.html;
    }
}