from tkinter import *
import inferenceSystem

ACOES = {
    'aquecMaximo': 'Aquecimento Máximo',
    'aquecNormal': 'Aquecimento Normal',
    'desligado': 'Desligado',
    'arNormal': 'Ar Normal',
    'arMaximo': 'Ar Máximo'
}

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.recomendacao = StringVar()
        self.create_widgets()
        self.acao = {}
        self.updateRecomendation()

    def updateRecomendation(self):
        self.acao = inferenceSystem.getAcao(self.getValues())
        recomenda = ""
        for i in self.acao.keys():
            recomenda += ACOES[i.name] + ": " + f'{(self.acao.get(i) * 100):.3g}' + "%\n"
        self.recomlabel.config(text=recomenda)
        print("update")

    def getValues(self):
        return (self.tempExt.get(),
                self.umidExt.get(),
                self.tempInt.get(),
                self.umidInt.get(),
                self.gostoPess.get(),
                self.densRoupa.get())
    
    def create_widgets(self):
        variaveis = Frame(self.master)
        variaveis.pack(side=LEFT)
        condi = Frame(variaveis)
        condi.pack(side=TOP, anchor=W)
        externo = LabelFrame(condi, text="Condições Externas")
        externo.pack(side=LEFT, anchor=N, padx=5, pady=5)
        self.tempExt = Scale(externo, from_=-20, to=50, orient=HORIZONTAL)
        self.tempExt.pack()
        labelTempExt = Label(externo, text='Temperatura')
        labelTempExt.pack()
        self.umidExt = Scale(externo, from_=0, to=100, orient=HORIZONTAL)
        self.umidExt.pack()
        labelUmidExt = Label(externo, text='Umidade')
        labelUmidExt.pack()

        interno = LabelFrame(condi, text="Condições Internas")
        interno.pack(side=LEFT, anchor=N, padx=5, pady=5)
        self.tempInt = Scale(interno, from_=-20, to=50, orient=HORIZONTAL)
        self.tempInt.pack(fill=X)
        labelTempInt = Label(interno, text='Temperatura')
        labelTempInt.pack(fill=X)
        self.umidInt = Scale(interno, from_=0, to=100, orient=HORIZONTAL)
        self.umidInt.pack(fill=X)
        labelUmidInt = Label(interno, text='Umidade')
        labelUmidInt.pack(fill=X)

        config = LabelFrame(variaveis, text="Configurações Adicionais")
        config.pack(side=BOTTOM, anchor=SW, padx=5, pady=5, fill=X)
        self.gostoPess = Scale(config, from_=0, to=10, orient=HORIZONTAL)
        self.gostoPess.pack(fill=X)
        labelGostoPess = Label(config, text='Gosto Pessoal')
        labelGostoPess.pack(fill=X)
        self.densRoupa = Scale(config, from_=0, to=10, orient=HORIZONTAL)
        self.densRoupa.pack(fill=X)
        labelDensRoup = Label(config, text='Densidade das Roupas')
        labelDensRoup.pack(fill=X)

        botaoAvaliar = Button(self.master, text="Avaliar", width= 9, command=self.updateRecomendation)
        botaoAvaliar.pack(side=LEFT, padx=10 )

        recomendacao = LabelFrame(self.master, text="Ação sugerida", padx=10, pady=10)
        recomendacao.pack(side=RIGHT, padx=5)
        self.recomlabel = Label(recomendacao, text="", anchor='w')
        self.recomlabel.pack()

root = Tk()
root.title("Climatização Residencial Automática")
app = Application(master=root)
app.mainloop()
