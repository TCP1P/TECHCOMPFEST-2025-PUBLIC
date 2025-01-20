#!/bin/bash
set -euo pipefail

if [ ! -f flag.txt ]; then
    echo "TCF{I_got_another_OS_PWN_for_ACE_CTF_2025}" > flag.txt
fi

if [ ! -f image.iso ]; then
    wget https://github.com/klange/ponyos/releases/download/v8.0/ponyos.iso
fi

bsdtar -xf ponyos.iso kernel ramdisk.igz

tar -xf ramdisk.igz etc/master.passwd
sed -i "s/root:toor/root:$(tr -dc 'A-Za-z0-9' < /dev/urandom | head -c 22)/g" etc/master.passwd
sed -i "s/local:local/local:$(tr -dc 'A-Za-z0-9' < /dev/urandom | head -c 22)/g" etc/master.passwd
sed -i "s/guest:guest/guest:$(tr -dc 'A-Za-z0-9' < /dev/urandom | head -c 22)/g" etc/master.passwd
zcat ramdisk.igz > ramdisk
tar --delete -f ramdisk etc/master.passwd
tar -rf ramdisk etc/master.passwd flag.txt --mode=400 --owner=0 --group=0

gzip -c ramdisk > ramdisk.igz

rm -rf ramdisk etc
