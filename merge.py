import csv


with open('movies.csv',encoding='utf8')as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]

headers.append('poster_links')

with open('final.csv','a+',encoding='utf8')as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)

with open('movie_links.csv',encoding='utf8')as f:
    csvreader = csv.reader(f)
    moviedata = list(csvreader)
    all_movies_link = data[1:]

for i in all_movies:
    poster_found = any(i[8]in movie_linked_items for movie_linked_items in all_movies_link)
    if poster_found:
        for movie_linked_items in all_movies_link:
            if i[8] == movie_linked_items[0]:
                i.append(movie_linked_items[1])
                if len(i) == 28:
                    with open('final.csv','a+',encoding='utf8') as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(i)
                