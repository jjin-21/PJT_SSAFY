import requests
from pprint import pprint

url = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'





def author_other_works(title):
    params = {
    'ttbkey': 'ttbljj19001508001',
    'Query' : title,
    'QueryType': 'Title',
    'MaxResults' : 20,
    'start' : 1,
    'SearchTarget' : 'Book',
    'output' : 'js',
    'Version' : '20131101'
    }

    response = requests.get(url,params=params).json()
    if response['totalResults'] == 0:
        return None
    else:
        author = response['item'][0]['author'].split(',')[0][:-6]
        new_params = {
        'ttbkey': 'ttbljj19001508001',
        'Query' : author,
        'QueryType': 'Author',
        'MaxResults' : 20,
        'start' : 1,
        'SearchTarget' : 'Book',
        'output' : 'js',
        'Version' : '20131101'
        }

        new_response = requests.get(url,params=new_params).json()
        new_items = new_response['item']
        
        result = []
        for i in range(5):
            result.append(new_items[i]['title'])

        return result




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(author_other_works('베니스의 상인'))

    pprint(author_other_works('개미'))

    pprint(author_other_works('*'))
