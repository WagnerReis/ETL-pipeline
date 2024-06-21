from typing import List, Dict
from bs4 import BeautifulSoup
from .interfaces.html_collector import HtmlCollectorInterface


class HtmlCollector(HtmlCollectorInterface):

    def collect_essential_information(self, html: str) -> List[Dict[str, str]]:
        soup = BeautifulSoup(html, 'html.parser')
        essential_information = []

        artist_name_list = soup.find(class_='BodyText')
        if artist_name_list:
            artist_name_list_items = artist_name_list.find_all('a')

            essential_information = []
            for artist_name in artist_name_list_items:
                names = artist_name.contents[0]
                links = 'https://web.archive.org' + artist_name.get('href')
                essential_information.append({
                    'name': names,
                    'link': links
                })

        return essential_information
