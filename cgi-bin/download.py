#!/usr/bin/env python3

#print("""Content-Type: application/octet-stream; name=\"track.txt\"\r\n""")
print("""Content-Type: application/octet-stream; name=\"FileName\"\r\n""")
print("""Content-Disposition: attachment; filename=\"FileName\"\r\n\n """)


##
##
##
fo = open("/home/pi/track0203.txt", "rb")
stri = fo.read()
##
print (stri)
##
fo.close
