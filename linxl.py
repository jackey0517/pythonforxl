__author__ = 'liux'

import urllib.request
import urllib.parse
import json
import dataprase
from json import *

def Post_Web(url,data=None):
    headers={
        'content-type': 'application/json',
        'Cookie':'guid=b440cdac-d48e-5234-d158-d157217012d8; Hm_lvt_b011482b865a36822b1d999b9d98d028=1473734776; Hm_lpvt_b011482b865a36822b1d999b9d98d028=1473734776; mirrorId=0000; originRefer=; fs_token=CZTZPJPXP3SjCpHXD2qqDs9aBJanD3CjOcPXPZapOcPaOZCm; FSAuthX=0G60tF8vLm4000167dDVb9Lk8zp38rplWJ4r4vkRCv1gBQEyO5Q5yj9c0MGHAsIQS5AGSJHAhdtyzGW7LmyAu3GmLkjsOakyxPGzyvkcmnBcUizxLuIPSjUTYmBUdqK120zXfu7DcB1DlB1AX3aY4vxikr3mGO3LhDuvtEn9ozCFcLZYWagwgps0EThkKmQ85KnR3dtcTE50m8JCUcXHLE9fsycg5H8JnUtcq80; FSAuthXC=0G60tF8vLm4000167dDVb9Lk8zp38rplWJ4r4vkRCv1gBQEyO5Q5yj9c0MGHAsIQS5AGSJHAhdtyzGW7LmyAu3GmLkjsOakyxPGzyvkcmnBcUizxLuIPSjUTYmBUdqK120zXfu7DcB1DlB1AX3aY4vxikr3mGO3LhDuvtEn9ozCFcLZYWagwgps0EThkKmQ85KnR3dtcTE50m8JCUcXHLE9fsycg5H8JnUtcq80; sso_token=df6a8563-37ef-40d2-96b0-56dd43a54337; RouteUp=; enterprise=7; current_index_url=/XV/Home/index'
    }
    url='http://www.fsceshi.com/FHH/EM1HCRM/Contact/GetContactDetailByID'
    values= {"ContactID":"842dede8e929410383f0b2a26c0a35f2", "WithoutRightCheck":"false", "active":"true" }

    jdata = json.dumps(values)
    temp=jdata.encode('utf8')
    req=urllib.request.Request(url=url,data=jdata,headers=headers)
    response=urllib.request.urlopen(req)
    res=response.read()

    res_str=res.decode('utf-8')
    res_json=json.loads(res_str)


    print(res_json)

def Post_Mobile(url,data=None):
    headers={
        'content-type': 'application/xml',
        'Cookie':'FSAuthX=0G60sB6wLm40003qXiazpjkKwTl2QOfnYCjihoOfzH0rC5bj1eSXrYjx00dDysozbIxtYxKsSdjnG2NO33Dtyf7KqsRyKAqlhw7jaUBfkDdc1jSVSBTJm7gyclNAUY2Kf1YlPsM4k8C6LjZMi5Z1uqxcaJAyK1F07TBv0F07ZnhPnirInBW65dOBRZjFeonxtUI5pdM9J8zO6OZt7Q6tQYBCBs5pd08BaAzlqYzwuAUkt9MyS65zwzr16M5A; RouteUp=; fs_token=DZSoOs8nCp8jP6DcDIqqOc8sBM5aCJSjPZSrOZOtDc9XCJOs; FSAuthXC=0G60sB6wLm40003qXiazpjkKwTl2QOfnYCjihoOfzH0rC5bj1eSXrYjx00dDysozbIxtYxKsSdjnG2NO33Dtyf7KqsRyKAqlhw7jaUBfkDdc1jSVSBTJm7gyclNAUY2Kf1YlPsM4k8C6LjZMi5Z1uqxcaJAyK1F07TBv0F07ZnhPnirInBW65dOBRZjFeonxtUI5pdM9J8zO6OZt7Q6tQYBCBs5pd08BaAzlqYzwuAUkt9MyS65zwzr16M5A; sso_token=b7edf6cc-9286-4a6c-991f-aa4c047e43d3'
    }
    url='http://www.fsceshi.com/FHE/EM1ACRM/Product/GetProductByID/iOS.100540021?_vn=100540021&_ov=8.4&_postid=-895965397&traceId=E-E.7.3621-EA210E86-766D-4A7F-B648-8AA7E90C2A6E'
    data='<?xml version="1.0"?><FHE><Tickets/><PostId>1562470364</PostId><Data DataType="Json/P">{  "M1" : "5dd6040ed69e49e7944013b3d2de34b4"}</Data></FHE>'

    jdata=data.encode('utf8')

    req=urllib.request.Request(url=url,data=jdata,headers=headers)
    response=urllib.request.urlopen(req)
    res=response.read()

    res_str=res.decode('utf-8')


    print(res_str)

if __name__=='__main__':
    Post_Mobile('1')