import pprint
import requests

# 상품과 옵션 정보들을 담고 있는 새로운 객체를 만들어 반환하시오.
# [힌트] 상품 리스트와 옵션 리스트를 금융상품 코드를 기준으로 매칭할 수 있습니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 변수에 저장합니다.
# 3. 2번의 결과 중 key 값이 "baseList" 인 데이터를 변수에 저장합니다.
# 4. 2번의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 5. 3번에서 저장된 변수를 순회하며, 4번에서 저장된 값들에서 금융 상품 코드가 
#     같은 모든 데이터들을 가져와 새로운 딕셔너리로 저장합니다.
#     저장 시, 명세서에 맞게 출력되도록 저장합니다.
# 6. 5번에서 만든 딕셔너리를 결과 리스트에 추가합니다.


def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = "4e541a7cfc6caf65843483ee86c2d6a2"

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    url="http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json"
    params = {
    'auth' : api_key,
    'topFinGrpNo' : '020000',
    'pageNo' : 1}

    response = requests.get(url,params=params).json()
    
    base_ls = response["result"]["baseList"]

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
    
    
    code_ls = list()
    for dic in product_ls:
        if dic['금융상품코드'] not in code_ls:
            code_ls.append(dic['금융상품코드'])

    result_ls = list()
    for code in code_ls:
        new_dic = {'금리정보' : [],
                   '금융상품명': None,
                   '금융회사명' : None}
        for base in base_ls:
            if base['fin_prdt_cd'] == code:
                new_dic['금융상품명'] = base['fin_prdt_nm']
                new_dic['금융회사명'] = base['kor_co_nm']
                break
        
        for product in product_ls:
            if product['금융상품코드'] == code:
                inner_dict = {}
                inner_dict['저축 금리'] = product['저축 금리']
                inner_dict['저축 기간'] = product['저축 기간']
                inner_dict['저축 금리 유형'] = product['저축 금리 유형']
                inner_dict['저축 금리 유형명'] = product['저축 금리 유형명']
                inner_dict['최고 우대금리'] = product['최고 우대금리']

                new_dic['금리정보'].append(inner_dict)

        result_ls.append(new_dic)
    result = result_ls
    
    return result

if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)