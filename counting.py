urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",
]

def count(urls):
    url_dict = {}
    
    for url in urls:
        filename = url.split('/')[-1]
        if filename in url_dict:
            url_dict[filename] += 1
        else:
            url_dict[filename] = 1
    
    sorted_url = sorted(url_dict.items(), key=lambda kv: kv[1], reverse=True)
    
    for i in range(3):
        print(sorted_url[i][0])

count(urls)