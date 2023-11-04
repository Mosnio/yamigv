import requests
import json,os
import time
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import time,random
import requests
from bs4 import BeautifulSoup




def Session():
    session = requests.Session()
    retry = Retry(connect=5, backoff_factor=1)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


class Api_MB:
    def __init__(self):
        self.url = "http://api.multibot.in"
        self.key = "5Z4sWvudz6Jjfw2nK10YcOFkRbQVMU"
        self.max_wait = 300
        self.sleep = 5

    def in_api(self, data):
        session = Session()
        params = {"key": (None, self.key), "json": (None, "1")}
        for key in data:
            params[key] = (None, data[key])
        return session.post(self.url + '/in.php', files=params, verify=False, timeout=5)

    def res_api(self, api_id):
        session = Session()
        params = {"key": self.key, "id": api_id, "json": "1"}
        return session.get(self.url + '/res.php', params=params, verify=False, timeout=5)

    def run(self, data):
        get_in = self.in_api(data)
        if get_in:
            if json.loads(get_in.text)['status']:
                api_id = json.loads(get_in.text)['request']
            else:
                return json.loads(get_in.text)['request']
        else:
            return "WRONG_RESPONSE_API"
        for i in range(self.max_wait//self.sleep):
            time.sleep(self.sleep)
            get_res = self.res_api(api_id)
            if get_res:
                answer = json.loads(get_res.text)['request']
                if 'CAPCHA_NOT_READY' in answer:
                    continue
                else:
                    return answer







def db():
    if os.path.exists("user-agent.txt"):
        with open("user-agent.txt", "r") as user_agent_file:
            u = user_agent_file.read()
    else:
        u = input("user-agent : ")  
        with open("user-agent.txt", "w") as user_agent_file:
            user_agent_file.write(u)
    
    if os.path.exists("coki.txt"):
        with open("coki.txt", "r") as coki_file:
            cokie = coki_file.read()
    else:
        cokie = input("Cookie : ")    
        with open("coki.txt", "w") as coki_file:
            coki_file.write(cokie)



headers = {
    'Host': 'faucet.mom',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Cookie': 'Referral_Source=https%3A%2F%2Fwww.google.com%2F; _ga=GA1.1.459789300.1699103855; bitmedia_fid=eyJmaWQiOiIwYWExMWFmZWYyMGE5ZTVhM2ZhZTJkYWY5MTc1MGNkMSIsImZpZG5vdWEiOiJmMzU1MTVhMzA3MjgyZDY2NGM1YzQ2MmQ1Yzc1MjNkZCJ9; _ccnsad_pop=500; ci_session=o6q7e3ur32q495pus9akbsqg57ua57n8; csrf_cookie_name=fb2ac5672c45844e6bbadf75a6fdfc65; _ga_3YMV9JNW1Q=GS1.1.1699103855.1.1.1699104083.0.0.0; adbit-viewed-ads=20808,20460',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; moto g32 Build/S2SNS32.34-72-31-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36',
    'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
}

url='https://faucet.mom/'

def msg_line():   
    line_length = 50
    print(f"{'━' * line_length}")
    
def faucet():
    while True:
        api = Api_MB()

        res = get(url + 'faucet', headers=headers)        
        
        soup = BeautifulSoup(res, 'html.parser')
        
        token= soup.find('input', {'id': 'token'})['value']
        
        


        data = {"method": "hcaptcha", "pageurl": "https://faucet.mom/faucet", "sitekey": "1483288d-b1a7-42f2-b622-5071c3622000"}
        
        hCaptcha = api.run(data)
        
        payload = {
                    'csrf_token_name':f'{token}',
                    'captcha':'hcaptcha',
                    'recaptchav3':' ',
                    'g-recaptcha-response': f'{hCaptcha}',
                    'h-captcha-response': f'{hCaptcha}'
                }
        load(2)
        res = requests.post(url + "faucet/verify",headers=headers, data=payload )
        
        d=(res.status_code)
        if d==200:
        	print('success...')
        	print('faucet claimed successfully ! ! !')
        else:
        	print('failed')
        time.sleep(random.randint(60,75))
        
        msg_line()
        
        

def notimer():
    while True:
        api = Api_MB()
        res = get(url + 'madfaucet', headers=headers)  
        soup = BeautifulSoup(res, 'html.parser')        
        token= soup.find('input', {'id': 'token'})['value']
        data = {"method": "hcaptcha", "pageurl": "https://faucet.mom/madfaucet", "sitekey": "1483288d-b1a7-42f2-b622-5071c3622000"}        
        hCaptcha = api.run(data)     
        payload = {
                    'csrf_token_name':f'{token}',
                    'captcha':'hcaptcha',
                    'recaptchav3':' ',
                    'g-recaptcha-response': f'{hCaptcha}',
                    'h-captcha-response': f'{hCaptcha}'
                }
        load(2)
        res = requests.post(url + "madfaucet/verify",headers=headers, data=payload )
        
        d=(res.status_code)      
        if d==200:
        	print('success...')
        	print('mad claimed successfully ! ! !')
        else:
        	print('failed')
        time.sleep(random.randint(60,75))
        
        msg_line()
        
 
 
 
def wheel():
    while True:
        api = Api_MB()
        res = get('https://faucet.mom/wheel', headers=headers)              
        soup = BeautifulSoup(res, 'html.parser')      
        token= soup.find('input', {'id': 'token'})['value']
        data = {"method": "hcaptcha", "pageurl": "https://faucet.mom/wheel/", "sitekey": "1483288d-b1a7-42f2-b622-5071c3622000"}        
        hCaptcha = api.run(data)        
        payload = {
                    'h-captcha-response': f'{hCaptcha}',
                    'token':f'{token}',
                    'captcha':'hcaptcha',
                }        
        load(2)
        res = requests.post("https://faucet.mom/wheel/verify",headers=headers, data=payload )      
        d=(res.status_code)
        if d==200:
        	print('success...')
        	print('wheeled successfully ! ! !')
        else:
        	print('failed')
        time.sleep(random.randint(60,75))        
        msg_line()
        

def get(url, headers):
    response = requests.get(url, headers=headers)
    return response.text

def post(url, data, headers):
    response = requests.post(url, data=data, headers=headers)
    return response.text

def load(seconds):
    time.sleep(seconds)




         
           
 
def bal():
    pass

class Api_GXP:
    def get_balance(self):
        pass

    def run(self, data):
        pass

def date():
    return time.strftime("%H:%M:%S")



#db()
def run_wheel():
    try:
        wheel()  
    except Exception as e:
        print(f"Error in 'wheel': {e}")
        run_notimer()  

def run_notimer():
    try:
        notimer()  
    except Exception as e:
        print(f"Error in 'notimer': {e}")
        run_faucet()  

def run_faucet():
    try:
        faucet()  
    except Exception as e:
        print(f"Error in 'faucet': {e}")
        
run_wheel()
      
