import urllib.request as request

def get_data():
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = request.Request(url)
    with request.urlopen(r) as res:
        data=res.read()
        print(data)

get_data()