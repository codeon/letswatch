from search.models import * 
import gdata
import gdata.youtube
import gdata.youtube.service
import datetime.datetime

serviceObj =  gdata.youtube.service.YouTubeService()
serviceObj.ssl = True
serviceObj.developer_key = "AI39si5d0rvqykK18EUEVXh9f8i3OitywaQgJisBaH2kxUuEl6qTijdjNBqamZccYZaKyJdNbgeSzB1vLhpDQfYx_AIFD1QbOA"

def getSearchResults(serviceObj, query, orderby='relevance' , starts =1, maxnumber=25):
	queryObj = gdata.youtube.service.YouTubeVideoQuery() # http://gdata-python-client.googlecode.com/hg/pydocs/gdata.youtube.service.html#YouTubeVideoQuery
	queryObj.vq = query
	queryObj.orderby = orderby
	queryObj.start_index = starts
	queryObj.max_results = maxnumber
	results = self.serviceObj.YouTubeQuery(queryObj)
	return results


res = getSearchResults(serviceObj, "Agnee")
for entry in res.entry:
	link = entry.media.player.url
	video_id = link.lsplit('?v=')[1].split('?')[0]
	title = entry.media.title.text
	thumbnail_link = entry.media.thumbnail[0].url
	category = entry.GetYouTubeCategoryAsString()
	tags = entry.media.keywords.text.split()
	permalink = ""
	fb_comments_plugin = ""
	posted_by = Users.objects.get(id=1)
	timestamp = datetime.now()
	rating = entry.rating.average
	num_views= entry.statistics.view_count
	video = Videos(video_id = video_id , link = link, thumbnail_link=thumbnail_link , category = category , tags = tags, permalink=permalink, fb_comments_plugin= fb_comments_plugin, posted_by= posted_by, timestamp = timestamp, rating= rating, num_views = num_views )
	video.save()
		
	
