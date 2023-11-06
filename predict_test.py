import requests


url = 'http://localhost:9696/predict'

water_data = {
    "ph": 8.860324,
    "hardness": 233.625145,
    "solids": 19550.299680,
    "chloramines": 6.519063,
    "sulfate": 334.564290,
    "conductivity": 285.412436,
    "organic_carbon": 13.093262,
    "trihalomethanes": 25.061904,
    "turbidity": 2.476674
}


response = requests.post(url, json=water_data).json()
print(response) # expect output 0


water_data = {
    "ph": 5.736676,
    "hardness": 180.290908,
    "solids": 12683.483292,
    "chloramines": 7.907877,
    "sulfate": 423.876297,
    "conductivity": 415.006576,
    "organic_carbon": 12.392869,
    "trihalomethanes": 83.707045,
    "turbidity": 2.741791
}


response = requests.post(url, json=water_data).json()
print(response) # expect output 1

