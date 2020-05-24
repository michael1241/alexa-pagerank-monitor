#!/usr/bin/env python3
import os
import requests
from lxml import html
import re

sites = ["lichess.org", "chess24.com", "chessbomb.com", "chess.com", "chesstempo.com", "chessable.com", "chessgames.com", "blitztactics.com"]

xpath = '''/html/body/div/div/section/div/section/div[2]/div[2]/div[3]/div/div[5]/section/div[1]/section[2]/div[2]/div[1]/div[2]/p[1]'''

alexapage = "https://www.alexa.com/siteinfo/"

output = []
for site in sites:
    pageContent=requests.get(alexapage + site)
    tree = html.fromstring(pageContent.content)
    try:
        rank = re.sub("\D", "", str(html.tostring(tree.xpath(xpath)[0])))
        output.append(f"popularity,website={site} rank={rank}")
    except IndexError:
        continue
print("\n".join(output))
