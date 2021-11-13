pipeline {
    
    agent any 
    
    environment{
        dockerImage = ''
        registry = 'vivek13s/javaapp'
        registryCredential = 'docker_hub'
    }
    
    stages{
        stage('Checkout'){
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Svivek13/13sv']]])        }
            }
        
        stage('Build Dockerimage'){
            steps {
                script{
                    dockerImage =  docker.build registry
                }
            }
        }
        
        stage('uploading Image'){
            steps{
                script{
                    docker.withRegistry('',registryCredential){
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
