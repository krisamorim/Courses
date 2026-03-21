# #logical operators
# Operador	Significado	        Exemplo	Resultado
#    ==	       Igual	         5 == 5	  True
#    !=	    Diferente	         5 != 2	  True
#    >	    Maior que	         5 > 2	  True
#    <	    Menos que	         5 < 2	  False
#    >=	    Maior ou igual a	 5 >= 2	  True
#    <=  	Menor ou igual a	 5 <= 5	  True

# Operador	   Significado    	                               Exemplo	         Resultado
#   and	       Ambas as condições devem ser verdadeiras	       5 > 2 and 3 < 5	 True
#   or	       Pelo menos uma condição deve ser verdadeira	   5 > 2 or 3 > 5	 True
#   not	        Inverte o valor verdadeiro de uma condição	   not (5 > 2)	     False


movie_info = ['Fight Club', 'USA', 1999, 'thriller, drama, crime', 139, 8.644]

# primeiro, vamos escrever uma condição como fizemos antes e imprimir o resultado
print(movie_info[2] > 1996 and movie_info[2] < 1998)

# depois, vamos reverter com 'not' e também imprimir o resultado
print(not(movie_info[2] > 1996 and movie_info[2] < 1998))


#predicate functions
# islower() retorna True se todos os caracteres da string alfabética forem minúsculos
# isdigit() retorna o valor True se a string tiver apenas números
# isalpha() retorna True se uma string contém apenas letras. Se uma string contiver sinais de pontuação ou espaços, será retornado False.


