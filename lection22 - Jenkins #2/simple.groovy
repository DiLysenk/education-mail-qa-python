properties([disableConcurrentBuilds()])

pipeline {
    agent {
        label 'master'
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '3'))
        timestamps()
    }

    environment {
        PYTHON = "/Library/Frameworks/Python.framework/Versions/3.8/bin/"
    }

    stages {

        stage("Build") {
            steps {
                echo 'building..'
                echo 'build done!'
            }
        }

        stage("Testing") {
            steps {
                withEnv(["PATH+EXTRA=$PYTHON"]) {
                    sh 'cd code_pipeline'
                    dir('code_pipeline') {
                        sh "pytest -s -l -v test.py --alluredir=$WORKSPACE/alluredir"
                    }
                }
            }
        }
    }

    post {
        always {
            allure([
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'alluredir']]
            ])
            cleanWs()
        }
    }
}
