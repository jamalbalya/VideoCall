from vidstream import *
import tkinter as tk
import socket
import threading

local_ip_address = socket.gethostbyname(socket.gethostname())

server1 = StreamingServer(local_ip_address, 1313)
server2 = StreamingServer(local_ip_address, 1515)
receiver1 = AudioReceiver(local_ip_address, 1414)
receiver2 = AudioReceiver(local_ip_address, 1616)

def start_listening():
    j1 = threading.Thread(target=server1.start_server)
    j2 = threading.Thread(target=server2.start_server)
    j3 = threading.Thread(target=receiver1.start_server)
    j4 = threading.Thread(target=receiver2.start_server)
    j1.start()
    j2.start()
    j3.start()
    j4.start()

def start_camera_stream():
    camera_Client1 = CameraClient(text_target_ip.get(1.0,'end-1c'), 1515)
    camera_Client2 = CameraClient(text_target_ip.get(1.0,'end-1c'), 1313)
    j3 = threading.Thread(target=camera_Client1.start_stream)
    j4 = threading.Thread(target=camera_Client2.start_stream)
    j3.start()
    j4.start()

def start_screen_sharing():
    screen_client1 = ScreenShareClient(text_target_ip.get(1.0,'end-1c'), 1313)
    screen_client2 = ScreenShareClient(text_target_ip.get(1.0,'end-1c'), 1515)
    j5 = threading.Thread(target=screen_client1.start_stream)
    j6 = threading.Thread(target=screen_client2.start_stream)
    j5.start()
    j6.start()

def start_audio_stream():
    audio_sender1 = AudioSender(text_target_ip.get(1.0,'end-1c'), 1414)
    audio_sender2 = AudioSender(text_target_ip.get(1.0,'end-1c'), 1616)
    j7 = threading.Thread(target=audio_sender1.start_stream)
    j8 = threading.Thread(target=audio_sender2.start_stream)
    j7.start()
    j8.start()

# Grafic User Interface

window = tk.Tk()
window.title("VC by Jemz B v.1.0.0")
window.geometry('300x200')

Label_target_ip = tk.Label(window, text='Target IP:')
Label_target_ip.pack()

text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

button_listen = tk.Button(window, text="Start Listening", width=50, command=start_listening)
button_listen.pack(anchor=tk.CENTER, expand=True)

button_camera = tk.Button(window, text="Start Camera Stream", width=50, command=start_camera_stream)
button_camera.pack(anchor=tk.CENTER, expand=True)

button_screen = tk.Button(window, text="Start Screen Sharing", width=50, command=start_screen_sharing)
button_screen.pack(anchor=tk.CENTER, expand=True)

button_audio = tk.Button(window, text="Start Audio Stream", width=50, command=start_audio_stream)
button_audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()