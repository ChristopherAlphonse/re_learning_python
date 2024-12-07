import requests

api_key = "34e5b86e802f48d5a35224408240512"
city = "New York"
base_url = str(
    f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
)


response = requests.get(base_url).json()
# print(response)

temp = response.get("current").get("temp_f")
condition = response.get("current").get("condition").get("text")

print(
    f"The current temperature in {city} is {temp} degrees fahrenheit and the weather condition is {condition}"
)
