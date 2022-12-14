from bs4 import BeautifulSoup
import requests

class G1Scrapper:
    url = 'https://g1.globo.com/busca/?q=violencia+infantil'
    def parse(self):
        html = requests.get(self.url).content
        soup = BeautifulSoup(html, 'html.parser')

        for item in soup.find_all('li', class_='widget widget--card widget--info'):
            try: 
                spans = item.find_all('span')
                date = spans[2].text.strip()

                link = 'https:' + item.find('a', class_='widget--info__media').get('href').strip()
                image = 'https:' + item.find('img').get('src').strip()
                title = item.find('div', class_='widget--info__title product-color').text.strip()
                description = item.find('p', class_='widget--info__description').text

                yield dict(
                    date=date,
                    link=link,
                    image=image,
                    title=title,
                    description=description
                )
            except:
                pass


class OGloboScrapper:
    url = 'https://oglobo.globo.com/busca/?q=violencia+infantil'

    def parse(self):
        html = requests.get(self.url).content
        soup = BeautifulSoup(html, 'html.parser')

        for item in soup.find_all('li', class_='widget widget--card widget--info'):
            try:
                spans = item.find_all('span')
                date = spans[2].text.strip()

                link = 'https:' + item.find('a').get('href').strip()
                image = 'https:' + item.find('img').get('src').strip()
                title = item.find('div', class_='widget--info__title product-color').text.strip()
                description = item.find('p', class_='widget--info__description').text

                yield dict(
                    date=date,
                    link=link,
                    image=image,
                    title=title,
                    description=description
                )
            except:
                pass
