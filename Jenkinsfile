pipeline {
  agent any

  environment {
    REPO_URL = "https://github.com/sh95fit/CICD-MSA_Project"
    BRANCH = "main"
    REMOTE_PATH = "/home/cicd"
    SSH_CREDENTIALS_ID = "cicd"
    REMOTE_USER = "cicd"
    REMOTE_HOST = "152.70.90.174"
    GIT_ORIGIN = "CICD_MSA"
    GIT_URL = "https://github.com/sh95fit/CICD-MSA_Project.git"
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

            // // [성공 스크립트]
            // // 존재 여부 체크
            // def directoryExists = sh(script: "ssh ${REMOTE_USER}@${REMOTE_HOST} '[ -d ${REMOTE_PATH} ] && echo true || echo false'", returnStdout: true).trim() == "true"

            // if (directoryExists) {
            //   // 존재하는 경우
            //   sh """
            //     ssh -o StrictHostKeyChecking=no ${REMOTE_USER}@${REMOTE_HOST} '
            //       cd ${REMOTE_PATH}
            //       git fetch CICD_MSA ${BRANCH}
            //       git reset --hard CICD_MSA/${BRANCH}
            //     '
            //   """
            // } else {
            //   // 비어있는 경우
            //   sh """
            //     ssh -o StrictHostKeyChecking=no ${REMOTE_USER}@${REMOTE_HOST} '
            //       git clone -b ${BRANCH} ${REPO_URL} ${REMOTE_PATH}
            //     '
            //   """
            // }

            // Check if the directory exists on remote
            def remoteDirExists = sshCommand(
                remote: REMOTE_HOST,
                user: REMOTE_USER,
                command: "[ -d '${REMOTE_PATH}' ] && echo 'true' || echo 'false'"
            ).trim() == 'true'

            if (remoteDirExists) {
                // Check if .git directory exists within REMOTE_PATH
                def gitDirExists = sshCommand(
                    remote: REMOTE_HOST,
                    user: REMOTE_USER,
                    command: "[ -d '${REMOTE_PATH}/.git' ] && echo 'true' || echo 'false'"
                ).trim() == 'true'

                if (gitDirExists) {
                    // Perform git reset to update repository
                    sshCommand(
                        remote: REMOTE_HOST,
                        user: REMOTE_USER,
                        command: "cd '${REMOTE_PATH}' && git reset --hard HEAD"
                    )
                } else {
                    // Initialize Git repository and clone
                    sshCommand(
                        remote: REMOTE_HOST,
                        user: REMOTE_USER,
                        command: "cd '${REMOTE_PATH}' && git init && git branch -M main && git remote add '${GIT_ORIGIN} '${GIT_URL}' && git fetch && git checkout '${GIT_ORIGIN}'/main -f"
                    )
                }
            } else {
                // Initialize Git repository and clone
                sshCommand(
                    remote: REMOTE_HOST,
                    user: REMOTE_USER,
                    command: "mkdir -p '${REMOTE_PATH}' && cd '${REMOTE_PATH}' && git init && git branch -M main && git remote add '${GIT_ORIGIN} '${GIT_URL}' && git fetch && git checkout '${GIT_ORIGIN}'/main -f"
                )
            }


          }
        }
      }
    }
  }
}

// Push 시 Jenkins 동작 테스트
// Git Clone 테스트