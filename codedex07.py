

def write_liked_songs(liked_songs, file_name):
    with open(file_name, "a") as file:
        file.write("Lista di cose che mi piacciono \n")
        for i in range(len(liked_songs)):
            file.write(f"{list(liked_songs.keys())[i]} by {liked_songs[list(liked_songs.keys())[i]]} \n")
            


liked_songs = {"Vermintide" : "Fatshark", "Demoni" : "Lamberto Bava"}
write_liked_songs(liked_songs, "playlist.txt")  
    