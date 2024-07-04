pipeline {
    agent any 
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
    }
}