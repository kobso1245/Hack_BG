import requests as rq

if __name__ == "__main__":
    jsoned = rq.get("https://api.github.com/users/RadoRado/followers?page=1").json()
    cnt = 1
    names = set()
    while jsoned != []:
        lst = [name['login'] for name in jsoned]
        for name in lst:
            names.add(name)
        cnt += 1
        jsoned = rq.get("https://api.github.com/users/RadoRado/followers?page={}".format(cnt)).json()


    print(len(names))
