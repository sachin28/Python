import urllib2

'''retrieving data from the internet'''


def main():
    webUrl = urllib2.urlopen("https://google.com")
    print "result: " + str(webUrl.getcode())

    data = webUrl.read()
    print data


if __name__ == "__main__":
    main()
