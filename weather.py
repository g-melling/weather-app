from tkinter import *
import requests
import json

root = Tk()
root.title("Weather App")
root.geometry("400x100")

# API: airnow.gov
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=85519&distance=25&API_KEY=7D99F44B-1DA2-4F75-8801-530F46CE99D9

try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=70836&distance=25&API_KEY=7D99F44B-1DA2-4F75-8801-530F46CE99D9")
    api = json.loads(api_request.content)
    city = text=api[0]["ReportingArea"]
    quality = text=api[0]["AQI"]
    category = text=api[0]["Category"]["Name"]
    
    color = "green"
    
    if category == "Good":
        color = "#0C0"
    elif category == "Moderate":
        color = "#FFFF00"
    elif category == "Unhealthy for Sensitive Groups":
        color = "#FF9900"
    elif category == "Unhealthy":
        color = "#FF0000"
    elif category == "Very Unhealthy":
        color = "#990066"
    elif category == "Hazardous":
        color = "#660000"
    else:
        color = "#000000"
        
    root.configure(background=color)
    
    output = f"City: {city}\nAir Quality Index: {quality}\nCategory: {category}"
    
    myLabel = Label(root, text=output, font=("Helvetica", 20), background=color).pack()   
except Exception as e:
    api = "Error..."

root.mainloop()