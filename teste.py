import tkinter as tk
import consulta as c
from multiprocessing import Pool
root = tk.Tk()

respostas = "1"
sec = None
consulta = c.Consulta()
def tick():
    global sec
    global respostas
    if sec == None or sec == 0:
        sec = int(inicio.get())

    if sec == 1:
        time['text'] = 'Consultando...'
        root.update()
        sec = 0
        if sec == 0:
            resposta['text'] = consulta.login()
            time['text'] = int(inicio.get())
            root.update()
            tick()
    else:
        sec = sec - 1
        time['text'] = sec
        time.after(1000, tick)

    return sec

label = tk.Label(root, text="Tempo de verificação no Maestro")
label.grid(row=0, column=0)
inicio = tk.Entry(root, textvariable=0)
inicio.grid(row=1, column=0)
time = tk.Label(root, fg='green')
time.grid(row=2, column=0)
resposta = tk.Label(root, fg='blue')
resposta.grid(row=4, column=0)
tk.Button(root, fg='blue', text='Start', command=tick).grid(row=3, column=0)

root.mainloop()


tick()