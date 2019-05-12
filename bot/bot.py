# -*- coding: utf-8 -*-
# Import libraries.
import socket, random

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

def hello(msg): # This function responds to a user that inputs "Hello Mybot"
  name = username(msg)
  ircsock.send("PRIVMSG ".encode()+ channel +" :Hello ".encode() + name.encode() + "\n".encode())

def help(): # This will respond what commands that exist for the bot!
    ircsock.send("PRIVMSG ".encode() + channel +" :I have no commands righ now!".encode())

def roll(msg):
  rand = random.randint(1,100) #Here do we get a random int between 1 and 100
  randtostring = str(rand) #Here we convert the int to string
  name = username(msg)
  ircsock.send("PRIVMSG ".encode()+ channel + " :".encode() +name.encode() + " ".encode() + randtostring.encode() + "\n".encode())
def username(msg):
    msg = msg.split('!', 1) # first we remove everything after !
    msg = msg[0].split(':', 1) #Then we remove everything before :
    return(msg[1]) #And then we return the username to the caller

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, port)) # Here we connect to the server using the port 6667
ircsock.send("PASS ".encode() + password +"\n".encode()) # This send the password to the irc server
ircsock.send("USER ".encode() + botnick +" ".encode()+ botnick +" ".encode()+ botnick +" :All hail Sandia!\n".encode()) # user authentication
ircsock.send("NICK ".encode()+ botnick +"\n".encode()) # here we actually assign the nick to the bot

joinchan(channel) # Join the channel using the functions we previously defined

while 1: # Be careful with these! it might send you to an infinite loop
    ircmsg = ircsock.recv(2048) # receive data from the server
    ircmsg = ircmsg.strip('\n\r'.encode()) # removing any unnecessary linebreaks.
    print(ircmsg) # Here we print what's coming from the server

    if ircmsg.lower().find(":Hello ".lower().encode()+ botnick.lower()) != -1: # If we can find "Hello Mybot" it will call the function hello()
        hello(ircmsg.decode())
    elif ircmsg.lower().find(":Hi ".lower().encode()+ botnick.lower()) != -1:
        hello(ircmsg.decode())
    elif ircmsg.lower().find(":Hey ".lower().encode()+ botnick.lower()) != -1:
        hello(ircmsg.decode())

    if ircmsg.find("PING :".encode()) != -1: # if the server pings us then we've got to respond!
        ping()

    if ircmsg.find(":!help".encode()) != -1: # this looks for someone that want to know what commands exist
        help()

    if ircmsg.find(":!roll".encode()) != -1:
        roll(ircmsg.decode())
