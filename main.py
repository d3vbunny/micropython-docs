from machine import Pin
from umqtt.simple import MQTTClient

led = Pin(4,Pin.OUT)
SERVER = "mqtt.mydevices.com"
USERNM = "cff55150-3f29-11e8-8361-73b3e3e6e8e4"
PASSWD = "0639db88c4553553665a85791fd7affda7d86b3a"
CLIENT_ID = "02434dd0-4522-11e8-8424-21b60c5342be"
TOPIC = b"v1/cff55150-3f29-11e8-8361-73b3e3e6e8e4/things/02434dd0-4522-11e8-8424-21b60c5342be/cmd/4"

state = 0

def sub_cb(topic, msg):
    global state
    print((topic, msg))
    if msg == b"on" or str('1'):
        led.off()
    if msg == b"off" or str('0'):
        led.on()

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect('AdityaTripathiYT', 'kk9310028206')
        while not sta_if.isconnected():
            pass
    print('Network config:', sta_if.ifconfig())
    
def main(server = SERVER):
    c = MQTTClient(CLIENT_ID, server, user = USERNM, password = PASSWD )
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(TOPIC)
    print("Connected to %s, subscribed to %s topic" % (server, TOPIC))
    try:
        while 1:
            c.wait_msg()
    finally:
        c.disconnect()

do_connect()     
main() 

