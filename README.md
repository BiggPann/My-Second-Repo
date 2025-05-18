🎵 Billboard 100 Spotify Playlist Creator
This Python project creates a private Spotify playlist in your Spotify account containing the Billboard Hot 100 songs from a user-specified date. It scrapes the Billboard website using BeautifulSoup, and uses Spotipy (a Python client for the Spotify Web API) to search for and save the songs to your Spotify account.

📌 Features
Scrapes the Billboard Hot 100 chart for a specified date.

Searches for the songs on Spotify.

Creates a private playlist in your Spotify account with the top 100 songs.

Automatically adds found songs to the playlist.

🛠️ Technologies Used
Python 3

BeautifulSoup

Spotipy

Billboard Hot 100

✅ Requirements
Python 3.x

Spotify Developer Account

Spotify App credentials:

CLIENT_ID

CLIENT_SECRET

A valid Spotify username

Install required packages:

bash
Copy
Edit
pip install beautifulsoup4 requests spotipy
🚀 How to Use
Clone the repository or copy the script into a .py file.

Replace the placeholders:

CLIENT_ID

CLIENT_SECRET

USERNAME

Run the script:

bash
Copy
Edit
python script.py
Enter a date when prompted (in the format YYYY-MM-DD).

Log in to your Spotify account when the browser window opens.

After authorization, the playlist will be created in your account.

📌 Example
bash
Copy
Edit
Enter the date in YYYY-MM-DD format: 2000-08-12
🎉 A private playlist named "08 12, 2000 Billboard 100" will appear in your Spotify account!

⚠️ Notes
Some tracks may not be found on Spotify and will be skipped.

The script uses playlist-modify-private scope and creates only private playlists.

Ensure your redirect URI is added in the Spotify developer dashboard (https://example.com/ in this script).

🔒 Disclaimer
This is a personal project. Your Spotify credentials and token are stored in token.txt and should be handled securely.
