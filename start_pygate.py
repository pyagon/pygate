"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

import os
import subprocess
import platform
import sys

def start_script_in_background(script_name):
    current_os = platform.system()

    if current_os == 'Windows':
        subprocess.Popen([sys.executable, script_name], creationflags=subprocess.CREATE_NO_WINDOW)
        print(f"Started {script_name} in the background on Windows.")
    elif current_os == 'Linux' or current_os == 'Darwin':
        subprocess.Popen(['nohup', sys.executable, script_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Started {script_name} in the background on {current_os}.")
    else:
        print(f"Unsupported operating system: {current_os}")

if __name__ == '__main__':
    script_to_run = 'pygate.py'
    start_script_in_background(script_to_run)

# End of file
