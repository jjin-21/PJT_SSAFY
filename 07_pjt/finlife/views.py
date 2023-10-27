from django.shortcuts import render, redirect
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from .models import DepositOptions, DepositProducts
from .serializers import DepositOptionsSerializer, DepositProductsSerializer

# Create your views here.
@api_view(['GET'])
def save_deposit_products(request):
    BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
    'auth': settings.API_KEY,
    'topFinGrpNo': '020000',
    'pageNo': 1
    }
    result = []
    response = requests.get(URL, params=params).json()
    res_data = response['result']
    baseList = res_data['baseList']
    optionList = res_data['optionList']

    # baseList
    for base in baseList:
        serializer = DepositProductsSerializer(data=base)
        if serializer.is_valid():
            serializer.save()
            result.append(serializer)
    # optionList
    for option in optionList:
        product = DepositProducts.objects.get(fin_prdt_cd=option['fin_prdt_cd'])
        serializer = DepositOptionsSerializer(data=option)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)
            result.append(serializer)
    
    return Response({'message': "Good!"}, status=201)


@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data)
    


@api_view(['GET'])
def top_rate(request):
    max_option = DepositOptions.objects.order_by('-intr_rate2').first()
    ser_option = DepositOptionsSerializer(max_option)
    
    max_product = max_option.product
    ser_product = DepositProductsSerializer(max_product)
    data = {
        'max_product': ser_product.data,
        'max_option': ser_option.data,
    }
    return Response(data)