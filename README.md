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
