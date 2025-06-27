import requests
import hashlib
import sys

def reader(filename):
    with open(filename ,'r') as myfile:
        return [line.strip() for line in myfile if line.strip()]

def pass_api(query_char):
    url=  'https://api.pwnedpasswords.com/range/'+ query_char
    res = requests.get(url)
    if res.status_code!=200:
        raise RuntimeError(f'error fetching {res.status_code}')
    return res

def getpasscount(hashes,response):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    # print(hashes)
    for h,count in hashes:
        # print(h,count)
        if h==response:
            return count
    return 0

def check_pass(password):
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    f5_char,tail = sha1pass[:5],sha1pass[5:]
    response = pass_api(f5_char)
    # print(f5_char,tail)
    return getpasscount(response,tail)

def main():
    passwords = reader('password.txt')
    for password in passwords:
        
        count = check_pass(password)
        if count:
            print(f'Your password \'{password}\' has been hacked {count} times.. You should change it!')
        else:
            print(f'{password} was not found! All Good')
    return 'done!'
if __name__ == '__main__':
    sys.exit(main())