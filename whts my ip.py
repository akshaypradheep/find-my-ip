from requests import get
sys.tracebacklimit=0
ip = get('https://api.ipify.org').text
print('My public IP address is: {}'.format(ip))
