import urllib.request
import http.cookiejar

# 网页下载器
url = "http://www.baidu.com"

print("第一种方法")

response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))


print("第二种")
request = urllib.request.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib.request.urlopen(url)
print(response2.getcode())
print(len(response2.read()))


print("第三种")
cj = http.cookiejar
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
#urllib.request.install_urlopen(url)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(cj)
print(response3.read())
