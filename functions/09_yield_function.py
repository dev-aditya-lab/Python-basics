def even_genreator(limit):
    for i in range(2, limit + 1, 2):
        yield i
        

for num in even_genreator(10):
    print(num)