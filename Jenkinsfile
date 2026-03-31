pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install frontend dependencies') {
            steps {
                dir('frontend') {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest frontend/tests backend/tests'
            }
        }

        stage('Build frontend image') {
            steps {
                dir('frontend') {
                    sh 'docker build --platform linux/amd64 -t lina-jay-weather-app .'
                }
            }
        }
    }
}