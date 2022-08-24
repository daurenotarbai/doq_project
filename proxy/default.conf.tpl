# the IP(s) on which your node server is running. I chose port 3000.
upstream admin_upstream{
    server 127.0.0.1:3001;
}

upstream app_back{
    server 127.0.0.1:9000;
}

#Point http requests to https
server {
    listen 0.0.0.0:80;
    server_name docfinder.kz;
    server_tokens off;
    return 301 https://$host$request_uri;
}

# the secure nginx server instance
server {
    listen 443 ssl;
    server_name  docfinder.kz;
    ssl_certificate /etc/ssl/certs/ssl-bundle.crt;
    ssl_certificate_key /etc/ssl/certs/docfinder_kz.key;
    ssl_prefer_server_ciphers on;
    # pass the request to the node.js server with the correct headers and much more can be added, see nginx config options

    location /favicon.ico { alias /home/ubuntu/img/favicon_rc.ico; }

    location / {
      # auth_basic "Restricted";
      # auth_basic_user_file /home/ubuntu/app/.htpasswd;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header Host $http_host;
      proxy_set_header X-NginX-Proxy true;
      proxy_set_header X-Ssl on;

      proxy_pass https://admin_upstream;
      proxy_redirect off;
    }

    location /static {
        alias /vol/static;
    }

    location /superadmin/ {
      rewrite /superadmin/(.*)$ /$1 break;

      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header Host $http_host;
      proxy_set_header X-NginX-Proxy true;
      proxy_set_header X-Ssl on;

      proxy_pass https://app_back;
      proxy_redirect off;
    }
 }