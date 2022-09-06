import tkinter
from tkinter import *
import socket
from threading import Thread

def recieve():
    while True:
        try:
            msg = s.recv(1024).decode('utf8')
            msg_list.insert(tkinter.END, msg)
        except:
            print("there is an error reciving massage message")
            
def send():
    msg = my_msg.get()
    my_msg.set("")
    s.send(bytes(msg,'utf8'))        
    if msg == '#quit':
        s.close()
        window.close()

def on_closing():
    my_msg.set("#quit")
    send()
    

        
window = Tk()
window.title("chat room application")
window.configure(bg="green")

message_frame = Frame(window,height = 100,width = 100,bg='red')
message_frame.pack()


my_msg = StringVar()
my_msg.set("")


scrol_bar = Scrollbar(message_frame)
msg_list = Listbox(message_frame,height =15,width=100,bg='red',yscrollcommand=scrol_bar.set)
scrol_bar.pack(side = RIGHT,fill=Y)
msg_list.pack(side =LEFT,fill=BOTH)
msg_list.pack()

label = Label(window,text="enter the message",fg='blue',font='Aeria',bg='red')
label.pack()

entry_field = Entry(window,textvariable=my_msg,fg='red',width=50)
entry_field.pack()

send_button = Button(window,text="send",font='Aeria',fg='white',command = send)
send_button.pack()

quiet_button = Button(window,text="queit",font='Aeria',fg='white',command =on_closing)
quiet_button.pack()

host = '127.0.0.1'
port =1023

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

recieve_Thread = Thread(target=recieve)
recieve_Thread.start()

mainloop()











