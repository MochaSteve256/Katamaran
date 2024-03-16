import net
import camera
import threading
import os

cam_thread = threading.Thread(target=camera.run)
try:
    cam_thread.start()
except:
    pass

def run_frontend():
    os.chdir("/home/pi/Katamaran/Server/Frontend")
    os.system("npm run dev")

frontend_thread = threading.Thread(target=run_frontend)
frontend_thread.start()

net.run()