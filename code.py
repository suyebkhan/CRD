import threading  # this is for python 3.0 and above. use import thread for python2.0 versions
from threading import *  # importing all functions of Threading
import time

d = {}  # 'd' is the dictionary(Data structure  key-value pair based) in which we are storing data.


# Create module

# timeout is optional you can continue by passing two arguments without timeout

def create(key, value, timeout=0):
    if key in d:
        print("error: this key already exists")  # error for redundancy.
    else:
        if (key.isalpha()):
            if len(d) < (1024 * 1020 * 1024) and value <= (
                    16 * 1024 * 1024):  # constraints for file size less than 1GB and Jasonobject value less than 16KB
                if timeout == 0:
                    l = [value, timeout]
                else:
                    l = [value, time.time() + timeout]
                if len(key) <= 32:  # constraints for input key_name capped at 32chars
                    d[key] = l
            else:
                print("error: Memory limit exceeded!! ")  # error for memory excceeding.
        else:
            print(
                "error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")  # input error


# for read operation

def read(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key")  # False error
    else:
        b = d[key]
        if b[1] != 0:
            if time.time() < b[1]:  # comparing the present time with expiry time
                stri = str(key) + ":" + str(
                    b[0])  # to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("error: time-to-live of", key, "has expired")  # time excceeding error.
        else:
            stri = str(key) + ":" + str(b[0])
            return stri


# for delete operation

def delete(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key")  # False error
    else:
        b = d[key]
        if b[1] != 0:
            if time.time() < b[1]:  # comparing the current time with expiry time
                del d[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of", key, "has expired")  # time excceeding error.
        else:
            del d[key]
            print("key is successfully deleted")


# I have an additional operation of modify in order to change the value of key before its expiry time if provided

# for modify operation


def modify(key, value):
    b = d[key]
    if b[1] != 0:
        if time.time() < b[1]:
            if key not in d:
                print("error: given key does not exist in database. Please enter a valid key")  # false error
            else:
                l = []
                l.append(value)
                l.append(b[1])
                d[key] = l
        else:
            print("error: time-to-live of", key, "has expired")  # time excceeding error
    else:
        if key not in d:
            print("error: given key does not exist in database. Please enter a valid key")  # false error
        else:
            l = []
            l.append(value)
            l.append(b[1])
            d[key] = l


# for checking emptiness of file
# using is_empty operation
def is_empty():
    if len(d) == 0:
        print("File is under underflow")  # underflow error

