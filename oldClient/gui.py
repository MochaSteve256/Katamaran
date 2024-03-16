import tkinter as tk
import os
import pygame as pg
import subprocess
import cam
import radar

w, h = 400, 400
root = tk.Tk()                                        # Basis-Einstellungen vom TKInter-Fenster
root.title("Katamaran mit Kamera und Radar")          #
radarframe = tk.Frame(root, width=w, height=h, relief="ridge", borderwidth=2)                        # Radar-Platz (mit PyGame)
radarframe.grid(row=1, column=0, padx=10, pady=10, columnspan=2)                                     #
xtermframe = tk.Frame(root, width=400, height=100, relief="ridge", borderwidth=2)      #
xtermframe.grid(row=4, column=0, padx=10, pady=10, columnspan=2)                       # Terminal-Platz (xterm)
xtermframeid = xtermframe.winfo_id()                                                   #
os.chdir("/")                                                                          #
subprocess.call("xterm -into %d &" % xtermframeid, shell=True)                         #
camframe = tk.Frame(root, width=200, height=150, relief="ridge", borderwidth=2)               #
camframe.grid(row=3, column=0, padx=15, pady=10, sticky="N")                                  # Kamera-Platz (mit MPlayer und NetCat)
camframeid = camframe.winfo_id()                                                              #
rsframe = tk.Frame(root, relief="ridge", borderwidth=2)                                             #
rsframe.grid(row=1, column=2, padx=10, pady=10, sticky='N', rowspan=2)                              #
rsettings = tk.IntVar()                                                                             #
rsettings.set(16)                                                                                   #
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
tk.Button(csframe, text="Foto!", command=cam.foto, padx=20, pady=20).grid(row=2, column=0, padx=10, pady=10)              #
tk.Button(csframe, text="Video\nStart/Stopp!", command=cam.vid, padx=20, pady=20).grid(row=3, column=0, padx=10, pady=10) # Kamera-Einstellungen
e = tk.Entry(csframe)                                                                                                 #
e.insert(0, "/home/pi")                                                                                               #
e.grid(row=1, column=0)                                                                                               #
tk.Label(csframe, text="Speicherpfad:").grid(row=0, column=0)                                                         #
tk.Label(root, text="Bildvorschau:\n(verzögert!)").grid(row=2, column=0)                                              #
#subprocess.call("nc -l -p 5002 | mplayer -fps 32 -cache 32 -cache-min 1 -wid %d - &" % camframeid, shell=True) # Video-Empfang und -Abbildung
os.environ['SDL_WINDOWID'] = str(radarframe.winfo_id())