pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'python -m py_compile hi.py' 
                stash(name: 'compiled-results', includes: '*.py*') 
            }
        }
    }
}