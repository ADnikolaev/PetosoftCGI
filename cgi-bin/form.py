#!/usr/bin/env python3
# coding: utf-8
import urllib
import cgi
#import html
import subprocess
import os
import sys
import signal
import http.cookies
from _createHtml import CreateHtml
from _operate import Operate
###################

form = cgi.FieldStorage()
operate = Operate()
html = CreateHtml()

######################
#arraySettings = operate.parseSettingFileDemo("/home/pi/Settings/demo.txt")
#print(html.gpsSettingElem(arraySettings))
###################

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
nameCookie = cookie.get("name")
passwCookie = cookie.get("passw")

if nameCookie is None and passwCookie is None:
    loginText = form.getfirst("LOGIN", "" )
    passwordText = form.getfirst("PASSWORD", "" )
    print("set-cookie: name=" + loginText)
    print("set-cookie: passw=" + passwordText)
    nameCookie = cookie.get("name")
    passwCookie = cookie.get("passw")
    html.goToLinkJs("http://192.168.21.180:8000/cgi-bin/form.py")
    

else:

    login, password = operate.openAccountFile("/home/pi/Settings/account.txt")

    if nameCookie.value == login and passwCookie.value == password:
        
        length, height, fps, rtmpServerIp, tcpServerIp = operate.parseSettingFile("/home/pi/Settings/CameraSetting.txt")

        html.createHtmlPage(length, height, fps, rtmpServerIp, tcpServerIp)

        resolutionText = form.getfirst("RESOLUTION_TEXT", length +"*"+ height )
        resolutionText = resolutionText.split('*')
        fpsText = form.getfirst("FPS_TEXT", fps)
        rtmpText = form.getfirst("RTMP_TEXT", rtmpServerIp)
        tcpText = form.getfirst("TCP_TEXT", tcpServerIp)

        operate.writeSettingFile(resolutionText[0], resolutionText[1], fpsText, rtmpText, tcpText)

        ps = subprocess.Popen("ps -ax | grep simulatorgps | grep -v grep", shell=True, stdout=subprocess.PIPE)
        output = str(ps.stdout.read())
        outputNew = output.split(' ')
        print(outputNew)
        print(operate.openImg())
        #os.kill(int(outputNew[1]), signal.SIGKILL)
        #os.chmod("/home/pi/scriptsdemo/bashopen.py", 777)
        
        #os.system("python /home/pi/scriptsdemo/bashopen.py")
        
        #com = subprocess.Popen("python /home/pi/cgi/cgi-bin/bashopen.py", shell=True, stdout=subprocess.PIPE)
        #os.execle("sudo", 3986)
   
    else:
    #elif nameCookie.value != login and passwCookie.value != password:  
        html.clearCookieJs()
        html.goToLinkJs("http://192.168.21.180:8000")

    
    
   