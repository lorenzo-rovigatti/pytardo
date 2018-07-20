#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 13
// 9 is 0.5°, 10 is 0.25°
#define TEMPERATURE_PRECISION 10

// setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
OneWire one_wire(ONE_WIRE_BUS);

// pass the one_wire reference to the Dallas Temperature library
DallasTemperature sensors(&one_wire);

DeviceAddress T1, T2;

void setup(void)
{
  // start serial port
  Serial.begin(9600);

  // start up the library
  sensors.begin();

  // locate the sensors
  if (!sensors.getAddress(T1, 0)) Serial.println("Unable to find address for Device 0");
  if (!sensors.getAddress(T2, 1)) Serial.println("Unable to find address for Device 1");

  // set the resolution
  sensors.setResolution(T1, TEMPERATURE_PRECISION);
  sensors.setResolution(T2, TEMPERATURE_PRECISION);
}

void loop(void)
{
  // wait till something gets written to the serial port
  while (!Serial.available()) {}
  // read and throw away whatever is written
  while (Serial.available()) {
    Serial.read();
  }
  
  // call sensors.requestTemperatures() to issue a global temperature request to all devices on the bus
  sensors.requestTemperatures();

  // print the sensors
  Serial.print("T1 = ");
  Serial.print(sensors.getTempC(T1));
  Serial.print(",");
  Serial.print("T2 = ");
  Serial.println(sensors.getTempC(T2));

  delay(100);
}

