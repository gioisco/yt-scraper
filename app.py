import pyfiglet
import scrapetube
import textwrap

from utils import extract_number

ascii_art = pyfiglet.figlet_format("Youtube scraper")
print(ascii_art)

channel_url = input("Insert channel URL: ")
if channel_url == "":
    channel_url = "https://www.youtube.com/c/EntropyforLife"
    print("Setted: " + channel_url)

while True:
    limit = input("How many videos do you want? ")
    if limit == "":
        print("No input received. Exiting...")
        exit()
    elif limit.isdigit():
        limit = int(limit)
        break
    else:
        print("Invalid input. Please insert a number.")
print("")


print("Searching {} videos for {}".format(limit, channel_url))

videos = scrapetube.get_channel(channel_url=channel_url, limit=limit)

videos_data = []
x = -1
for video in videos:
    title = video['title']['runs'][x+1]['text']
    view_count = extract_number(video['viewCountText']['simpleText'])
    videos_data.append((view_count, title))

# Configure output
views_width = len(str(max(v[0] for v in videos_data))) + 2
title_width = 60
format_string = "{{:>{}s}}  {{:<{}s}}".format(views_width, title_width)

# Print list videos
print(format_string.format("Views", "Title"))
for view_count, title in videos_data:
    print(format_string.format(str(view_count), textwrap.shorten(str(title), width=title_width, placeholder="...")))
print("")

# Print average views
average_views = round(sum(v[0] for v in videos_data) / len(videos_data))
print("The average views is " + str(average_views))
print("")





