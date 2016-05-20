#!/usr/bin/python3
import os
import shutil

prov_header="""/** Trace point provider_{0} */
#undef TRACEPOINT_PROVIDER
#define TRACEPOINT_PROVIDER tp_{0}

#undef TRACEPOINT_INCLUDE
#define TRACEPOINT_INCLUDE <tp_{0}.h>

#if !defined(_TP_{0}_H_) || defined (TRACEPOINT_HEADER_MULTI_READ)
#define _TP_{0}_H_

#include <lttng/tracepoint.h>

TRACEPOINT_EVENT(
    tp_{0},
    my_first_tracepoint,
    TP_ARGS(
        int, my_integer_arg,
        char*, my_string_arg
    ),
    TP_FIELDS(
        ctf_string(my_first_string_field, my_string_arg)
        ctf_integer(int, my_first_integer_field, my_integer_arg)
    )
)
TRACEPOINT_EVENT(
    tp_{0},
    my_second_tracepoint,
    TP_ARGS(
        int, my_integer_arg,
        char*, my_string_arg
    ),
    TP_FIELDS(
        ctf_string(my_second_string_field, my_string_arg)
        ctf_string(my_second_string_field_2, my_string_arg)
        ctf_integer(int, my_second_integer_field, my_integer_arg)
    )
)

TRACEPOINT_EVENT(
    tp_{0},
    my_third_tracepoint,
    TP_ARGS(
        int, my_int_arg,
        char*, my_str_arg
    ),
    TP_FIELDS(
        /* simple integer field with constant value */
        ctf_integer(
            int,                    /* field C type */
            my_constant_field,      /* field name */
            23 + 17                 /* argument expression */
        )

        /* my_int_arg tracepoint argument */
        ctf_integer(
            int,
            my_int_arg_field,
            my_int_arg
        )

        /* my_int_arg squared */
        ctf_integer(
            int,
            my_int_arg_field2,
            my_int_arg * my_int_arg
        )

        /* sum of first 4 characters of my_str_arg */
        ctf_integer(
            int,
            sum4,
            my_str_arg[0] + my_str_arg[1] +
            my_str_arg[2] + my_str_arg[3]
        )

        /* my_str_arg as string field */
        ctf_string(
            my_str_arg_field,       /* field name */
            my_str_arg              /* argument expression */
        )

        /* half of my_str_arg string as text sequence */
        ctf_sequence_text(
            char,                   /* element C type */
            half_my_str_arg_field,  /* field name */
            my_str_arg,             /* argument expression */
            size_t,                 /* length expression C type */
            strlen(my_str_arg) / 2  /* length expression */
        )
    )
)

#endif /* _TP_{0}_H_ */

#include <lttng/tracepoint-event.h>

"""

prov_c="""
#define TRACEPOINT_CREATE_PROBES
#define TRACEPOINT_DEFINE

#include "%s"\n"""


main_c="""#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include "tp_{0}.h"
#include <lttng/tracef.h>

int main (int argc, char *argv[])
{{
    int x;
    pid_t pid;

 //   puts("Hello, World!\\nPress Enter to continue...");

    /*
     * The following getchar() call is only placed here for the purpose
     * of this demonstration, for pausing the application in order for
     * you to have time to list its events. It's not needed otherwise.
     */
//    getchar();
     sleep(50);

    /*
     * A tracepoint() call. Arguments, as defined in hello-tp.h:
     *
     *     1st: provider name (always)
     *     2nd: tracepoint name (always)
     *     3rd: my_integer_arg (first user-defined argument)
     *     4th: my_string_arg (second user-defined argument)
     *
     * Notice the provider and tracepoint names are NOT strings;
     * they are in fact parts of variables created by macros in
     * hello-tp.h.
     */
    pid = getpid();
    tracepoint(tp_{0}, my_first_tracepoint, (int)pid, "Process ID:");
    for (x = 0; x < 50; ++x) {{
        tracepoint(tp_{0}, my_second_tracepoint, x, "x^2");
    }}

  //  puts("Quitting now!");

    tracepoint(tp_{0}, my_third_tracepoint, x,
               "Checkout the third tracepoint");
    tracef("my message, my integer: %d", 20);

   // puts("Press enter again");
   // getchar();

    return 0;
}}
"""

lttng_provider_cnt_fp = open("lttng_provider_cnt","r")
lttngMaxProvider=int(lttng_provider_cnt_fp.read())
lttng_provider_cnt_fp.close()

tp_h_f = ""
def providerGen(index):
    global tp_h_f
    # TP_H file
    tp_h_f = "tp_"+str(index)+".h"
    # Open TP_H file
    tp_h_fp = open(tp_h_f, "w")
    tp_h_fp.write(prov_header.format(str(index)))
    # Close TP_H file
    tp_h_fp.close()
    # TP_C file
    tp_c_f = "tp_"+str(index)+".c"
    # Open TP_C file
    tp_c_fp = open(tp_c_f, "w")
    tp_c_fp.write(prov_c%(tp_h_f))
    tp_c_fp.close()
    return

def mainGen(index):
    main_f = "main_"+str(index)+".c"
    main_f_fp = open(main_f, "w")
    dict={"idx":str(index)}
    main_f_fp.write(main_c.format(str(index)))
    main_f_fp.close()
    return

def provInit(index):
    d = "lttngprov/lttngprov_"+str(index)
    #Get the current working directory
    cwd  = os.getcwd()
    if os.path.exists(d):
        # Remove provider directory if it already exists
        shutil.rmtree(d, ignore_errors=True)
    #Create a new provider directoy
    os.makedirs(d)
    os.chdir(d)
    providerGen(index)
    mainGen(index)
    os.chdir(cwd)
    return

if __name__=="__main__":
    d = "lttngprov"
    if not os.path.exists(d):
        os.makedirs(d)
    i = 0;
    while (i < lttngMaxProvider):
        provInit(i)
        i+=1
