import random
from time import sleep

number = 0
weather_forecast = []

time_forecast = {

}



while number <= 5:
    number += 1
    temp=(random.randint(15,27))
    weather_forecast.append(temp)
    print(temp)
    weather_forecast_size = len(weather_forecast)
    if weather_forecast_size <= 1:
        print("Today's temperature has been:", *weather_forecast)
    else:
        print("Today's temperatures have been:", *weather_forecast, sep=", ")
    sleep(1)
    time_forecast.update( {weather_forecast[-1] : "2am"})
    print(time_forecast)


