from win10toast import ToastNotifier

def push():
    ToastNotifier().show_toast('Maestro Monitor', '\nO Maestro de Toledo pode não estar sincronizando com o sistema de nota.',
                                  duration=20, icon_path='equiplano-logo-vertical.ico',threaded=True)
