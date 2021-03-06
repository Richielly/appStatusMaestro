import tkinter as tk
import consulta as c
import push
import slack_mensage
import time
from datetime import datetime

root = tk.Tk()

root.geometry('600x200')
root.title("Monitor Maestro")
root.iconbitmap('equiplano-logo-vertical.ico')

sec = None
consulta = c.Consulta()
def tick():
    global sec
    global respostas

    hora = datetime.now().strftime('%H:%M:%S')

    if sec == None or sec == 0:

        sec = int(inicio.get())*60


    if hora in ['07:00:00', '12:00:00', '17:00:00']:
        print(hora)
        slack_mensage.mensage_slack('Olá ... fiquem tranquilos ... estou monitorando o Maestro de Toledo ... :white_check_mark:')

    if sec == 1:
        time['text'] = 'Consultando...'
        root.update()
        sec = 0
        if sec == 0:
            msg = consulta.login()
            print(msg)

            if msg == 'Maestro pode estar parado.':
                erro['text'] = msg
                push.push()
                root.update()
            else:
                resposta['text'] = msg
                root.update()

            time['text'] = int(inicio.get())
            root.update()
            tick()
    else:
        sec = sec - 1
        relogio = int(sec/60)
        if sec%2:
            t = '. . .'
        else: t = ' . . '
        if relogio > 1:
            time['text'] = 'A próxima consulta será realizada em menos de '+ str(relogio+1) + ' minutos ' + t
        elif relogio == 1:
            time['text'] = 'A próxima consulta será realizada em menos de ' + str(relogio+1) + ' minuto ' + t
        else:
            time['text'] = 'Restam ' + str(sec) + ' segundos para próxima consulta.'
        time.after(1000, tick)

    return sec

label = tk.Label(root, text="Tempo de verificação no Maestro")
label.pack()
inicio = tk.Entry(root, textvariable=0)
inicio.pack()
time = tk.Label(root, fg='green')
time.pack()
resposta = tk.Label(root, fg='blue')
resposta.pack()
erro = tk.Label(root, fg='red')
erro.pack()
tk.Button(root, fg='blue', text='Start', command=tick, state='normal').pack()

root.update()
root.mainloop()

tick()

#pyinstaller --onefile -n MaestroMonitoring --noconsole --icon=equiplano-logo-vertical.ico main.py
