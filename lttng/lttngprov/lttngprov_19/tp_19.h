/** Trace point provider_19 */
#undef TRACEPOINT_PROVIDER
#define TRACEPOINT_PROVIDER tp_19

#undef TRACEPOINT_INCLUDE
#define TRACEPOINT_INCLUDE <tp_19.h>

#if !defined(_TP_19_H_) || defined (TRACEPOINT_HEADER_MULTI_READ)
#define _TP_19_H_

#include <lttng/tracepoint.h>

TRACEPOINT_EVENT(
    tp_19,
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
    tp_19,
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
    tp_19,
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

#endif /* _TP_19_H_ */

#include <lttng/tracepoint-event.h>

