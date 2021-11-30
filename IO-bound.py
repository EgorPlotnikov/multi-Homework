import urllib
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from tqdm import tqdm
import concurrent.futures


wiki_random = r'https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
res = open('wiki_links.txt', 'w', encoding='utf8')

for i in tqdm(range(100)):
    html = urlopen(wiki_random).read().decode('utf8')
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')

    for l in links:
        href = l.get('href')
        if href and href.startswith('http') and 'wiki' not in href:
            print(href, file=res)

links = open('wiki_links.txt', encoding='utf8').read().split('\n')


def single_thread_execution(links):
    global code
    for url in links:
        try:
            request = Request(
                url,
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
            )
            response = urlopen(request, timeout=5)
            code = response.code
            print(code)
            response.close()
        except Exception as e:
            print(url, e)


#single_thread_execution(links)


def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


def multi_thread_execution():
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        future_to_url = {executor.submit(load_url, url, 60): url for url in links}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data)))


#single_thread_execution(links)
multi_thread_execution()
