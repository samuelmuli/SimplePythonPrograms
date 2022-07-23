import pytube
url =input( "Enter URL VIDEO FORMAT: ")
path = "D:"
pytube.YouTube(url).streams.get_highest_resolution().download(path)
