#!/usr/bin/python3
import os
prov_header="""/** Trace point provider_%d */\n"""
prov_c="""#define TRACEPOINT_CREATE_PROBES\n#define TRACEPOINT_DEFINE\n\n#include %s\n"""
main_c="""#include <stdio.h>\n#include<sys/types.h>\n#include<unistd.h>\n#include"""

lttngMaxProvider=2000
def providerGen(index):
    # TP_H file
    tp_h_f = "tp_"+str(index)+".h"
    # Open TP_H file
    tp_h_fp = open(tp_h_f, "w")
    tp_h_fp.write(prov_header%(index))
    # Close TP_H file
    tp_h_fp.close()
    # TP_C file
    tp_c_f = "tp_"+str(index)+".c"
    # Open TP_C file
    tp_c_fp = open(tp_c_f, "w")
    tp_c_fp.write(prov_header%(index))
    tp_c_fp.write(prov_c%(tp_h_f))
    tp_c_fp.close()
    return

def mainGen(index):
    main_f = "main_"+str(index)+".c"
    return

def provInit(index):
    d = "lttngprov/lttngprov_"+str(index)
    #Get the current working directory
    cwd  = os.getcwd()
    if os.path.exists(d):
        # Remove provider directory if it already exists
        os.rmdir(d)
    #Create a new provider directoy
    os.makedirs(d)
    os.chdir(d)
    providerGen(index)
    mainGen(index)
    os.chdir(cwd)
    return

def mainGen(index):
    return

if __name__=="__main__":
    d = "lttngprov"
    if not os.path.exists(d):
        os.makedirs(d)
    i = 0;
    while (i < 2000):
        provInit(i)
        i+=1



