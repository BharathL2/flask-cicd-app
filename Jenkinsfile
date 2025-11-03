pipeline {
    agent any

        environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-login')
        IMAGE_NAME = "bharathl2/flask-cicd-app"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/BharathL2/flask-cicd-app'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Run Container for Testing') {
            steps {
                sh 'docker run -d -p 5000:5000 --name test_container $IMAGE_NAME:latest'
                sh 'sleep 5'
                sh 'curl -f http://localhost:5000 || (echo "Test failed" && exit 1)'
                sh 'docker stop test_container && docker rm test_container'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([ credentialsId: 'dockerhub' ]) {
                    sh 'docker push $IMAGE_NAME:latest'
                }
            }
        }

        stage('Deploy (Optional)') {
            steps {
                echo 'Deploying container to local or remote server...'
            }
        }
    }
}
