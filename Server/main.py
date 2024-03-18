import subprocess
import os
import threading
import signal
try:
    os.system("sudo pigpiod")
except:
    pass
try:
    signal.signal(signal.SIGTERM, lambda *args: sys.exit(0))
    import net
    net_thread = threading.Thread(target=net.run)
    net_thread.start()
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
