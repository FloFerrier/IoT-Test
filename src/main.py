from src.config.config import config_read
from openweathermap import OpenWeatherMap

def main() -> None:
    config = config_read("config.yaml")

    weather = OpenWeatherMap()
    response = weather.init(config["openweathermap"]["url"], config["openweathermap"]["key"], config["openweathermap"]["city"])

    if response["error"]["code"] != 200:
        print("Fail to init OpenWeatherMap [{}]:\"{}\"".format(response["error"]["code"], response["error"]["message"]))
        exit(0)

    data = weather.weather_get()
    if response["error"]["code"] != 200:
        print("Fail to get data OpenWeatherMap [{}]:\"{}\"".format(response["error"]["code"], response["error"]["message"]))
        exit(0)

    print(response)

if __name__ == "__main__":
    main()