import random
import time 

min_temperature=int(input("Enter minimum temperature: "))
max_temperature=int(input("Enter maximum temperature: "))
while True:
    temperature = random.randint(1,120)
    if temperature>max_temperature:
        print("Alert temperature is too high",temperature)
        time.sleep(2)
    elif temperature<min_temperature:
        print("Alert temperature is too LOW",temperature)
        time.sleep(2)
    else:
        print("temperature is within Normal range",temperature)
        time.sleep(2)