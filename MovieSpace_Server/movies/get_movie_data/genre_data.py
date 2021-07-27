import requests
import json

my_key = '7a8df8004890b70d9d4175ce5a47331d'

url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={my_key}&language=ko'

res = requests.get(url).json()
data_list = res.get('genres')

genre_list = []
for data in data_list:
    genre_dict = {
        "model": "movies.genre",
        "pk": data.get("id"),
        "fields": {
            "name": data.get("name")
        }
    }
    genre_list.append(genre_dict)

with open('genres.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(genre_list, ensure_ascii=False))
