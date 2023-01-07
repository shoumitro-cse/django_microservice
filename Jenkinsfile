pipeline {
    agent any
    
    stages {
        
        stage('Cleanup Workspace') {
            steps {
                cleanWs()
                sh """
                echo "Cleaned Up Workspace for django_microservice"
                """
            }
        }
        
        stage('Code Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM', 
                    branches: [[name: '*/main']], 
                    userRemoteConfigs: [[url: 'https://github.com/shoumitro-cse/django_microservice.git']]
                ])
            }
        }
        
         stage('Setup user_auth microservice'){
            steps {
                sh '''
                    cd user_auth
                    pwd
                    cp env_docker.example .env
                    
                    docker stop user_auth_backend user_auth_queue user_auth_db
                    docker rm user_auth_backend user_auth_queue user_auth_db
                    docker-compose up -d --build
                    docker start user_auth_db user_auth_backend user_auth_queue 
                    
                    whoami
                    docker exec -u root user_auth_backend python /app/manage.py makemigrations
                    docker exec -u root user_auth_backend python /app/manage.py migrate
                '''
            }
        }
        stage('Setup business microservice'){
            steps {
                sh '''
                    cd business
                    pwd
                    cp env_docker.example .env
                    docker-compose up -d --build
                    docker start business_backend business_queue business_db
                    docker exec -u root business_backend python /app/manage.py makemigrations
                    docker exec -u root business_backend python /app/manage.py migrate
                '''
            }
        }
    }
}
