# Legacy script. Must keep running on Python 2.7 in the old reporting box.
import urllib2


def fetch_report(url):
    print "Fetching %s" % url
    response = urllib2.urlopen(url)
    return response.read()


if __name__ == "__main__":
    print fetch_report("http://reports.internal/daily")
