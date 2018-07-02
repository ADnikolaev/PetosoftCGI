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
    html.goToLinkJs("http://" + operate.getIp() + ":8000/cgi-bin/networkOption.py")
    

else:

    login, password = operate.openAccountFile("/home/pi/Settings/account.txt")

    if nameCookie.value == login and passwCookie.value == password:
        
        #length, height, fps, rtmpServerIp, tcpServerIp = operate.parseSettingFile("/home/pi/Settings/videoSetting.txt")
        settingArray = operate.parseSettingFileDemo("/home/pi/Settings/wifiSetting.txt")
        ssid = settingArray[0]
        psk = settingArray[1]
                
        #videoOptionBlock = html.createVideoOptionBlock("videoOption.py", length, height, fps, rtmpServerIp)
        networkOptionBlock = html.createNetworkOptionBlock("networkOption.py", ssid, psk)
        html.createHtmlPageOption(html.createCss(), html.mainJsFile(), networkOptionBlock)

        ssidText = form.getfirst("SSID", ssid).rstrip()
        pskText = form.getfirst("PSK", psk).rstrip()
        
        nameOnTheFormArray = ["SSID","PSK"]
        valueOnTheFormArray = [ssidText, pskText]
        operate.writeSettingFileDemo("/home/pi/Settings/wifiSetting.txt", nameOnTheFormArray, valueOnTheFormArray)

   
    else:
    #elif nameCookie.value != login and passwCookie.value != password:  
        html.clearCookieJs()
        html.goToLinkJs("http://" + operate.getIp() + ":8000")