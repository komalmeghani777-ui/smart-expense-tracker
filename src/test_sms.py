import requests

url = "http://127.0.0.1:8000/sms"
message = {"message": "Rs 40 paid to bus"}

response = requests.post(url, json=message)
print(response.json())
