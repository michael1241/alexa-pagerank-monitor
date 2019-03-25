#!/usr/bin/env python3
import os
import requests
from lxml import html
import re

sites = ["lichess.org", "chess24.com", "chessbomb.com", "chess.com", "chesstempo.com", "chessable.com", "chessgames.com", "blitztactics.com"]

xpath = '''//*[@id="traffic-rank-content"]/div/span[2]/div[1]/span/span/div/strong/text()'''
alexapage = "https://www.alexa.com/siteinfo/"

output = []
for site in sites:
	pageContent=requests.get(alexapage + site)
	tree = html.fromstring(pageContent.content)
	rank = re.sub("\D", "", str(tree.xpath(xpath)))
	output.append(f"popularity,website={site} rank={rank}")
print("\n".join(output))