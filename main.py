# -*- coding: utf-8 -*-

import os
import sys
import socket
import logging
import webbrowser

REMOTE_SERVER = 'http://google.com' # server we will try to connect to
class CheckNet:
    """
    An object to check if there is a connection to the 
    internet by getting google.com address
    """ 
    def is_connected(self):
        address = REMOTE_SERVER
        try:
            # check if there is a DNS listening
            host = socket.gethostbyname(address)
            # check whether the host is reachable
            socket.create_connection((host, 80), 2)
            return True
        except:
            pass
        return False


def main():
    conn_attempt = CheckNet()
    if conn_attempt.is_connected:
        webbrowser.open(REMOTE_SERVER)
    else:
        print('not internet connection')


if __name__ == '__main__':
    main()












