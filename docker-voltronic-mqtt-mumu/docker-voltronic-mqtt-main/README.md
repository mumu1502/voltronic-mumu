# MQTT interface for Voltronic (aka MPPSolar, Axpert, Powland, EASun, etc) solar inverters.

Supports protocols PI30 and PI41 devices.

### Exposed sensors:
- Inverter status
- Grid voltage
- Grid frequency
- Output load watt
- Battery capacity (SOC)
- Heatsink temperature
- PV Input Current
- SCC voltage
- Warnings
### How to run
Change credentials to your MQTT server and USB port in the command below and run it.
```bash
docker run -t -i --privileged -v /dev:/dev --restart=always --name voltronic-mqtt --pull=always -e \
MQTT_PASSWORD='F49ycrvbn,%' -e \
MQTT_SERVER='192.168.1.53' -e \
MQTT_USER='homeassistant' -e \
SERIAL_PORT='/dev/ttyUSB0' \
lavron/voltronic-mqtt:latest
```

### Home Assistant users
Copy the content of 'ha-sensors.yaml' to your 'configuration.yaml' file. Edit as needed.

### Aditional protocols and sensors
Please check [this discussion](https://github.com/lavron/docker-voltronic-mqtt/discussions/5).

### Source
https://github.com/lavron/docker-voltronic-mqtt

