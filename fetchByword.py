import urllib2

# er_sn_in=1-607
# unum=1-9404
baseurl = "http://home.alc.co.jp/db/owa/etm_sch?unum={num}&stg=2"
for i in xrange(3266, 9404):
    url = baseurl.format(num=i+1)
    html = urllib2.urlopen(url).read()
    fname = "wordhtml/word{num}.html".format(num=str(i+1).rjust(4, '0'))
    f = open(fname, "w")
    f.write(html)
    f.close()
