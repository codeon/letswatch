# The script scrapes bollywood movies list from Wikipedia. 
from BeautifulSoup import  *
import urllib2

def get_movie_list(letter, pageno):
	url= "http://www.planetradiocity.com/lyricsfinder/lyrics-category-details.php?page="+str(pageno)+"&letter="+letter+"&catid=1"
	headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7'}
	request = urllib2.Request(url, '', headers)
	response = urllib2.urlopen(request)
	returned_array = [response.geturl(), response.read()]
	page = BeautifulSoup(returned_array[1])
	#~ print page
	content_div = page.findAll(attrs = {'class': "lyrics_list_div" })[0]
	movies = content_div.findAll(attrs = {'class': "lyrics_category_list_new" })
	temp = {}
	if len(movies) == 0 :
		return False
	else:
		for movie in movies:
			#~ print movie
			link = movie.findAll('a')[0]
			temp[link.text] = link['href']
		#~ print letter, pageno, len(movies)
		return temp

if __name__ == "__main__":
	letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	page = 0
	movies={} # Stores movie name and link to movie lyrics page
	i=0
	while i < len(letter):
		result = get_movie_list(letter[i], page)
		if result == False:
			page = 0
			i += 1
		else:
			for movie in result.keys():
				movies[movie] = result[movie]
				print movie
			page += 1
			
