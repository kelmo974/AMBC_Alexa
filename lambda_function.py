# pull in dependencies
import time
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'https://ambcknox.org/'

response = requests.get(url)
soup = bs(response.text, 'html.parser')

trail_data = []

for trail in soup.find_all('div', class_='status_block status_yes'):
    trail_name = trail.find('span', class_='trail_name').text
    # trail_name = [span.text.split('-')[0].strip() for span in trail.find('span', class_='trail_name')]
    trail_status = trail.find('span', class_='trail_status status_yes').text[0:4]
    
    
    trail_data.append({'Park Name': trail_name, 'Status': trail_status})


for trail in soup.find_all('div', class_='status_block status_no'):
    trail_name_element = trail.find('span', class_='trail_name')
    trail_name = trail_name_element.text.split('-')[0].strip()
    # trail_status = "Closed"
    trail_status = trail.find('span', class_='trail_status status_no').text[0:6]
    trail_data.append({'Park Name': trail_name, 'Status': trail_status})



for trail in soup.find_all('div', class_='status_block status_maybe'):
    trail_name_element = trail.find('span', class_='trail_name')
    trail_name = trail_name_element.text.split('-')[0].strip()
    # trail_status = "Maybe"
    trail_status = trail.find('span', class_='trail_status status_maybe').text[0:7]
    trail_data.append({'Park Name': trail_name, 'Status': trail_status})



print(trail_data)
 
trail_df = pd.DataFrame(trail_data)
trail_df

trail_df.to_csv('C:\\Users\\kfinn1\\Documents\\trails.csv', index=False)

# the following lines are intended to serve as a framework allowing the user 
# to interact with Alexa to inquire about a specific trail

user_input = input("Enter the name of the trail you want to know about: ")

# Filter the trail data based on user input
filtered_trails = [trail for trail in trail_data if user_input.lower() in trail['Trail Name'].lower()]

if filtered_trails:
    for trail in filtered_trails:
        print(f"Trail Name: {trail['Trail Name']}, Status: {trail['Status']}")
else:
    print(f"No information found for the trail with the name '{user_input}'.")