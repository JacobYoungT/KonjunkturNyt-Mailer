import requests
from bs4 import BeautifulSoup

# URL'en til Økonomiministeriets KonjunkturNyt arkiv.
url = "https://oem.dk/nyheder/konjunkturnyt-arkiv/"

# Henter HTML indhold fra Økonomiministeriets hjemmeside.
response = requests.get(url)
html_content = response.text

# Omdanner HTML indhold til et BeautifulSoup objekt.
soup = BeautifulSoup(html_content, 'html.parser')

# Finder nyeste version af KonjunkturNyt.
latest_url = soup.find('a', class_='results-item results-item--link')
latest_url = latest_url['href']

# Henter HTML indhold fra seneste versions URL.
latest_response = requests.get(latest_url)
latest_html_content = latest_response.text

# Omdanner seneste HTML til et BeautifulSoup objekt.
latest_soup = BeautifulSoup(latest_html_content, 'html.parser')

# Finder alle relevante containers.
containers = latest_soup.find_all('div', class_='container custom-grid__container')[1:] # Skipper første da denne er blank.

# Fetch overskrifter og tekst
for container in containers:
    headline = container.find('h2', class_='module-headline module-headline--small multi-box__headline')
    text_elements = container.find_all('li', class_='BoksTekstCxSpFirst')

    if headline:
        print(f"\n{headline.text.strip()}")

    for text in text_elements:
        print(f"\n{text.text.strip()}")