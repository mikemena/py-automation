# run terminal command from python using subprocess

import subprocess

for i in range(0, 5):
    subprocess.check_call(["python3", "example.py"])
