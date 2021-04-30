import bs4
import lxml
import requests

query = input('search: ')
r = requests.get(r'https://www.xvideos.com/?k={query}')
soup = bs4.BeautifulSoup(r.text, 'lxml')
div = soup.find('div', class_='thumb-block')

for div in soup.find_all('div',  class_='thumb-block'):
  main = div.p
  
  title = main.a['title']
  video = 'https://xvideos.com' + main.a['href']
  duration = main.span.text

  print(
      f"""
      Title     : {title}
      Duration  : {duration}
      Video Link: {video}
      """
  )
