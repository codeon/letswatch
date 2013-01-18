import gdata
import gdata.youtube
import gdata.youtube.service


class YoutubeQueryObject:
	
	def __init__(self, developer_key):
		self.serviceObj =  gdata.youtube.service.YouTubeService()
		self.serviceObj.ssl = True
		self.serviceObj.developer_key = developer_key
	
	def getSearchResults(self, query, orderby='relevance' , starts =1, maxnumber=25):
		queryObj = gdata.youtube.service.YouTubeVideoQuery() # http://gdata-python-client.googlecode.com/hg/pydocs/gdata.youtube.service.html#YouTubeVideoQuery
		queryObj.vq = query
		queryObj.orderby = orderby
		queryObj.start_index = starts
		queryObj.max_results = maxnumber
		results = self.serviceObj.YouTubeQuery(queryObj)
		return results
		
	def getUserUploads(self, username , starts=1, maxnumber=25):
		uri = 'http://gdata.youtube.com/feeds/api/users/%s/uploads?max-results=%s&start-index=%s' % (username, maxnumber, starts )
		return self.serviceObj.GetYouTubeVideoFeed(uri)
		
	def getRelatedFeed(self, videoid):
		return self.serviceObj.GetYouTubeRelatedVideoFeed(uri=videoid)
	#~ def get


class ProcessData:
	@staticmethod
	def PrintVideoTitles(feed):
		for result in feed.entry:
			print result.media.title.text 
			for author in result.author:
				print author.text
			#~ print result.media.player.url
			#~ print result.id.text

			
	@staticmethod
	def DetailedEntryListInfo(videos):
		for entry in videos:
			ProcessData.PrintCompleteInfo(entry)
			
	@staticmethod
	def DetailedFeedInfo(feed):
		for entry in feed.entry:
			ProcessData.PrintCompleteInfo(entry)
	
	@staticmethod
	def PrintCompleteInfo(entry):
		print 'Video title: %s' % entry.media.title.text
		#~ print '\tVideo published on: %s ' % entry.published.text
		print '\tVideo description: %s' % entry.media.description.text
		print '\tVideo category: %s' % entry.GetYouTubeCategoryAsString()
		print '\tVideo tags: %s' % entry.media.keywords.text
		print '\tVideo watch page: %s' % entry.media.player.url
		for author in entry.author:
			print '\tVideo Author : %s' % author.name.text
		#~ print '\tVideo flash player URL: %s' % entry.GetSwfUrl()
		print '\tVideo duration: %s' % entry.media.duration.seconds
		print ""

		#~ # non entry.media attributes
		#~ print 'Video geo location: %s' % entry.geo.location()
		#~ print 'Video view count: %s' % entry.statistics.view_count
		#~ print 'Video rating: %s' % entry.rating.average
#~ 
		#~ # show alternate formats
		#~ for alternate_format in entry.media.content:
			#~ if 'isDefault' not in alternate_format.extension_attributes:
			  #~ print 'Alternate format: %s | url: %s ' % (alternate_format.type,
                                                 #~ alternate_format.url)
#~ 
		#~ # show thumbnails
		#~ for thumbnail in entry.media.thumbnail:
			#~ print 'Thumbnail url: %s' % thumbnail.url

if __name__ == '__main__':
	mainObj = YoutubeQueryObject('AI39si5d0rvqykK18EUEVXh9f8i3OitywaQgJisBaH2kxUuEl6qTijdjNBqamZccYZaKyJdNbgeSzB1vLhpDQfYx_AIFD1QbOA')
	query = raw_input("Enter a query \n")
	results = mainObj.getUserUploads(query, starts = 25, maxnumber=25)
	ProcessData.DetailedFeedInfo(results)
	
	
