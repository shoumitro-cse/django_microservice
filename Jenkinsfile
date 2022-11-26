pipeline {
    agent any
    stages {
         stage('Setup user_auth microservice'){
            steps {
                sh '''
                    git clone https://github.com/shoumitro-cse/django_microservice.git
                    
                    #git pull
                    #git config --global --add safe.directory /var/lib/jenkins/workspace/ci_cd/django_microservice
                    
                    cd django_microservice/user_auth
                    chmod +x /var/lib/jenkins/workspace/ci_cd/django_microservice/user_auth/project_setup/venv_setup.sh
                    /var/lib/jenkins/workspace/ci_cd/django_microservice/user_auth/project_setup/venv_setup.sh
                    
                    chmod +x /var/lib/jenkins/workspace/ci_cd/django_microservice/user_auth/project_setup/gunicorn.sh
                    /var/lib/jenkins/workspace/ci_cd/django_microservice/user_auth/project_setup/gunicorn.sh
                    
                    chmod +x /var/lib/jenkins/workspace/ci_cd/django_microservice/user_auth/project_setup/nginx.sh
                    /var/lib/jenkins/workspace/ci_cd/django_microservice/user_auth/project_setup/nginx.sh
                '''
            }
        }
        stage('Setup business microservice'){
            steps {
                sh '''
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
                '''
            }
        }
    }
}
