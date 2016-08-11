#! /usr/bin/env python
# http://dev-console.blogspot.in/2012/01/some-knowledge-about-vdso.html

from __future__ import with_statement
import re
import os

## regex pattern for finding out the memory address range from the output line
pattern = re.compile(r'[\w\d]+-[\w\d]+')

with open('/proc/self/maps', 'r') as file:
    for line in file:
        line = line.rstrip()
        if '[vdso]' in line:
            addr_range = pattern.findall(line)[0]
            start_addr, end_addr = [int(addr, 16) for addr in addr_range.split('-')]
            break
file.close()
fd = os.open('/proc/self/mem', os.O_RDONLY)
os.lseek(fd, start_addr, os.SEEK_SET)
buf = os.read(fd, (end_addr-start_addr))
with open('linux-gate.so.1', 'w') as file:
    file.write(buf)
    file.close()
os.close(fd)
