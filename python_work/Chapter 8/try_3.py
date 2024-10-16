# 8-6. City Names
def city_country(city, country):
    sentence = f"{city.title()}, {country.title()}"
    return sentence

ans_a = city_country('santiago', 'chile')
print(ans_a)
ans_b = city_country('london', 'england')
print(ans_b)
ans_c = city_country('mumbai', 'india')
print(ans_c)
print('\n')

# 8-7. Album
def make_album(artist_name, album_title, song_num=None):
    album = {'artist_name': artist_name, 'album_title': album_title}
    if song_num:
        album['song_num'] = song_num
    
    return album
album_a = make_album('Post Malone', 'F-1 Trillion', 18)
print(album_a)
album_b = make_album('Vulfpeck', 'Sauna')
print(album_b)
album_c = make_album('Beyonce', 'Freedom')
print(album_c)

while True:
    print("(press q to quit anytime)")
    name = input("What is your favorite artist's name? ")
    if name == 'q':
        break
    title = input("What album does this artist have? ")
    if title == 'q':
        break
    full_album = make_album(name.title(), title.title())
    print(full_album)
