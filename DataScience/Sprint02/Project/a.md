### Escreva suas observações. Aqui estão algumas perguntas que podem ajudar: <a id='data_review_conclusions'></a>


`1.   Que tipo de dados temos nas linhas? E como podemos entender as colunas?`

`2.   Esses dados são suficientes para responder à nossa hipótese ou precisamos de mais dados?`

`3.   Você notou algum problema nos dados, como valores ausentes, duplicados ou tipos de dados errados`


**RESPOSTA:**  
**1.1 NAS LINHAS podemos observar que ao dar print no comando df.info() ou df.shape, temos 65079 linhas, onde cada linha registra a execução de uma música. Na linha é registrado o indentificador único por usuário, a música reproduzida e seu respectivo artista e gênero musical, e também temos a cidade do usuário, bem como a hora e o dia da semana em que a musica foi reproduzida**

**1.2 NAS COLUNAS: Temos 7 como confirmado pela documentação, onde:**  
**Os cabeçalhos precisaram ser padronizados (remover espaços de city e userID, além de transforma tudo em minúsculo)**  
**acredito que o código abaixo resolveria a questão:**
```python
new_col_names = []
for old_name in df.columns:
    name_stripped = old_name.strip()
    name_lowered = name_stripped.lower()
    name_no_spaces = name_lowered.replace(' ','_')
    new_col_names.append(name_no_spaces)
df.columns = new_col_names
#Antes: Index(['  userID', 'Track', 'artist', 'genre', '  City  ', 'time', 'Day'], dtype='str')
#Depois: Index(['userid', 'track', 'artist', 'genre', 'city', 'time', 'day'], dtype='str')
```

**2 Todos os atributos são importantes, mas podemos dizer que city e day são focais para a hipotese que visa verificar se a atividade dos usuários é diferente dependendo do dia da semana e da cidade**

**3 Os dados paresentam alguns problemas:**  
  
**VALORES NULOS:**
- **Utilizando df.isna().sum() podemos notar a coluna track com 1343 registro nulos, artist com o 7567 e genre com 1198.**  
- **Se utilizarmos o comando print(df.isna().mean().round(2) * 100) podemos notar que esses valores em porcentagem estão abaixo de 13% o que indica que podemos desconsidera-los e removê-los sem afetar a análise e para isso utilizamos o seguintes comando:**
```python
df.dropna(subset=['track', 'artist', 'genre'], inplace=True)

```
  
**VALORES DUPLICADOS:**
- **Podemos identificar 3826 duplicidades no arquivo com o comando:**
```python
print(df[df.duplicated()]) 
```
- **Iremos remover as 3826 duplicidades identificadas (somente 6% do total de 65079 do arquivo geral - antes de qualquer tratamento) e para isso iremos utilizar o comando:**
```python
df.drop_duplicates(inplace=True) 
```
- **E para gerar no index utilizaremos:**
```python
df.reset_index(drop=True)
```

**VALORES QUESTIONÁVEIS:**
- **Valor único: Utilizei o código a seguir para listar os valores unicos da coluna artista e salvar em uma lista**
```python
artist = df['artist'].unique()
list_artist = []
for a in artist:
    list_artist.append(a)
```
- **Encontrei alguns valores nas respectivas posições da lista valores que não parecem ser nomes de artistas: (Considerando que eu ja removi os duplicados e as linhas com valores núlos):**
```python

artista_Valor_posicao = { 
    'Pink Floyd Floydhead':10,
    'FOrΣvΣrT':74
    'Vol.2':95,
    'Christmas Hits':125,
    'Summer Hit Superstars':163,
    'Films Movie':174,
    'Mindfulness Meditation Music Spa Maestro':203,
    'Richard Lewis/James Milligan/John Cameron/Owen Brannigan/Glyndebourne Chorus/Peter Gellhorn/Pro Arte Orchestra/Sir Malcolm Sargent':359
    '80s Greatest Hits':725,
    'Lo Mejor Del Rock De Los 80':1366,
    'Elsie Morison/Alexander Young/Michael Langdon/Beecham Choral Society/Royal Philharmonic Orchestra/Sir Thomas Beecham':1506,
    'Le\xadæther Strip':30335,
}

```
- **Observações sobre os nomes encontrados:**  
**Nome alterado do artista:** "Pink Floyd Floydhead" em vez de "Pink Floyd Floyd";  
**Caracteres especiais e barra:** "FOrΣvΣrT", "Le\xadæther Strip";  
**Nomes de álbuns em vez de nome do artista:** 'vol.2', 'Christmas Hits', 'Summer Hit Superstars', 'Films Movie','Mindfulness Meditation Music Spa Maestro', '80s Greatest Hits','Lo Mejor Del Rock De Los 80'.

**Obs: Na vida real é bom verificar com o time de negócios se algum dado é realmente relevante antes de tomar qualquer decisão de remoção, mas para fins didáticos irei remover as linhas, pois, se compararmos com o total de linhas**  

**Irei gerar uma lista com os nomes "não conforme":**
```python
lista_artistas = [
    'Pink Floyd Floydhead',
    'FOrΣvΣrT',
    'Vol.2',
    'Christmas Hits',
    'Summer Hit Superstars',
    'Films Movie',
    'Mindfulness Meditation Music Spa Maestro',
    'Richard Lewis/James Milligan/John Cameron/Owen Brannigan/Glyndebourne Chorus/Peter Gellhorn/Pro Arte Orchestra/Sir Malcolm Sargent',
    '80s Greatest Hits',
    'Lo Mejor Del Rock De Los 80',
    'Elsie Morison/Alexander Young/Michael Langdon/Beecham Choral Society/Royal Philharmonic Orchestra/Sir Thomas Beecham',
    'Le\xadæther Strip'
]
```

**Depois irei contar quantas vezes eles aparecem no dataframe na coluna artist e armazenar o valor que cada item aparece em um objeto e depois somar o total para verificar que o total é irrelevante**  

```python
total_count = 0
for artista in lista_artistas:
    count = df['artist'].str.contains(artista, case=False, na=False).sum()
    total_count += count
    print(f'{artista}: {count}')
print(f'Total count of artists in the list: {total_count}')

#Total count of artists in the list: 53
```

**Agora iremos recriar o dataframe SEM as linhas em que a coluna artist é igual a algum item da variavel lista_artistas criada anteriormente:**
```python
print(df.shape) # para verificar a quantidade de linhas antes

for artista in lista_artistas:
    df = df[~df['artist'].str.contains(artista, case=False, na=False)]

print(df.shape) # para verificar se a quantidade de linhas removidas foi 53
```
