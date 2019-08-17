import urllib.request


class HtmlDownloader(object):

    def download(self, url):
        try:
            if url is None:
               return None
            response = urllib.request.urlopen(url)

            if response.getcode() != 200:
              return None
            #print(response.read())
            return response.read()
        except:
            print("这个链接失效")