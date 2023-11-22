from pytube import YouTube

myStream = YouTube("https://www.youtube.com/watch?v=oS8lASbvlpI").streams.first()

myStream.download("C:/Users/xaziv/OneDrive/Рабочий стол")
