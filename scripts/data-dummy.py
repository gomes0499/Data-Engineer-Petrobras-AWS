import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import random

class PetrobrasSensorData:

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
            "temperature": random.uniform(-50.0, 150.0),
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
    

def generate_data(data_type, num_records=1000):
    data_generator = PetrobrasSensorData()

    data_list = []
    for _ in range(num_records):
        if data_type == "seismic":
            data_list.append(data_generator.seismic_data())
        elif data_type == "temperature_pressure":
            data_list.append(data_generator.temperature_pressure_data())
        elif data_type == "fluid_flow":
            data_list.append(data_generator.fluid_flow_data())
        elif data_type == "chemical_composition":
            data_list.append(data_generator.chemical_composition_data())
        elif data_type == "corrosion_wear":
            data_list.append(data_generator.corrosion_wear_data())
        elif data_type == "environmental":
            data_list.append(data_generator.environmental_data())
        elif data_type == "equipment_monitoring":
            data_list.append(data_generator.equipment_monitoring_data())

    return pd.DataFrame(data_list)

def save_to_parquet(df, file_path):
    table = pa.Table.from_pandas(df)
    pq.write_table(table, file_path)

# Generate data for each data type and save to separate Parquet files
data_types = ["seismic", "temperature_pressure", "fluid_flow", "chemical_composition", "corrosion_wear", "environmental", "equipment_monitoring"]
for data_type in data_types:
    data_df = generate_data(data_type)
    save_to_parquet(data_df, f'{data_type}_data.parquet')

