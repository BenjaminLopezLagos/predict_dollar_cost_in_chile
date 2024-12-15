pipeline {
    agent any
    /*
    environment {
        DH_S3_KEY = credentials('dagshub_token')
        DOCKER_HUB_KEY = credentials('dockerhub_token')
    }
    */
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
        stage('Extract Data') {
            steps {
                sh '''
                   . venv/bin/activate
                   python ./model_training/data_extraction/scripts/extract_historic_data.py /var/jenkins_home/workspace/model_pipeline/model_training/data_extraction/scripts 
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
        stage('Deploy Model') {
            steps {
                sh '''
                    ls
                '''
            }
        }
    }
}