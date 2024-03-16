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
    os.system("cd /home/pi/Katamaran/Server/Frontend && npm run dev")

frontend_thread = threading.Thread(target=run_frontend)
frontend_thread.start()

net.run()