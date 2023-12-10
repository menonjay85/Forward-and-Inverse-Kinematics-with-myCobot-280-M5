from pymycobot.mycobot import MyCobot
import time

# Initialize a MyCobot object 
mc = MyCobot("COM11", 115200)

# Turn on the suction pump, note: use one of pins 2 and 5 to control the switch of the suction pump
def pump_on():
    # Let bit 2 work
    mc.set_basic_output(2, 0)
    # Let bit 5 work
    mc.set_basic_output(5, 0)

# Stop suction pump
def pump_off():
    # Make position 2 stop working
    mc.set_basic_output(2, 1)
    # Make position 5 stop working
    mc.set_basic_output(5, 1)

pump_off()
time.sleep(3)
pump_on()
time.sleep(3)
pump_off()
time.sleep(3)