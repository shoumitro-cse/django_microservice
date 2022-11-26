#!/bin/sh

sudo cp -rf user_auth_nginx.conf /etc/nginx/conf.d
sudo usermod -a -G shoumitro nginx
chmod 710 /var/lib/jenkins/workspace/ci_cd/django_microservice/user_auth
sudo nginx -t
sudo systemctl reload nginx
sudo systemctl restart nginx
sudo systemctl status nginx
