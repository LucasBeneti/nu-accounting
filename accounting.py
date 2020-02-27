
# from pynubank import Nubank

# user = os.getenv('NU_USER')
# passwd = os.getenv('NU_PASSWD')

# nu = Nubank()
# nu.authenticate(user, passwd)

# bills = nu.get_bills()
# print(len(bills))
import os
from pynubank import Nubank

user = os.getenv('NU_USER')
passwd = os.getenv('NU_PASSWD')
nu = Nubank()
uuid, qr_code = nu.get_qr_code()
# Nesse momeento será printado o QRCode no console
# Você precisa escanear pelo o seu app do celular
# Esse menu fica em NU > Perfil > Acesso pelo site
qr_code.print_ascii(invert=True)
input('Após escanear o QRCode pressione enter para continuar')
# Somente após escanear o QRCode você pode chamar a linha abaixo
nu.authenticate_with_qr_code(user, passwd, uuid)
print(nu.get_bills())