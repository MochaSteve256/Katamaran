import net
import subprocess

camera_process = subprocess.Popen(["python3", "/home/pi/Katamaran/Server/camera.py"])
frontend_process = subprocess.Popen(["npm", "run", "dev"], cwd="/home/pi/Katamaran/Server/Frontend")

net.run()