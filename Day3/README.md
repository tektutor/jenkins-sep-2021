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
     - DevOps recommends QA to automate all the types of testing by "Writing code" using Test Frameworks.
     - Test Frameworks
          - Behaviour Driven Development (BDD - Test Frameworks)
          - Domain Driven Development (DDD - Test Frameworks)
          - Selenium, Cucumber, Postman,etc
     - QA folks are expected to learn Configuration Management Tools to automate QA environment setup
 
 - Operations Team (System Administrators, DBA, Infra Engineers, Production support )
     - Probably Operation Team have been doing administrative activities manually 
     - DevOps recommends them to automate all the administrative activities by "Writing code" using 
       Configuration Management Tools
     - Configuration Management Tools
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
  - Ansible is developed in Python
  - developed by Michael Deehan, a former RedHat employee
  - Michael Deehan after he quit RedHat, incorporated a company by name Ansible Inc
  - Ansible Inc organization created the Ansible core as a open source tool
  - Once Ansible became very popular, RedHat acquired Ansible Inc
  - RedHat developed Ansible Tower(Enterprise Product for Commercial use)
  - RedHat was acquired by IBM

  - uses YAML(Yet Another Markup Language) as the DSL
	- learning is easy
	- installation is very easy
	- architecture is very simpler(any one should be understand)
		- uses existing tools like SSH,SCP/SFTP
		- uses Python scripts to develop Ansible and Ansible Modules
  - Ansible Controller Machine (ACM)
	- is the system where automation scripts(Playbooks) are developed
	- is the system where Ansible is installed

  - Ansible Modules
	- are Python scripts in case of Unix/Linux/Mac Ansible nodes
	- are Powershell scripts in case of Windows Ansible nodes
	- modules are the one which does Infrastructure automation
	- can be built-in that comes out of the box with Ansible or user-defined custom modules
   	  e.g
	    - copy - copies file from local to ansible nodes and vice versa
	    - file - helps in creating files/folders on the ansible node
	    - apt  - helps in installing/uninstalling softwares on Debian Linux Distros
	    - yum  - helps in installing/uninstalling softwares on RedHat Linux Distros

  - Ansible Playbooks
       - YAML files
       - will invoke one or more Ansible module to automate configuration management
       
  - Ansible Nodes
       - are the machines where configuration management automation must be done
       - ansible is "NOT" installed on these machines
       - the softwares that need to be installed	
       - Unix/Linux/Mac Servers
         - Python (which comes out of the box)
         - SSH Server (mostly comes out of the box)

       - Windows Servers
         - PowerShell(.Net)
         - WinRM 
         
  - Alternate for Ansible
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

### You can get detailed help about any particular module as shown below
```
ansible-doc apt
```

### Building custom ubuntu image to use as Ansible containers
We need some Virtual Machines or On-Prem servers to be used as Ansible nodes, since we don't have additional Virtual Machines in training setup, we would like to use containers as Ansible nodes.

Let us generate key pairs for rps user. Accept all defaults by hitting enter thrice.

```
ssh-keygen
```

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
The expected output is
<pre>
[jegan@localhost ubuntu-ansible]$ docker images
REPOSITORY                                       TAG       IMAGE ID       CREATED         SIZE
<b>
tektutor/ansible-ubunutu-node                    latest    e6a97031776d   2 minutes ago   220MB
</b>

tektutor/spring-ms                               1.0       d05e6c1660df   26 hours ago    487MB
releases-docker.jfrog.io/jfrog/artifactory-oss   latest    60c5d817a8d1   2 days ago      980MB
ubuntu                                           16.04     b6f507652425   8 days ago      135MB
hello-world                                      latest    d1165f221234   6 months ago    13.3kB
openjdk                                          12        e1e07dfba89c   2 years ago     470MB
</pre>

### Let us create ubuntu1 and ubuntu2 containers
```
docker run -d --name ubuntu1 --hostname ubuntu1 -p 2001:22 -p 8001:80 tektutor/ansible-ubuntu-node 
docker run -d --name ubuntu2 --hostname ubuntu2 -p 2002:22 -p 8002:80 tektutor/ansible-ubuntu-node 
```

### Let's SSH into ubuntu1 to test if the custom image works as expected
```
ssh -p 2001 root@localhost
exit
```
The expected output is 
<pre>
[jegan@localhost jenkins-sep-2021]$ ssh -p 2001 root@localhost
The authenticity of host '[localhost]:2001 ([::1]:2001)' can't be established.
ECDSA key fingerprint is SHA256:k1bVnKnB97AVJOFzMLRVkarXFPX11KQfTWLOoL/O7v4.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[localhost]:2001' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 16.04.7 LTS (GNU/Linux 4.18.0-240.el8.x86_64 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

root@ubuntu1:~# exit
</pre>

### Let's SSH into ubuntu2 to test if the custom image works as expected
```
ssh -p 2002 root@localhost
exit
```
The expected output is
<pre>
thenticity of host '[localhost]:2002 ([::1]:2002)' can't be established.
ECDSA key fingerprint is SHA256:k1bVnKnB97AVJOFzMLRVkarXFPX11KQfTWLOoL/O7v4.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[localhost]:2002' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 16.04.7 LTS (GNU/Linux 4.18.0-240.el8.x86_64 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

root@ubuntu2:~# exit
</pre>

### Ansible ping ad-hoc command
```
cd ~/jenkins-sep-2021
git pull
cd Day3/Ansible
ansible -i hosts all -m ping
```
<pre>
-i - this switch indicates what follows is the inventory name
-m - this switch indicates what follows is the name of the module name
all - indicates the group of machines defined in the inventory file
</pre>

The expected output is
<pre>
[jegan@localhost Ansible]$ ansible -i hosts all -m ping
ubuntu1 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
ubuntu2 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
</pre>

### Commonly used ansible ad-hoc commands
```
ansible -i hosts all -m setup
```
setup is an ansible module(setup.py) that collects lot of facts(meta-data) about ansible nodes
For example
  - ansible_os_family : Debian or RedHat, etc
  - ansible_distribution: Ubuntu or CentOS
  - ansible_hostname: ubuntu1, ubuntu2

The below ansible ad-hoc command will show hostname of ubuntu1 and ubuntu2 ansible nodes
```
ansible -i hosts all -m shell -a "hostname"
```
The below ansible ad-hoc command will show IP Address of ubuntu1 and ubuntu2 ansible nodes
```
ansible -i hosts all -m shell -a "hostname -i"
```

### Running your first ansible playbook
```
cd ~/jenkins-sep-2021
git pull
cd Day3/Ansible
ansible-playbook -i hosts ping-playbook.yml
```

The expected output is
<pre>
jegan@localhost Ansible]$ ansible-playbook -i hosts ping-playbook.yml 

PLAY [Ping playbook] ********************************************************************************

TASK [Gathering Facts] ******************************************************************************
ok: [ubuntu1]
ok: [ubuntu2]

TASK [Ping the ansible node] ************************************************************************
ok: [ubuntu2]
ok: [ubuntu1]

PLAY RECAP ******************************************************************************************
ubuntu1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ubuntu2                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

</pre>

### Ansible Playbook structure
1. Playbook is a YAML file
2. Each Playbook has a list of Plays
3. Each Play will target atleast one Ansible Node(Server)
4. Each Play has an optional Tasks and Roles sections
5. Each Play has an optional vars and/or vars_files section
6. Each Tasks section has a list of Tasks
7. Each Task has a description and can invoke atmost one Ansible Module(Python or Powershell script).

### Executing the install nginx playbook
```
cd ~/jenkins-sep-2021
git pull
cd Day3/Ansible
ansible-playbook install-nginx-playbook.yml
```

### What happens internally when you perform ansible ping
```
ansible ubuntu1 -m ping
```

1. Ansible finds ansible.cfg in current directory and identifies the inventory it should be using
2. From the inventory file, Ansible understands how to connect to ubuntu1 ansible node
3. Ansible will perform SSH into ubuntu1 ansible node
4. Ansible creates tmp directory in Ansible Controller machine(ACM) and Ansible node
5. Ansible copies the ping.py from ACM to Ansible node
6. Ansible gives execute permission to the ping.py in the Ansible node
7. Ansible executes the ping.py file on the Ansible node
8. Ansible records the output of the ping.py and cleans up the tmp folder created on the Ansible node 
9. Ansible gives a summary of the output in the Ansible Controller Machine.







