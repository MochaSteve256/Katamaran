import pygame as pg
def rexec():             #
    global d             # Funktion zum Übernehmen des ausgewählten Radiobuttons von den Radar-Einstellungen
    d = rsettings.get()  #
pg.display.init()                                        #
pg.font.init()                                           #
screen = pg.display.set_mode((w,h))                      # Anderer gemischter Kram
screen.fill(pg.Color(255,255,255))                       #
angle = 0                                                #
d = 16                                                   #
running = True                                           #
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