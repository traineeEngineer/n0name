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
                sh 'pip3 install --break-system-packages -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest tests/ --verbose'
            }
        }

        stage('Build Image with Podman') {
            steps {
                sh 'podman build -t chatbot-app:latest .'
            }
        }

        stage('Deploy with Podman') {
            steps {
                sh 'podman stop chatbot || true'
                sh 'podman rm chatbot || true'
                sh 'podman run -d --name chatbot -p 5000:5000 chatbot-app:latest'
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
