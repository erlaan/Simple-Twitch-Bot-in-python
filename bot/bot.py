# -*- coding: utf-8 -*-
# Import libraries.
import socket

#Some varibles!
command = "I have no custom commands just now!"
command1 = "Empty"

# Some basic variables used to configure the bot
server = "irc.twitch.tv" # Server
password = "oauth:" # You get your OAuth key here http://twitchapps.com/tmi/
channel = "#channel" # Channel
botnick = "Nick" # Your bots nick

def ping(): # This is our first function! It will respond to server Pings.
  ircsock.send("PONG :pingis\n")

def sendmsg(chan , msg): # This is the send message function, it simply sends messages to the channel.
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n")

def joinchan(chan): # This function is used to join channels.
  ircsock.send("JOIN "+ chan +"\n")

def hello(): # This function responds to a user that inputs "Hello Mybot"
  ircsock.send("PRIVMSG "+ channel +" :Hello!\n")

def tyst(): # This function responds to a user that he gona be quiet!
  ircsock.send("PRIVMSG "+ channel +" :TYST!\n")

def hailsandia(): # ALL HAIL SANDIA!
  ircsock.send("PRIVMSG "+ channel  + " : ALL HAIL SAND1A! \n")


def cadd(cabb):
 global command
 global command1
 if command1 == "Empty" :
  command1 = cabb
 else :
  command1 = command1 + " , "  + cabb

 command = command1
 #return command
def commands():
 ircsock.send("PRIVMSG " + channel + " :" + command + "\n")

def ldel():
 global command
 global command1
 command = "I have no custom commands just now!"
 command1 = "Empty"

def rip():
 ircsock.send("PRIVMSG " + channel + " :Rest in PEACE! \n")

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
ircsock.send("PASS "+ password +"\n")
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :All hail Sandia!\n") # user authentication
ircsock.send("NICK "+ botnick +"\n") # here we actually assign the nick to the bot

joinchan(channel) # Join the channel using the functions we previously defined

while 1: # Be careful with these! it might send you to an infinite loop
  ircmsg = ircsock.recv(2048) # receive data from the server
  ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
  print(ircmsg) # Here we print what's coming from the server

  if ircmsg.find(":Hello "+ botnick) != -1: # If we can find "Hello Mybot" it will call the function hello()
    hello()

  if ircmsg.find(":hello ") != -1 :
    hello()

  if ircmsg.find(":*!")

  if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
    ping()


  if ircmsg.find(":!sandia") != -1:
    hailsandia()

  if ircmsg.find(":!command") != -1:
    commands()
  if ircmsg.find(":!cadd") != -1:
    cadd(ircmsg.split(":!cadd")[1])

  elif ircmsg.find(":!cdel") != -1:
    cdel()

  if ircmsg.find("QUIT") != -1:
    rip()
