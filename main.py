import feedparser
import random
from bs4 import BeautifulSoup

# Parse the RSS feed
rss_url = "https://www.reddit.com/r/conspiracytheories.rss"
feed = feedparser.parse(rss_url)

# Get a random post from the feed
post = random.choice(feed.entries)

# Extract the title and link from the post
title = post.title
link = post.link

rss_striped_link = link[:-1] + ".rss"

feed2 = feedparser.parse(rss_striped_link)

for post in feed2.entries:
    html = post.description
    soup = BeautifulSoup(html, "html.parser")
    try:
        first_p = soup.find("p").text.strip()
        end_p = first_p.find("</p>")
        first_paragraph = BeautifulSoup(first_p[:end_p], "html.parser").text.strip()
    except:
        print("Couldnt find description")

# Print the results
print("Title:", title)
print("Description:", first_paragraph)
print("Link:", link)