import cgi 
import base64
import socket

class Operate:

    def openAccountFile(self, link):
        fileSettings = open(link, 'r')
        arraySettings = fileSettings.read()
        fileSettings.close()
        
        loginPassStr = arraySettings.split('|')
        login = loginPassStr[0].rstrip()
        password = loginPassStr[1].rstrip()
        
        return login, password
    
    def changeAccountFile(self, link, login, password):
        fileSettings = open(link, 'w')
        fileSetting.write(login + "|" + password)
        fileSetting.close()
              
        
    def parseSettingFile(self, link):
        fileSettings = open(link, 'r')
        arraySettings = fileSettings.readlines()
        fileSettings.close()    
        
        resolutionStr = arraySettings[0].split('|:')
        resolution = resolutionStr[1].rstrip().split('*')
        length = str(resolution[0])
        height = str(resolution[1])
        fpsStr = arraySettings[1].split('|:')
        fps = fpsStr[1].rstrip()
        rtmpServerIpStr = arraySettings[2].split('|:')
        rtmpServerIp=rtmpServerIpStr[1].rstrip()
        tcpServerIpStr = arraySettings[3].split('|:')
        tcpServerIp=tcpServerIpStr[1].rstrip()
        
        return length, height, fps, rtmpServerIp, tcpServerIp


    def writeSettingFile(self, length, height, fps, rtmpServerIp, tcpServerIp):
    
        resolutionStr = "resolution|:" + length +"*"+ height
        fpsStr = "framerate|:" + fps
        rtmpServerIpStr = "rtmp_server_ip|:" + rtmpServerIp 
        tcpServerIpStr = "tcp_server_ip|:" + tcpServerIp

        listSetting = [resolutionStr, fpsStr, rtmpServerIpStr, tcpServerIpStr]
    
        fileSettingsNew = open("/home/pi/Settings/CameraSetting.txt", 'w')
        for index in listSetting:
            fileSettingsNew.write(index + "\n")
        fileSettingsNew.close  
        return True
    
    
    def parseSettingFileDemo(self, link):
        fileSettings = open(link, 'r')
        arraySettings = fileSettings.readlines()
        newArraySettings = []
        for line in arraySettings:
             newArraySettings.append(line.split("|:")[1])
        fileSettings.close()
        return  newArraySettings
            
        
    def writeSettingFileDemo(self, link, nameOnTheInputForm, valueOnTheInputForm):
    
        #listSetting = [resolutionStr, fpsStr, rtmpServerIpStr, tcpServerIpStr]        
        fileSettingsNew = open(link, 'w')
       
        i=0
        for value in valueOnTheInputForm:
            fileSettingsNew.write(str(nameOnTheInputForm[i]) + "|:" + value+"\n")
            i = i+1
        fileSettingsNew.close()
        
        
    def openImg(self, link):
        data_uri = base64.b64encode(open(link, 'rb').read()).decode('utf-8').replace('\n', '')
        img_tag = '<img src="data:image/png;base64,%s">' % data_uri 
        return img_tag
    
    def getIp(self): 
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        try: 
            # doesn't even have to be reachable 
            s.connect(('10.255.255.255', 1)) 
            ipAddress = s.getsockname()[0] 
        except: 
            ipAddressip = '127.0.0.1' 
        finally: 
            s.close() 
        return ipAddress
