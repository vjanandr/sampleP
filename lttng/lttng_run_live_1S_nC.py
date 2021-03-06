#!/usr/bin/python3
# Create one session and enable a channel for a process/provider.
# There is 1 session and n channels corresponding to n processess.
import os

lttng_provider_cnt_fp = open("lttng_provider_cnt","r")
lttngMaxProvider=int(lttng_provider_cnt_fp.read())
lttng_provider_cnt_fp.close()

if __name__=="__main__":
    lttng_session_start = False
    index = 0;
    cwd = os.getcwd()

    lttng_cmd_str_1 = "lttng create tp_session --live > /dev/null"
    print(lttng_cmd_str_1)
    os.system(lttng_cmd_str_1)

    while (index < lttngMaxProvider):
        lttng_cmd_str_5 = "lttng enable-channel --num-subbuf 16 --subbuf-size 512k -u tp_channel_{0} -s tp_session".format(str(index))
        print(lttng_cmd_str_5)
        os.system(lttng_cmd_str_5)
        index += 1

    lttng_cmd_str_3 = "lttng start tp_session"
    print(lttng_cmd_str_3)
    os.system(lttng_cmd_str_3)

    index = 0
    while (index < lttngMaxProvider):
        d = "lttngprov/lttngprov_"+str(index)
        if os.path.exists(d):
            os.chdir(d)

            lttng_cmd_str_2 = "lttng enable-event -u -s tp_session -c tp_channel_{0} 'tp_{0}:*'".format(str(index))
            print(lttng_cmd_str_2)
            os.system(lttng_cmd_str_2)

            lttng_cmd_str_4 = "./tp_{0} &".format(str(index))
            print(lttng_cmd_str_4)
            os.system(lttng_cmd_str_4)

            os.chdir(cwd)
        index += 1
