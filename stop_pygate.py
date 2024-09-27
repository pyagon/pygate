"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pygate-dev/pygate for more information
"""

# Start of file

import os
import signal
import platform
import psutil

def stop_script(script_name):
    current_os = platform.system()

    if current_os == 'Windows':
        try:
            for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                if 'python' in proc.info['name'] and script_name in proc.info['cmdline']:
                    os.kill(proc.info['pid'], signal.SIGTERM)
                    print(f"Stopped {script_name} (PID: {proc.info['pid']}) on Windows.")
        except Exception as e:
            print(f"Error stopping {script_name} on Windows: {e}")
    elif current_os == 'Linux' or current_os == 'Darwin':
        try:
            for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                if 'python' in proc.info['name'] and script_name in proc.info['cmdline']:
                    os.kill(proc.info['pid'], signal.SIGTERM)
                    print(f"Stopped {script_name} (PID: {proc.info['pid']}) on {current_os}.")
        except Exception as e:
            print(f"Error stopping {script_name} on {current_os}: {e}")
    else:
        print(f"Unsupported operating system: {current_os}")

if __name__ == '__main__':
    script_to_stop = 'pygate.py'
    stop_script(script_to_stop)

# End of file
