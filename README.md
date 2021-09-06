### Version Control Softwares
Client/Server Architecture
- CVS 
- SVN
- Perforce
- IBM Clearcase
- Microsoft Visual Source Safe (VSS)

# Git commands

### Open a terminal in your CentOS Lab
On the top left corner, click on Activities menu and open the terminal (black window)

### Creating an empty repository locally (from terminal)
```
cd /home/rps
mkdir Training
cd Training
git init
```

### Performing basic configuration on your local git repo
```
git config --local user.name "Jeganathan Swaminathan"
git config --local user.email "mail2jegan@gmail.com"
```
You need to replace the name, email with your name and email.

### Checking the status of local git repo
```
git status
```

### Create a file with gedit called cars.txt
```
gedit cars.txt
```
Type Maruti 800 and save it

### Checking git status
```
git status
```
You will see that cars.txt file is untracked.

### You need to stage the file so that Git can track the changes as shown below
```
git add cars.txt
git status
```
Now you will see the file cars.txt in green color as new file. From this point, Git will track the changes done in cars.txt file.

### Commit the changes to the local git repo
```
git commit -m "Initial commit."
git status
```
-m - indicates checkin comment

Now your changes are committed locally

### Adding your GitHub repo to your local git
```
git remote add origin https://github.com/tektutor/gitdemo.git
```
You may verify to see if your remote Github url is added correctly by
```
git remote -v
```

### Generating a Personal Access Token in GitHub
1. Login to your GitHub account
2. Select your account on the top right corner and click on Settings
3. On the left side menu, select Developer Settings --> Personal Access Token
4. Select all the access (check boxes) and click on Generate Personal Access Token
5. Copy and save the token somewhere as you won't be able to see the token details later.

### Push your local changes to your GitHub repository
```
git push -u origin master
```
When it prompts for user, type your email-id that is associated with your GitHub account.  You need to paste the Personal Access Token of your GitHub account as password when prompted.

At this point, you may refresh you GitHub repo and see your local files pushed into your GitHub !

### Git clone ( Taking a snapshot copy of repository from GitHub to Local )
```
git clone
```

### Git pull vs clone
Git clone - will get a copy of entire repository from GitHub to Local
Git pull  - will only get the delta changes from GitHub to Local, assumption is you already have clone it before pull.

# Docker

### Installing Docker in CentOS 8
```
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce --allowerasing
sudo systemctl enable docker && sudo systemctl start docker
sudo systemctl status docker
```

### See if you issue docker commands (Try this as rps user
```
docker --version
docker images
```

### Troubleshooting permission denied error
```
sudo usermod -aG docker rps
sudo su rps
docker images
```

### How can install 2 or 3 Operating Systems on the same PC?
You may partition the hard disk.

#### Partitions are of 2 types
1. Primary partition
     - is required to install Operating System 
     - Master Boot Record(MBR) - location where Boot Loader utility is installed 
     - Boot Loader is the utility which loads Operating once the BIOS POST is done
3. Secondary partions 
     - Good for backup and installing softwares but not Operating System

#### Boot Loaders
  - LILO ( Linux Loader )
  - GRUB 1/GRUB 2 (used in Linux)
  - you can install multiple OS on the same PC but you can only boot one OS at a time

### What is Hypervisor?
 - general term used to refer to the Virtualization Technology
 - this technology let's you boot many OS in the same PC simultaneously
 - heavy weight
     - because the Guest OS or Virtual Machines require dedicated
           - CPU core(s)
           - RAM
           - Storage (Hard Disk)
 - primarily the number of Guest OS(VMs) a Workstation/Server can support depends on the total number of CPU cores
   the Workstation/Server has
   
#### Benefits of Virtualization Technology
  - Hardware consolidation
  - Better hardware utilization
  - Less Power consumption ( You need to pay less electricity bill )
  - Less Rental/Leasing as you need a smaller Server room, hence you save in terms of Real Estate (Rent/Lease) costing

### Is Hypervisor a Software or Hardware solution?
  - Hardware + Software technology
  - General Purpose Processor
        - Intel
            - supports Virtualization feature called VT-X
        - AMD
            - supports Virtualization feature called AMD-V
  - Basic Input Output System (BIOS) also needs to support Virtualization
  - Host OS also needs to support Virtualiztion

# Container Technically
  - is a Linux Technology
  - Linux Kernel
     1. Namespace
         - Isolate one container from the other containers
         - Isolation helps in preventing one container accessing the memory of other container, hence avoids
           heap/memory corruptions in general
         - Namespace Example
             - Process Namespace
             - Network Namespace
             - User Namespace, etc.,
     2. Control Groups (CGroups)
         - one can put some upper bound on the hardware utilization of a container
         Example (Restrictions or Resource Quota can be put on each containers optionally)
         - how much RAM a container can access
         - how many CPU Cores a container can access
         - how much storage a container can use

### What are the Container Runtimes available in market today?
1. LXC (Lightweight Containership)
2. Docker (More popular)
       - it gives root access to a regular user inside containers
       - this gives a chance for a smart hacker to gain root access on Servers where Docker is installed
       - now supported daemonless(rootless containers - but kind of it is too late)
4. Rkt ( pronounced as Rocket )
5. Podman (This is expected to take the place of Docker, while Docker might still be there)
     - rootless/daemonless
     - any user will get similar permissions(access) inside containers
     - in other words, whatever access a user has outside container, the same set of access only the user will
       gain inside container as well
     - RedHat(IBM Company) Openshift has already moved to Podman (default container runtime used in OpenShift)
     - Google Kubernetes (opensource) is expected to drop Docker as default container runtime this Dec 2021 
       and then they planning to make Podman container runtime as the default container runtime.
     - is 100% compatible in terms of Docker commands
        - all the docker commands works as it is in Podman
        - just you need to replace docker with podman

### Docker
     - is developed by Docker Inc organization
     - is developed in Google Go language
     - it follows Client/Server Architecture
     - Client (docker)
          - any command user issue, the client will write the request into the Unix socket
     - Server (dockerd - runs a linux service)
          - server on the other end will read the request from the docker client and responds back to client
            via Unix Socket
          - also support REST API
               - third party application need to talk to Docker Server
               - Jenkins has to communicate with Docker Server 
               - REST API works for local/remote Docker clients
               - not enabled by default
     - When Docker Client and Server runs locally, they communicate via Local Unix Socket

### What is Docker Image?
 - specification/blueprint of a Docker container
 - Whatever softwares are installed on the Docker image they will be available on the container level
 - any number of containers can be created with a Docker Image
 - Docker Images are similar to OS ISO Images or VMWare Images

### What is a Docker Container?
  - is an instance of Docker Image
  - an application process
  - runs in its network namespace
  - has it own Network Stack, hence it has its own Network Interface Card(NIC)
  - has an IP Address (Private)
  - supports 3 types of Network
       - Bridge network (172.17.0.0/16)
           - any container created by default joins this bridge network
           - all containers which join this network, they get their IP in the range of 172.17.0.0/16
       - Host network
           - container shares the same Network stack as your Host Machine(meaning no isolation - it runs like a normal application process )
       - None network
           - any container that doesn't need any network support, they join this network


