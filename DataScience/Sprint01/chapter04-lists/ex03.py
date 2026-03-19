#sort
years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997]
print(years)

# ascending order
years.sort()
print(years)

# descending order
years.sort(reverse=True)
print(years)

#lexicographical order
movies = ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Schindler\'s List']
movies.sort()
print(movies)

#serted() returns a new sorted list, leaving the original list unchanged
movies_duration = [142, 175, 152, 195, 201, 154, 178, 139]
movies_duration_sorted = sorted(movies_duration, reverse=True)# classificar a lista movies_duration usando sorted()
print(movies_duration_sorted)# imprima a lista resultante aqui
