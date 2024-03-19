import subprocess
import os
import threading
import signal
print("Loading PiGPIO daemon")
try:
    os.system("sudo pigpiod")
except Exception as e:
    print(e)
print("Starting network endpoint")
try:
    signal.signal(signal.SIGTERM, lambda *args: sys.exit(0))
    import net
    net_thread = threading.Thread(target=net.run)
    net_thread.start()
except Exception as e:
    print(e)
print("Starting camera endpoint")
try:
    camera_process = subprocess.Popen(["python3", "/home/pi/Katamaran/Server/camera.py"])
except Exception as e:
    print(e)
print("Starting frontend server")
try:
    frontend_process = subprocess.Popen(["npm", "run", "dev"], cwd="/home/pi/Katamaran/Server/Frontend")
except Exception as e:
    print(e)
