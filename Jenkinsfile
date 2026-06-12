pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/company/propertyguru-automation.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t propertyguru-automation .'
            }
        }

        stage('Execute Tests') {
            steps {
                sh '''
                docker run --rm \
                -v ${WORKSPACE}/allure-results:/app/allure-results \
                -v ${WORKSPACE}/reports:/app/reports \
                propertyguru-automation
                '''
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
        }
    }
}