import urllib2

url='https://photos.app.goo.gl/lsqJ0euXOftfIJXp2'
response = urllib2.urlopen(url)
dong = response.read()
dong=dong.split("\n")
#    #if len(dong[i])>277 or len(dong[i])<275 or dong[i][0:3]!=',["' :
    #    del dong[i]
hinh=[]
#print dong
for i,d in enumerate(dong):
    hinh.append(d[3:47])   
for h in hinh:
    href=url.replace("?key","/photo/"+h+"?key")
    print href