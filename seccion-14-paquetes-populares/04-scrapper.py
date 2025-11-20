# ref. v135
# pipenv install beautifulsoup4

import os
import json
import requests
from bs4 import BeautifulSoup

os.system('cls' if os.name == 'nt' else 'clear')

url = "https://news.ycombinator.com/"

response = requests.get(url)
plain_text = response.text

soup = BeautifulSoup(plain_text, "html.parser")
titles_notes = soup.select(".titleline")

""" 
titles_notes[0] vvv

<span class="titleline">
    <a href="https://www.ntsb.gov:443/news/press-releases/Pages/NR20251118.aspx">
        Loose wire leads to blackout, contact with Francis Scott Key bridge
    </a>
    <span class="sitebit comhead"> 
        (
            <a href="from?site=ntsb.gov">
                <span class="sitestr">ntsb.gov</span>
            </a>
        )
    </span>
</span>
"""

notes = list()
for title in titles_notes:
    note = {
        "title": title.find("a").get_text(strip=True), 
        "href": title.find("a")["href"]
    }
    notes.append(note)

print(json.dumps(notes, indent=4))
