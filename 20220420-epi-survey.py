import requests
import re
from bs4 import BeautifulSoup
from sympy import print_glsl
r=requests.get("https://mp.weixin.qq.com/s/sLnnwrcyN_KcIAFLKMcxdw")
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
for add in soup.find_all(string=re.compile('平房区')):
    print(add)
