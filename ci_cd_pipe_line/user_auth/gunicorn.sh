#!/bin/sh

source venv/bin/activate
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
sudo cp -rf user_auth_gunicorn.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start user_auth_gunicorn
echo "Gunicorn has started."
sudo systemctl enable user_auth_gunicorn
echo "Gunicorn has been enabled."
sudo systemctl status user_auth_gunicorn
sudo systemctl restart user_auth_gunicorn
