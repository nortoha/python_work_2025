def make_album(artist_name, album_title, num_songs=0):
    """Ex8-8 Return an album dictionary"""
    music_album = {
        'artist': artist_name.title(),
        'title': album_title.title(),
        }
    if num_songs:
        music_album['num_songs'] = num_songs

    return music_album


## Ex 8-8
# Prepare the prompts.
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    
    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding!")
