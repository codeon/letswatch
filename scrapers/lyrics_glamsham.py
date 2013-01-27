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

def get_song_list(link):
	url= "http://www.glamsham.com"+link
	headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7'}
	request = urllib2.Request(url, '', headers)
	response = urllib2.urlopen(request)
	returned_array = [response.geturl(), response.read()]
	page = BeautifulSoup(returned_array[1])
	songs = page.findAll('table')[9].__unicode__()
	till = songs.find("<!-- Music Review starts-->")
	#~ print till
	songs = songs[:till]
	#~ print songs 
	songs = page = BeautifulSoup(songs)
	try:
		links = songs.findAll('a')
	except:
		return False
	temp = {}
	for link in links:
		temp[link.text]=link['href']
	
	return temp
	
def get_lyrics(link):
	url= "http://www.glamsham.com"+link
	headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7'}
	request = urllib2.Request(url, '', headers)
	response = urllib2.urlopen(request)
	returned_array = [response.geturl(), response.read()]
	page = BeautifulSoup(returned_array[1])
	lyrics = page.findAll(attrs = {'class': 'general'})[6]
	print lyrics
	
	
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
				movies[movie] = [result[movie]]
				print movie
				songs=get_song_list(movies[movie][0])
				if not songs == False:
					print len(songs)
					movies[movie].append(songs)
					for key in songs.keys():
						get_lyrics(songs[key])
				else :
					print 0
					movies[movie].append({})
				#~ break
			page += 1
	#~ for movie in movies:
		
