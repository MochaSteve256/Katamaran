import subprocess
import os
os.system("sudo pigpiod")

import net
net.run()
camera_process = subprocess.Popen(["python3", "/home/pi/Katamaran/Server/camera.py"])
frontend_process = subprocess.Popen(["npm", "run", "dev"], cwd="/home/pi/Katamaran/Server/Frontend")
