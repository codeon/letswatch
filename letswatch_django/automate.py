from search.models import * 
import gdata
import gdata.youtube
import gdata.youtube.service
import datetime

serviceObj =  gdata.youtube.service.YouTubeService()
serviceObj.ssl = True
serviceObj.developer_key = "AI39si5d0rvqykK18EUEVXh9f8i3OitywaQgJisBaH2kxUuEl6qTijdjNBqamZccYZaKyJdNbgeSzB1vLhpDQfYx_AIFD1QbOA"

def getSearchResults(serviceObj, query, orderby='relevance' , starts =1, maxnumber=25):
	queryObj = gdata.youtube.service.YouTubeVideoQuery() # http://gdata-python-client.googlecode.com/hg/pydocs/gdata.youtube.service.html#YouTubeVideoQuery
	queryObj.vq = query
	queryObj.orderby = orderby
	queryObj.start_index = starts
	queryObj.max_results = maxnumber
	results = serviceObj.YouTubeQuery(queryObj)
	return results

user = Users(name = "Kapil Garg", username= "kapilg")
user.save()

#~ def createCategory(category):
	#~ print category
	#~ cat = Categories(name= category )
	#~ cat.save()
	#~ return cat

cat = Categories(name= "Music" )
cat.save()


res = getSearchResults(serviceObj, "Coke Studio")
for entry in res.entry:
	link = entry.media.player.url
	video_id = entry.media.player.url
	#~ video_id = link.split('?v=')[1].split('?')[0][:25]
	title = entry.media.title.text
	thumbnail_link = entry.media.thumbnail[0].url
	category = ""
	#~ if Categories.objects.filter(name = entry.GetYouTubeCategoryAsString()) == []:
		#~ category = createCategory(entry.GetYouTubeCategoryAsString())
	#~ else:
	category = Categories.objects.filter(name = 'Music')[0]
	#~ tags = entry.media.keywords.text.split()
	#~ tags = 'Music Video'
	permalink = ""
	fb_comments_plugin = ""
	posted_by = user
	timestamp = datetime.datetime.now()
	rating = entry.rating.average
	num_views= entry.statistics.view_count
	#~ video = Videos.objects.create(video_id = video_id , link = link, thumbnail_link=thumbnail_link , category = category , permalink=permalink, fb_comments_plugin= fb_comments_plugin, posted_by= posted_by, timestamp = timestamp, rating= rating, num_views = num_views )
	#~ video.tags.add("Kapil", "Garg")
	#~ 
	video = Videos(video_id = video_id , link = link, thumbnail_link=thumbnail_link , category = category , permalink=permalink, fb_comments_plugin= fb_comments_plugin, posted_by= posted_by, timestamp = timestamp, rating= rating, num_views = num_views , title=title )
	video.save()
	print "SAved"
		
	
