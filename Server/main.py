import subprocess
import os
import threading
try:
    os.system("sudo pigpiod")
except:
    pass
try:
    import net
    net_thread = threading.Thread(target=net.run)
    net_thread.run()
except:
    pass
try:
    camera_process = subprocess.Popen(["python3", "/home/pi/Katamaran/Server/camera.py"])
except:
    pass
try:
    frontend_process = subprocess.Popen(["npm", "run", "dev"], cwd="/home/pi/Katamaran/Server/Frontend")
except:
    pass
