from colorama import Fore



_banner = '''
88  88 888888 88     88      dP"Yb      8888b.     db    8888b.  8888b.  Yb  dP 
88  88 88__   88     88     dP   Yb      8I  Yb   dPYb    8I  Yb  8I  Yb  YbdP
888888 88""   88  .o 88  .o Yb   dP      8I  dY  dP__Yb   8I  dY  8I  dY   8P 
88  88 888888 88ood8 88ood8  YbodP      8888Y"  dP""""Yb 8888Y"  8888Y"   dP 
'''



def banner(host, port):
    '''Вывод баннера с ссылкой'''

    print(Fore.MAGENTA + _banner)
    print(f'Перейдите по http://{host}:{port}')
