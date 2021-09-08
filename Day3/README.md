# DevOps
  - industry direction is everyone should code
  - Developers
       - do application development as their primary task
       - DevOps expects that developers should learn how to automate Unit/Integration by writing code
      		- Test Driven Development (TDD)
      		- Java
      	            - Test Frameworks
      	                 - JUnit, TestNg, Cucumber, Mockito, PowerMock, EasyMock, JMock, etc.,
      	        - C/C++
      	            - Test Frameworks
      	                 - CppUnit, GoogleTest, GoogleMock, etc
      	        - JavaScript, Angular, NodeJS, etc
      	            - Test Frameworks
      	                 - Jasmine, Karma, etc.,
      - Developers are also expected to learn Configuration Management Tools to automate Dev environment setup
 - QA
     - does end-to-end smoke test, component test, API test, functional testing, Performance test, 
       Stress Test, Load Test, etc
     - DevOps recommends QA to automate all the types of testing by "Writing code"
       Test Frameworks
           - Behaviour Driven Development (BDD - Test Frameworks)
           - Domain Driven Development (DDD - Test Frameworks)
           - Selenium, Cucumber, Postman,etc
     - QA folks are expected to learn Configuration Management Tools to automate QA environment setup
 
 - Operations Team (System Administrators, DBA, Infra Engineers, Production support )
     - Probably Operation Team have been doing administrative activities manually 
     - DevOps recommends them to automate all the administrative activities by "Writing code"
       Configuration Management Tools
          - Ansible, Puppet, Chef & SaltStack
     - are expected to automate Pre-Prod, Staging, Production environment setup using Configuration Management Tools
 


# Ansible
  - Configuration Management Tool
	- it is a Infrastruce as a Code Tool
	- helps in automating administrative activities
		- you should be able to provision Virtual Machines
		- you should be able to provision containers, cloud bases VMs
		- install/uninstall softwares (Oracle, Weblogic,etc,.)
		- configure softwares (Configure Weblogic, etc)
		- Restart services/machines
  - comes in 2 flavours
     - Ansible Core (Opensource)
     - Ansible Tower - RedHat(IBM Product)
  - open source tool
  - developed by Michael Deehan
  - Ansible is developed in Python
  - Michael Deehan - a former RedHat employee
  - Michael incorporated a company by name Ansible Inc
  - Ansible Inc organization created the Ansible core open source tool
  - Once Ansible became very popular, RedHat acquired Ansible Inc
  - RedHat developed Ansible Tower(Enterprise Product - Commercial use)
  - RedHat was acquired by IBM

  - Ansible 
	- uses YAML(Yet Another Markup Language) as the DSL
	- learning is easy
	- installation is very easy
	- architecture is very simpler(any one should be understand)
		- uses existing tools like SSH,SCP/SFTP
		- user Python scripts to develop Ansible and Ansible Modules
        - Ansible Controller Machine (ACM)
		- is the system where automation scripts(Playbooks) are developed
		- is the system where Ansible is installed


	- Ansible Modules
		- are Python scripts in case of Unix/Linux/Mac Ansible nodes
		- are Powershell scripts in case of Windows Ansible nodes
		- module are the one which does automation
			e.g
			  copy - copies file from local to ansible nodes and vice versa
			  file - helps in creating files/folders on the ansible node
			  apt  - helps in installing/uninstalling softwares on Debian Linux Distros
			  yum  - helps in installing/uninstalling softwares on RedHat Linux Distros

	- Ansible Playbooks
		- YAML files
		- will invoke one or more Ansible module to automate configuration management
		    
	- Ansible Nodes
		- are the machines where configuration management automation must be done
		- ansible is "NOT" installed on these machines
		- the softwares that need to be installed	
			Unix/Linux/Mac Servers
				- Python (which comes out of the box)
				- SSH Server (mostly comes out of the box)

			Windows Servers
				- PowerShell(.Net)
				- WinRM 

  - alternate tools
	- Puppet - DSL(Ruby)
	- Chef - DSL(Ruby)
	- Salt(SaltStack) 
  - Domain Specific Language (DSL)
	- language in which the automation script 

### Installing Ansible in CentOS 
```
sudo yum install -y epel-release
sudo yum install -y ansible
```

### You may verify if Ansible is installed as shown below (do this as rps user)
```
ansible --version
```
### Finding the total number of Ansible modules supported by your version of ansible
```
ansible-doc -l | wc -l
```

### You can get detailed help about any particular modules as shown below
```
ansible-doc apt
```

### Build custom ubuntu image to use as Ansible containers
We need some Virtual Machines or On-Prem servers to be used as Ansible nodes, since we don't have additional Virtual Machines in training setup, we would like to use containers as Ansible nodes.

Let us generate key pairs for rps user
```
ssh-keygen
```
Accept all defaults by hitting enter.

```
cd ~/jenkins-sep-2021
git pull
cd Day3/ubuntu-ansible
cp ~/.ssh/id_rsa.pub authorized_keys
docker build -t tektutor/ansible-ubuntu-node .
```

You may verify if the docker images is built successfuly
```
docker images
```
