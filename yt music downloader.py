from pytube import Playlist
p = Playlist('add your playlist here')
print(f'Downloading: {p.title}')
for video in p.videos:
    video.streams.first().download()
