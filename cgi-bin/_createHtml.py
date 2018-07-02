
class CreateHtml:
         
    def createHtmlPage(self, resolution1, resolution2, fps, rtmpServerIp, tcpServerIp):
        #<meta http-equiv="Refresh" content="1"/>
        print("Content-type: text/html\n") 
        print("""<!DOCTYPE HTML>
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>Настройки</title>
                    <style type = "text/css">
                    #hat{
                    with: 100%;
                    background: #009933;
                    height: 30px;
                    padding: 5px;
                    }
                    .hatname{                  
                    font: Geneva;
                    font-size: 18px;
                    color: white;
                    float: left;
                    margin: 15px 3px 3px 3px;
                    }                   
                    .hatlogout{                  
                    font: Geneva;
                    font-size: 12px;
                    float: right;
                    margin: 20px;                  
                    }                    
                    A:hover
                    {color:#ffffff;
                    }        
                    #body{
                    position: relative;
                    with: 300%;
                    background: #c0c0c0;
                    padding: 5px;
                    }
                    #element{                  
                    background: #ffffff;                  
                    padding: 5px;
                    }
                    .inputstr1{
                    width: 100px;                  
                    float: left;
                    }
                    .inputstr2{
                    width: 200px;                    
                    float: left;
                    }
                    .inputstr3{
                    clear: both;
                    padding: 5px;
                    }
                    a {
                    color: #145a32;
                    }
                    a:hover {
                    color: white;
                    }
                    </style>
                </head>
                    <body>""")#document.cookie="entrance=1; path=/;";
        print("""       <script type="text/javascript">
                            document.cookie="entrance=1; path=/;";
                            var L=parseInt(getCookie("loaded")); 
                            if (L==0)
                            { 
                            locs(); 
                            document.cookie="loaded=1; path=/;"; 
                             } 
                            else
                            { 
                            document.cookie="loaded=0; path=/;"; 
                            }
                            
                            function locs()
                            {
                            location.reload();
                            } //Адрес для второй загрузки
                            
                            function getCookie(name)
                            { 
                            var nameEQ = name + "="; 
                            var ca = document.cookie.split(';'); 
                            for (var i = 0; i < ca.length; i++)
                            { 
                            var c = ca[i]; 
                            while (c.charAt(0) == ' ') c = c.substring(1, c.length); 
                            if (c.indexOf(nameEQ) == 0)
                            return c.substring(nameEQ.length, c.length) 
                            } 
                            return 0 
                            }
                            
                            function clearCookie()
                            {
                            //alert('fuuuu');
        
                            document.cookie="entrance=0; path=/;";
                            deleteCookie('passw');
                            deleteCookie('name');
                            deleteCookie('entrance');
                            
                            }                           
                            function deleteCookie(cookie_name)
                            {
                            var cookie_date = new Date ();
                            cookie_date.setTime (cookie_date.getTime() - 1);
                            document.cookie = cookie_name +="=; expires=" + cookie_date.toGMTString();
                            }
                            </script>""")
        
        print("""<form action="/cgi-bin/form.py" method="POST">""")
        
        print("""<div id="hat">
                    <div class="hatname">GPS OPTION</div>
                    <div class ="hatlogout"><a href="http://192.168.18.10:8000" style="text-decoration: none;" onclick="clearCookie(this)">Log out</a></div>
                </div>""")
        
        print("""<div id="body">""")
        
        print("""<div id="element">""")
        print("""<div class = "inputstr3">
                    <div class="inputstr1"> Resolution:</div>
                    <div class="inputstr2"><input class="inputstr2 type="text" name="RESOLUTION_TEXT" value=""" + resolution1 +"*" + resolution2+ """></div>
                </div>""")
        print("""<div class = "inputstr3">
                    <div class="inputstr1"> Framerate:</div>
                    <div class="inputstr2"><input class="inputstr2" type="text" name="FPS_TEXT" value=""" + fps + """></div>
                 </div> """)
        print("""<div class = "inputstr3">
                    <div class="inputstr1"> RTMP server:</div>
                    <div class="inputstr2"><input class="inputstr2 name="RTMP_TEXT" value=""" +rtmpServerIp + """></div>
                 </div>""")
        print("""<div class = "inputstr3">
                    <div class="inputstr1"> TCP server:</div>
                    <div class="inputstr2"><input class="inputstr2 type="text" name="TCP_TEXT" value=""" + tcpServerIp + """></div>
                </div>""")
        
        #print(""" <div class="inputstr2"><a download="track.txt" href="http://192.168.18.10:8000/cgi-bin/track0503.txt">track</a></div>""")
        print("""<div class = "inputstr3">
                    <div><input type="submit" value = Save></div>
                </div>""")
        
        print("""</div>""")
        
        print("""</div>""")

        print("""</form>""")

        print("""</body></html>""")
        
        
    def goToLinkJs(self, link):
        print("Content-type: text/html\n") 
        print("""<!DOCTYPE HTML>""")
        print("""<html>""")
        print("""<head>""")
        print("""<script language = "JavaScript" type="text/javascript">document.location.href=" """+ link + """ "</script>""")
        print("</head>")
        print("</html>")
        
        
    def clearCookieJs(self):
        print("Content-type: text/html\n") 
        print("""<!DOCTYPE HTML>""")
        print("""<html>""")
        print("""<head>""")
        print("""<script language = "JavaScript" type="text/javascript">      
        delete_cookie("name");
        delete_cookie("passw");
        delete_cookie("entrance");
        function delete_cookie (cookie_name)
        {
        var cookie_date = new Date ();
        cookie_date.setTime (cookie_date.getTime() - 1);
        document.cookie = cookie_name +="=; expires=" + cookie_date.toGMTString();
        }
        </script>""")
        print("</head>")
        print("</html>")



    def gpsSettingElem(self, arraySettings):
        elemStart = """<div id="element">"""
        for lines in arraySettings:
            elemStart +="""<div class = "inputstr3">
                                <div class="inputstr1">""" +  lines[0] + """</div>
                                <div class="inputstr2"><input class="inputstr2 type="text" name=""" +'"'+ lines[0].rstrip() + '"'+""" value=""" + lines[1].rstrip() + """></div>
                            </div>"""
                                     
        elemEnd = """<div class = "inputstr3">
                            <div><input type="submit" value = Save></div>
                        </div>"""
            #print(""" <div class="inputstr2"><a download="track.txt" href="http://192.168.18.10:8000/cgi-bin/track0503.txt">track</a></div>""")
        
        gpsSetElem = elemStart + elemEnd
        return gpsSetElem
    
    
    def createHtmlPattern(self, css, javaScripts, pageElem):
        #<meta http-equiv="Refresh" content="1"/>
        print("Content-type: text/html\n") 
        print("""<!DOCTYPE HTML>
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>Настройки</title>
                    <style type = "text/css">"""
              + css +
              """</style>
                </head>
                    <body>""")
        print("""<script type="text/javascript">"""
              + javaScripts +
                """</script>""")
        
        print("""<form action="/cgi-bin/gpsoption.py" method="POST">""")
        
        print("""<div id="hat">
                    <div class="hatname">GPS OPTION</div>
                    <div class ="hatlogout"><a href="http://192.168.18.10:8000" style="text-decoration: none;" onclick="clearCookie(this)">Log out</a></div>
                </div>""")
        
        print("""<div id="body">""")
        
        print(pageElem)
        
        print("""</div>""")
        
        print("""</div>""")

        print("""</form>""")

        print("""</body></html>""")
        
        
    def createJavaScripts(self):
        js ="""//document.cookie="entrance=1; path=/;";                       
                function locs()
                {
                location.reload();
                } //Адрес для второй загрузки
                            
                function getCookie(name)
                { 
                    var nameEQ = name + "="; 
                    var ca = document.cookie.split(';'); 
                    for (var i = 0; i < ca.length; i++)
                    { 
                    var c = ca[i]; 
                    while (c.charAt(0) == ' ')
                        c = c.substring(1, c.length); 
                        if (c.indexOf(nameEQ) == 0)
                            return c.substring(nameEQ.length, c.length) 
                    } 
                return 0 
                }
                            
                function clearCookie()
                {
                    //alert('fuuuu');
        
                    document.cookie="entrance=0; path=/;";
                    deleteCookie('passw');
                    deleteCookie('name');
                    deleteCookie('entrance');
                            
                }                           
                function deleteCookie(cookie_name)
                {
                    var cookie_date = new Date ();
                    cookie_date.setTime (cookie_date.getTime() - 1);
                    document.cookie = cookie_name +="=; expires=" + cookie_date.toGMTString();
                }"""     
        return js
        
    def createCss(self):
    
        css ="""
                #hat{
                with: 100%;
                background: #009933;
                height: 50px;
                padding: 5px;
                }
                .hatname{                  
                font: Geneva;
                font-size: 18px;
                color: white;
                float: left;
                margin: 15px 3px 3px 3px;
                }                   
                .hatlogout{                  
                font: Geneva;
                font-size: 12px;
                float: right;
                margin: 20px;                  
                }                    
                A:hover
                {color:#ffffff;
                }        
                #body{
                position: relative;
                with: 300%;
                background: #c0c0c0;
                padding: 5px;
                }
                #element{                  
                background: #ffffff;                  
                padding: 5px;
                }
                .inputstr1{
                width: 100px;                  
                float: left;
                }
                .inputstr2{
                width: 200px;                    
                float: left;
                }
                .inputstr3{
                clear: both;
                padding: 5px;
                }
                a {
                color: #145a32;
                }
                a:hover {
                color: white;
                }"""
        return css
    
    