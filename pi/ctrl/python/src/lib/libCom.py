
## @package src.RasPiHome.lib.libCom
# Constants used to simplify the communication between the Systems.
#
# Type Ranges
#   Sensors         0x00 - 0x6F
#   Actuators       0x70 - 0xDF
#   Miscellaneous   0xE0 - 0xFF
#
###

# -- Types -- #
CONN_OTHER              = 0x00
CONN_DIREKT             = 0x01
CONN_BLUETOOTH          = 0x02
CONN_I2C                = 0x03
CONN_SPI                = 0x04

# -- Sensors -- #
SENSOR_TEMPERATURE      = 0x01 ##<
SENSOR_HUMIDITY         = 0x02
SENSOR_LIGHT            = 0x03
SENSOR_COLOR            = 0x04

# -- Actuators -- #
ACTR_SERVO              = 0x70
ACTR_PELTIER            = 0x71
ACTR_LED                = 0x72
ACTR_SIREN              = 0x73

# -- Predefined PORTS -- #
PORT_DEBUG              = 0xFE
PORT_DISCOVERY          = 0xFF