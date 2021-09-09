### Building CentOS custom image to create centos ansible nodes
```
cd ~/jenkins-sep-2021
git pull
cd Day4/Ansible
cp ~/.ssh/id_rsa.pub authorized_keys
docker build -t tetktutor/ansible-centos-node .
```

### List and check the CentOS custom image
```
docker images
```

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

### Ansible ping on centos and ubuntu ansible nodes
```
cd ~/jenkins-sep-2021
git pull
cd Day4/Ansible
ansible all -m ping
```
