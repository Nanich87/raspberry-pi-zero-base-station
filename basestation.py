import os
import time
import subprocess
import signal
from subprocess import check_call
from signal import pause
from gpiozero import Button, LED

LOG_PATH = "/mnt"
SERIAL_PORT_BAUD_RATE = 460800

proc = None
button = Button(21)
green = LED(20)

def str2str():
    global proc
    if proc is None:
        args = 'str2str -in serial://ttyAMA0:' + '{0}'.format(SERIAL_PORT_BAUD_RATE) + ':8:n:1:off -out ' + os.path.join(LOG_PATH, time.strftime("base-%Y-%m-%d-%H-%M-%S")) + '.ubx'
        proc = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)
        green.blink()
    else:
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
        proc = None
        green.on()

def shutdown():
    green.off()
    check_call(['sudo', 'poweroff'])

if __name__ == "__main__":
    button.when_pressed = str2str
    button.when_held = shutdown
    green.on()
    pause()
