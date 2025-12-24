pipeline {
    agent any

    stages {
        stage('Setup Venv') {
            steps {
                echo "Building branch: ${env.BRANCH_NAME}"
                // Create venv and install requirements
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo "Running Tests..."
                // Must activate venv again because each 'sh' block is a new shell
                sh '''
                    . venv/bin/activate
                    pytest test_app.py
                '''
            }
        }

        stage('Deploy (Main Only)') {
            // Only runs if the branch is 'main'
            when {
                branch 'main'
            }
            steps {
                echo ">>> Deploying Production Build..."
                // Example of running a script using the venv
                sh """
                    . venv/bin/activate
                    echo "Deploying version for ${env.BRANCH_NAME}"
                """
            }
        }
    }
    
    post {
        always {
            // Good practice: Clean up the workspace to save disk space
            cleanWs()
        }
    }
}