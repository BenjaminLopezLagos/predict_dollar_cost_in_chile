pipeline {
    agent any
    environment {
        DH_S3_KEY = credentials('dagshub_token')
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
                   python ./movel_training/preprocess.py
                '''
            }
        }
        stage('Train Model') {
            steps {
                sh '''
                   . venv/bin/activate
                   python ./movel_training/train.py
                '''
            }
        }
        stage('Test Model') {
            steps {
                sh '''
                   . venv/bin/activate
                   python ./movel_training/test.py
                '''
            }
        }
        stage('Deploy Model') {
            steps {
                sh '''
                    ls
                '''
            }
        }
    }
}