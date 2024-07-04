pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') { 
            steps {
                sh 'python -m py_compile hi.py' 
                stash(name: 'compiled-results', includes: '*.py*') 
            }
        }
        stage('Test') {
            steps {
                sh 'py.test --junit-xml test-reports/results.xml test_hi.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Deliver') {
            steps {
                sh "pyinstaller --onefile hi.py"
            }
            post {
                success {
                    archiveArtifacts 'dist/'
                }
            }
        }
    }
}