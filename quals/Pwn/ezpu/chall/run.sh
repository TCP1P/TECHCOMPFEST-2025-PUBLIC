#!/bin/bash

#gcc -masm=intel -static fs/x.c -o fs/a.out
#cd fs; find . | cpio -H newc -o | gzip -c > ../rootfs.cpio.gz; cd ..

cd $(dirname $0)
exec timeout --foreground 300 ./qemu-system-x86_64 \
        -L bios \
	-m 64M \
        -cpu qemu64,+smep,+smap \
        -nographic \
        -monitor none \
        -kernel bzImage \
        -initrd rootfs.cpio.gz \
	-no-reboot \
	-append "console=ttyS0 quiet kaslr panic=1 kpti=1 oops=panic" \
	-net user -net nic -device e1000 \
