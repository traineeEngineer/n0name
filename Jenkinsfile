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

        stage('Process PDFs'){
              steps{
                  sh'''
                   for pdf in pdfs/*.pdf; do
                    echo "Processing: $pdf"
                    python3 pdf_extractor.py "$pdf"
                    done
                  '''
              }
        }     

        stage('Build Image') {
            steps {
                echo 'Build stage - Podman not available in Jenkins container'
                echo 'In production: podman build -t chatbot-app:latest .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy stage - Podman not available in Jenkins container'
                echo 'In production: podman run -d --name chatbot -p 5000:5000 chatbot-app:latest'
            }
        }
    }

    post {
        success {
            echo '✅ CI/CD Pipeline completed successfully!'
        }
        failure {
            echo '❌ Build failed - check logs'
        }
    }
}
