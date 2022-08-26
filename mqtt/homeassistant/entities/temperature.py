from paho.mqtt.client import Client

from mqtt.devices.display import DisplayDevice
from mqtt.homeassistant.display_entity import DisplayEntity

class TemperatureEntity(DisplayEntity):
    _update_interval = 60
    _entity_mqtt_name = "temperature"

    def __init__(self, client: Client, display: DisplayDevice):
        super().__init__(client, display)

        self.device_class = "temperature"
        self.name = "onzo.display.temperature"
        self.unique_id = f"{display.identifiers[0]}_temperature"
        self.state_topic = self.construct_onzo_mqtt_topic("temperature")
        self.value_template = "{{ value_json['state'] }}"
        print(self.serialize())
    
    def get(self):
        return {
            "state": self.__display_device.__display.get_register(self.__display_device.__display.registers.TEMPERATURE)
        }