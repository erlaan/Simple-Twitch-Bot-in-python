# -*- coding: utf-8 -*-
# Import libraries.
import socket

#Some varibles!
lab = "Har inga labbar just nu!"
lab1 = "TOM"

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

def mat(): # This function responds to a user wich food it is
  ircsock.send("PRIVMSG "+ channel + " :Read here for att decide dig vart du ska eat! http://lunchguide.nu/hudiksvall \n")

def matkebab(): #Fat kid!
  ircsock.send("PRIVMSG "+ channel + " :FAT KID!! \n")

def hailsandia(): # ALL HAIL SANDIA!
  ircsock.send("PRIVMSG "+ "#etiskhackare-15"  + " : ALL HAIL SAND1A! \n")

def jonte(msg):
  ircsock.send("PRIVMSG "+ channel + " :" + ' '.join([x for x in msg if x != x.upper()]) + "\n" )

def kick(user):
  ircsock.send("KICK "+ "#etiskhackare-15"  + " : " + user + "\n")

def msg(msg):
  ircsock.send("PRIVMSG "+ channel + " :" + msg + "\n")

def ladd(labb):
 global lab
 global lab1
 if lab1 == "TOM" :
  lab1 = labb
 else :
  lab1 = lab1 + " , "  + labb

 lab = lab1
 #return lab
def labs():
 ircsock.send("PRIVMSG " + channel + " :" + lab + "\n")

def ldel():
 global lab
 global lab1
 lab = "Har inga labbar just nu!"
 lab1 = "TOM"

def welcom():
 ircsock.send("PRIVMSG " + channel + " :Hello and Welcome To EtiskHackare-15! \n")

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

  if ircmsg.lower().find(":hello ") != -1 :
    hello()

  if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
    ping()

  if ircmsg.find(":!tyst") != -1:
    tyst()

  if ircmsg.find(":!mat kebab") != -1:
    matkebab()

  elif ircmsg.find(":!mat") != -1:
    mat()

  if ircmsg.find(":!sandia") != -1:
    hailsandia()

  if ircmsg.find(":!jonte") != -1:
    jonte(ircmsg.split(":!jonte")[1])

  if ircmsg.find(":!kick") != -1:
    kick(ircmsg.split(":!kick")[1])

  if ircmsg.find(":!send") != -1:
    msg(ircmsg.split(":!send")[1])

  if ircmsg.find(":!ladd") != -1:
    ladd(ircmsg.split(":!ladd")[1])

  elif ircmsg.find(":!ldel") != -1:
    ldel()

  elif ircmsg.find(":!labs") != -1:
    labs()

 # if ircmsg.find("JOIN") != -1:
  #  welcom()

  if ircmsg.find("QUIT") != -1:
    rip()
