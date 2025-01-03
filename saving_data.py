from datetime import datetime

def save_data(temperature: float, humidity: float) -> None:
    ct = datetime.now()
    timestamp = int(round(ct.timestamp()))
    filename = ct.isoformat()[:10]
    data_file = open(f"{filename}.txt", "a+")
    data_file.write(str(timestamp) + ";" + str(temperature) + ";" + str(humidity) + "\n")
    data_file.close()
    