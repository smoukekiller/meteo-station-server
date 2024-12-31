def save_data(temperature: float, humidity: float) -> None:
    data_file = open("data.txt", "a+")
    data_file.write(str(temperature) + ";" + str(humidity) + "\n")
    data_file.close()
    