from _operate import Operate

class createPage_:
    
    def createHtmlPageOption(self, css, js, OptionBlock):
        ip = Operate().getIp()
        print("Content-type: text/html\n") 
        print("""<!DOCTYPE html>
                    <html>
                        <head>
                        <meta charset="utf-8">
                        <title>Настройки GPS</title><style>""" + css+ """</style>""")
       
        print(""" </head>
                 <body>
                 <script type="text/javascript">""" + js + """</script>                
                     <div id="header">
                        <div><a class ="logo" >""" + Operate().openImg('/home/pi/cgi/cgi-bin/logoPetr.png') + """</a></div></div>
                        <div id = "headerLine">
                            <ul class="nav">
                                <li><a href="http://""" + ip + """:8000/cgi-bin/situation.py">Состояние</a></li>
                                <li><a href="http://""" + ip + """:8000/cgi-bin/networkOption.py">Настройки сети</a></li>
                                <li><a href="http://""" + ip +""":8000/cgi-bin/gpsOption.py">Настройки GPS</a></li>
                                <li><a href="http://""" + ip + """:8000/cgi-bin/videoOption.py">Настройки видео</a></li>
                                <li><a href="http://"""+ ip + """:8000/cgi-bin/appOption.py">Настройки входа</a></li>
                                <li><a href="http://""" + ip + """:8000" onclick="clearCookie(this)" >Выход</a></li>
                            </ul>
                        </div>""")

        print(""" <div id="login-form">""" + OptionBlock+ """</div>
                </body>
                </html>""")
        
    def createVideoOptionBlock(self, nameApps, resolution, fps, rtmpServerIp):
        videoOptionBlock=""" <h1>Настройки видео</h1>
                            <fieldset>
                                <form action="/cgi-bin/""" + nameApps + """" method="POST">
                                <div class="pain">
                                <div class = "field">
					<label style ="labe">Razrisshenie:</label><input type="text" name="RESOLUTION_TEXT" required value=""" + resolution + """>
				</div>
				<div class = "field">
					<label style ="labe">framerate:</label><input type="text" name="FPS_TEXT" required value=""" + fps + """>
                                </div>
				<div class = "field">
					<label style ="labe">IP адресс сервера видеозахвата:</label><input type="text" name="RTMP_TEXT"  required value=""" +rtmpServerIp + """>
                                </div>
				<input type="submit" value="Сохранить">
                            </div>
                            <footer class="clearfix">
                            </footer>
                            </form>
                            </fieldset>
"""
        return videoOptionBlock         
    
    def createGpsOptionBlock(self, nameApps, timezone, tcpServerIp):
        gpsOptionBlock=""" <h1>Настройки GPS</h1>
                            <fieldset>
                                <form action="/cgi-bin/""" + nameApps + """" method="POST">
                                <div class="pain">
                                <div class = "field">
					<label style ="labe">Chasovoy poyas:</label><input type="text" name="TIMEZONE_TEXT" required value=""" + timezone + """>
				</div>
				<div class = "field">
					<label style ="labe">IP адресс сервера geopozicii:</label><input type="text" name="TCP_TEXT"  required value=""" +tcpServerIp + """>
                                </div>
				<input type="submit" value="Сохранить">
                            </div>
                            <footer class="clearfix">
                            </footer>
                            </form>
                            </fieldset>
"""
        return gpsOptionBlock

    def createNetworkOptionBlock(self, nameApps, ssid, psk):
        networkOptionBlock=""" <h1>Настройки WiFi</h1>
                            <fieldset>
                                <form action="/cgi-bin/""" + nameApps + """" method="POST">
                                <div class="pain">
                                <div class = "field">
					<label style ="labe">WiFi SSID:</label><input type="text" name="SSID" required value=""" + ssid + """>
				</div>
				<div class = "field">
					<label style ="labe">WiFi password:</label><input type="text" name="PSK"  required value=""" +psk + """>
                                </div>
				<input type="submit" value="Сохранить">
                            </div>
                            <footer class="clearfix">
                            </footer>
                            </form>
                            </fieldset>
"""
        return networkOptionBlock
    
    def createAppOptionBlock(self, nameApps):
        appOptionBlock=""" <h1>Настройки application</h1>
                            <fieldset>
                                <form action="/cgi-bin/""" + nameApps + """" method="POST">
                                <div class="pain">
                                <div class = "field">
					<label style ="labe">Tecushiy logib ot prilozheniya:</label><input type="text" name="LOG" required value="">
				</div>
				<div class = "field">
					<label style ="labe">Tecushiy parol ot prilozheniya:</label><input type="text" name="PASSW"  required value="">
                                </div>
                                <div class = "field">
					<label style ="labe">Noviy logib ot prilozheniya:</label><input type="text" name="NEWLOG" required value="">
				</div>
				<div class = "field">
					<label style ="labe">Noviy parol ot prilozheniya:</label><input type="text" name="NEWPASSW"  required value="">
                                </div>
				<input type="submit" value="Сохранить">
                            </div>
                            <footer class="clearfix">
                            </footer>
                            </form>
                            </fieldset>
"""
        return appOptionBlock


    def createCss(self):
        css = """body {
	color: #999;
	font: 100%/1.5em sans-serif;
	margin: 0;
        }

        h1 { margin: 0; }

        a {
	color: #999;
	text-decoration: none;
        }

        a:hover { color: #1dabb8; }

        fieldset {
	border: none;
	margin: 0;
        }

        input {
	border: none;
	font-family: inherit;
	font-size: inherit;
	margin: 0;
	outline: none;
	-webkit-appearance: none;
        }

        input[type="submit"] { cursor: pointer; }

        .clearfix { *zoom: 1; }
        .clearfix:before, .clearfix:after {
	content: "";
	display: table;	
        }
        .clearfix:after { clear: both; }

    /* ---------- LOGIN-FORM ---------- */

        #login-form {
	margin: 40px auto;
	width: 680px;
        }

        #login-form h1 {
	background-color: #4E342E;	
	color: #ECEFF1;
	font-size: 14px;
	padding: 20px;
	text-align: center;
	text-transform: uppercase;
        }

        #login-form fieldset {
	background: #ECEFF1;	
	padding: 13px;
	position: relative;
        }

        #login-form fieldset:before {
	background-color: #ECEFF1;
	content: "";
	height: 8px;
	left: 50%;
	margin: -4px 0 0 -4px;
	position: absolute;
	top: 0;
	-webkit-transform: rotate(45deg);
	-moz-transform: rotate(45deg);
	-ms-transform: rotate(45deg);
	-o-transform: rotate(45deg);
	transform: rotate(45deg);
	width: 8px;
        }

        #login-form input {
	font-size: 14px;
        }

        #login-form input[type="text"],
        #login-form input[type="password"] {
	border: 1px solid #dcdcdc;
	padding: 12px 10px;
	width: 238px;
        }

        #login-form input[type="password"] {
	border-top: none;
	border-radius: 0px 0px 3px 3px;
	margin-top: 10px;
        }

        #login-form input[type="submit"] {
	background: #5D4037;	
	color: #fff;
	float: right;
	margin-right:215px;
	font-weight: bold;
	margin-top: 20px;
	padding: 12px 20px;
        }

        #login-form input[type="submit"]:hover { background: #c4c005; }

        #login-form footer {
	font-size: 12px;
	/* margin-top: 16px; */
        }

        @-webkit-keyframes slideOut{
	0%{top:-30px; opacity: 0;}
	100%{top:0px; opacity: 1;}
        }

        #header{ 
	background-color: white;          
	height: 250px;
        }
        #headerLine{ 
	/* background-color: #c4c005; */          
	height: 20px;
	/* margin: 5px 10% 5px  10%; */
        }

        .field {clear:both; text-align:right; line-height:40px; padding-top: 20px;}
         label {float:left; padding-left:10px; padding-right:10px; }
        .pain {float:left; padding-top: 0; padding-left: 40px;} 

        a.logo{
	margin-left: 38%;
	margin-top: 5px;
	}
 
 
        ul.nav{
        margin-left: 0px;
        padding-left: 0px;
        list-style: none;
        }
        .nav li { 
        float: left;
	 padding-left: 6%;
				
        }
        ul.nav a {
        display: block;
        /* width: 5em; */
        /* padding-left: 25px; */
        font-family: Arial Black;			
        text-decoration: none;
        color: #4E342E;				
        text-align: center;
        }
        ul.nav a:hover{
        /* background-color: #333; */
        color: #c4c005;
        }
"""
        return css
    
    def mainJsFile(self):
        js = """
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
                            alert('fuuuu');   
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

"""
        return js
    
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
        print("""</head>""")
        print("""</html>""")
