import net
import threading
import os

def run_camera():
    os.system("cd /home/pi/Katamaran/Server && python3 camera.py")

camera_thread = threading.Thread(target=run_camera)
camera_thread.start()

def run_frontend():
    os.system("cd /home/pi/Katamaran/Server/Frontend && npm run dev")

frontend_thread = threading.Thread(target=run_frontend)
frontend_thread.start()

net.run()