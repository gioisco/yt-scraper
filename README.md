# yt-scraper

CLI to calculate the average views of the last n videos of a channel

## How to install

1) Get the project
    - clone the project `git clone https://github.com/gioisco/yt-scraper.git`  
  or
    - download the [zip](https://github.com/gioisco/yt-scraper/archive/refs/heads/main.zip) file 
2) Install dependecies  
   `pip install -r requirements.txt`
   
## How to use

1) Run program  
2) Insert the channel URL
3) Insert the number of videos you want
   
```
$ python app.py 
__   __          _         _                                               
\ \ / /__  _   _| |_ _   _| |__   ___   ___  ___ _ __ __ _ _ __   ___ _ __ 
 \ V / _ \| | | | __| | | | '_ \ / _ \ / __|/ __| '__/ _` | '_ \ / _ \ '__|
  | | (_) | |_| | |_| |_| | |_) |  __/ \__ \ (__| | | (_| | |_) |  __/ |   
  |_|\___/ \__,_|\__|\__,_|_.__/ \___| |___/\___|_|  \__,_| .__/ \___|_|   
                                                          |_|              

Insert channel URL: https://www.youtube.com/@Computerphile
How many videos do you want? 3

Searching 3 videos for https://www.youtube.com/@Computerphile
  Views  Title                                                       
  54512  Garbage Collection (Mark & Sweep) - Computerphile           
  98182  Emulation - Computerphile                                   
  49928  Malware and Machine Learning - Computerphile                

The average views is 67541
```
 
## Dependency

[scrapetube](https://github.com/dermasmid/scrapetube)

