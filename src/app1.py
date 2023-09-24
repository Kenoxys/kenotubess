from pytube import YouTube
YouTube('https://www.youtube.com/shorts/JZhpnpgPxl0').streams.first().download()
yt = YouTube('https://www.youtube.com/shorts/JZhpnpgPxl0')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
