import requests

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

def author_works():
    book_ls = []
    items = response['item']
    for item in items:
        book_ls.append(item['title'])
    
    return book_ls



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    print(author_works())
