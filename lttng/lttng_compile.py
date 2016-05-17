#!/usr/bin/python3
import os

lttngMaxProvider=2000

if __name__=="__main__":
    index = 0;
    cwd = os.getcwd()
    while (index < lttngMaxProvider):
        d = "lttngprov/lttngprov_"+str(index)
#        print(d)
        if os.path.exists(d):
            os.chdir(d)
            cmd_str = "gcc -o tp_{0} main_{0}.c tp_{0}.c \
                    -L/home/lttng/lib32nxos/lib -llttng-ust -ldl \
                    -I. -I/home/lttng/lib32nxos/include".format(str(index))
#            print(cmd_str)
            os.system(cmd_str)
            os.chdir(cwd)
        index += 1

