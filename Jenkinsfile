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

    DOCKER_COMPOSE_FILE = 'docker-compose.yml'

    PROJECT_NAME = 'cicd'
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
            def remoteDirExists = sh(script: "ssh ${REMOTE_USER}@${REMOTE_HOST} '[ -d ${REMOTE_PATH} ] && echo true || echo false'", returnStdout: true).trim() == 'true'

            if (remoteDirExists) {
                // .git 파일 존재 유무 체크 함수
                def gitDirExists = sh(script: "ssh ${REMOTE_USER}@${REMOTE_HOST} '[ -d ${REMOTE_PATH}/.git ] && echo true || echo false'", returnStdout: true).trim() == 'true'

                if (gitDirExists) {
                    // .git 파일이 존재하는 경우
                    sh "ssh ${REMOTE_USER}@${REMOTE_HOST} 'cd ${REMOTE_PATH} && git reset --hard HEAD && git pull ${GIT_ORIGIN} main'"
                } else {
                    // .git 파일이 존재하지 않는 경우  git init 후 clone
                    sh "ssh ${REMOTE_USER}@${REMOTE_HOST} 'cd ${REMOTE_PATH} && git init && git branch -M main && git remote add ${GIT_ORIGIN} ${GIT_URL} && git fetch && git checkout ${GIT_ORIGIN}/main -f'"
                }
            } else {
                // Initialize Git repository and clone
                sh "ssh ${REMOTE_USER}@${REMOTE_HOST} 'mkdir -p ${REMOTE_PATH} && cd ${REMOTE_PATH} && git init && git branch -M main && git remote add ${GIT_ORIGIN} ${GIT_URL} && git fetch && git checkout ${GIT_ORIGIN}/main -f'"
            }
          }
        }
      }
    }

    stage('Build with docker-compose') {
      steps {
        script {
          sshagent (credentials: [SSH_CREDENTIALS_ID]) {
            // docker-compose 파일 유무 확인
            def composeFileExists = sh(script: "ssh ${REMOTE_USER}@${REMOTE_HOST} '[ -f ${REMOTE_PATH}/${DOCKER_COMPOSE_FILE} ] && echo true || echo false'", returnStdout: true).trim() == 'true'

            if (composeFileExists) {
              // 동작 중인 컨테이너가 있는지 확인
              def runningContainers = sh(script: "ssh ${REMOTE_USER}@${REMOTE_HOST} 'cd ${REMOTE_PATH} && docker-compose ps -q'", returnStatus: true)

              if (runningContainers == 1) {
                  echo "Stopping and removing existing docker-compose containers..."
                  // 컨테이너 정지 및 삭제
                  sh "ssh ${REMOTE_USER}@${REMOTE_HOST} 'cd ${REMOTE_PATH} && docker-compose down -v --remove-orphans && docker image rm \$(docker images -q ${PROJECT_NAME}-* | uniq)'"
              } else {
                  echo "No running docker-compose containers found."
              }

              // docker-compose를 빌드하고 시작
              echo "Building and starting new docker-compose containers..."
              sh "ssh ${REMOTE_USER}@${REMOTE_HOST} 'cd ${REMOTE_PATH} && docker-compose up --build -d'"

            } else {
                  echo "Error: ${DOCKER_COMPOSE_FILE} not found in ${REMOTE_PATH}"
                  currentBuild.result = 'FAILURE'
                  error "docker-compose file not found"
              }
          }
        }
      }
    }
  }
}

// Push 시 Jenkins 동작 테스트
// Git Clone 테스트