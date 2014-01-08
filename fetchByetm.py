import urllib2

# er_sn_in=1-607
baseurl = "http://home.alc.co.jp/db/owa/etm_rsch?er_sn_in={num}"
for i in xrange(607):
    url = baseurl.format(num=i+1)
    html = urllib2.urlopen(url).read()
    fname = "etmhtml/etm{num}.html".format(num=str(i+1).rjust(3, '0'))
    f = open(fname, "w")
    f.write(html)
    f.close()
