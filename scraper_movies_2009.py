# The script scrapes bollywood movies list from Wikipedia. 
from BeautifulSoup import  *
import urllib2

def process_table(table):
	headings = [heading.text for heading in table.tr.findAll('th')]
	print headings
	rows = table.findAll('tr')
	numRows = len(rows)
	month = ""
	date = ""
	details = []
	for j in range(1,numRows):
		#~ print month , date
		if month == "":
			movie = rows[j].findAll('td')
			#~ print movie
			month = movie[0].text
			try:
				numMoviesInMonth= int(movie[0]['rowspan'])
			except: 
				numMoviesInMonth= 1
			try:
				numMoviesOnDate= int(movie[1]['rowspan'])
			except: 
				numMoviesOnDate=  1
			date = movie[1].text
			i=2
		elif date == "":
			movie = rows[j].findAll('td')
			date = movie[0].text
			try:
				numMoviesOnDate= int(movie[0]['rowspan'])
			except:
				numMoviesOnDate= 1
			i=1
		else :
			movie = rows[j].findAll('td')
			i=0
		numMoviesInMonth -= 1
		numMoviesOnDate -= 1
		#~ print i , numMoviesInMonth , numMoviesOnDate
		movie_details = [(date,month,year), movie[i].text, movie[i+1].text , movie[i+3].text, movie[i+2].text.split(',') ]
		#~ print movie_details
		details.append(movie_details)
		if numMoviesInMonth == 0 : 
			month =""
		if numMoviesOnDate == 0 : 
			date =""
	print details



year = 2008
url= "http://en.wikipedia.org/wiki/List_of_Bollywood_films_of_" + str(year)

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7'}
request = urllib2.Request(url, '', headers)
response = urllib2.urlopen(request)
returned_array = [response.geturl(), response.read()]
#~ print returned_array

page = BeautifulSoup(returned_array[1])

#~ print page

movies = page.findAll(attrs = {'class': "wikitable" })
for table in movies:
	process_table(table)
