

import subprocess

cmd = ["pyinstaller","-F",
r"--paths=C:\Users\lhz\AppData\Local\Programs\Python\Python36\Lib\site-packages\PyQt5",
r"--paths=C:\Users\lhz\AppData\Local\Programs\Python\Python36\Lib\site-packages\PyQt5\Qt\bin",
r"--paths=C:\Users\lhz\AppData\Local\Programs\Python\Python36\Lib\site-packages\PyQt5\Qt\plugins",
"dzfh_auto.py"]

sub = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)