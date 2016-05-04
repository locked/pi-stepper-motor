import RPi.GPIO as GPIO
import time
import json
import sys

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
pins = [3, 4, 17, 27]

for pin in pins:
  GPIO.setup(pin, GPIO.OUT)

print "Init OK"

def change(pin, up_down, delay=0):
  print "pin %d %s" % (pin, up_down)
  GPIO.output(pin, up_down == "up")
  time.sleep(delay)

def up(pin, delay=0.04):
  change(pin, "up", delay)

def down(pin, delay=0.01):
  change(pin, "down", delay)

up(3, 10)

time.sleep(2)
for pin in pins:
  down(pin, 0)
time.sleep(2)
print "All false"

seq = [2, 3]

def setStep(a, b, c, d):
  change(3, a)
  change(4, b)
  change(17, c)
  change(27, d)

delay = 0.5
while True:
  """
  setStep("up", "down", "up", "down")
  time.sleep(delay)
  setStep("down", "up", "up", "down")
  time.sleep(delay)
  setStep("down", "up", "down", "up")
  time.sleep(delay)
  setStep("up", "down", "down", "up")
  time.sleep(delay)
  """
  up(3)
  down(27, 0)
  up(4)
  down(3, 0)
  up(17)
  down(4, 0)
  up(27)
  down(17, 0)
  #time.sleep(2)
  print "Output OK"
  """
  for s in seq:
    if isinstance(s, list):
      for i in s:
        pin = pins[i]
        up(pin, 0)
      time.sleep(0.5)
      for i in s:
        pin = pins[i]
        down(pin, 0)
      time.sleep(0.5)
    else:
      pin = pins[s]
      down(pin)
      up(pin, 0)
  """
