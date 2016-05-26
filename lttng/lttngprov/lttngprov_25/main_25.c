#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include "tp_25.h"
#include <lttng/tracef.h>

int main (int argc, char *argv[])
{
    int x;
    pid_t pid;

 //   puts("Hello, World!\nPress Enter to continue...");

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
    tracepoint(tp_25, my_first_tracepoint, (int)pid, "Process ID:");
    for (x = 0; x < 50; ++x) {
        tracepoint(tp_25, my_second_tracepoint, x, "x^2");
    }

  //  puts("Quitting now!");

    tracepoint(tp_25, my_third_tracepoint, x,
               "Checkout the third tracepoint");
//    tracef("my message, my integer: %d", 20);

   // puts("Press enter again");
   // getchar();

    return 0;
}
