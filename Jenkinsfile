pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/traineeEngineer/n0name.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python -m pytest tests/ --verbose'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t chatbot-app:latest .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker stop chatbot || true
                    docker rm chatbot || true
                    docker run -d --name chatbot -p 5000:5000 chatbot-app:latest
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Chatbot deployed at http://localhost:5000'
        }
        failure {
            echo '❌ Build failed - check logs'
        }
    }
}
