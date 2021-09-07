# Maven

### Overview
 - is a build tool used pre-dominently by Java projects
 - prior to this Apache Ant was the tool used mostly
 - it is an opensource tool from Apache
 - Convention over Configuration
      - 80 - 20 Principle

### Installing JDK in CentOS 
```
sudo yum install -y epel-release
sudo yum install java-11-openjdk-devel
```
Test if javac and java works as expected
```
java -version
javac -version
```

### Setting up Maven
```
wget https://dlcdn.apache.org/maven/maven-3/3.8.2/binaries/apache-maven-3.8.2-bin.tar.gz
tar xvfz apache-maven-3.8.2-bin.tar.gz
```

#### Set up environments path to access Maven from any directory
You need to edit ~/.bashrc and append the below lines
```
# User specific aliases and functions
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-11.0.12.0.7-0.el8_4.x86_64
export M2_HOME=/home/rps/Downloads/apache-maven-3.8.2
export PATH=$JAVA_HOME/bin:$M2_HOME/bin:$PATH
```
To apply the exports on the current terminal session
```
source ~/.bashrc
```
Try maven version
```
mvn --version
```
The expected output is
<pre>
[jegan@localhost ~]$ mvn --version
Apache Maven 3.8.2 (ea98e05a04480131370aa0c110b8c54cf726c06f)
Maven home: /home/jegan/Downloads/apache-maven-3.8.2
Java version: 11.0.12, vendor: Red Hat, Inc., runtime: /usr/lib/jvm/java-11-openjdk-11.0.12.0.7-0.el8_4.x86_64
Default locale: en_US, platform encoding: UTF-8
OS name: "linux", version: "4.18.0-240.el8.x86_64", arch: "amd64", family: "unix"
[jegan@localhost ~]$ 
</pre>

### Cloning TekTutor training repository
You need to clone if you haven't done it already.  This is done only the first time, moving forward whenever I push code changes to this repository, you just need to pull to get the delta changes.
```
cd ~
git clone https://github.com/tektutor/jenkins-sep-2021.git
```

### Compiling Hello Java application
```
cd ~/jenkins-sep-2021
git pull
cd Day2/Hello
mvn compile
```
Maven compiles includes the below Maven phases
1. mvn compile --> this compiles all the sources kept at src/main/java and its sub-folders

### Compiling Hello Java application and running unit test cases as part of the build
```
cd ~/jenkins-sep-2021
git pull
cd Day2/Hello
mvn test
```
Maven test includes the below major Maven phases
1. mvn compile --> this compiles all source kept at src/main/java and its subfolders
2. mvn testCompile --> this compiles all source kept at src/test/java and its subfolders
3. mvn test --> this execute the compiled test case

### Just in case, you are curious to list all default maven life-cycle phases
```
cd ~/jenkins-sep-2021
git pull
cd Day2/Hello
mvn help:describe -Dcmd=compile
```
The expected output is
<pre>
jegan@localhost Hello]$ mvn help:describe -Dcmd=compile
[INFO] Scanning for projects...
[INFO] 
[INFO] ------------------< org.tektutor:tektutor-hello-app >-------------------
[INFO] Building tektutor-hello-app 1.0.0
[INFO] --------------------------------[ jar ]---------------------------------
[INFO] 
[INFO] --- maven-help-plugin:3.2.0:describe (default-cli) @ tektutor-hello-app ---
[INFO] 'compile' is a phase corresponding to this plugin:
org.apache.maven.plugins:maven-compiler-plugin:3.1:compile

It is a part of the lifecycle for the POM packaging 'jar'. This lifecycle includes the following phases:
* validate: Not defined
* initialize: Not defined
* generate-sources: Not defined
* process-sources: Not defined
* generate-resources: Not defined
* process-resources: org.apache.maven.plugins:maven-resources-plugin:2.6:resources
* compile: org.apache.maven.plugins:maven-compiler-plugin:3.1:compile
* process-classes: Not defined
* generate-test-sources: Not defined
* process-test-sources: Not defined
* generate-test-resources: Not defined
* process-test-resources: org.apache.maven.plugins:maven-resources-plugin:2.6:testResources
* test-compile: org.apache.maven.plugins:maven-compiler-plugin:3.1:testCompile
* process-test-classes: Not defined
* test: org.apache.maven.plugins:maven-surefire-plugin:2.12.4:test
* prepare-package: Not defined
* package: org.apache.maven.plugins:maven-jar-plugin:2.4:jar
* pre-integration-test: Not defined
* integration-test: Not defined
* post-integration-test: Not defined
* verify: Not defined
* install: org.apache.maven.plugins:maven-install-plugin:2.4:install
* deploy: org.apache.maven.plugins:maven-deploy-plugin:2.7:deploy

[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  0.675 s
[INFO] Finished at: 2021-09-06T23:59:26-07:00
[INFO] ------------------------------------------------------------------------

</pre>

### Building spring-boot java microservice
You can compile and package the microservice as shown below. This will package the microservice in a jar file.
```
cd ~/jenkins-sep-2021
git pull
cd Day2/spring-ms
mvn package
```

### Containerizing the spring-boot microservice 
```
cd ~/jenkins-sep-2021
cd Day2/spring-ms
cp target/*.jar hello.jar
docker build -t tektutor/spring-ms:1.0 .
```
At this point, you should be able to see custom docker image
```
docker images
```
The expected output is
<pre>
[jegan@localhost jenkins-sep-2021]$ docker images
REPOSITORY           TAG       IMAGE ID       CREATED          SIZE
<b>
tektutor/spring-ms   1.0       d05e6c1660df   10 minutes ago   487MB
</b>
ubuntu               16.04     b6f507652425   7 days ago       135MB
hello-world          latest    d1165f221234   6 months ago     13.3kB
openjdk              12        e1e07dfba89c   2 years ago      470MB
</pre>

At work place, you may consider using alpine based docker images as base image.  The reason being, our microservice docker image size is pretty fat(487 MB).  In the microservices world, it is considered to big.

### Let's create a container out of our custom microservice docker image
```
docker run -d --name ms --hostname ms tektutor/spring-ms:1.0
```
You can list the containers to verify if ms container is running
```
docker ps
```
The expected output is
<pre>
[jegan@localhost jenkins-sep-2021]$ docker ps
CONTAINER ID   IMAGE                    COMMAND                CREATED          STATUS          PORTS     NAMES
<b>
0a1ecb950650   tektutor/spring-ms:1.0   "java -jar /app.jar"   10 minutes ago   Up 10 minutes             ms
</b>
</pre>

### Find the IP Address of the container and access the microservice from command line and web browser
```
docker inspect ms | grep IPA
curl http://172.17.0.2:8080
```
The expected output is
<pre>
[jegan@localhost jenkins-sep-2021]$ docker inspect ms | grep IPA
            "SecondaryIPAddresses": null,
            "IPAddress": "172.17.0.2",
                    "IPAMConfig": null,
                    "IPAddress": "172.17.0.2",
[jegan@localhost jenkins-sep-2021]$ curl http://172.17.0.2:8080
<b>
Greetings from Spring Boot!
</b>
</pre>

You may also access the web page from your favourite web browser on the lab machine
http://172.17.0.2:8080
