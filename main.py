from bs4 import BeautifulSoup
import requests
import re
"""
privacy policyまたはプライバシーポリシー、個人情報がサイトにあるか。
あればTrueなければFalse
"""
import warnings
warnings.filterwarnings('ignore')

def get_html():
    """
    - bs4, requestsが必要
    スクレイピングするならこの関数を最初に使う
    指定したURLのhtml文書を整列して.htmlに保存。
    ページからタグを除去して全テキストを抽出。
    用途: スクレイピングをするときにファイル構造を見る
    """
    r = requests.get("https://www.oreilly.co.jp/index.shtml")
    r.encoding = r.apparent_encoding
    html_doc = r.text
    soup = BeautifulSoup(html_doc)

    html1 = open('Oreilly.html', 'w')
    html1.write(soup.prettify())
    html1 = soup.prettify()

    text1 = open('Oreilly.text', 'w')
    text1.write(soup.get_text())
    text1 = soup.get_text()

    """
    以下からは需要に応じてオプション
    プライバシーポリシー系を探す
    Privacy policy、プライバシーポリシー、個人情報
    """

    pattern = r"privacy policy|個人情報|プライバシーポリシー"

    with open('Oreilly.html') as f:
        soup = BeautifulSoup(f.read(), 'lxml')

        for link in soup.findAll('a', text=re.compile(pattern, re.IGNORECASE)):
            print(link['href'])
    """
    priv_htm = re.search(r"privacy policy|プライバシーポリシー|個人情報", html1).start()
    if priv_htm != -1:
        print(priv_htm)
        print(re.search(r"privacy policy|プライバシーポリシー|個人情報", html1))
        print("hrefを取得します")


    else: print("ありませんでした")
    """
get_html()
