from typing import List, Dict


class HtmlCollectorSpy:

    # collect_essential_information_attributes = None

    def __init__(self) -> None:
        self.collect_essential_information_attributes = {}

    def collect_essential_information(self, html: str) -> List[Dict[str, str]]:
        self.collect_essential_information_attributes["html"] = html
        return [{ "name": 'some name', "link": 'https://something.com' }]
