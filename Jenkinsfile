pipeline {
    agent any

    environment {
        AWS_REGION = 'eu-west-2'
        AWS_ACCOUNT_ID = '664047078509'
        ECR_REPO = 'lina-jay-weather-app'
        IMAGE_TAG = 'latest'
    }

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
                    sh 'docker build --platform linux/amd64 -t $ECR_REPO:$IMAGE_TAG .'
                }
            }
        }

        stage('Check AWS access') {
            steps {
                sh 'aws sts get-caller-identity'
            }
        }

        stage('Login to ECR') {
            steps {
                sh '''
                aws ecr get-login-password --region $AWS_REGION | \
                docker login --username AWS --password-stdin \
                $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
                '''
            }
        }

        stage('Tag image for ECR') {
            steps {
                sh '''
                docker tag $ECR_REPO:$IMAGE_TAG \
                $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO:$IMAGE_TAG
                '''
            }
        }

        stage('Push image to ECR') {
            steps {
                sh '''
                docker push \
                $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO:$IMAGE_TAG
                '''
            }
        }

        stage('Deploy Lambda') {
            steps {
                dir('backend') {
                    sh '''
                    rm -f function.zip
                    zip function.zip lambda_function.py
                    aws lambda update-function-code \
                    --function-name lina-jay-weather-lambda \
                    --zip-file fileb://function.zip \
                    --region $AWS_REGION
                    '''
                }
            }
        }

        stage('Deploy to ECS') {
            steps {
                sh '''
                aws ecs update-service \
                --cluster lina-jay-weather-app-ecs \
                --service lina-jay-weather-app-task-service-423ul5x4 \
                --force-new-deployment \
                --region $AWS_REGION
                '''
            }
        }
    }
}