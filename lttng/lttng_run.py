#!/usr/bin/python3
import os

lttng_provider_cnt_fp = open("lttng_provider_cnt","r")
lttngMaxProvider=int(lttng_provider_cnt_fp.read())
lttng_provider_cnt_fp.close()

if __name__=="__main__":
    index = 0;
    cwd = os.getcwd()
    while (index < lttngMaxProvider):
        d = "lttngprov/lttngprov_"+str(index)
#        print(d)
        if os.path.exists(d):
            os.chdir(d)
            lttng_cmd_str_1 = "lttng create tp_session_%s > /dev/null"%(str(index))
            os.system(lttng_cmd_str_1)
            lttng_cmd_str_4 = "./tp_{0} &".format(str(index))
            os.system(lttng_cmd_str_4)
            lttng_cmd_str_2 = "lttng enable-event -u -s tp_session_{0} 'tp_{0}:*'".format(str(index))
            os.system(lttng_cmd_str_2)
            lttng_cmd_str_3 = "lttng start tp_session_%s"%(str(index))
            os.system(lttng_cmd_str_3)
#            print(cmd_str)
            os.chdir(cwd)
        index += 1
