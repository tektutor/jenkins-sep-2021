# Maven

### Overview
 - is a build tool used pre-dominently by Java projects, however it's language agnostic build tool.
 - prior to this Apache Ant was the tool used mostly for Java projects
 - Ant doesn't have any standards, hence different teams use different project folder conventions which leads
   to confusions.
 - Ant doesn't have dependency management support, hence it is our responsibility to downloads third-party library
   jars, place them in respective folders and we need to take care of classpaths.
 - pretty much all the above issues are resolved by Maven, hence Maven is a better build tool
 - Maven is an opensource tool from Apache
 - Maven Convention over Configuration
      - 80 - 20 Principle
      - most common use-cases doesn't require any configuration when we strictly follow Maven's convention
      - but when you can't follow Maven's convention, let's say a legacy project that currently uses Ant as a build
        tool may not be inline with Maven's convention.  In such cases, you may configure Maven to pick 
        application and test source code from your preffered folders.
 - Maven supports 3 in-built lifecycle's
     1. default (23 Phases)
     2. clean   (3 Phases)
     3. site    (4 Phases)

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
1. mvn compile --> this compiles all the source code kept at src/main/java and its sub-folders

### Compiling Hello Java application and running unit test cases as part of the build
```
cd ~/jenkins-sep-2021
git pull
cd Day2/Hello
mvn test
```
Maven test includes the below major Maven phases
1. mvn compile --> this compiles all source code kept at src/main/java and its subfolders
2. mvn testCompile --> this compiles all source code kept at src/test/java and its subfolders
3. mvn test --> this executes the compiled test cases

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

### You may list all clean maven life-cycle phases
```
cd ~/jenkins-sep-2021
git pull
cd Day2/Hello
mvn help:describe -Dcmd=clean
```

### You may list all site maven life-cycle phases
```
cd ~/jenkins-sep-2021
git pull
cd Day2/Hello
mvn help:describe -Dcmd=site
```

### You may list all goals maven plugin supports as shown below
```
cd ~/jenkins-sep-2021
git pull
cd Day2/Hello
mvn help:describe -Dplugin=org.apache.maven.plugins:maven-compiler-plugin:3.1 -Ddetail
```

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
At this point, you should be able to see your custom docker image
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

At work place, you may consider using alpine based docker images as base image for your custom Docker images.  The reason being, our microservice docker image size is pretty fat(487 MB).  In the microservices world, it is considered too big.

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

# Jenkins

## Agile Methodology
  - Fail-fast Project development Methodology
  - In case of Waterfall Framework
      - customer feedback arrives pretty delayed
      - Once in 3 months or 6 months or yearly project/product releases are shared with the customer
      - If evertything goes well i.e requirements captured is inline with customer's expectation there is no issue
      - In case there is a deviation from the requirements captured vs actual customer expectation, 
        then course correction is almost impossible as the effort is already consumed.
        
 - SCRUM/Kanban
     - Agile Frameworks
     - helps in getting frequent customer feedbacks
     - Sprint duration
           - 1 week(5 days) to 4 (20 days) weeks maximum
           - SCRUM ceremonies
                - Daily stand-up meeting
                   - Inspect and Adapt meeting(Fail-fast meeting)
                       1. What was yesterday's plan?
                       2. Were there any obstacles? Some team members can help offline after the meeting.
                       3. What you are planning to do today?
                       
 - What is the equivalent engineering practice to Daily Stand-up meeting?
      - Whenever code commit happens, there should be some tool which detects code commit
        and grabs the latest code, triggers the build, automates testing and then give a build report(feedback)
        to the team including the person who did code commit.
      - Recommended approaches 
          - Test Driven Development (TDD)
          - Behaviour Driven Development (BDD)
          - Domain Driven Development (DDD)
         
    - Continuous Integration
         - Source code should be commited(integrated) to dev branch several times a day by all the team members
         - Whenever the code is logically complete, code must be committed without delay. 
           To develop a complex functionality, assuming you need to develop 10~15 unit level functions. Whenever 
           you completed one unit-level function along with the necessary automated test-cases, you 
           should check-in the code.
         - build failures are seen as a good thing in case build fails due to test case failures.
         - When one or more automated test cases fail, your automated test cases have caught some bugs, 
           which is the reason you are following Continuous Integration.
                 
         - Jenkins (CI Server) (Hudson, Teamcity, Bamboo, Microsoft TFS)
              - a former Sun Microsystems employee by name Kohsuke Kawaguji developed Hudson CI Server
              - was developed using Java but works for any programming language stack
              - Sun Microsystems was acquired by Oracle (led by Larry Ellison)
              - Hudson team got split into two, there were conflicts of interest in the Hudson future 
                strategy after Oracle acquired Sun MicroSystems
              - a part of Hudson team came out of Oracle and they created branch(Jenkins) keeping Hudson code 
                base as baseline
              - Oracle maintains Hudson CI Server, while the Jenkins CI Server is being developed as opensource tool
                by the Kohsuke Kawaguji with more than 10000 active Opensource community contributers.
              - will automatically detect code changes done in Version Control 
                (GitHub,GitLab, BitBucket, Perforce,etc)
              - will get the latest code snapshot from GitHub
              - triggers a Maven/Gradle/Make/MSBuild/etc build
              - runs the automated test cases as part of build
              - sends out an email with Build report to all team members (Feedback)
     
#### Continuous Integration(CI)
     - Source code is frequently integrated several times a day by all the team members
     - any time code is commited, the respective member will also write automated test cases to test his/her
       source code part of code commit
     - CI Servers like Jenkins, automates the build and test process and gives Build Report as feedback
     - Each time code is commited, CI Servers repeats the existing and new Test cases added to verify
       the new functionality and existing functionalities.  This helps in reporting bugs as and when new code
       is committed (fail-fast approach).

#### Continuous Deployment
     - Release binaries are tested automatically in Dev environment and promoted to QA environment for
       further automated test cases added by QA team, which is then promoted to Pre-prod environment to
       further test in a production equivalent environment to certify the release is good to go live or not.
       
#### Continuous Delivery
     - Highest maturity level in DevOps, this is followed by some very big product companies, who are highly confident
       about the quality of automated test-cases added by their team.
     - In this end-2-end build and test is automated all way to deliveries to live production 
       environment automatically.
     - Once the release binaries are certified, the release binaries will be deployed/delivered to the live production
       environment or to the Customer's staging environment to go live any time the customer decides.

#### Setting up Jenkins
```
cd ~/Downloads
wget https://get.jenkins.io/war-stable/2.303.1/jenkins.war
java -jar ./jenkins.war
```
The above command will interactively start jenkins CI server, hence we may have to use different Terminal tabs.

Once you see, Jenkins is fully up and running, you may access Jenkins web page from your web browser at http://localhost:8080

### Let's create a CI/CD pipeline in Jenkins

1. Create a Freestyle Jenkins Job Dashboard --> New Item(Create New Job) --> FreeStyle Job.  Let's call this
   Freestyle Job as "Compile Hello Java Application".
   
   In the SCM (Source Code Management) Section, select "Git" and paste the below GitHub Repository
   https://github.com/tektutor/jenkins-sep-2021.git
   
   In the Build Triggers section, select "Poll SCM" and paste the below to setup poll for every 2 minutes
   H/02 * * * *
   
   In the Build Section, paste the below
   cd Day2/Hello
   mvn compile
   
   Save the Job.
   
 2. Create your second Freestyle Jenkins Job by copying existing "Copy Hello Java Application" and let's call
    this Job as "Test Hello Java Application".
    
    In the Build Triggers section, unselect "Poll SCM" and select "Build after other projects are built" and choose
    "Compile Hello Java Application".
    
    In the Build section, replace "mvn compile" with "mvn test" and Save the Job.
    
 3. Create your third Freestyle Jenkins Job by copying existing "Test Hello Java Application" and let's call this
    Job as "Package Hello Java Application".
    
    In the Build Triggers section, select the "Build after other projects are build" and this time change 
    "Compile Hello Java Application" to "Test Hello Java Application".
    
    In the Build section, replace "mvn test" with "mvn package" and Save the Job.

 4. Create your fourth Freestyle Jenkins Job by copying existing "Package Hello Java Application" and let's call this
    Job as "Install Hello Java Application".
    
    In the Build Triggers section, select the "Build after other projects are build" and this time change
    "Test Hello Java Application" to "Package Hello Java Application".

    In the Build section, replace "mvn package" to "mvn install" and Save the Job.
    
 5. Create your final Freestyle Jenkins Job by copying existing "Install Hello Java Application" and let's call this
    Job as "Deploy Hello Java Application Aritifacts to Artifactory".
    
    In the Build Triggers section, select the "Buid after other projects are build" and this time change 
    "Package Hello Java Application" to "Install Hello Java Application".
    
    In the Build section, replace "mvn install" to "mvn deploy" and Save the Job.

Any source code commit to "jenkins-sep-2021" GitHub repository will automatically trigger the Jenkins CI/CD pipeline you created.

### Setting up JFrog artifactory as a docker container
```
docker run -d --name artifactory --hostname artifactory -p 8081-8082:8081-8082 releases-docker.jfrog.io/jfrog/artifactory-oss:latest
```
You may access JFrog Artifactory webpage in the Web browse at http://localhost:8081
Login credentials are
<pre>
Username - admin
Password - password
</pre>
