import requests

BASE_URL = 'https://api.openweathermap.org/data/2.5'
API_KEY = 'bh7xubmyn67mdo8a1mc1ya0s62o0t00n'

def get_weather(city: str, state_code: str, api_key=API_KEY):
        
    url = f"{BASE_URL}/weather?q={city},{state_code},US&appid={api_key}"

    print(f"Trying this URL:  {url}")

    
    response = requests.get(
        url, 
        headers={'Content-Type': 'application/json'}, 
        verify=False,
    )
    
    return response.json()
