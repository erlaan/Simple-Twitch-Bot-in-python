# -*- coding: utf-8 -*-
# Import libraries.
import socket

#Some varibles!
command = "I have no custom commands just now!"
command1 = "Empty"

# Some basic variables used to configure the bot
server = "irc.chat.twitch.tv" # Server
password = "oauth:".encode() # You get your OAuth key here https://twitchapps.com/tmi/
channel = "#channel".encode() # Channel
botnick = "Nick".encode() # Your bots nick
port = 6667

def ping(): # This is our first function! It will respond to server Pings.
  ircsock.send("PONG :pingis\n".encode())

def sendmsg(chan , msg): # This is the send message function, it simply sends messages to the channel.
  ircsock.send("PRIVMSG ".encode()+ chan +" :".encode()+ msg +"\n".encode())

def joinchan(chan): # This function is used to join channels.
  ircsock.send("JOIN ".encode()+ chan +"\n".encode())

def hello(): # This function responds to a user that inputs "Hello Mybot"
  ircsock.send("PRIVMSG ".encode()+ channel +" :Hello!\n".encode())

def help(): # This will respond what commands that exist for the bot!
    ircsock.send("PRIVMSG ".encode() + channel +" :I have no commands righ now!".encode())

def rip():
 ircsock.send("PRIVMSG ".encode() + channel + " :Rest in PEACE! \n".encode())

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, port)) # Here we connect to the server using the port 6667
ircsock.send("PASS ".encode() + password +"\n".encode())
ircsock.send("USER ".encode() + botnick +" ".encode()+ botnick +" ".encode()+ botnick +" :All hail Sandia!\n".encode()) # user authentication
ircsock.send("NICK ".encode()+ botnick +"\n".encode()) # here we actually assign the nick to the bot

joinchan(channel) # Join the channel using the functions we previously defined

while 1: # Be careful with these! it might send you to an infinite loop
  ircmsg = ircsock.recv(2048) # receive data from the server
  ircmsg = ircmsg.strip('\n\r'.encode()) # removing any unnecessary linebreaks.
  print(ircmsg) # Here we print what's coming from the server

  if ircmsg.find(":Hello ".encode()+ botnick) != -1: # If we can find "Hello Mybot" it will call the function hello()
    hello()

  if ircmsg.find("PING :".encode()) != -1: # if the server pings us then we've got to respond!
    ping()

  if ircmsg.find(":!help".encode()) != -1:
    help()

  if ircmsg.find("QUIT".encode()) != -1:
    rip()
