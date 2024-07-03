FROM ubuntu:22.10

RUN echo 'deb http://old-releases.ubuntu.com/ubuntu kinetic main multiverse restricted universe' > /etc/apt/sources.list && \
    echo 'deb http://old-releases.ubuntu.com/ubuntu kinetic-backports main multiverse restricted universe' >> /etc/apt/sources.list && \
    echo 'deb http://old-releases.ubuntu.com/ubuntu kinetic-proposed main multiverse restricted universe' >> /etc/apt/sources.list && \
    echo 'deb http://old-releases.ubuntu.com/ubuntu kinetic-security main multiverse restricted universe' >> /etc/apt/sources.list && \
    echo 'deb http://old-releases.ubuntu.com/ubuntu kinetic-updates main multiverse restricted universe' >> /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y openssh-client openssh-server && \
    apt-get clean

RUN mkdir -p /var/run/sshd && \
    echo 'root:root' | chpasswd && \
    useradd -m prueba && \
    echo 'prueba:prueba' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    echo 'export PATH=$PATH:/usr/sbin' >> /etc/profile

EXPOSE 22

WORKDIR /data

CMD ["/usr/sbin/sshd", "-D"]