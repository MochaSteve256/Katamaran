import os
import subprocess

# Define the process names to check
processes_to_check = ["main.py", "camera.py", "npm run dev"]

# Function to check if a process is running
def is_process_running(process_name):
    cmd = f"ps aux | grep '{process_name}' | grep -v grep"
    output = subprocess.getoutput(cmd)
    return len(output.splitlines()) > 0

# Function to kill a process
def kill_process(process_name):
    cmd = f"pkill -f '{process_name}'"
    subprocess.run(cmd, shell=True)

# Check if processes are running and kill them if they are
for process in processes_to_check:
    if is_process_running(process):
        print(f"Killing process: {process}")
        kill_process(process)
    else:
        print(f"Process '{process}' is not running.")

# cd into katamaran folder
os.chdir("/home/pi/Katamaran/Server")
# pull changes
os.system("git pull")
# run
print("Starting main.py")
os.system("python3 main.py")
