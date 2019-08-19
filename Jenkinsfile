#!/usr/bin/env groovy
import java.net.URL
node{
    stage('Git Checkout'){
        git'https://github.com/edureka-git/DevOpsClassCodes.git'
    }
    stage('AB Compile'){
        withMaven(maven:'SreehariMaven'){
            sh 'mvn compile'
        }
    }
    stage('AB Package'){
        withMaven(maven:'SreehariMaven'){
            sh 'mvn package'
        }
    }
}
