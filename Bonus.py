#Bonus

# Question done by Ishaan Agrawal (2022221), Aarav Mathur (2022005), and Swapnil Panigrahi (2022522)

import requests
IPAddress = requests.get("https://api.ipify.org") 
#API call 1
print(f"Your current IP Address is {IPAddress.text}")

#API call 2
weatherjson = requests.get(f"https://api.weatherapi.com/v1/current.json?key=f70810071ffc492797690923231701&q={IPAddress.text}&aqi=yes") #API call 2
x=weatherjson.text

weatherDict = eval(x)
print(weatherDict)

print(f'Your current city is {weatherDict["location"]["name"]}.')
print(f'Your current country is {weatherDict["location"]["country"]}.')

print("Do you want to access the menu from your current location, or from a remote location?")
x=int(input("Enter 1 for current location, 2 for remote location: "))

if x==2:
    city = input("Enter a valid city: ")
    weatherjson = requests.get(f"https://api.weatherapi.com/v1/current.json?key=f70810071ffc492797690923231701&q={city}&aqi=yes") #API call 2
    x=weatherjson.text

    weatherDict = eval(x)

city = weatherDict["location"]["name"]
country = weatherDict["location"]["country"]
pm10 = weatherDict["current"]["air_quality"]["pm10"]
pm2_5 = weatherDict["current"]["air_quality"]["pm2_5"]
wind = weatherDict["current"]["wind_kph"]
temperature = weatherDict["current"]["temp_c"]

while True:
    print("Press 1 to check the current temperature.")
    print("Press 2 to check if outdoor badminton can be played or not.")
    print("Press 3 to check AQI")
    print("Press 4 to quit.")
    
    y = int(input())

    if  y== 1:
        print(f"The current temperature in {city} is {temperature} Celsius.")
    
    elif y == 2:
        if wind >=11:
            print(f"The current wind speed is {wind} km/h which is too high to play badminton.")
        else:
            print(f"The current wind speed is {wind} km/h which is okay to play badminton.")
    
    elif y == 3:
        print(f"The current pm 10 level is {pm10} and current pm 2.5 level is {pm2_5}.")
    
    elif y == 4:
        break
    else:
        print("Enter valid number")