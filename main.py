# -*- coding: utf-8 -*-

import wx
import os
import sys
import socket
import logging
import threading
import webbrowser

REMOTE_SERVER = 'http://google.com' # server we will try to connect to
class CheckNet:
    def __init__(self, parent, *args, **kwargs):
        super(CheckNet, self).__init__(parent, *args, **kwargs)

        panel = wx.Panel(self)
        button = wx.Button(panel, label='Check Connection')
        hsizer = wx.BoxSizer()
        hsizer.AddStretchSpacer()
        hsizer.Add(button, 0, wx.ALIGN_CENTER) 
        hsizer.AddStretchSpacer()
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(hsizer, 1, wx.ALIGN_CENTER_HORIZONTAL)
        panel.SetSizer(vsizer)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Bind(wx.EVT_BUTTON, self.is_connected, button)

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

    def onButton(self, event):
        style = wx.OK
        if self.is_connected:
            message = wx.MessageBox('Internet connection available!!', style)
        message = wx.MessageBox('No internet connection.!!!')
        if message:
            print('Thanks for using net checker')


if __name__ == '__main__':
    app = CheckNet(False)
    app.MainLoop()



# def main():
#     conn_attempt = CheckNet()
#     if conn_attempt.is_connected:
#         webbrowser.open(REMOTE_SERVER)
#     else:
#         print('not internet connection')


# if __name__ == '__main__':
#     main()












