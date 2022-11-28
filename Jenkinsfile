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
                    {
                        docker stop pg_db user_auth_queue_1 user_auth_backend_1
                        docker rm pg_db user_auth_queue_1 user_auth_backend_1
                    } || {}
                    docker-compose up -d --build
                    docker start rabbitmq pg_db user_auth_queue_1 user_auth_backend_1
                    docker exec -u root user_auth_backend_1 python /app/manage.py makemigrations
                    docker exec -u root user_auth_backend_1 python /app/manage.py migrate
                '''
            }
        }
        stage('Setup business microservice'){
            steps {
                sh '''
                    cd business
                    pwd
                    cp env_docker.example .env
                    {
                        docker stop p_db business_queue_1 business_backend_1
                        docker rm p_db business_queue_1 business_backend_1
                    } || {}
                    docker-compose up -d --build
                    docker start rabbitmq p_db business_queue_1 business_backend_1
                    docker exec -u root business_backend_1 python /app/manage.py makemigrations
                    docker exec -u root user_auth_backend_1 python /app/manage.py migrate
                '''
            }
        }
    }
}
