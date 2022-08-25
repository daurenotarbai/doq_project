#!/bin/sh

set -e

envsubst '\$WP \$PMA' < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf
nginx -g "daemon off;"