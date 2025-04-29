import subprocess
import os
import threading
import signal
try:
    os.system("sudo pigpiod")
except Exception as e:
    print(e)
print("Starting network endpoint")
print("Loading PiGPIO daemon")
import net
try:
    signal.signal(signal.SIGTERM, lambda *args: sys.exit(0))
    print("1")
    import net
    print("2")
    net_thread = threading.Thread(target=net.run)
    print("3")
    net_thread.start()
    print("4")
except Exception as e:
    #print("Failed to start network endpoint with error: " + e)
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
