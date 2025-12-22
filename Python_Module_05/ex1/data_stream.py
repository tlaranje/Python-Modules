from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == None:
            return data_batch
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id}


class SensorStream(DataStream):
    def __init__(self, stream_id):
        self.stream_id = stream_id
        self.total_readings = 0
        self.avg_temp = 0.0

    def filter_data(self, data_batch, criteria: Optional[str] = None) -> List[Any]:
        if criteria == "Temp":
            return [d for d in data_batch if 'temp' in d]
        return data_batch

    def process_batch(self, data_batch: List[Any]) -> str:
        filtered = self.filter_data(data_batch, 'Temp')
        self.total_readings = sum(len(d) for d in filtered)
        self.avg_temp = sum(d['temp'] for d in filtered) / len(filtered)

        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Environmental Data")
        print(*(f"Processing sensor batch: [temp:{d['temp']}, "
                f"humidity:{d['humidity']}, pressure:{d['pressure']}]"
                for d in filtered))
        print(f"Sensor analysis: {self.total_readings} readings processed, "
            f"avg temp: {self.avg_temp}°C\n")

        return filtered

    def get_stats(self):
        return {
            "stream_id": self.stream_id,
            "stream_type": "Sensor",
            "total_readings": self.total_readings,
            "avg_temp": self.avg_temp
        }

""" 
Initializing Transaction Stream...
Stream ID: TRANS_001, Type: Financial Data
Processing transaction batch: [buy:100, sell:150, buy:75]
Transaction analysis: 3 operations, net flow: +25 units
 """
class TransactionStream(DataStream):
    def __init__(self, stream_id):
        self.stream_id = stream_id
        self.net_flow = 0
        self.total_operations = 0

    def filter_data(self, data_batch, criteria: Optional[str] = None) -> List[Any]:
        return [d for d in data_batch if "buy" in d]

    def process_batch(self, data_batch: List[Any]) -> str:
        filtered = self.filter_data(data_batch, "Trans")
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Financial Data")
        print(f"Processing transaction batch: {filtered}")


class EventStream(DataStream):
    def __init__(self, stream_id):
        self.stream_id = stream_id

    def process_batch(self, data_batch: List[Any]) -> str:
        pass


class StreamProcessor():
    pass


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    data_batch = [
        {"type": "sensor", "temp": 22.5, "humidity": 65, "pressure": 1013},
        {"type": "transactions", "buy": [100, 75], "sell": [150]}, 
        {"logs": "logs", "events": ["login", "error", "logout"]}
    ]

    """ Sensor Stream """
    ss = SensorStream("SENSOR_001")
    ss.process_batch(data_batch)

    """ Transaction Stream """
    ss = TransactionStream("TRANS_001")
    ss.process_batch(data_batch)


""" 
=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===

Initializing Sensor Stream...
Stream ID: SENSOR_001, Type: Environmental Data
Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]
Sensor analysis: 3 readings processed, avg temp: 22.5°C

Initializing Transaction Stream...
Stream ID: TRANS_001, Type: Financial Data
Processing transaction batch: [buy:100, sell:150, buy:75]
Transaction analysis: 3 operations, net flow: +25 units

Initializing Event Stream...
Stream ID: EVENT_001, Type: System Events
Processing event batch: [login, error, logout]
Event analysis: 3 events, 1 error detected

=== Polymorphic Stream Processing ===
Processing mixed stream types through unified interface...

Batch 1 Results:
- Sensor data: 2 readings processed
- Transaction data: 4 operations processed
- Event data: 3 events processed

Stream filtering active: High-priority data only
Filtered results: 2 critical sensor alerts, 1 large transaction

All streams processed successfully. Nexus throughput optimal.  
"""