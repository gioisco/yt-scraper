import os
import pyfiglet
import scrapetube
from datetime import datetime
import pandas as pd

from utils import extract_number

ascii_art = pyfiglet.figlet_format("YT Scraper Analyzer")
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

now = datetime.now()
videos_data = []
x = -1
for video in videos:
    video_id = video['videoId']
    title = video['title']['runs'][x+1]['text']
    view_count = extract_number(video['viewCountText']['simpleText'])
    view_count = view_count
    videos_data.append((now, video_id, view_count, title))

videos_data.reverse()
df = pd.DataFrame(videos_data, columns=['date_time', 'video_id', 'view_count', 'title'])
print(df)

# Save file
if os.path.isfile('videos_data.csv'):
    existing_df = pd.read_csv('videos_data.csv', nrows=1)
    existing_columns = set(existing_df.columns)
    new_columns = set(df.columns)
    if existing_columns == new_columns:
        df.to_csv('videos_data.csv', mode='a', header=False, index=False)
    else:
        missing_columns = new_columns.difference(existing_columns)
        raise ValueError(f"Columns {missing_columns} do not match between new DataFrame and existing csv file.")
else:
    df.to_csv('videos_data.csv', index=False)





