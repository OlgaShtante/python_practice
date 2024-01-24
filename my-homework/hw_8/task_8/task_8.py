FILE_PATH = "weather_log.txt"
def weather_data(file_path):
    max_temp_city = {"name": None, "temperature": float('-inf')}
    min_temp_city = {"name": None, "temperature": float('inf')}

    with open(file_path, 'r') as file:
        for line in file:

            city_data = line.split(',')
            city_name = city_data[0].strip()
            temperature = int(city_data[1].strip())

            if temperature > max_temp_city["temperature"]:
                max_temp_city["name"] = city_name
                max_temp_city["temperature"] = temperature

            if temperature < min_temp_city["temperature"]:
                min_temp_city["name"] = city_name
                min_temp_city["temperature"] = temperature

    def message(temp, degree, city):
        return f"City with the {temp} temperature ({degree} C): {city}"

    print(message('highest', max_temp_city['temperature'],max_temp_city['name']))
    print(message('lowest', min_temp_city['temperature'],min_temp_city['name']))


weather_data(FILE_PATH)