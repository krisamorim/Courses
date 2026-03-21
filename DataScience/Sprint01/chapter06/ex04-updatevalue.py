movies = [
    ["The Shawshank Redemption", 1994, "Frank Darabont"],
    ["The Godfather", 1972, "Francis Ford Coppola"],
    ["The Dark Knight", 2008, "Christopher Nolan"],
    ["12 Angry Men", 1957, "Sidney Lumet"],
    ["Schindler's List", 1994, "Steven Spielberg"],
    ["The Lord of the Rings: The Return of the King", 2003, "Peter Jackson"]
]

movie_name = "Schindler's List"
correct_year = 1993

for movie in movies: # itere sobre todos os filmes
    if movie[0] == movie_name: # se o título do filme é o que queremos corrigir
        movie[1] = correct_year # corrija o valor que queremos


for movie in movies: # itere sobre todos os filmes
    print(movie)


#==========================================================================

movies = [
    ["The Shawshank Redemption", 1994, "Frank Darabont"],
    ["The Godfather", 1972, "Francis Ford Coppola"],
    ["The Dark Knight", 2008, "Christopher Nolan"],
    ["12 Angry Men", 1957, "Sidney Lumet"],
    ["Schindler's List", 1993, "Steven Spielberg"],
    ["The Lord of the Rings: The Return of the King", 2003, "Peter Jackson"]
]

movie_to_change = "The Lord of the Rings: The Return of the King"
new_movie = "The Lord of the Rings: The Fellowship of the Ring"
new_year = 2001

for movie in movies:
    if movie[0] == movie_to_change:# defina uma condição aqui
        movie[0] = new_movie
        movie[1] = new_year

# não modifique o código abaixo. Ele imprime o resultado
for movie in movies:
    print(movie)
