upstream client_upstream {
    server 185.146.1.69:83;
}

upstream admin_upstream {
    server 185.146.1.69:82;
}

upstream app_back {
    server 185.146.1.69:81;
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
    server_name docfinder.kz;
    ssl_certificate /etc/ssl/certs/ssl-bundle.crt;
    ssl_certificate_key /etc/ssl/certs/docfinder_kz.key;
    ssl_prefer_server_ciphers on;
    # pass the request to the node.js server with the correct headers and much more can be added, see nginx config options

    location / {
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header Host $http_host;
      proxy_set_header X-NginX-Proxy true;
      proxy_set_header X-Ssl on;
      proxy_pass https://client_upstream;
    }
}
server {
    listen 80;
    listen [::]:80;
    root /var/www;
    server_name admin.docfinder.kz;

    location / {
      proxy_pass http://admin_upstream;
    }
}
server {
    listen 80;
    listen [::]:80;
    root /var/www;
    server_name api.docfinder.kz;

    location / {
      proxy_pass http://app_back;
    }
}