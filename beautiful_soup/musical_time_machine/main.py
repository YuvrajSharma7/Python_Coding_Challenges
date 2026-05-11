import os

from bs4 import BeautifulSoup
import requests
import os
from ytmusicapi import YTMusic


# Optional Troubleshooting Step - Check for browser.json before doing anything else
if not os.path.exists("browser.json"):
    print("browser.json not found.")
    print("You need to authenticate with YouTube Music first.")
    print("Run one of these commands in your terminal from this project folder:\n")
    print("  Mac:     pbpaste | ytmusicapi browser")
    print("  Windows: ytmusicapi browser\n")
    print("Copy the request headers from Firefox first.")
    print("This will create browser.json.")
    exit()

# Scraping Bakeboard Hot 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
html=requests.get(f'https://appbrewery.github.io/bakeboard-hot-100/{date}/',headers=header).text
soup = BeautifulSoup(html, 'html.parser')

song_titles=soup.find_all('h3', class_='chart-entry__title')
top_100_titles=[item.get_text() for item in song_titles]
# top_100_titles = [tag.getText().strip() for tag in soup.select("h3.chart-entry__title")] short way, string comprihension
# print(top_100_titles)



yt = YTMusic("browser.json")

# Verify authentication works
playlists = yt.get_library_playlists()
print(f"Found {len(playlists)} playlists in your library.")
print(playlists)

PLAYLIST_NAME = f"{date} Billboard 100"

# Check if playlist already exists
playlist_id = None
playlists = yt.get_library_playlists(limit=100)

for p in playlists:
    if p["title"] == PLAYLIST_NAME:
        playlist_id = p["playlistId"]
        break

if playlist_id:
    print("This playlist already exists.")
else:
    playlist_id = yt.create_playlist(
        PLAYLIST_NAME,
        f"Playlist with the hottest songs from {date}",
        privacy_status="PRIVATE",
    )
    print(f"Created playlist: {PLAYLIST_NAME}")

# Search and add each song
for song in top_100_titles:
    try:
        search_results = yt.search(song, filter="songs", limit=1)
        yt.add_playlist_items(playlist_id, [search_results[0]["videoId"]])
        print(f"Added: {song}")
    except Exception as e:
        print(f"Skipped: {song} | Reason: {e}")