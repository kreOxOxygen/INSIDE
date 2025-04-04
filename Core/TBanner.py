from colorama import Fore



_banner = '''
 88888  dP"Yb   dP""b8 88  dP 888888 88""Yb 
    88 dP   Yb dP   `" 88odP  88__   88__dP 
o.  88 Yb   dP Yb      88"Yb  88""   88"Yb
"bodP'  YbodP   YboodP 88  Yb 888888 88  Yb 
'''



def banner(host, port):
    '''Вывод баннера с ссылкой'''

    print(Fore.MAGENTA + _banner)
    print(f'Перейдите по http://{host}:{port}')
