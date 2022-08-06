import uuid

import requests
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import exceptions
import json


def createUrl():
    url = "https://b2b.taxi.yandex.net/b2b/cargo/integration/v1/check-price"
    return url

def createURLMultiDots():
    requestID = uuid.uuid1()
    url = f"https://b2b.taxi.yandex.net/b2b/cargo/integration/v2/claims/create?request_id={requestID}"
    return url


def createHeader():
    headers = {
        'Accept-Language': 'ru',
        'Authorization': 'Bearer AQAAAABg0bhFAAVM1ZFEFSJs900Rhu9DJtyekEU',
        'Content-Type': 'application/json',
        'Cookie': '_yasc=/FlU/J7VQp9IRY8DIucXjdh/ZE2SmqGOXE9Bwc5YuXB7fQ=='
    }
    return headers

def createBody():
    body = json.dumps({
        "items": [{"quantity": 1, "weight": 2.105}],
        "route_points": [{"coordinates": [55.7522200, 55.7522200]}]
    })
    return body

class DeliveryPrice(generics.ListAPIView):

    def get(self, request):

        response = requests.post(url=createURLMultiDots(), headers=createHeader(), data=createBody())


        print(response.status_code, 'status_code')
        return Response(response.json())