pipeline {
    agent any
    stages {
         stage('Setup user_auth microservice'){
            steps {
                sh '''
                    #whoami
                    if [ -d "django_microservice" ] 
                    then
                        cd ./django_microservice
                        git pull origin main
                        cd ./user_auth
                    else
                        git clone https://github.com/shoumitro-cse/django_microservice.git
                        cd ./django_microservice/user_auth
                    fi
                    
                    if [ -e .env ]
                    then
                        rm .env
                    else
                        echo "nok"
                    fi
                    cp env_docker.example .env
                    docker start rabbitmq 
                    docker-compose up -d --build
                    #docker-compose exec -it  user_auth_backend_1 python manage.py makemigrations
                    #docker exec -it user_auth_backend_1 python /app/manage.py makemigrations
                    docker start user_auth_backend_1 
                    docker exec -u root user_auth_backend_1 python /app/manage.py makemigrations
                '''
            }
        }
        stage('Setup business microservice'){
            steps {
                sh '''
                    if [ -d "django_microservice" ] 
                    then
                        cd ./django_microservice
                        git pull origin main
                        cd ./user_auth
                    else
                        git clone https://github.com/shoumitro-cse/django_microservice.git
                        cd ./django_microservice/user_auth
                    fi
                    
                    if [ -e .env ]
                    then
                        rm .env
                    else
                        echo "nok"
                    fi
                    cp env_docker.example .env
                    docker start rabbitmq 
                    docker-compose up -d --build
                    #docker-compose exec -it  business_backend_1 python manage.py makemigrations
                    #docker exec -it business_backend_1 python /app/manage.py makemigrations
                    docker start business_backend_1 
                    docker exec -u root business_backend_1 python /app/manage.py makemigrations
                '''
            }
        }
    }
}
