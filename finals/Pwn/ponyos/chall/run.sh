#!/bin/bash
set -euo pipefail

pushd /home/ctf > /dev/null 2>&1

if [ ! -f ramdisk.igz ]; then
	./build.sh
fi

exec timeout --foreground 300 qemu-system-x86_64 \
    -M q35 \
    -smp 2 \
    -m 128M \
    -kernel kernel \
    -initrd ramdisk.igz \
    -append "root=/dev/ram0 migrate start=--headless" \
    -no-reboot \
    -monitor none \
    -serial null -serial stdio \
    -fw_cfg name=opt/org.toaruos.gettyargs,string="-a local /dev/ttyS1" \
    -fw_cfg name=opt/org.toaruos.bootmode,string=headless \
    -nographic \
