#!/usr/bin/python3
import os

lttngMaxProvider=2000

if __name__=="__main__":
    index = 0;
    while (index < lttngMaxProvider):
#       print(d)
        lttng_cmd_str_1 = "lttng stop tp_session_%s > /dev/null 2>&1"%(str(index))
        os.system(lttng_cmd_str_1)
        lttng_cmd_str_2 = "lttng destroy tp_session_{0} > /dev/null 2>&1".format(str(index))
        os.system(lttng_cmd_str_2)
#       print(cmd_str)
        index += 1
