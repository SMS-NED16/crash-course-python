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

while True:
	print("\nEnter album details. Enter 'q' to quit at any time.")
	name = input("Enter album name: ")
	if name.lower() == 'q':
		break

	artist = input("Enter album artist: ")
	if artist.lower() == 'q':
		break

	tracks = input("Enter number of tracks: ")
	if tracks.lower() == 'q':
		break

	user_album = make_album(artist, name, tracks)
	print(user_album)
print("END OF PROGRAMME")