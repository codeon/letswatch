# The script scrapes bollywood movies list from Wikipedia. 
from BeautifulSoup import  *
import urllib2

def get_movie_list(letter, pageno):
	url= "http://www.glamsham.com/music/lyrics/1/"+str(pageno)+"/"+letter+".htm"
	headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7'}
	request = urllib2.Request(url, '', headers)
	response = urllib2.urlopen(request)
	returned_array = [response.geturl(), response.read()]
	page = BeautifulSoup(returned_array[1])
	#~ print page
	movies = page.findAll('table')[8]
	#~ print movies
	movies = movies.findAll(attrs = {'class': "titlebg" })
	#~ print len(movies)
	temp = {}
	for movie in movies:
		#~ print movie
		try:
			link = movie.findAll('a')[1]
		except:
			return False
		#~ print link
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
			
