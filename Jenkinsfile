pipeline {
  agent any

  environment {
    REPO_URL = "https://github.com/sh95fit/CICD-MSA_Project"
    BRANCH = "main"
    REMOTE_PATH = "/home/cicd"
    SSH_CREDENTIALS_ID = "cicd"
    REMOTE_USER = "cicd"
    REMOTE_HOST = "152.70.90.174"
  }

  stages {
    stage('Checkout') {
      steps {
        git branch: 'main',
          credentialsId: 'sh95fit',
          url: 'https://github.com/sh95fit/CICD-MSA_Project.git'
      }
    }

    stage('Clone Repository') {
      steps {
        script {
          sshagent (credentials: [SSH_CREDENTIALS_ID]) {
              sh """
              ssh -o StrictHostKeyChecking=no ${REMOTE_USER}@${REMOTE_HOST} '
                  rm -rf ${REMOTE_PATH}/* || exit 1
                  git clone -b ${BRANCH} ${REPO_URL} ${REMOTE_PATH} || exit 1
              '
              """
          }
        }
      }
    }
  }
}

// Push 시 Jenkins 동작 테스트
// Git Clone 테스트