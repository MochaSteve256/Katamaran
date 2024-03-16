import net
import camera
import threading
import os

cam_thread = threading.Thread(target=camera.run)
try:
    cam_thread.start()
except:
    pass

net_thread = threading.Thread(target=net.run)
net_thread.start()

os.chdir("/home/pi/Katamaran/Server/Frontend")
os.system("npm run dev")