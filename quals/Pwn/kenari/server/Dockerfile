FROM ubuntu:22.04

RUN apt update && apt upgrade -y && apt update --fix-missing
RUN apt install socat -y

COPY files /chall/

RUN chmod 700 /usr/bin/* /bin/* /tmp /dev/shm
RUN chmod 755 /usr/bin/env /bin/dash /bin/bash /bin/sh /bin/cat /usr/bin/groups /usr/bin/id /bin/ls
RUN chown root:root -R /chall

RUN chmod +x /chall/kenari

WORKDIR /chall

CMD ["/bin/bash", "-c", "exec socat -d TCP-LISTEN:11001,reuseaddr,fork EXEC:./kenari,su=nobody"]
