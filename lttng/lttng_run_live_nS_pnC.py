#!/usr/bin/python3
# Live n sessions p:n channels per session, where p is the maximum number of tracepoint providers
import os

lttng_provider_cnt_fp = open("lttng_provider_cnt","r")
lttngMaxProvider=int(lttng_provider_cnt_fp.read())
lttng_provider_cnt_fp.close()

if __name__=="__main__":
    cwd = os.getcwd()

    index = 0;
    while (index < 25):
        lttng_cmd_str_1 = "lttng create tp_session_{0} --live > /dev/null".format(str(index))
        print(lttng_cmd_str_1)
        os.system(lttng_cmd_str_1)
        index += 1

    index = 0
    # We have to enable the channel before starting sessions.
    while (index < lttngMaxProvider):
        lttng_cmd_str_5 = "lttng enable-channel --num-subbuf 16 --subbuf-size 512k -u tp_channel_{0} -s tp_session_{1}".format(str(index), str(index % 25))
        print(lttng_cmd_str_5)
        os.system(lttng_cmd_str_5)
        index += 1

    index = 0
    while (index < 25):
        lttng_cmd_str_3 = "lttng start tp_session_{0}".format(str(index))
        print(lttng_cmd_str_3)
        os.system(lttng_cmd_str_3)
        index += 1

    index = 0
    while (index < lttngMaxProvider):
        d = "lttngprov/lttngprov_"+str(index)
        if os.path.exists(d):
            os.chdir(d)

            lttng_cmd_str_2 = "lttng enable-event -u -s tp_session_{1} -c tp_channel_{0} 'tp_{0}:*'".format(str(index), str(index % 25))
            print(lttng_cmd_str_2)
            os.system(lttng_cmd_str_2)

            lttng_cmd_str_4 = "./tp_{0} &".format(str(index))
            print(lttng_cmd_str_4)
            os.system(lttng_cmd_str_4)

            os.chdir(cwd)
        index += 1
