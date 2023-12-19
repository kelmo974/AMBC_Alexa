import requests
from bs4 import BeautifulSoup
from soco import discover, SoCo

# Function to scrape the webpage and return the desired content
def scrape_webpage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Customize this part to extract the specific content you want
    content = soup.find('h1', {'class': 'entry-title'}).text
    return content

# Function to announce the content over a Sonos speaker
def announce_over_sonos(content):
    speakers = discover()  # Discover Sonos speakers on the network
    if not speakers:
        print("No Sonos speakers found on the network.")
        return
    sonos = speakers[0]  # Connect to the first discovered speaker
    sonos.play_uri(f'tts://{content}')

# Function to retrieve and increment the counter
def get_counter():
    try:
        with open('counter.txt', 'r') as file:
            count = int(file.read())
    except FileNotFoundError:
        count = 0

    count += 1

    with open('counter.txt', 'w') as file:
        file.write(str(count))

    return count

# Handler function for the Alexa intent
def handle_alexa_intent(intent):
    # Customize the URL according to the webpage you want to scrape
    webpage_url = 'https://ambcknox.org/'
    content = scrape_webpage(webpage_url)
    count = get_counter()
    print(f"Webpage content announced {count} times.")
    announce_over_sonos(content)

# Example invocation of the handle_alexa_intent() function
handle_alexa_intent('your_intent_name')
