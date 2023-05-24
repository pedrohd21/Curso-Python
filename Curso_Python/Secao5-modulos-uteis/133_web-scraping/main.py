from bs4 import BeautifulSoup
import requests  # instala o html css

# pip install requests  // instalando web scraping
# pip install beautifulsoup4

url = 'https://pt.stackoverflow.com/questions'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for question in html.select('.question-summary'):
    title = question.select_one('.question-hyperlink')
    date = question.select_one('.relativetime')
    wishes = question.select_one('.vote-count-post ')
    print(date.text, title.text, wishes.text, sep='\t')


