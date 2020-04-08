"""
Tarea 1
#1 favorite song
#2 this application gives us information about the song gravity of John Mayer
#3 in this section the values are given to each attribute
"""
def favsong():
    Name = "Gravity"
    Artist = "John Mayer"
    DurationInMinutes = 4.05
    DurationInSeconds = 243
    AgeArtist = 42
    Album = "Continuum"
    AlbumAge = 2006
    LaunchMonth = "September"
    AlbumDuration = 50.00
    Genre = "blues,rock,pop"
    Discography = "Aware, Columbia, Sony BMG"
    Producers = "John Mayer and Steve Jordan"


# in this section it will print each attribute implemented previously
    print("Name: " + Name)
    print("Artist: " + Artist)
    print("Duration in Minutes:",DurationInMinutes) #use commas in case float, integer
    print("Duration in Seconds:", DurationInSeconds) #use commas in case float, integer
    print("Age Artist:",AgeArtist) #use commas in case float, integer
    print("Album name: " + Album)
    print("Album age:",AlbumAge) #use commas in case float, integer
    print("Launch month: " + LaunchMonth)
    print("Album duration:",AlbumDuration) #use commas in case float, integer
    print("Genre:"+ Genre)
    print("Discography" + Discography)
    print("Producers: " + Producers)
favsong()
