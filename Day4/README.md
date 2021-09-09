### Building CentOS custom image to create centos ansible nodes
```
cd ~/jenkins-sep-2021
git pull
cd Day4/centos-ansible
cp ~/.ssh/id_rsa.pub authorized_keys
docker build -t tektutor/ansible-centos-node .
```

### List and check the CentOS custom image
```
docker images
```
The expected output is
<pre>
[jegan@localhost Day4]$ <b>docker images</b>
REPOSITORY                                       TAG       IMAGE ID       CREATED          SIZE
<b>
tektutor/ansible-centos-node                     latest    56491a566f81   10 minutes ago   259MB
tektutor/ansible-ubuntu-node                     latest    e6a97031776d   20 hours ago     220MB
</b>
tektutor/spring-ms                               1.0       d05e6c1660df   45 hours ago     487MB
releases-docker.jfrog.io/jfrog/artifactory-oss   latest    60c5d817a8d1   3 days ago       980MB
ubuntu                                           16.04     b6f507652425   9 days ago       135MB
hello-world                                      latest    d1165f221234   6 months ago     13.3kB
centos                                           8         300e315adb2f   9 months ago     209MB
openjdk                                          12        e1e07dfba89c   2 years ago      470MB
</pre>

### Create centos1 and centos2 containers
```
cd ~
docker run -d --name centos1 --hostname centos1 -p 2003:22 -p 8003:80 tektutor/ansible-centos-node
docker run -d --name centos2 --hostname centos2 -p 2004:22 -p 8004:80 tektutor/ansible-centos-node
```
### List and check the centos containers
```
docker ps --filter="name=ubuntu*|centos*"
```
The expected output is
<pre>
[jegan@localhost Day4]$ <b>docker ps --filter="name=ubuntu*|centos*"</b>
CONTAINER ID   IMAGE                                 COMMAND               CREATED          STATUS          PORTS     <b>                                                                     NAMES
fc30df7adc40   tektutor/ansible-centos-node:latest   "/usr/sbin/sshd -D"   9 minutes ago    Up 9 minutes    0.0.0.0:2004->22/tcp, :::2004->22/tcp, 0.0.0.0:8004->80/tcp, :::8004->80/tcp   centos2
94309427724d   tektutor/ansible-centos-node:latest   "/usr/sbin/sshd -D"   10 minutes ago   Up 10 minutes   0.0.0.0:2003->22/tcp, :::2003->22/tcp, 0.0.0.0:8003->80/tcp, :::8003->80/tcp   centos1
</b>
260aaad1df35   tektutor/ansible-ubuntu-node          "/usr/sbin/sshd -D"   19 hours ago     Up 23 minutes   0.0.0.0:2002->22/tcp, :::2002->22/tcp, 0.0.0.0:8002->80/tcp, :::8002->80/tcp   ubuntu2
6b516c130ba4   tektutor/ansible-ubuntu-node          "/usr/sbin/sshd -D"   19 hours ago     Up 23 minutes   0.0.0.0:2001->22/tcp, :::2001->22/tcp, 0.0.0.0:8001->80/tcp, :::8001->80/tcp   ubuntu1

</pre>

### Ansible ping on centos and ubuntu ansible nodes
```
cd ~/jenkins-sep-2021
git pull
cd Day4
ansible all -m ping
```
The expected output is
<pre>
[jegan@localhost Day4]$ <b>ansible all -m ping</b>
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
centos2 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    },
    "changed": false,
    "ping": "pong"
}
centos1 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    },
    "changed": false,
    "ping": "pong"
}
</pre>

### Provisioning Docker Ansible Nodes using Ansible Playbook
The below playbook demonstrates one practical usecase of sequence loop in Ansible Playbook

```
cd ~/jenkins-sep-2021
git pull
cd Day4/Loops
ansible-playbook provision-container-playbook.yml --ask-become-pass
```
When prompted for password, you may type the sudo password which is rps@12345

### List and see there is ubuntu-001, ubuntu-002, centos-001 and centos-002 containers
```
docker ps
```
The expected output is
<pre>
[jegan@localhost]$<b> docker ps</b>
CONTAINER ID   IMAGE                                 COMMAND               CREATED         STATUS         PORTS                                        NAMES
a0ddb99c163a   tektutor/ansible-centos-node:latest   "/usr/sbin/sshd -D"   4 minutes ago   Up 4 minutes   0.0.0.0:3002->22/tcp, 0.0.0.0:9002->80/tcp   centos-002
10e864e7abab   tektutor/ansible-centos-node:latest   "/usr/sbin/sshd -D"   4 minutes ago   Up 4 minutes   0.0.0.0:3001->22/tcp, 0.0.0.0:9001->80/tcp   centos-001
d0e24e0d1b43   tektutor/ansible-ubuntu-node:latest   "/usr/sbin/sshd -D"   4 minutes ago   Up 4 minutes   0.0.0.0:2002->22/tcp, 0.0.0.0:8002->80/tcp   ubuntu-002
f5d024fc3540   tektutor/ansible-ubuntu-node:latest   "/usr/sbin/sshd -D"   4 minutes ago   Up 4 minutes   0.0.0.0:2001->22/tcp, 0.0.0.0:8001->80/tcp   ubuntu-001

</pre>
### Executing the ansible vault playbook
```
cd ~/jenkins-sep-2021
git pull
cd Day4/AnsibleVault
ansible-playbook vault-playbook -e my_msg=Hello --ask-vault-pass
```

### Executing the playbook that builds docker ansible node images
The below playbook demonstrates one practical usecase of list variables in Ansible Playbook
```
cd ~/jenkins-sep-2021
git pull
cd Day4/Loops
ansible-playbook build-ansible-node-docker-images-playbook.yml --ask-become-pass
```
When prompted ### Executing the ansible vault playbook
```
cd ~/jenkins-sep-2021
git pull
cd Day4/AnsibleVault
ansible-playbook vault-playbook -e my_msg=Hello --ask-vault-pass
```
type your sudo password i.e rps@12345

### List and see if the images build are shown
```
docker images
```

### Running the playbook that demonstrates dictionary variable
```
cd ~/jenkins-sep-2021
git pull
cd Day4/Loops
ansible-playbook dictionary-playbook.yml
```

### Creating vault protected file
```
cd ~/jenkins-sep-2021
cd Day4/AnsibleVault
ansible-vault create credentials.yml
```
When prompted for password, type your password and confirm the same password.

### Viewing vault-protected file
```
ansible-vault view credentials.yml --ask-vault-pass
```
Type your vault password, rps@12345

### Edit vault-protected file
```
ansible-vault edit credentials.yml --ask-vault-pass
```
Type your vault password, rps@12345

### Decrypt vault-protected file
```
ansible-vault decrypt credentials.yml
cat credentials.yml
```

### Encrypt vault-protected file
```
ansible-vault encrypt credentials.yml
cat credentials.yml
```
When prompted for password, type your preferred password


### Changing your existing vault-password
```
ansible-vault rekey credentials.yml
```
When prompted for current password type rps@12345, you may change the password to rps@123 and confirm rps@123


### Executing the ansible vault playbook
```
cd ~/jenkins-sep-2021
git pull
cd Day4/AnsibleVault
ansible-playbook vault-playbook -e my_msg=Hello --ask-vault-pass
```
When prompted for password, type your vault password, i.e rps@12345

### Executing the ansible vault playbook when vault password is stored in a user-defined file
```
cd ~/jenkins-sep-2021
git pull
cd Day4/AnsibleVault
ansible-playbook vault-playbook -e my_msg=Hello
```
Ansible will locate the secrets file with the help of ansible.cfg.  You need to ensure the .secrets file isn't
commited to GitHub or similar version control as it would reveal your password :)

I commited the .secrets file for your to try out the exercises, but committing vault password file into version control must be avoided.

### Executing the playbook that invokes Custom Ansible Module
```
cd ~/jenkins-sep-2021
git pull
cd Day4/CustomAnsibleModule
ansible-playbook custom-module-playbook.yml
```

The expected output is
<pre>
[jegan@localhost CustomAnsibleModule]$ <b>ansible-playbook custom-module-playbook.yml</b> 

PLAY [Demonstrates invoking our custom ansible module in a playbook] ****************************************************

TASK [Gathering Facts] **************************************************************************************************
ok: [ubuntu1]
ok: [ubuntu2]
ok: [centos2]
ok: [centos1]

TASK [Invoke hello custom module] ***************************************************************************************
changed: [ubuntu2]
changed: [ubuntu1]
changed: [centos1]
changed: [centos2]

TASK [debug] ************************************************************************************************************
ok: [ubuntu1] => {
    "output": {
        "changed": true,
        "failed": false,
        "response": "Hello Ansible custom module !"
    }
}
ok: [ubuntu2] => {
    "output": {
        "changed": true,
        "failed": false,
        "response": "Hello Ansible custom module !"
    }
}
ok: [centos1] => {
    "output": {
        "changed": true,
        "failed": false,
        "response": "Hello Ansible custom module !"
    }
}
ok: [centos2] => {
    "output": {
        "changed": true,
        "failed": false,
        "response": "Hello Ansible custom module !"
    }
}

TASK [Retrieve IP Address] **********************************************************************************************
ok: [ubuntu1]
ok: [ubuntu2]
ok: [centos1]
ok: [centos2]

TASK [debug] ************************************************************************************************************
ok: [ubuntu1] => {
    "output": {
        "IPAddress": "172.17.0.2",
        "changed": false,
        "failed": false
    }
}
ok: [ubuntu2] => {
    "output": {
        "IPAddress": "172.17.0.3",
        "changed": false,
        "failed": false
    }
}
ok: [centos1] => {
    "output": {
        "IPAddress": "172.17.0.4",
        "changed": false,
        "failed": false
    }
}
ok: [centos2] => {
    "output": {
        "IPAddress": "172.17.0.5",
        "changed": false,
        "failed": false
    }
}

PLAY RECAP **************************************************************************************************************
centos1                    : ok=5    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
centos2                    : ok=5    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ubuntu1                    : ok=5    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ubuntu2                    : ok=5    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

</pre>

### Executing playbook with custom role
```
cd ~/jenkins-sep-2001
git pull
cd Day4/CustomAnsibleRole
ansible-playbook install-apache-playbook.yml
```
