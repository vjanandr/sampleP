#!/usr/bin/python3

multiline="""Hello world %(idx)s
one more %(idx)s let us check if this { okay what happens now } works"""
#print(multiline%{"idx":"vijay"})
multiline2="""Hello world {0}
one more {0} let us check if this {{ okay what happens now }} works"""
print(multiline2.format("vijay"))

