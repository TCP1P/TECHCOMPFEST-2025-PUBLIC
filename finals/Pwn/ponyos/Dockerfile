FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install xinetd libarchive-tools qemu-system-x86-64 -y
RUN groupadd -r ctf && useradd -r -g ctf ctf

WORKDIR /home/ctf

COPY chall/ramdisk.igz .
COPY chall/kernel .
COPY chall/run.sh .
COPY chall/build.sh .

RUN echo '#!/bin/bash\nservice xinetd restart && /bin/sleep infinity' > /etc/init.sh
RUN echo 'service ctf\n\ 
{\n\ 
    disable = no\n\ 
    socket_type = stream\n\ 
    protocol = tcp\n\ 
    wait = no\n\ 
    user = ctf\n\ 
    type = UNLISTED\n\ 
    port = 8000\n\ 
    bind = 0.0.0.0\n\ 
    server = /home/ctf/run.sh\n\ 
}' > /etc/xinetd.d/ctf

RUN chmod 400 /etc/xinetd.d/ctf
RUN chmod +x /home/ctf/run.sh /home/ctf/build.sh /etc/init.sh

WORKDIR /home/ctf

RUN chown -R root:ctf /home/ctf
RUN service xinetd restart
