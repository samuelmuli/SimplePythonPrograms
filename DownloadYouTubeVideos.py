import pytube
url =input( "Enter URL VIDEO FORMAT: ")
path = "D:" #specify you local path, could be C,D,E etc
pytube.YouTube(url).streams.get_highest_resolution().download(path)
