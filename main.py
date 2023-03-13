import feedparser
import sys

print(sys.executable)

# URL of the RSS feed
url = 'https://www.reddit.com/r/conspiracytheories.rss'

# Parse the RSS feed
feed = feedparser.parse(url)

# Extract the titles of the posts
titles = []
for entry in feed.entries:
    title = entry.title
    titles.append(title)

# Print the titles
print(titles)