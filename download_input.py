import urllib.request
import argparse
import datetime
import time
HERE=os.path.dirname(os.path.abspath(__file__))
def _get_cookie():
    with open(os.path.join(HERE,.env)) as f:
        contents=f.read().strip()
        return {'Cookie':contents}
if __name__=='__main__':
    today=datetime.date.today()
    year=today.year
    day=today.day
    parser=argparse.ArgumentParser()
    parser.add_argument('--year',type=int,default=year)
    parser.add_argument('--day',type=int,default=day)
    url=f'https://adventofcode.com/{year}/day/{day}/input'
    req=urllib.request.Request(url,headers=_get_cookie())
    for i in range(5):
        try:
            s=urllib.request.urlopen(req).read().decode()
        except urllib.error.URLError as e:
            print('not ready yet')
            time.sleep(2)
        else:
            break
    else:
        raise SystemExit('timed out')
    with open(f'{year}/input_{day}.txt','w') as f:
        f.write(s)


    
