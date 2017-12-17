#coding=utf-8
import socket

import requests
from bs4 import BeautifulSoup


headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}


def get_code(money):
    host = 'http://demo.sucaihuo.com'
    url = 'http://demo.sucaihuo.com/1200/Pay/submit.html'
    payload = {'money': str(money), 'paytype': 'wechat_code'}
    r = requests.post(url, headers=headers, data=payload)
    # print r.text
    soup = BeautifulSoup(r.text, 'html.parser')
    item = soup.find_all('img')[1]['src']
    code = host+item
    order_no = soup.input['value']
    return [code,order_no]

def save_img(img_url,code_id="0"):
    r=requests.get(img_url)
    # print r.content
    f=file("./tmp/"+code_id+".png","wb")
    try:
        f.write(r.content)
    finally:
        f.close()
    # print "img save"
def check_status(order_no):
    url = 'http://demo.sucaihuo.com/1200/Pay/check_status'
    payload2 = {'order_no': order_no}
    r = requests.post(url,headers=headers,data=payload2)
    print "checking..."
    print r.text
    if(r.text):
        return 'Y'
    else:
        return 'N'
    # if(r.text):
    #     print "付款成功"
    # else:
    #     print "未付款"


# print "save img"
# save_img("http://demo.sucaihuo.com/1200/Application/Common/Org/Wxpay/example/qrcode.php?data=weixin%3A%2F%2Fwxpay%2Fbizpayurl%3Fpr%3D5EJWQHt","02165156156165165165")
# print "over"

HOST = ''
PORT = 8000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(100)
print "Server running ..."
content="RETURN"
while True:
    conn, addr = sock.accept()
    request = conn.recv(1024)
    print 'Connect by: ', addr
    print 'Request is:\n', request
    method = request.split('#')[1]
    val = request.split('#')[2]
    print "METHOD:"+method
    print "VAL:"+val
    if method == 'REQ_ORDER_ID':
        print "RETURN CODE ORDER_ID"
        rt = get_code(val)
        content=rt[1]
        src=rt[0]
        save_img(src,content)
    elif method == 'REQ_CODE':
        print "RETURN CODE.PNG"
        f=file("./tmp/"+val+".png","rb")
        content=f.read()
        f.close()

    elif method == 'CHECK_STA':
        print "CHECK_STA"
        content=check_status(val)
        print "CHECK_STA==>"+content
    else:
        continue
    conn.sendall(content)
    # close connection
    conn.close()


#         img=request
#
#         print"save the img..."
#     conn.close()
# #
