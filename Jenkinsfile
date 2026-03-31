pipeline {
    agent any

    stages {

        stage('Set up Python') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
            }
        }

        stage('Install frontend dependencies') {
            steps {
                dir('frontend') {
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }

        stage('Install test dependencies') {
            steps {
                sh 'pip3 install pytest'
            }
        }

        stage('Run frontend tests') {
            steps {
                sh 'python3 -m pytest frontend/tests'
            }
        }

        stage('Run backend tests') {
            steps {
                sh 'python3 -m pytest backend/tests'
            }
        }

        stage('Build frontend image') {
            steps {
                dir('frontend') {
                    sh 'docker build --platform linux/amd64 -t lina-jay-weather-app .'
                }
            }
        }

        stage('Check AWS access') {
            steps {
                sh 'aws sts get-caller-identity'
            }
        }
    }
}