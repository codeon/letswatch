from letswatch.api import *

queryString = ["Indian Short Movies", "India short film" ]

YTobj = YoutubeQueryObject('AI39si5d0rvqykK18EUEVXh9f8i3OitywaQgJisBaH2kxUuEl6qTijdjNBqamZccYZaKyJdNbgeSzB1vLhpDQfYx_AIFD1QbOA')

def getInfoSearchResults(listSearchQuery):
	videos = []
	for query in listSearchQuery:
		starts = 1
		maxnumber = 50 
		feed = YTobj.getSearchResults(query , starts = starts, maxnumber=maxnumber)
		while len(feed.entry) > 0 and starts<50:# cannot request item beyond 1000 
			videos.extend(feed.entry)		
			starts = starts+maxnumber
			feed = YTobj.getSearchResults(query , starts = starts, maxnumber=maxnumber)
	ProcessData.DetailedEntryListInfo(videos)

#~ getInfoSearchResults(queryString)

channels = ["cokestudioatmtv" , "yrftrailers"]
channels_mov =  ["yrftrailers","erosentertainment","tseries","sonymusicindiaSME","UTVMotionPictures","bigpictures","Viacom18Movies","DharmaMovies","tipsmusic","excelmovies","yrf","BalajiMotionPictures","WideFrameOfficial"]
channels_sf = ["1takemedia","TheCurioFilms","TheViralFeverVideos"]
channels_news = ["ndtv","newsxlive","ibnlive","timesnowonline","ndtvindia","headlinestoday","tehelkatv"]
channels_edu = ["nptelhrd"]

def getInfoChannels(listChannels , vids):
	videos = []
	for channel in listChannels:
		starts = 1
		maxnumber = 50 
		feed = YTobj.getUserUploads(channel , starts = starts, maxnumber=maxnumber)
		while len(feed.entry) > 0 and starts<950:# cannot request item beyond 1000 
			videos.extend(feed.entry)		
			starts = starts+maxnumber
			feed = YTobj.getSearchResults(channel , starts = starts, maxnumber=maxnumber)
		#~ print len(feed.entry), starts
	ProcessData.DetailedEntryListInfo(videos)
	print videos
	vids= videos

vids=""
#~ getInfoChannels(["qZR7KVVsZRSfezZKJllxVQ"], vids )
getInfoChannels(channels_mov , vids)
#~ getInfoChannels(channels_sf)
#~ getInfoChannels(channels_news)
#~ getInfoChannels(channels_edu)
