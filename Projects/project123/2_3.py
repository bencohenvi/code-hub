-`0
+`0`from socket import *
-`1
+`1`import thread
-`2
+`2`import threading
-`3
+`3`import time
-`4
+`4`import sys
-`5
+`5`
-`6
+`6`
-`7
+`7`
-`8
+`8`
-`9
+`9`def get_open_port():
-`10
+`10`    s = socket(AF_INET, SOCK_STREAM)
-`11
+`11`    s.bind(("", 0))
-`12
+`12`    s.listen(1)
-`13
+`13`    port = s.getsockname() [1]
-`14
+`14`    s.close()
-`15
+`15`    return port
-`16
+`16`
-`17
+`17`
-`18
+`18`def save_information(serversock):
-`19
+`19`    import socket
-`20
+`20`    f = open("C:\\Users\Ben\Desktop\Details.txt", "w")
-`21
+`21`    f.write("pass123"+"\n"+str(PORT)+"\n"+get_ip())
-`22
+`22`
-`23
+`23`
-`24
+`24`def set_timer():
-`25
+`25`    clientsock.send("How much time in seconds? ")
-`26
+`26`    data = clientsock.recv(BUFSIZ)
-`27
+`27`    try:
-`28
+`28`        time.sleep(int(data))
-`29
+`29`        return"Timer Done"
-`30
+`30`    except:
-`31
+`31`        return "Invalid Input, Going back for the echo function"
-`32
+`32`
-`33
+`33`
-`34
+`34`def handler(clientsock, addr):
-`35
+`35`    while 1:
-`36
+`36`        data = clientsock.recv(BUFSIZ)
-`37
+`37`        print data
-`38
+`38`        if not data: break
-`39
+`39`        if data == "exit": break
-`40
+`40`        if data == "Current Time":
-`41
+`41`            data = "current time (of the server PC): " + str(datetime.datetime.now())
-`42
+`42`        if data == "Set a Timer":
-`43
+`43`                data = Set_A_Timer()
-`44
+`44`        clientsock.send(data)
-`45
+`45`    print "ending communication with",addr
-`46
+`46`    clientsock.close()
-`47
+`47`
-`48
+`48`BUFSIZ = 1024
+`49`HOST = get_ip()
+`50`PORT = get_open_port()
+`51`ADDR = (HOST, PORT)
+`52`serversock = socket(AF_INET, SOCK_STREAM)
+`53`serversock.bind(ADDR)
+`54`serversock.listen(2)
+`55`save_information(serversock)
+`56`print "Type This into the Client:\n IP = "+str(get_ip())+"\n PORT = "+str(PORT)
+`57`
+`58`while 1:
+`59`    print 'waiting for connection...'
+`60`    clientsock, addr = serversock.accept()
+`61`    print '...connected from:', addr
+`62`    thread.start_new_thread(handler, (clientsock, addr))
+`63`
