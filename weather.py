from tkinter import *
import requests
import json

root = Tk()
root.title("Weather App")
root.geometry("400x400")

# API: airnow.gov
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=7D99F44B-1DA2-4F75-8801-530F46CE99D9

try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=7D99F44B-1DA2-4F75-8801-530F46CE99D9")
    api = json.loads(api_request.content)
except Exception as e:
    api = "Error..."
    
myLabel = Label(root, text=api[0]["Category"]["Name"]).pack()

root.mainloop()