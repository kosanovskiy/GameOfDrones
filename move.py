from bluedot import BlueDot
from gpiozero import Robot
from signal import pause

# Need forward and backward pins for H bridge on left and the H bridge on right
R2D2 = Robot(left=(22, 27), right = (9, 10))
R4D4 = Robot(left=(23, 24), right = (8, 1))

bd = BlueDot()

def move(pos):
  if pos.top:
    R2D2.forward()
    R4D4.forward()
    print("forward")
  elif pos.bottom:
    R2D2.backward()
    R4D4.backward()
    print("backward")
  elif pos.left:
    R2D2.left()
    R4D4.left()
    print("left")
  elif pos.right:
    R2D2.right()
    R4D4.right()
    print("right")

def stop():
    R2D2.stop()
    R4D4.stop()
    print("stop")
  
bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop
pause()