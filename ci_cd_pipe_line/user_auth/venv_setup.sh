#!/bin/sh

if [ -d "django_microservice" ] 
then
    cd django_microservice
    git pull origin main
    cd user_auth
else
    git clone https://github.com/shoumitro-cse/django_microservice.git
    cd django_microservice/user_auth
fi

if [ -d "venv" ] 
then
    echo "Python virtual environment exists." 
else
    python3 -m venv venv
fi

cp env.example .env
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
rm -rf static
mv staticfiles static


if [ -d "logs" ] 
then
    echo "Log folder exists." 
else
    mkdir logs
    touch logs/error.log logs/access.log
fi

sudo chmod -R 777 logs
