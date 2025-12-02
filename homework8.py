from datetime import datetime,timedelta,timezone



class WeatherSnapshot:
    def __init__(self,temperature: float ,humidity,observed_at: datetime):
        self.temperature = temperature
        self.humidity = humidity
        self.observed_at = observed_at
    
    def __repr__(self):
        timestamp = self.observed_at.isoformat(timespec = "minutes")
        return f"WeatherSnapshot({timestamp}, {self.temperature}C, {int(self.humidity)}%)"
    
    def cool_down(self,delta=1):
        return WeatherSnapshot(
            temperature = self.temperature - delta,
            humidity = self.humidity,
            observed_at = self.observed_at
        )


class SmartIrrigator:
    def __init__(self,name,water_reserve,daily_limit):
        self.name = name
        self.water_reserve = water_reserve
        self.capacity = water_reserve
        self.daily_limit = daily_limit
        self.used_today = 0
        self.total_used = 0 

    @property
    def needs_refill(self):
        return self.water_reserve < 0.2 * self.capacity

    def refill(self,amount):
        self.water_reserve += amount
        print(f"{self.name} refilled  with {amount}L water. total reserve: {self.water_reserve}")
        
    def sprinkle(self,volume):
        if volume > self.daily_limit - self.used_today:
            raise ValueError(f"{self.name} cant sprinke more than daily limit")
        if volume > self.water_reserve:
            raise ValueError(f"{self.name} doesnt have enough water")

        self.water_reserve -= volume
        self.used_today += volume
        self.total_used += volume

        print(f"{self.name} sprinkled {volume}L. Remaining reserve: {self.water_reserve}L")



    def status(self):
        return f"{self.name}: {self.water_reserve}L left, daily used: {self.used_today}L"

 

class GreenHouse:
    def __init__(self):
        self.devices = {}

    def register_devices(self,device):
        self.devices[device.name] = device
        return device

    def get_device(self,name):
        return self.devices.get(name, None)
    
    def total_water_remaining(self):
        return sum(d.water_reserve for d in self.devices.values())

    def busiest_device(self):
        if not self.devices:
            return None
        return max(self.devices.values(), key=lambda d: d.total_used)


    

if __name__ == "__main__":
    now = datetime.now(timezone.utc).replace(second=0, microsecond=0)
    snapshots = [
        WeatherSnapshot(20.0, 55.0, now - timedelta(hours=3)),
        WeatherSnapshot(22.5, 60.0, now - timedelta(hours=2)),
        WeatherSnapshot(19.0, 65.0, now - timedelta(hours=1)),
        WeatherSnapshot(16.5, 70.0, now),
    ]

    print("original -> Cooled (delta=3 C)")
    for s in snapshots:
        cooled = s.cool_down(3) 
        print(f"{s}  ->  {cooled}")

    device1 = SmartIrrigator("\nStorage 1", 50, 20)
    device2 = SmartIrrigator("\nStorage 2", 30, 15)


    device1.sprinkle(10)
    device2.sprinkle(5)


