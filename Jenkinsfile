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
          // SSH 원격 접속 및 레포지토리 클론
          sshPublisher(publishers: [
              sshPublisherDesc(
                  configName: SSH_CREDENTIALS_ID,
                  transfers: [
                      sshTransfer(
                          execCommand: """
                              cd ${REMOTE_PATH} || exit 1
                              rm -rf ${REMOTE_PATH}/* || exit 1
                              git clone -b ${BRANCH} ${REPO_URL} ${REMOTE_PATH} || exit 1
                          """,
                          sourceFiles: '',
                          removePrefix: ''
                      )
                  ],
                  usePromotionTimestamp: false,
                  // alwaysPublishFromMaster: true,
                  // failOnError: true  // 전송 중 하나라도 실패 시 전체 실패
              )
          ])
        }
      }
    }
  }
}

// Push 시 Jenkins 동작 테스트
// Git Clone 테스트