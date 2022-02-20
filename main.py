import tkinter as tk
import consulta as c

root = tk.Tk()

root.geometry('400x200')
root.title("Monitor Maestro")
root.iconbitmap('equiplano-logo-vertical.ico')

sec = None
consulta = c.Consulta()
def tick():
    global sec
    global respostas

    if sec == None or sec == 0:

        sec = int(inicio.get())*60

    if sec == 1:
        time['text'] = 'Consultando...'
        root.update()
        sec = 0
        if sec == 0:
            inf_1, inf_2 = consulta.login()
            resposta['text'] = 'Última verificação do maestro com sucesso: ' + inf_1
            erro['text'] = inf_2
            time['text'] = int(inicio.get())
            root.update()
            tick()
    else:
        sec = sec - 1
        relogio = int(sec/60)
        if relogio > 1:
            time['text'] = 'A próxima consulta será realizada em menos de ' + str(relogio+1) + ' minutos.'
        elif relogio == 1:
            time['text'] = 'A próxima consulta será realizada em menos de ' + str(relogio+1) + ' minuto.'
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

#pyinstaller --onefile -n csv_to_postgre --noconsole main.py
