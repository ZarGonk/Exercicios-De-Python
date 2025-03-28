import urllib
import urllib.request

try:
    url = str(input('Digite a URL: '))
    site = urllib.request.urlopen(url)

except urllib.error.URLError:
    print(f'\033[31mO site {url} não esta acessivel ou não é seguro\033[m ')
else:
    print(f'\033[32mSite {url} acessdo com sucesso\033[m') 