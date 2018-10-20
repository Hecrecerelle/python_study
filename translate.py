from urllib import request
from urllib import parse
import json

word=str(input())

formData={}
formData['action']='FY_BY_REALTIME'
formData['client']='fanyideskweb'
formData['doctype']='json'
formData['from']='AUTO'
formData['i']=word
formData['keyfrom']='fanyi.web'
formData['salt']='1539917469870'
formData['sign']='3dfdb3592060689ca11662c9d0f94b1a'
formData['smartresult']='dict'
formData['to']='AUTO'
formData['typoResult']='false'
formData['version']='2.1'

data=parse.urlencode(formData).encode('utf-8')

req=request.Request("http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule")

response=request.urlopen(req,data)
html=response.read().decode('utf-8')

translate_results=json.loads(html)
translate_results=translate_results['translateResult'][0][0]['tgt']
print(translate_results)