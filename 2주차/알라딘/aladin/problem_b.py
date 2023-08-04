import requests
from pprint import pprint

url = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

params = {
    'ttbkey': 'ttbljj19001508001',
    'Query' : '파울로 코엘료',
    'QueryType': 'Author',
    'MaxResults' : 20,
    'start' : 1,
    'SearchTarget' : 'Book',
    'output' : 'js',
    'Version' : '20131101'
}

response = requests.get(url,params=params).json()

def best_review_books():
    items = response['item']

    result = []
    for item in items:
        if item['customerReviewRank'] >= 9:
            result.append(item)

    return result




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(best_review_books())