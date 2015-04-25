import requests as rq

if __name__ == "__main__":
    req = rq.get("https://api.github.com/users/RadoRado/followers")
    names = set()
    status = req.status_code
    jsoned = req.json()
    lst = [name['login'] for name in jsoned]
    for name in lst:
        names.add(name)
    req = rq.get("https://api.github.com/users/RadoRado/followers?page=2")
    status = req.status_code
    cnt = 3
    while status == 200:
        jsoned = req.json()
        lst = [name['login'] for name in jsoned]
        for name in lst:
            names.add(name)
        req = rq.get("https://api.github.com/users/RadoRado/followers?page={}".format(cnt))
        status = req.status_code
        cnt += 1

    print(len(names))
