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
    time=(random.randint(0,23))
    weather_forecast_size = len(weather_forecast)
    sleep(0.1)
    time_forecast.update( {weather_forecast[-1] : time})


for key, value in time_forecast.items():
    print("The temperature was", key, "degrees at",value, "o'clock")



while True:
    question = int(input("How many degrees is it: "))
    if question in weather_forecast:
        print("Yay correct")
        break
    else:
        print("Guess again")