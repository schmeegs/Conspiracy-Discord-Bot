import feedparser
import random
from bs4 import BeautifulSoup
import pyshorteners

def get_conspiracy_post():
    # Parse the RSS feed
    rss_url = "https://www.reddit.com/r/conspiracytheories.rss"
    feed = feedparser.parse(rss_url)

    # Get a random post from the feed
    post = random.choice(feed.entries)    

    # Extract the title and link from the post
    title = post.title

    # Get a list of URLs of posts made before
    with open("posted_urls.txt", "r") as f:
        posted_urls = f.read().splitlines()

    # Find a new post that hasn't been made before
    for post in feed.entries:
        link = post.link
        if link not in posted_urls:
            break
    else: # If all posts have been made before, return a message saying so
        return "Cant find any new conspiracies boiz, check back tomorrow ;)"
    
    rss_striped_link = link[:-1] + ".rss"

    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(link)

    feed2 = feedparser.parse(rss_striped_link) #parse the feed from the individual link selected
    content = feed2.entries[0].content[0].value #extract content for first entry

    soup = BeautifulSoup(content, "html.parser")
    p_tags = soup.find_all("p")

    if p_tags:
        first_p_tag = p_tags[0]
        content_text = first_p_tag.get_text()
    else:
        content_text = "N/A"

    with open("posted_urls.txt", "a") as f:
        f.write(link + "\n")

    # Return the results
    # Format the results as a string with bold formatting
    formatted_title = f"**Title:** {title}"
    formatted_description = f"**Description:** {content_text}"
    formatted_link = f"**Link:** {short_url}"

    return f"{formatted_title}\n{formatted_description}\n{formatted_link}"
