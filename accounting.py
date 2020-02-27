import os
from pynubank import Nubank

user = os.getenv('NU_USER')
passwd = os.getenv('NU_PASSWD')

nu = Nubank()
nu.authenticate(user, passwd)

bills = nu.get_bills()
print(len(bills))
