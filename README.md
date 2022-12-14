## User Business Microservice
A user_auth and business microservice application have been built using Python, JWT Token, 
Rabbitmq, Django, Django rest framework, and drf_spectacular package for API docs. 
where the user_auth application can do to handle new user register and can manage 
permission for different service of business application.


## Installation of Rabbitmq
```
docker run --restart=always -d -e RABBITMQ_NODENAME=rabbitmq -v /opt/docker/rabbitmq/data:/var/lib/rabbitmq/mnesia/rabbitmq -p 5672:5672 -p 15672:15672 -e RABBITMQ_DEFAULT_USER=root -e RABBITMQ_DEFAULT_PASS=1234 --name rabbitmq rabbitmq:management
```

## Installation of user_auth service(Docker)
```
git clone https://github.com/shoumitro-cse/django_microservice.git
cd django_microservice/user_auth
cp env_docker.example .env
docker-compose up --build
docker exec -it user_auth_backend_1 bash
python manage.py makemigrations
python manage.py migrate
```

## Installation of user_auth service
```
git clone https://github.com/shoumitro-cse/django_microservice.git
cd django_microservice/user_auth
cp env.example .env
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
rm -rf static
mv staticfiles static
python manage.py runserver localhost:8001
```

## Installation of business application(Docker)
```
git clone https://github.com/shoumitro-cse/django_microservice.git
cd django_microservice/business
cp env_docker.example .env
docker-compose up --build
docker exec -it business_backend_1 bash
python manage.py makemigrations
python manage.py migrate
```

## Installation of business service
```
git clone https://github.com/shoumitro-cse/django_microservice.git
cd django_microservice/business
cp env.example .env
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
rm -rf static
mv staticfiles static
python manage.py runserver localhost:7000
```

## API docs

```
Here, It has been used as a drf_spectacular package for API docs, I think that it will be 
very helpful for frontend developers. If you would like to see special instructions for 
each api, please keep your eye on each API doc.
protocol = http, https
domain = localhost or others
port = 80, 8000 etc
{protocol}://{domain}:{port}/api/docs/ (for API HTTP methods and descriptions)
{protocol}://{domain}:{port}/api/redocs/
{protocol}://{domain}:{port}/api/schema/ (for download API ymal file)
```

![](https://github.com/shoumitro-cse/django_microservice/blob/main/docs/user_auth.png)
![](https://github.com/shoumitro-cse/django_microservice/blob/main/docs/business.png)


## Jenkins docker ownership and Then restart Jenkins.

````
chown jenkins:docker /var/run/docker.sock
sudo usermod -a -G docker jenkins
sudo systemctl restart jenkins

[shoumitro@shoumitro-pc ~]$ grep docker /etc/group
docker:x:965:shoumitro,jenkins
```

