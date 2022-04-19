from win10toast import ToastNotifier

import configparser

config = configparser.ConfigParser()
config.read("config.ini");

def push():
    push = config['default']["push"]
    if push == 'ativo':
        ToastNotifier().show_toast('Maestro Monitor', '\nO Maestro de Toledo pode não estar sincronizando com o sistema de nota.',
                                  duration=60, icon_path='equiplano-logo-vertical.ico',threaded=True)
