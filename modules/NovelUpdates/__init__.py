
from util.WebRequest import WebGetRobust
import urllib.error

class PluginInterface_NovelUpdates(WebGetRobust):

	name = 'NUWebRequest'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.calls = {
			'getItem'               : self.getItem_Wrapper,
			'getItemPhantomJS'      : self.getItemPhantomJS_Wrapper,
			'getHead'               : self.getHead_Wrapper,
			'stepThroughCloudFlare' : self.stepThroughCloudFlare,
		}

	def getItemPhantomJS_Wrapper(self, url, *args, **kwargs):
		return self.getItemPhantomJS(url, *args, **kwargs)
	def getHeadPhantomJS(self, url, referer):
		return self.getHeadPhantomJS(url, referer)

	def getItem_Wrapper(self, url, *args, **kwargs):
		try:
			return self.getItem(url, *args, **kwargs)
		except urllib.error.HTTPError:
			self.stepThroughCloudFlare(url, titleContains = 'Novel Updates')
			return self.getItem(url, *args, **kwargs)

	def getHead_Wrapper(self, url, *args, **kwargs):
		try:
			return self.getHead(url, *args, **kwargs)
		except urllib.error.HTTPError:
			self.stepThroughCloudFlare(url, titleContains = 'Novel Updates')
			return self.getHead(url, *args, **kwargs)

