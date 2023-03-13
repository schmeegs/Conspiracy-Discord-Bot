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

feed2 = feedparser.parse(rss_striped_link) #parse the feed from the individual link selected
content = feed2.entries[0].content[0].value #extract content for first entry

soup = BeautifulSoup(content, "html.parser")
p_tags = soup.find_all("p")
if p_tags:
    first_p_tag = p_tags[0]
    content_text = first_p_tag.get_text()
else:
    print("N/A (probably because there was only an image)")

# Print the results
print("Title:", title)
print("Description:", content_text)
print("Link:", link)