import requests
import json
import pprint

api_key="4e541a7cfc6caf65843483ee86c2d6a2"
url="http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json"
params = {
    'auth' : api_key,
    'topFinGrpNo' : '020000',
    'pageNo' : 1}

response = requests.get(url,params=params).json()

product_ls = list()
for dic in response["result"]["optionList"]:
    product_dic = {}
    product_dic['금융상품코드'] = dic['fin_prdt_cd']
    product_dic['저축 금리'] = dic['intr_rate']
    product_dic['저축 기간'] = dic['save_trm']
    product_dic['저축 금리 유형'] = dic['intr_rate_type']
    product_dic['저축 금리 유형명'] = dic['intr_rate_type_nm']
    product_dic['최고 우대금리'] = dic['intr_rate2']
    product_ls.append(product_dic)

new_ls = list()
for dic in product_ls:
    if dic['금융상품코드'] not in new_ls:
        new_ls.append(dic['금융상품코드'])


new_dict = {'금리정보' : []}
for code in new_ls:
    
    new_dict['금리정보'].append()


# pprint.pprint(f'Key값 : {response["result"].keys()}')
# pprint.pprint(f'전체 정기예금 상품 리스트 : {response["result"]["baseList"]}')
# pprint.pprint(f'전체 정기예금 옵션 리스트 : {product_ls}')
# pprint.pprint(product_ls[:4])

print(new_ls)