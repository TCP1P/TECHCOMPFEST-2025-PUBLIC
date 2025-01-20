FROM ubuntu:latest

RUN apt-get -y update
RUN apt-get -y install libc6 libstdc++6

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
EXPOSE 8000
CMD ["./main"]