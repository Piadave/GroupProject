import requests
from bs4 import BeautifulSoup

#Comedy Url
url = "https://www.rottentomatoes.com/browse/movies_in_theaters/genres:comedy~sort:popular"

# Fetch the webpage
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Locate the movie blocks
    movie_blocks = soup.find_all('div', class_='js-tile-link', limit=5)

    # Extract and display movie details and also displaying the results
    for i, block in enumerate(movie_blocks, start=1):
        title = block.find('span', class_='p--small').get_text(strip=True) if block.find('span', class_='p--small') else "Unknown"
        score = block.find('span', class_='tMeterScore').get_text(strip=True) if block.find('span', class_='tMeterScore') else "No Score"
        print(f"{i}. {title} - {score}")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")