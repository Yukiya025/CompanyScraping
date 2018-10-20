# [Python `.find()` 文字列検索] 「または」の設定方法

こんにちは! 取得した文字列で3つの文字列のうちどれがあるか、またはないのかを検索したいです。しかし、「または」の設定方法がわかりません。


**現在のコード**

```python
    r = requests.get("https://www.oreilly.co.jp/index.shtml")
    r.encoding = r.apparent_encoding
    html_doc = r.text
    soup = BeautifulSoup(html_doc)

    html1 = open('Oreilly.html', 'w')
    html1.write(soup.prettify())
    text1 = open('Oreilly.text', 'w')
    text1.write(soup.get_text())
    text1 = soup.get_text()

    index = text1.find("privacy policy" or "プライバシーポリシー" or "個人情報") # 
    if index != -1:
        print("Found!" + str(index))
    else: print("Not found")
```
`index = text1.find("個人情報")`のみにすると出力結果が`Found at 3787
`となるのですが、`or`を足すと`Not found`が出力されます。
「または」はどのように設定すれば良いでしょうかorz
よろしくお願いしますm(__)m

**text1の中身**
```text
新刊情報
カタログ
Makezine
オラの村


取扱書店
Bookclub
フィードバック
ご注文
企業概要
個人情報について
```

# できました<3
[hayataka2049](https://teratail.com/users/hayataka2049)様のおかげで判定できるようになりました! ありがとうございます(≧▽≦) 以下の点も気をつけます^^/

> re.search()はマッチしなかったときNoneを返すので、結果を受け取る部分のコードに多少気を使ってあげてください

```python
def get_html():

    r = requests.get("https://www.oreilly.co.jp/index.shtml")
    r.encoding = r.apparent_encoding
    html_doc = r.text
    soup = BeautifulSoup(html_doc)

    html1 = open('Oreilly.html', 'w')
    html1.write(soup.prettify())
    html1 = soup.prettify()

    text1 = open('Oreilly.text', 'w')
    text1.write(soup.get_text())

    priv_htm = re.search(r"privacy policy|プライバシーポリシー|個人情報", html1).start()
    if priv_htm != -1:
        print(priv_htm)
        print("hrefを取得します")

    else: print("ありませんでした")
get_html()
```

# [Python3] 検索した文字列からhtmlタグを取得
`re.search(r"privacy policy|プライバシーポリシー|個人情報", html1)`で一致した文字列のhrefタグはどうやれば取得できるでしょうか。これまで`soup.find_all('a', {'href': re.compile(r'^/projects/python/')})`などとしてhtmlタグからリンクを取得したことはあるのですが、今回は検索して見つかった文字列のタグを取得する方法を知りたいです。

```python
    priv_htm = re.search(r"privacy policy|プライバシーポリシー|個人情報", html1).start()
    if priv_htm != -1:
        print(priv_htm)
        print(re.search(r"privacy policy|プライバシーポリシー|個人情報", html1))
        print("hrefを取得します")


    else: print("ありませんでした")
```

**html1の中身**
以下のhref のリンクを取得したいです。
```html
<li>
    <a href="/orj/privacypolicy.shtml">
        個人情報について
    </a>
</li>

<!-- 
<a href="/orj/privacypolicy.shtml">までの位置関係↓
html > body#index.home > div#page > section#content > div#right > div.footer.clearfix > div.footer-item.footer-right > ul.footer-category.service > li > a
-->


```

＃

# できました<3
[jun68ykt](https://teratail.com/users/jun68ykt)様のアドバイスのおかげで解決しました。`text =` で指定できるとは(≧▽≦) ありがとうございますヽ(｀▽´)/

```python
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
            

get_html()
```
