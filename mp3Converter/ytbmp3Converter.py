import youtube_dl
import os
import sys


ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'postprocessors':
            [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

if __name__ == "__main__":
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:

        while True:
            try:
                url = input("Enter the Youtube URL you wish to download as mp3 file: ")
                searchsong = url
                #print(searchsong)
                print("Downloading the File now")
                ydl.download([f"ytsearch1:{searchsong}"])
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        songname = file

                print("Download Finished! Exiting the program.")
                break;
            except:
                print("Invalid URL, please try again.")

                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, 'song.mp3')