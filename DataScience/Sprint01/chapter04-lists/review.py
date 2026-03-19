movie_info = ['Fight Club', 1999, ['thriller', 'drama', 'crime'], 139, 8.644]
print(movie_info[4]) #accessing an elemnt from the list
print(movie_info[2][-1]) #accessing subelemnt


#==============================================================================
#Slicing a list
movie_info = ['Fight Club', 1999, ['thriller', 'drama', 'crime'], 139, 8.644]
print(movie_info[2:4])


# Método	| Um elemento	| Vários elementos | No final da lista | Em qualquer parte da lista
# append()	        +   	          -             	+	                        -
# extend()	        +	              +             	+                       	-
# insert()	        +	              -	                +                       	+

#==============================================================================
#delet
movies = ['Matrix', 'Matrix 2', 'Matrix 3']
movies.pop(1)
print(movies)

#==============================================================================
movies_duration = [142, 175, 152, 195, 201, 154, 178, 139]
# movies_duration_sorted = sorted(movies_duration, reverse=True)
# print(f'Sorted: {movies_duration_sorted}')

movies_duration_sort = movies_duration.sort(reverse=True)
print(f'Sort: {movies_duration_sort}')

#==============================================================================
