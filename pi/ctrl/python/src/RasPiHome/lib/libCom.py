
## @package src.RasPiHome.lib.libCom
#  Constants used to simplify the communication between the Systems.
#
# The types specify the connection type at the interface
#
# The sensor and actuator specify certain sensors and Actuators
# Type Ranges
#   Sensors         0x00 - 0x6F
#   Actuators       0x70 - 0xDF
#   Miscellaneous   0xE0 - 0xFF
#
# The predefined Ports are used for actions that would other wise not work
# if they would run on all of the interfaces on a different port, e.g.
# the discovery process
#

# -- Types -- #
## Connection Type was not specified or not available
CONN_OTHER              = 0x00
## Connection and controls are through a pin of the interface
CONN_DIREKT             = 0x01
## Connected over a bluetooth connection
CONN_BLUETOOTH          = 0x02
## Connected over the i2c bus
CONN_I2C                = 0x03
## Connected over the spi bus
CONN_SPI                = 0x04

# -- Sensors -- #
## Sensor -> Temperatur
SENSOR_TEMPERATURE      = 0x01
## Sensor -> Humidity
SENSOR_HUMIDITY         = 0x02
## Sensor -> Light
SENSOR_LIGHT            = 0x03
## Sensor -> Color
SENSOR_COLOR            = 0x04

# -- Actuators -- #
## Actuator -> Servo
ACTR_SERVO              = 0x70
## Actuator -> Peltier element
ACTR_PELTIER            = 0x71
## Actuator -> LED
ACTR_LED                = 0x72
## RGB LED
ACTR_RGBLED             = 0x73
## Actuator -> Siren
ACTR_SIREN              = 0x74

# -- Predefined PORTS -- #
##  Used for debugging
PORT_DEBUG              = 0xFE
## Used for the discovery process
PORT_DISCOVERY          = 0xFF
