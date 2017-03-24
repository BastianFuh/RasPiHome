<?php

// SENSORS
  const SENSOR_TEMPERATURE  = 0x01;
  const SENSOR_HUMIDITY     = 0x02;
  const SENSOR_LIGHT        = 0x03;
  const SENSOR_COLOR        = 0x04;


// Actuators
  const ACTR_SERVO         = 0x70;
  const ACTR_PELTIER       = 0x71;
  const ACTR_LED           = 0x72;
  const ACTR_RGBLED        = 0x73;
  const ACTR_SIREN         = 0x74;


  const DEBUG              = 0xFF;

  function getName ($id)
  {

    switch($id)
    {
      case SENSOR_TEMPERATURE:
          return "Temperatur";
        break;

      case SENSOR_HUMIDITY:
          return "Luftfeuchtigkeit";
        break;

      case SENSOR_LIGHT:
          return "Licht";
        break;

      case SENSOR_COLOR:
          return "Farbe";
        break;


      case ACTR_SERVO:
          return "Servo Motor";
        break;

      case ACTR_PELTIER:
          return "Peltierelement";
        break;

      case ACTR_LED:
          return "LED";
        break;

      case ACTR_SIREN:
          return "Sirene";
        break;

      case DEBUG:
          return "Debug";
        break;

      default:
        return -1;
    }
  }


 ?>
