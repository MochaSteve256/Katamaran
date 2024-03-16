import tkinter as tk   #
import os              #
import pygame as pg    #
import random          # Bibliotheken (Module) einbinden
import math            #
import subprocess      #
import socket          #
import threading       #
TCP_IP = '172.20.10.6'                                  #
TCP_PORT = 5000                                         #
BUFFER_SIZE = 1024                                      # Socket-Objekt
running = True                                          #
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #
#s.connect((TCP_IP, TCP_PORT))                           #
connected = True
w, h = 400, 400
a = 0
def ms():
    global a
    while running:
        a = s.recv(5).decode("utf-8")
        a = int(a)
        if a > 451:
            a = 450
def ex():            #
    global running   #
    pg.quit()        # Definition zum Beenden des Programms
    root.destroy()   #
    running = False  #
def foto():                        #
    socket                         # Definitionen zum Fotos und Videos aufnehmen (noch nicht fertig)
def vid():                         #
    socket                         #
def rexec():             #
    global d             # Funktion zum Übernehmen des ausgewählten Radiobuttons von den Radar-Einstellungen
    d = rsettings.get()  #
root = tk.Tk()                                        # Basis-Einstellungen vom TKInter-Fenster
root.title("Katamaran mit Kamera und Radar")          #
radarframe = tk.Frame(root, width=w, height=h, relief="ridge", borderwidth=2)                        # Radar-Platz (mit PyGame)
radarframe.grid(row=1, column=0, padx=10, pady=10, columnspan=2)                                     #
xtermframe = tk.Frame(root, width=400, height=100, relief="ridge", borderwidth=2)      #
xtermframe.grid(row=4, column=0, padx=10, pady=10, columnspan=2)                          # Terminal-Platz (xterm)
xtermframeid = xtermframe.winfo_id()                                                   #
os.chdir("/")                                                                          #
subprocess.call("xterm -into %d &" % xtermframeid, shell=True)                         #
camframe = tk.Frame(root, width=200, height=150, relief="ridge", borderwidth=2)               #
camframe.grid(row=3, column=0, padx=15, pady=10, sticky="N")                                  # Kamera-Platz (mit MPlayer und NetCat)
camframeid = camframe.winfo_id()                                                              #
rsframe = tk.Frame(root, relief="ridge", borderwidth=2)                                             #
rsframe.grid(row=1, column=2, padx=10, pady=10, sticky='N', rowspan=2)                              #
rsettings = tk.IntVar()                                                                             #
tk.Label(rsframe, text="Radius des Radars", padx=5, pady=5).grid(row=0, column=0)                   #
rb1 = tk.Radiobutton(rsframe, text='1 Meter', variable=rsettings, value='4')                        #
rb2 = tk.Radiobutton(rsframe, text='2 Meter', variable=rsettings, value='8')                        # Radar-Einstellungen
rb3 = tk.Radiobutton(rsframe, text='4 Meter', variable=rsettings, value='16')                       #
tk.Button(rsframe, text="Übernehmen", command=rexec).grid(row=4, column=0, padx=10, pady=10)        #
rb1.grid(row=3, column=0, sticky='W')                                                               #
rb2.grid(row=2, column=0, sticky='W')                                                               #
rb3.grid(row=1, column=0, sticky='W')                                                               #
csframe = tk.Frame(root, relief="ridge", borderwidth=2)                                                               #
csframe.grid(row=2, column=1, padx=10, pady=10, sticky="N", rowspan=2)                                                #
tk.Button(csframe, text="Foto!", command=foto, padx=20, pady=20).grid(row=2, column=0, padx=10, pady=10)              #
tk.Button(csframe, text="Video\nStart/Stopp!", command=vid, padx=20, pady=20).grid(row=3, column=0, padx=10, pady=10) # Kamera-Einstellungen
e = tk.Entry(csframe)                                                                                                 #
e.insert(0, "/home/pi")                                                                                               #
e.grid(row=1, column=0)                                                                                               #
tk.Label(csframe, text="Speicherpfad:").grid(row=0, column=0)                                                         #
tk.Label(root, text="Bildvorschau:\n(verzögert!)").grid(row=2, column=0)                                              #
tk.Button(root, text="Beenden", command=ex).grid(row=0, column=5)
#subprocess.call("nc -l -p 5002 | mplayer -fps 32 -cache 32 -cache-min 1 -wid %d - &" % camframeid, shell=True) # Video-Empfang und -Abbildung
os.environ['SDL_WINDOWID'] = str(radarframe.winfo_id())  #
root.update()                                            #
pg.display.init()                                        #
pg.font.init()                                           #
screen = pg.display.set_mode((w,h))                      # Anderer gemischter Kram
screen.fill(pg.Color(255,255,255))                       #
angle = 0                                                #
d = 16                                                   #
running = True                                           #
rsettings.set(d)                                         #
f = 0                                                    #
a = 0                                                    #
measure = threading.Thread(target=ms)                    #
measure.start()                                          #
screen.fill((0,0,0))                              #
pg.draw.circle(screen, (0,0,0), (200,200),200)    #
pg.draw.circle(screen, (80,80,80), (200,200),200) # Ringe und Striche vom PyGame-Radar
pg.draw.circle(screen, (0,80,0), (200,200),150)   #
pg.draw.circle(screen, (80,80,0), (200,200),100)  #
pg.draw.circle(screen, (80,0,0), (200,200),50)    #
while running:
    #if not connected:
    #    s.connect((TCP_IP, TCP_PORT))
    #    connected = True
    if angle == 720:
        angle = 0
    print(a, "cm")
    a = int(a)
    a = a / 25 * 200 / d
    #a = random.randint(25, 450) #
    #if a > 400:                 # Dieser Bereich ist nur vorübergehend ein Zufallsagenerator als Radar-Daten-Quelle, da der echte sensor noch nicht angebaut und programmiert ist.
    #    a = 400                 #
    #a = a / 25 * 200 / d        #
    pg.draw.circle(screen, (255,255,255), (200,200),150, 1)
    pg.draw.circle(screen, (255,255,255), (200,200),100, 1)
    pg.draw.circle(screen, (255,255,255), (200,200),50, 1)
    pg.draw.circle(screen, (255,255,255), (200,200),200, 1)
    pg.draw.line(screen, (255,255,255), [200, 0], [200, 400])
    pg.draw.line(screen, (255,255,255), [0, 200], [400, 200])
    pg.draw.line(screen, (255,255,255), [0, 400], [400, 0])
    pg.draw.line(screen, (255,255,255), [0, 0], [400, 400])
    c = pg.font.SysFont('lato', 16)
    t1 = c.render("1/4", True, (255,255,255))
    t2 = c.render("2/4", True, (255,255,255))
    t3 = c.render("3/4", True, (255,255,255))
    t4 = c.render("4/4", True, (255,255,255))
    screen.blit(t1, [220, 200])
    screen.blit(t2, [270, 200])
    screen.blit(t3, [320, 200])
    screen.blit(t4, [370, 200])
    angle += 0.5
    angle2 = angle + 10
    angle3 = angle2 + 1
    radar = (200,200)
    radar_len = a
    radar2_len = 50
    radar5_len = 200
    x = radar[0] + math.cos(math.radians(angle)) * int(radar_len)
    y = radar[1] + math.sin(math.radians(angle)) * int(radar_len)
    x2 = radar[0] + math.cos(math.radians(angle2)) * radar2_len
    y2 = radar[1] + math.sin(math.radians(angle2)) * radar2_len
    radar2 = (x2, y2)
    x3 = radar2[0] + math.cos(math.radians(angle2)) * radar2_len
    y3 = radar2[1] + math.sin(math.radians(angle2)) * radar2_len
    radar3 = (x3, y3)
    x4 = radar3[0] + math.cos(math.radians(angle2)) * radar2_len
    y4 = radar3[1] + math.sin(math.radians(angle2)) * radar2_len
    radar4 = (x4, y4)
    x5 = radar4[0] + math.cos(math.radians(angle2)) * radar2_len
    y5 = radar4[1] + math.sin(math.radians(angle2)) * radar2_len
    radar5 = (x5, y5)
    x6 = radar5[0] + math.cos(math.radians(angle2)) * radar5_len
    y6 = radar5[1] + math.sin(math.radians(angle2)) * radar5_len
    x7 = radar[0] + math.cos(math.radians(angle3)) * radar5_len
    y7 = radar[1] + math.sin(math.radians(angle3)) * radar5_len
    pg.draw.circle(screen, (0,255,0), (round(x),round(y)), 2)
    pg.draw.line(screen, (80,0,0), radar, (x2,y2), 3)
    pg.draw.line(screen, (80,80,0), radar2, (x3,y3), 3)
    pg.draw.line(screen, (0,80,0), radar3, (x4,y4), 3)
    pg.draw.line(screen, (80,80,80), radar4, (x5,y5), 3)
    pg.draw.line(screen, (0,0,0), radar5, (x6,y6), 5)
    pg.draw.line(screen, (0,255,0), radar, (x7,y7), 1)
    pg.display.flip()
    root.update()
    #s.close()
    #connected = False