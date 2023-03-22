import random
import time
import boto3
import configparser
import json

config = configparser.ConfigParser()
config.read("/Users/gomes/Desktop/Projects/Data Engineer/2-Project/config/config.ini")

class PetrobrasSensorData:
    
    def  __init__(self, stream_name):
        self.stream_name = stream_name
        self.kinesis_client = boto3.client("kinesis", "us-east-1")

    def seismic_data(self):
        return {
            "geophone_id": random.randint(1, 1000),
            "seismic_wave_amplitude": random.uniform(0.0, 1.0),
            "seismic_wave_frequency": random.uniform(1.0, 100.0),
            "reflection_time": random.uniform(0.0, 10.0)
        }

    def temperature_pressure_data(self):
        return {
            "sensor_id": random.randint(1, 1000),
            "temperature": random.randint(-50.0, 150.0),
            "pressure": random.uniform(0.0, 10000.0)
        }

    def fluid_flow_data(self):
        return {
            "sensor_id": random.randint(1, 1000),
            "oil_flow_rate": random.uniform(0.0, 1000.0),
            "gas_flow_rate": random.uniform(0.0, 1000.0),
            "water_flow_rate": random.uniform(0.0, 1000.0)
        }

    def chemical_composition_data(self):
        return {
            "sample_id": random.randint(1, 1000),
            "oil_composition": random.randint(0.0, 100.0),
            "gas_composition": random.uniform(0.0, 100.0),
            "water_composition": random.uniform(0.0, 100.0)
        }

    def corrosion_wear_data(self):
        return {
            "sensor_id": random.randint(1, 1000),
            "corrosion_rate": random.uniform(0.0, 10.0),
            "wear_rate": random.uniform(0.0, 10.0)
        }

    def environmental_data(self):
        return {
            "air_temperature": random.uniform(-50.0, 50.0),
            "humidity": random.uniform(0.0, 100.0),
            "wind_speed": random.uniform(0.0, 50),
            "wind_direction": random.uniform(0.0, 360.0),
            "ocean_current_speed": random.uniform(0.0, 5.0),
            "wave_height": random.uniform(0.0, 10.0),
            "tide_level": random.uniform(0.0, 5.0)
        }

    def equipment_monitoring_data(self):
        return {
            "equipment_id": random.randint(1, 1000),
            "equipment_type": random.choice(["pump", "compressor", "motor"]),
            "performance": random.uniform(0.0, 100.0),
            "condition": random.choice(["good", "fair", "poor"])
        }

    def send_to_kinesis(self, data):
        response = self.kinesis_client.put_record(
            StreamName=self.stream_name,
            Data=json.dumps(data) + "\n",
            PartitionKey=str(random.randint(1, 1000)))
        print(f'Successfully sent data to Kinesis Data Stream: {response}')

    def generate_data_stream(self, interval=10):
        while True:
            self.send_to_kinesis(self.seismic_data())
            self.send_to_kinesis(self.temperature_pressure_data())
            self.send_to_kinesis(self.fluid_flow_data())
            self.send_to_kinesis(self.chemical_composition_data())
            self.send_to_kinesis(self.corrosion_wear_data())
            self.send_to_kinesis(self.environmental_data())
            self.send_to_kinesis(self.equipment_monitoring_data())
            
            time.sleep(interval)

# Usage
stream_name = config.get("kinesis", "stream_name")
sensor_data = PetrobrasSensorData(stream_name)
sensor_data.generate_data_stream(10)







