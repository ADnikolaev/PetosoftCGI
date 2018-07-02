#!/usr/bin/env python3
# coding: utf-8
import urllib
import cgi
#import html
import subprocess
import os
import http.cookies
from createPage import createPage_
from _operate import Operate
###################

form = cgi.FieldStorage()
operate = Operate()
html = createPage_()

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
    html.goToLinkJs("http://" + operate.getIp() + ":8000/cgi-bin/videoOption.py")
    

else:

    login, password = operate.openAccountFile("/home/pi/Settings/account.txt")

    if nameCookie.value == login and passwCookie.value == password:
        
        #length, height, fps, rtmpServerIp, tcpServerIp = operate.parseSettingFile("/home/pi/Settings/videoSetting.txt")
        settingArray = operate.parseSettingFileDemo("/home/pi/Settings/videoSetting.txt")
        resolution = settingArray[0]
        fps = settingArray[1]
        rtmpServerIp= settingArray[2]
        
        #videoOptionBlock = html.createVideoOptionBlock("videoOption.py", length, height, fps, rtmpServerIp)
        videoOptionBlock = html.createVideoOptionBlock("videoOption.py", resolution, fps, rtmpServerIp)
        html.createHtmlPageOption(html.createCss(), html.mainJsFile(), videoOptionBlock)

        resolutionText = form.getfirst("RESOLUTION_TEXT", resolution).rstrip()
        #resolutionText = resolutionText.split('*')
        fpsText = form.getfirst("FPS_TEXT", fps).rstrip()
        rtmpText = form.getfirst("RTMP_TEXT", rtmpServerIp).rstrip()
        #tcpText = form.getfirst("TCP_TEXT", tcpServerIp)
        
        nameOnTheFormArray = ["RESOLUTION_TEXT","FPS_TEXT", "RTMP_TEXT"]
        valueOnTheFormArray = [resolutionText, fpsText, rtmpText]
        operate.writeSettingFileDemo("/home/pi/Settings/videoSetting.txt", nameOnTheFormArray, valueOnTheFormArray)

        #operate.writeSettingFile(resolutionText[0], resolutionText[1], fpsText, rtmpText)
        

    else:
    #elif nameCookie.value != login and passwCookie.value != password:  
        html.clearCookieJs()
        html.goToLinkJs("http://" + operate.getIp() + ":8000")
