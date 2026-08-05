#pip install yt-dlp
import yt_dlp

url = input("https://www.youtube.com/live/WnBzZuB74Zk?si=UGU1L0lM0gZK8jsL")

opcoes = {
    "format": "bestvideo+bestaudio/best",
    "merge_output_format": "mp4",
    "outtmpl": "%(title)s.%(ext)s",
}

with yt_dlp.YoutubeDL(opcoes) as ydl:
    ydl.download([url])

    print("Download Concluído")