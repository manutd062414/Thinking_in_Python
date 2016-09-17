'''
Created on Sep 17, 2016

@author: omega
'''

def do_twice(f, str):
    f(str)
    f(str)

def print_spam(str):
    print str

def do_four(f, str):
    do_twice(f, str)
    do_twice(f, str)
    
do_four(print_spam, 'spam')