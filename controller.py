from bluedot import BlueDot
from gpiozero import Robot
from signal import pause
import time

# Need forward and backward pins for H bridge on left and the H bridge on right
R2D2 = Robot(left=(22, 27), right = (9, 10))
R4D4 = Robot(left=(23, 24), right = (8, 1))

start_time = time.time()

#Look of d-pad in the app
def up():
    print("up")
    start_time = time.time()

def down():
    print("down")
    start_time = time.time()

def left():
    print("left")
    start_time = time.time()

def right():
    print("right")
    start_time = time.time()

bd = BlueDot(cols=3, rows=3)
bd[1,2].color = "red"
bd[1,0].color = "green"
bd.square = True

bd[0,0].visible = False
bd[2,0].visible = False
bd[0,2].visible = False
bd[2,2].visible = False
bd[1,1].visible = False

def stop():
    print("stop")
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)

def time_convert(sec):
    sec = sec % 60
    print(sec)

bd[1,0].when_pressed = up
bd[1,2].when_pressed = down
bd[0,1].when_pressed = left
bd[2,1].when_pressed = right

bd.when_released = stop

pause()