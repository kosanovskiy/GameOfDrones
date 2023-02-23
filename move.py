from bluedot import BlueDot
from gpiozero import Robot
from signal import pause

# Need forward and backward pins for H bridge on left and the H bridge on right
R2D2 = Robot(left=(, ), right = (, ))
bd = BlueDot()

def move(pos):
  if pos.top:
    R2D2.forward()
  elif pos.bottom:
    R2D2.backward()
  elif pos.left:
    R2D2.left()
  elif pos.right:
    R2D2.right()
    
def stop():
    R2D2.stop()
  
bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop
pause()
