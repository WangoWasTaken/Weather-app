import random
from time import sleep

weather_forecast = []
time_forecast = {

}

clock = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

i = 0

temp = (random.randint(4,9))

while i < len(clock):
    print(clock[i])
    i = i +1
    prediction = (random.randint(0,100))
    if i >= 5 and i <= 19:
        if prediction >= 60 and prediction <=89:
            temp += 3
        elif prediction >=30 and prediction <=59:
            temp += 2
        elif prediction >=90:
            temp += 4
        else:
            temp -= 1
    else:
        if prediction >= 50:
            temp -= 1
        else:
            temp -= 2
    print("TEMPERATURE", temp)
    weather_forecast.append(temp)
    time_forecast.update({ i : weather_forecast[-1]})
    sleep(0.1)

#see tagurpidi time_forecast.update({ i : weather_forecast[-1]}) lubab sorteerida kraadidega
sorted_time_forecast = dict(sorted(time_forecast.items()))
print(sorted_time_forecast)
for key, value in sorted_time_forecast.items():
    print("The temperature was", value, "degrees at",key, "o'clock")

print(sorted_time_forecast)






while True:
    question = int(input("What is today's highest temperature: "))
    if question == max(weather_forecast):
        print("Yay correct")
        break
    else:
        print("Wrong, guess again")