from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import csv
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

    csv_input = pd.read_csv('CompanyURL.csv', sep=",")
    n = 1
    with open('CompanyURL0.csv', 'w+') as file:
        writer = csv.writer(file, lineterminator='\n')
        for index, row in csv_input.iterrows():
            url = csv_input['URL'][index]

            r = requests.get(url)
            r.encoding = r.apparent_encoding
            html_doc = r.text
            soup = BeautifulSoup(html_doc)

            """
            以下からは需要に応じてオプション
            プライバシーポリシー系を探す
            Privacy policy、プライバシーポリシー、個人情報
            """

            pattern = r"privacy|privacy policy|個人情報|プライバシーポリシー"

            for link in soup.findAll('a', text=re.compile(pattern, re.IGNORECASE)):
                link_h = link['href']
                print(str(n) + ' ' + link_h)

                writer.writerow([n, link_h])
            n += 1

def test1():
    """
    csvに保存しているURLを出力
    参考URL: https://tinyurl.com/ybngd5j4
    """
    csv_input = pd.read_csv('CompanyURL.csv', sep=",")
    for index, row in csv_input.iterrows():
        url = csv_input['URL'][index]
        print(url)

get_html()