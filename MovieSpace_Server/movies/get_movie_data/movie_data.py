import requests
import json

my_key = '7a8df8004890b70d9d4175ce5a47331d'
movie_list = []

# 불러오기
for page in range(1, 6):
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={my_key}&language=ko&page={page}'
    res = requests.get(url).json()
    data_list = res.get('results')

    # 새로운 리스트 생성
    for data in data_list:
        movie_dict = {
            "model": "movies.movie",
            "pk": data.get("id"),
            "fields" : {
                "title" : data.get('title'),
                "overview": data.get('overview'),
                "poster_path": data.get('poster_path'),
                "backdrop_path": data.get('backdrop_path'),
                "video": data.get('video'),
                "vote_average": data.get('vote_average'),
                "release_date": data.get('release_date'),
                "genres": data.get('genre_ids'),
                "adult": data.get('adult'),
            }
        }
        movie_list.append(movie_dict)

# # print(movie_list)
# print(len(movie_list))
# print(len(movie))

# with open('movies.json', 'w', encoding='UTF-8') as file:
#     file.write(json.dumps(movie_list, ensure_ascii=False))




