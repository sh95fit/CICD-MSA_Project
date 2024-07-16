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
            // 존재 여부 체크
            def directoryExists = sh(script: "ssh ${REMOTE_USER}@${REMOTE_HOST} '[ -d ${REMOTE_PATH} ] && echo true || echo false'", returnStdout: true).trim() == "true"

            if (directoryExists) {
              // 존재하는 경우
              sh """
                ssh -o StrictHostKeyChecking=no ${REMOTE_USER}@${REMOTE_HOST} '
                  cd ${REMOTE_PATH}
                  git fetch CICD_MSA ${BRANCH}
                  git reset --hard CICD_MSA/${BRANCH}
                '
              """
            } else {
              // 비어있는 경우
              sh """
                ssh -o StrictHostKeyChecking=no ${REMOTE_USER}@${REMOTE_HOST} '
                  git clone -b ${BRANCH} ${REPO_URL} ${REMOTE_PATH}
                '
              """
            }
          }
        }
      }
    }
  }
}

// Push 시 Jenkins 동작 테스트
// Git Clone 테스트