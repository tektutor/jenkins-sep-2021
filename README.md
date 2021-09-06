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

