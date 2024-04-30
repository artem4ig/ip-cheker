import requests
import os

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url='http://ip-api.com/json/{ip}').json()
        print(response)

    except requests.exceptions.ConnectionError:
        print('[!] please check Connection!')

def main():
    ip = input('say ip:  ')

    get_info_by_ip(ip=ip)

if __name__ == '__main__':

    main()
os.system('pause')


