#!/usr/bin/python3
# stop live tracing 1 session n channels
import os

lttng_provider_cnt_fp = open("lttng_provider_cnt","r")
lttngMaxProvider=int(lttng_provider_cnt_fp.read())
lttng_provider_cnt_fp.close()

if __name__=="__main__":
    index = 0;
    while (index < lttngMaxProvider):
#       print(d)
        lttng_cmd_str_2 = "lttng disable-event -c tp_channel_{0} -s tp_session 'tp_{0}' > /dev/null 2>&1".format(str(index))
        os.system(lttng_cmd_str_2)
        lttng_cmd_str_1 = "lttng disable-channel -u tp_channel_{0} -s tp_session".format(str(index))
        os.system(lttng_cmd_str_1)
#       print(cmd_str)
        index += 1
    lttng_cmd_str_3 = "lttng stop tp_session"
    os.system(lttng_cmd_str_3)
