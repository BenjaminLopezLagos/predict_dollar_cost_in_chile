pipeline {
    agent any
    environment {
        DOCKER_HUB_KEY = credentials('dockerhub_token')
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup Python Environment') {
            steps {
                sh '''
                   python3 -m venv venv
                   . venv/bin/activate
                   pip install --upgrade pip
                   pip install -r requirements.txt
                '''
            }
        }
        stage('Preprocess Data') {
            steps {
                sh '''
                   . venv/bin/activate
                   python ./model_training/preprocess.py
                '''
            }
        }
        stage('Train Model') {
            steps {
                sh '''
                   . venv/bin/activate
                   python ./model_training/train.py
                '''
            }
        }
        stage('Test Model') {
            steps {
                sh '''
                   . venv/bin/activate
                   python ./model_training/test.py
                '''
            }
        }
        stage('deploy image'){
            steps {
               sh '''
                   docker build -t benjaminlopezlagos/clp_dollar_prediction -f .
                   docker login -u benjaminlopezlagos -p ${DOCKER_HUB_KEY}
                   docker push benjaminlopezlagos/clp_dollar_prediction:latest
                '''
            }
        }
    }
}