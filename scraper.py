```python
import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    # Make a request to the given URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes

    # Parse the content of the request with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Custom parsing logic goes here
    # This is where you would extract the necessary information from the page
    # For example, if you're scraping user data:
    # users = soup.find_all('div', class_='user-info')
    # for user in users:
    #     username = user.find('span', class_='username').text
    #     user_data = {
    #         'username': username,
    #         # Extract other user data here
    #     }
    #     # Save the extracted data
    #     save_user_data(user_data)

    # Placeholder for actual data extraction
    # Replace the following line with your custom parsing logic
    extracted_data = {}  # Replace with actual data extraction logic

    return extracted_data

def save_user_data(user_data):
    # This function would save the scraped data to the database
    # You would need to import the necessary function from database.py
    # from database import save_data
    # save_data(user_data)
    pass  # Replace with actual database saving logic

# Example usage:
# if __name__ == "__main__":
#     url = 'http://example.com/users'
#     data = scrape_data(url)
#     print(data)
```