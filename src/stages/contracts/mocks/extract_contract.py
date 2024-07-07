from datetime import date
from src.stages.contracts.extract_contract import ExtractContract

extract_contract_mock = ExtractContract(
    raw_information_content=[
        {
            "name": "Zabaglia, Niccola",
            "link": "https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=11630"
        },
        {
            "name": "Zaccone, Fabian",
            "link": "https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=34202"
        },
        {
            "name": "Zadkine, Ossip",
            "link": "https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=3475"
        },
        {
            'name': '<strong>next<br/>page</strong>',
            'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ4.htm'
        }
    ],
    extraction_date= date.today()
)
