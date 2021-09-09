FROM centos:8
MAINTAINER Jeganathan Swaminathan <jegan@tektutor.org> 

#ENV http_proxy http://10.20.30.40:80
#ENV https_proxy http://10.20.30.40:80

RUN yum install -y openssh-server openssh-clients 
RUN ln -s -f /usr/libexec/platform-python3.6 /usr/bin/python 

# Set the password of root user to root
RUN echo 'root:root' | chpasswd

RUN usermod -aG wheel root 

RUN sed -ri 's/^session\s+required\s+pam_loginuid.so$/session optional pam_loginuid.so/' /etc/pam.d/sshd

# Disable root login &
# Disable password login, only allow public key. 
COPY sshd_config /etc/ssh/sshd_config
COPY sudoers /etc/sudoers

RUN mkdir -p /root/.ssh
COPY authorized_keys /root/.ssh/authorized_keys
RUN chmod 700 -R /root/.ssh

# Add sshd running directory.
RUN mkdir -m 700 /var/run/sshd

RUN ssh-keygen -A && rm -f /run/nologin

EXPOSE 22
EXPOSE 80
CMD ["/usr/sbin/sshd", "-D"]
