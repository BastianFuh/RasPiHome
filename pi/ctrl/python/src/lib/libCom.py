
###
#
# Constants used for the communication
#
# Ranges
#   Sensors         0x00 - 0x6F
#   Actuators       0x70 - 0xDF
#   Miscellaneous   0xE0 - 0xFF
#
###


##
#
# Const for the Discovery Process
#
##

# -- Sensors -- #

SENSOR_TEMPERATURE      = 0x00
SENSOR_TEMP             = 0x00

SENSOR_HUMIDITY         = 0x01
SENSOR_HUM              = 0x01

SENSOR_LIGHT            = 0x02

SENSOR_COLOR            = 0x03


# -- Actuators -- #

ACTR_SERVO              = 0x70
ACTR_PELTIER            = 0x71
ACTR_LED                = 0x72
ACTR_SIREN              = 0x73


# -- Predefined PORTS -- #

PORT_DEBUG              = 0xFE
PORT_DISCOVERY          = 0xFF