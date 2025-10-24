def make_album(artist_name, album_title, num_songs=0):
    """Ex8-7 Return an album dictionary"""
    music_album = {
        'artist': artist_name.title(),
        'title': album_title.title(),
        }
    if num_songs:
        music_album['num_songs'] = num_songs

    return music_album

album=make_album('The Wilder Blue', "Dixie Darlin'")
print(album)

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('willie nelson', 'red-headed stranger')
print(album)

album = make_album('the wilder blue', 'still runnin', num_songs=4)
print(album)
