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


