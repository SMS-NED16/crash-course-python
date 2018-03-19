def make_album(artist_name, album_title, number_of_tracks = ''):
	album = {}
	album['name'] = album_title
	album['artist'] = artist_name
	if number_of_tracks:
		album['tracks'] = number_of_tracks
	return album

album_1 = make_album("Guns N' Roses", "Appetite for Destruction", 12)
album_2 = make_album("Pink Season", "Pink Guy")

print(album_1)
print(album_2)