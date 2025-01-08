from datetime import datetime
import config
def save_data(temperature: float, humidity: float) -> None:
    ct = datetime.now()
    timestamp = int(round(ct.timestamp()))

    file = open(f"{config.DATA_PATH}last_updated.txt", "w")
    file.write(str(timestamp))

    ct = datetime.now()
    timestamp = int(round(ct.timestamp()))
    filename = ct.isoformat()[:10]
    data_file = open(f"{config.DATA_PATH}{filename}.txt", "a+")
    data_file.write(str(timestamp) + ";" + str(temperature) + ";" + str(humidity) + "\n")
    data_file.close()
    