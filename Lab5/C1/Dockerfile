FROM ubuntu:16.10

RUN echo 'deb http://old-releases.ubuntu.com/ubuntu yakkety main multiverse restricted universe' > /etc/apt/sources.list && \
    echo 'deb http://old-releases.ubuntu.com/ubuntu yakkety-backports main multiverse restricted universe' >> /etc/apt/sources.list && \
    echo 'deb http://old-releases.ubuntu.com/ubuntu yakkety-proposed main multiverse restricted universe' >> /etc/apt/sources.list && \
    echo 'deb http://old-releases.ubuntu.com/ubuntu yakkety-security main multiverse restricted universe' >> /etc/apt/sources.list && \
    echo 'deb http://old-releases.ubuntu.com/ubuntu yakkety-updates main multiverse restricted universe' >> /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y openssh-client && \
    apt-get clean

WORKDIR /data

CMD ["/bin/bash"]