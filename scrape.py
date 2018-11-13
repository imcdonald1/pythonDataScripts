import requests
from bs4 import BeautifulSoup

movie_superlist = list()

for i in range(1,101):
	url = 'https://www.imdb.com/search/title?genres=Sci-fi&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=75c37eae-37a7-4027-a7ca-3fd76067dd90&pf_rd_r=Z44TQQN4DPB9DXNMA3ZR&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&view=advanced&sort=user_rating,desc&page='+str(i)+'&ref_=adv_nxt'
	response = requests.get(url)
	html_response = BeautifulSoup(response.text, 'html.parser')
	movie_list = html_response.find_all('div', class_='lister-item mode-advanced')
	movie_superlist.append(movie_list)

for i in range(len(movie_superlist)):
	for j in range(len(movie_superlist[i])):
		movie = movie_superlist[i][j]
		movie_title = movie.h3.a.text
		movie_year = movie.h3.find('span', class_='lister-item-year text-muted unbold').text
		movie_genre = movie.p.find('span', class_='genre').text
		movie_rating = movie.strong.text
		movie_runtime = movie.p.span.text
		if(movie_title is None or movie_year is None or movie_genre is None or movie_rating is None or movie_runtime is None):
			continue
		line = str(movie_title)+','+str(movie_year)+','+str(movie_genre).strip()+','+str(movie_rating)+','+str(movie_runtime).strip()
		