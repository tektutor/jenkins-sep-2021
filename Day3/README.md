# Ansible
  - Configuration Management Tool
	- it is a Infrastruce as a Code Tool
	- helps in automating administrative activities
		- you should be able to provision Virtual Machines
		- you should be able to provision containers, cloud bases VMs
		- install/uninstall softwares (Oracle, Weblogic,etc,.)
		- configure softwares (Configure Weblogic, etc)
		- Restart services/machines

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

