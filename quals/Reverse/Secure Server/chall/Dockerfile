FROM ubuntu:20.04

RUN apt-get -y update

RUN useradd -ms /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

COPY flag.txt /flag.txt
RUN mv /flag.txt /flag_`cat /proc/sys/kernel/random/uuid`.txt

RUN chown root:root /flag_*.txt
RUN chmod 444 /flag_*.txt

COPY src /src

RUN chown -R ctf:ctf /src
RUN chmod -R 744 /src

WORKDIR /src

RUN chmod +x main

USER ctf
CMD ["./main"]