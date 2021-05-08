from src.fuzzylogic.classes import Domain, Set, Rule
from src.fuzzylogic.hedges import very, plus, minus
from src.fuzzylogic.functions import (sigmoid, gauss, trapezoid, 
                             triangular, rectangular, R, S)
import matplotlib.pyplot as plt


'''
Definindo as variáveis de entrada do sistema
'''
TempExt = Domain("Temperatura Externa", -20.01, 50.01, res=0.1)
TempExt.extremamenteFrio = trapezoid(-20.01, -20, -10, -5)
TempExt.extremamenteFrio = TempExt.extremamenteFrio.normalized()
#TempExt.extremamenteFrio.plot()
TempExt.muitoFrio = triangular(-7, 7)
#TempExt.muitoFrio.plot()
TempExt.frio = triangular(6, 18)
#TempExt.frio.plot()
TempExt.normal = triangular(16, 28)
#TempExt.normal.plot()
TempExt.quente = triangular(26, 34)
#TempExt.quente.plot()
TempExt.muitoQuente = triangular(32, 44)
#TempExt.muitoQuente.plot()
TempExt.extremamenteQuente = trapezoid(42, 45, 50, 50.1)
TempExt.extremamenteQuente = TempExt.extremamenteQuente.normalized()
#TempExt.extremamenteQuente.plot()

TempInt = Domain("Temperatura Interna", -20.01, 50.01, res=0.1)
TempInt.extremamenteFrio = trapezoid(-20.01, -20, -10, -5)
TempInt.extremamenteFrio = TempInt.extremamenteFrio.normalized()
#TempInt.extremamenteFrio.plot()
TempInt.muitoFrio = triangular(-7, 7)
#TempInt.muitoFrio.plot()
TempInt.frio = triangular(6, 18)
#TempInt.frio.plot()
TempInt.normal = triangular(16, 28)
#TempInt.normal.plot()
TempInt.quente = triangular(26, 34)
#TempInt.quente.plot()
TempInt.muitoQuente = triangular(32, 44)
#TempInt.muitoQuente.plot()
TempInt.extremamenteQuente = trapezoid(42, 45, 50, 50.1)
TempInt.extremamenteQuente = TempInt.extremamenteQuente.normalized()
#TempInt.extremamenteQuente.plot()

UmidExt = Domain("Umidade Externa", -0.01, 100.01, res=0.1)
UmidExt.muitoBaixa = triangular(-0.01, 40, c=0)
#UmidExt.muitoBaixa.plot()
UmidExt.baixa = triangular(30, 60)
#UmidExt.baixa.plot()
UmidExt.normal = triangular(50, 70)
#UmidExt.normal.plot()
UmidExt.alta = triangular(60, 80)
#UmidExt.alta.plot()
UmidExt.muitoAlta = triangular(75, 100.01, c=100)
#UmidExt.muitoAlta.plot()

UmidInt = Domain("Umidade Interna", -0.01, 100.01, res=0.1)
UmidInt.muitoBaixa = triangular(-0.01, 40, c=0)
#UmidInt.muitoBaixa.plot()
UmidInt.baixa = triangular(30, 60)
#UmidInt.baixa.plot()
UmidInt.normal = triangular(50, 70)
#UmidInt.normal.plot()
UmidInt.alta = triangular(60, 80)
#UmidInt.alta.plot()
UmidInt.muitoAlta = triangular(75, 100.01, c=100)
#UmidInt.muitoAlta.plot()

DensRoup = Domain("Densidade das Roupas", -0.01, 10.01, res=0.1)
DensRoup.baixa = triangular(-0.01, 4, c=0)
#DensRoup.baixa.plot()
DensRoup.normal = triangular(3, 7)
#DensRoup.normal.plot()
DensRoup.alta = triangular(6, 10.01, c=10)
#DensRoup.alta.plot()

GostoPess = Domain("Gosto Pessoal", -0.01, 10.01, res=0.1)
GostoPess.frio = triangular(-0.01, 4, c=0)
#GostoPess.baixa.plot()
GostoPess.normal = triangular(3, 7)
#GostoPess.normal.plot()
GostoPess.quente = triangular(6, 10.01, c=10)
#GostoPess.alta.plot()



'''
Definindo as variáveis de saída e as regras do sistema intermediário TEMPERATURA_APARENTE.
Neste ponto, reavalia-se a temperatura considerando a umidade do ar.
'''

TempExtPerc = Domain("Temperatura Externa Percebida", -20.01, 50.01)
TempExtPerc.extremamenteFrio = trapezoid(-20.01, -20, -10, -5)
TempExtPerc.extremamenteFrio = TempExtPerc.extremamenteFrio.normalized()
#TempExtPerc.extremamenteFrio.plot()
TempExtPerc.muitoFrio = triangular(-7, 7)
#TempExtPerc.muitoFrio.plot()
TempExtPerc.frio = triangular(6, 18)
#TempExtPerc.frio.plot()
TempExtPerc.normal = triangular(16, 28)
#TempExtPerc.normal.plot()
TempExtPerc.quente = triangular(26, 34)
#TempExtPerc.quente.plot()
TempExtPerc.muitoQuente = triangular(32, 44)
#TempExtPerc.muitoQuente.plot()
TempExtPerc.extremamenteQuente = trapezoid(42, 45, 50, 50.1)
TempExtPerc.extremamenteQuente = TempExtPerc.extremamenteQuente.normalized()
#TempExtPerc.extremamenteQuente.plot()

TempIntPerc = Domain("Temperatura Interna Percebida", -20.01, 50.01)
TempIntPerc.extremamenteFrio = trapezoid(-20.01, -20, -10, -5)
TempIntPerc.extremamenteFrio = TempIntPerc.extremamenteFrio.normalized()
#TempIntPerc.extremamenteFrio.plot()
TempIntPerc.muitoFrio = triangular(-7, 7)
#TempIntPerc.muitoFrio.plot()
TempIntPerc.frio = triangular(6, 18)
#TempIntPerc.frio.plot()
TempIntPerc.normal = triangular(16, 28)
#TempIntPerc.normal.plot()
TempIntPerc.quente = triangular(26, 34)
#TempIntPerc.quente.plot()
TempIntPerc.muitoQuente = triangular(32, 44)
#TempIntPerc.muitoQuente.plot()
TempIntPerc.extremamenteQuente = trapezoid(42, 45, 50, 50.1)
TempIntPerc.extremamenteQuente = TempIntPerc.extremamenteQuente.normalized()
#TempIntPerc.extremamenteQuente.plot()

regrasTempExtPerc = Rule({
                            (TempExt.extremamenteFrio, UmidExt.muitoBaixa): TempExtPerc.muitoFrio,
                            (TempExt.extremamenteFrio, UmidExt.baixa): minus(TempExtPerc.extremamenteFrio),
                            (TempExt.extremamenteFrio, UmidExt.normal): TempExtPerc.extremamenteFrio,
                            (TempExt.extremamenteFrio, UmidExt.alta): plus(TempExtPerc.extremamenteFrio),
                            (TempExt.extremamenteFrio, UmidExt.muitoAlta): very(TempExtPerc.extremamenteFrio),
                            (TempExt.muitoFrio, UmidExt.muitoBaixa): TempExtPerc.frio,
                            (TempExt.muitoFrio, UmidExt.baixa): minus(TempExtPerc.muitoFrio),
                            (TempExt.muitoFrio, UmidExt.normal): TempExtPerc.muitoFrio,
                            (TempExt.muitoFrio, UmidExt.alta): plus(TempExtPerc.muitoFrio),
                            (TempExt.muitoFrio, UmidExt.muitoAlta): TempExtPerc.extremamenteFrio,
                            (TempExt.frio, UmidExt.muitoBaixa): TempExtPerc.normal,
                            (TempExt.frio, UmidExt.baixa): minus(TempExtPerc.frio),
                            (TempExt.frio, UmidExt.normal): TempExtPerc.frio,
                            (TempExt.frio, UmidExt.alta): plus(TempExtPerc.frio),
                            (TempExt.frio, UmidExt.muitoAlta): TempExtPerc.muitoFrio,
                            (TempExt.normal, UmidExt.muitoBaixa): minus(TempExtPerc.normal),
                            (TempExt.normal, UmidExt.baixa): TempExtPerc.normal,
                            (TempExt.normal, UmidExt.normal): TempExtPerc.normal,
                            (TempExt.normal, UmidExt.alta): plus(TempExtPerc.normal),
                            (TempExt.normal, UmidExt.muitoAlta): very(TempExtPerc.normal),
                            (TempExt.quente, UmidExt.muitoBaixa): TempExtPerc.normal,
                            (TempExt.quente, UmidExt.baixa): minus(TempExtPerc.quente),
                            (TempExt.quente, UmidExt.normal): TempExtPerc.quente,
                            (TempExt.quente, UmidExt.alta): plus(TempExtPerc.quente),
                            (TempExt.quente, UmidExt.muitoAlta): TempExtPerc.muitoQuente,
                            (TempExt.muitoQuente, UmidExt.muitoBaixa): TempExtPerc.quente,
                            (TempExt.muitoQuente, UmidExt.baixa): minus(TempExtPerc.muitoQuente),
                            (TempExt.muitoQuente, UmidExt.normal): TempExtPerc.muitoQuente,
                            (TempExt.muitoQuente, UmidExt.alta): plus(TempExtPerc.muitoQuente),
                            (TempExt.muitoQuente, UmidExt.muitoAlta): TempExtPerc.extremamenteQuente,
                            (TempExt.extremamenteQuente, UmidExt.muitoBaixa): TempExtPerc.extremamenteQuente,
                            (TempExt.extremamenteQuente, UmidExt.baixa): minus(TempExtPerc.extremamenteQuente),
                            (TempExt.extremamenteQuente, UmidExt.normal): TempExtPerc.extremamenteQuente,
                            (TempExt.extremamenteQuente, UmidExt.alta): plus(TempExtPerc.extremamenteQuente),
                            (TempExt.extremamenteQuente, UmidExt.muitoAlta): very(TempExtPerc.extremamenteQuente)
                        })

regrasTempIntPerc = Rule({
                            
                            (TempInt.extremamenteFrio, UmidInt.muitoBaixa): TempIntPerc.muitoFrio,
                            (TempInt.extremamenteFrio, UmidInt.baixa): minus(TempIntPerc.extremamenteFrio),
                            (TempInt.extremamenteFrio, UmidInt.normal): TempIntPerc.extremamenteFrio,
                            (TempInt.extremamenteFrio, UmidInt.alta): plus(TempIntPerc.extremamenteFrio),
                            (TempInt.extremamenteFrio, UmidInt.muitoAlta): very(TempIntPerc.extremamenteFrio),
                            (TempInt.muitoFrio, UmidInt.muitoBaixa): TempIntPerc.frio,
                            (TempInt.muitoFrio, UmidInt.baixa): minus(TempIntPerc.muitoFrio),
                            (TempInt.muitoFrio, UmidInt.normal): TempIntPerc.muitoFrio,
                            (TempInt.muitoFrio, UmidInt.alta): plus(TempIntPerc.muitoFrio),
                            (TempInt.muitoFrio, UmidInt.muitoAlta): TempIntPerc.extremamenteFrio,
                            (TempInt.frio, UmidInt.muitoBaixa): TempIntPerc.normal,
                            (TempInt.frio, UmidInt.baixa): minus(TempIntPerc.frio),
                            (TempInt.frio, UmidInt.normal): TempIntPerc.frio,
                            (TempInt.frio, UmidInt.alta): plus(TempIntPerc.frio),
                            (TempInt.frio, UmidInt.muitoAlta): TempIntPerc.muitoFrio,
                            (TempInt.normal, UmidInt.muitoBaixa): minus(TempIntPerc.normal),
                            (TempInt.normal, UmidInt.baixa): TempIntPerc.normal,
                            (TempInt.normal, UmidInt.normal): TempIntPerc.normal,
                            (TempInt.normal, UmidInt.alta): plus(TempIntPerc.normal),
                            (TempInt.normal, UmidInt.muitoAlta): very(TempIntPerc.normal),
                            (TempInt.quente, UmidInt.muitoBaixa): TempIntPerc.normal,
                            (TempInt.quente, UmidInt.baixa): minus(TempIntPerc.quente),
                            (TempInt.quente, UmidInt.normal): TempIntPerc.quente,
                            (TempInt.quente, UmidInt.alta): plus(TempIntPerc.quente),
                            (TempInt.quente, UmidInt.muitoAlta): TempIntPerc.muitoQuente,
                            (TempInt.muitoQuente, UmidInt.muitoBaixa): TempIntPerc.quente,
                            (TempInt.muitoQuente, UmidInt.baixa): minus(TempIntPerc.muitoQuente),
                            (TempInt.muitoQuente, UmidInt.normal): TempIntPerc.muitoQuente,
                            (TempInt.muitoQuente, UmidInt.alta): plus(TempIntPerc.muitoQuente),
                            (TempInt.muitoQuente, UmidInt.muitoAlta): TempIntPerc.extremamenteQuente,
                            (TempInt.extremamenteQuente, UmidInt.muitoBaixa): TempIntPerc.extremamenteQuente,
                            (TempInt.extremamenteQuente, UmidInt.baixa): minus(TempIntPerc.extremamenteQuente),
                            (TempInt.extremamenteQuente, UmidInt.normal): TempIntPerc.extremamenteQuente,
                            (TempInt.extremamenteQuente, UmidInt.alta): plus(TempIntPerc.extremamenteQuente),
                            (TempInt.extremamenteQuente, UmidInt.muitoAlta): very(TempIntPerc.extremamenteQuente)
                        })

def getTemExtApar(temp, umid):
    values = {TempExt: temp, UmidExt: umid}
    return regrasTempExtPerc(values) + (-20.01) #o método supoe partir do zero, necessário normalizar

def getTemIntApar(temp, umid):
    values = {TempInt: temp, UmidInt: umid}
    return regrasTempIntPerc(values) + (-20.01) #o método supoe partir do zero, necessário normalizar


'''
Definindo a variável de saída e as regras do sistema intermediário TEMPERATURA_INTERNA_ROUPA.
Neste ponto, a temperatura percebida (temperatura + umidade) interna é reavalidada, dessa vez
considerando o padrão de vestimenta do local.
'''

TempIntRoupa = Domain("Temperatura Interna com Roupa", -20.01, 50.01)
TempIntRoupa.extremamenteFrio = trapezoid(-20.01, -20, -10, -5)
TempIntRoupa.extremamenteFrio = TempIntRoupa.extremamenteFrio.normalized()
#TempIntRoupa.extremamenteFrio.plot()
TempIntRoupa.muitoFrio = triangular(-7, 7)
#TempIntRoupa.muitoFrio.plot()
TempIntRoupa.frio = triangular(6, 18)
#TempIntRoupa.frio.plot()
TempIntRoupa.normal = triangular(16, 28)
#TempIntRoupa.normal.plot()
TempIntRoupa.quente = triangular(26, 34)
#TempIntRoupa.quente.plot()
TempIntRoupa.muitoQuente = triangular(32, 44)
#TempIntRoupa.muitoQuente.plot()
TempIntRoupa.extremamenteQuente = trapezoid(42, 45, 50, 50.1)
TempIntRoupa.extremamenteQuente = TempIntRoupa.extremamenteQuente.normalized()
#TempIntRoupa.extremamenteQuente.plot()


regrasTempIntRoupa = Rule({
                            (TempIntPerc.extremamenteFrio, DensRoup.alta): TempIntRoupa.muitoFrio,
                            (TempIntPerc.extremamenteFrio, DensRoup.normal): TempIntRoupa.extremamenteFrio,
                            (TempIntPerc.extremamenteFrio, DensRoup.baixa): very(TempIntRoupa.extremamenteFrio),
                            (TempIntPerc.muitoFrio, DensRoup.alta): TempIntRoupa.frio,
                            (TempIntPerc.muitoFrio, DensRoup.normal): TempIntRoupa.muitoFrio,
                            (TempIntPerc.muitoFrio, DensRoup.baixa): TempIntRoupa.extremamenteFrio,
                            (TempIntPerc.frio, DensRoup.alta): TempIntRoupa.normal,
                            (TempIntPerc.frio, DensRoup.normal): TempIntRoupa.frio,
                            (TempIntPerc.frio, DensRoup.baixa): very(TempIntRoupa.frio),
                            (TempIntPerc.normal, DensRoup.alta): TempIntRoupa.quente,
                            (TempIntPerc.normal, DensRoup.normal): TempIntRoupa.normal,
                            (TempIntPerc.normal, DensRoup.baixa): TempIntRoupa.frio,
                            (TempIntPerc.quente, DensRoup.baixa): TempIntRoupa.normal,
                            (TempIntPerc.quente, DensRoup.normal): TempIntRoupa.quente,
                            (TempIntPerc.quente, DensRoup.alta): very(TempIntRoupa.quente),
                            (TempIntPerc.muitoQuente, DensRoup.baixa): TempIntRoupa.quente,
                            (TempIntPerc.muitoQuente, DensRoup.normal): TempIntRoupa.muitoQuente,
                            (TempIntPerc.muitoQuente, DensRoup.alta): TempIntRoupa.extremamenteQuente,
                            (TempIntPerc.extremamenteQuente, DensRoup.baixa): TempIntRoupa.muitoQuente,
                            (TempIntPerc.extremamenteQuente, DensRoup.normal): TempIntRoupa.extremamenteQuente,
                            (TempIntPerc.extremamenteQuente, DensRoup.alta): very(TempIntRoupa.extremamenteQuente)
                            })

def getTempIntRoupa(tempIntAp, densRoup):
    values = {TempIntPerc: tempIntAp, DensRoup: densRoup}
    return regrasTempIntRoupa(values) + (-20.01) #o método supoe partir do zero, necessário normalizar


'''
Definindo variável de saída e regra para sistema intermediário CLIMATIZACAO.
Neste ponto, o sistema decide se deve aquecer ou resfriar o ambiente baseado
na diferença entre temperatura interna e externa.
'''

Climatizacao = Domain("Climatização", -0.01, 10.01)
Climatizacao.aquecMaximo = trapezoid(-0.01, 0, 2, 4)
Climatizacao.aquecMaximo = Climatizacao.aquecMaximo.normalized()
#Climatizacao.aquecMaximo.plot()
Climatizacao.aquecNormal = triangular(3, 5)
#Climatizacao.aquecNormal.plot()
Climatizacao.desligado = triangular(4, 6)
#Climatizacao.desligado.plot()
Climatizacao.arNormal = triangular(5, 7)
#Climatizacao.arNormal.plot()
Climatizacao.arMaximo = trapezoid(6, 8, 10, 10.1)
Climatizacao.arMaximo = Climatizacao.arMaximo.normalized()
#Climatizacao.arMaximo.plot()

regrasClimatizacao = Rule({
                    (TempExtPerc.extremamenteFrio, TempIntRoupa.extremamenteFrio): very(Climatizacao.aquecMaximo),
                    (TempExtPerc.extremamenteFrio, TempIntRoupa.muitoFrio): Climatizacao.aquecMaximo,
                    (TempExtPerc.extremamenteFrio, TempIntRoupa.frio): Climatizacao.aquecNormal,
                    (TempExtPerc.extremamenteFrio, TempIntRoupa.normal): Climatizacao.aquecNormal,
                    (TempExtPerc.extremamenteFrio, TempIntRoupa.quente): Climatizacao.desligado,
                    (TempExtPerc.extremamenteFrio, TempIntRoupa.muitoQuente): Climatizacao.arNormal,
                    (TempExtPerc.extremamenteFrio, TempIntRoupa.extremamenteQuente): very(Climatizacao.arNormal),
                    (TempExtPerc.muitoFrio, TempIntRoupa.extremamenteFrio): Climatizacao.aquecMaximo,
                    (TempExtPerc.muitoFrio, TempIntRoupa.muitoFrio): Climatizacao.aquecMaximo,
                    (TempExtPerc.muitoFrio, TempIntRoupa.frio): Climatizacao.aquecNormal,
                    (TempExtPerc.muitoFrio, TempIntRoupa.normal): Climatizacao.desligado,
                    (TempExtPerc.muitoFrio, TempIntRoupa.quente): Climatizacao.desligado,
                    (TempExtPerc.muitoFrio, TempIntRoupa.muitoQuente): Climatizacao.arNormal,
                    (TempExtPerc.muitoFrio, TempIntRoupa.extremamenteQuente): Climatizacao.arMaximo,
                    (TempExtPerc.frio, TempIntRoupa.extremamenteFrio): Climatizacao.aquecMaximo,
                    (TempExtPerc.frio, TempIntRoupa.muitoFrio): Climatizacao.aquecNormal,
                    (TempExtPerc.frio, TempIntRoupa.frio): Climatizacao.aquecNormal,
                    (TempExtPerc.frio, TempIntRoupa.normal): Climatizacao.desligado,
                    (TempExtPerc.frio, TempIntRoupa.quente): Climatizacao.arNormal,
                    (TempExtPerc.frio, TempIntRoupa.muitoQuente): Climatizacao.arNormal,
                    (TempExtPerc.frio, TempIntRoupa.extremamenteQuente): Climatizacao.arMaximo,
                    (TempExtPerc.normal, TempIntRoupa.extremamenteFrio): Climatizacao.aquecMaximo,
                    (TempExtPerc.normal, TempIntRoupa.muitoFrio): Climatizacao.aquecNormal,
                    (TempExtPerc.normal, TempIntRoupa.frio): Climatizacao.desligado,
                    (TempExtPerc.normal, TempIntRoupa.normal): Climatizacao.desligado,
                    (TempExtPerc.normal, TempIntRoupa.quente): Climatizacao.desligado,
                    (TempExtPerc.normal, TempIntRoupa.muitoQuente): Climatizacao.arNormal, 
                    (TempExtPerc.normal, TempIntRoupa.extremamenteQuente): Climatizacao.arMaximo,
                    (TempExtPerc.quente, TempIntRoupa.extremamenteFrio): Climatizacao.aquecMaximo,
                    (TempExtPerc.quente, TempIntRoupa.muitoFrio): Climatizacao.aquecNormal,
                    (TempExtPerc.quente, TempIntRoupa.frio): Climatizacao.aquecNormal,
                    (TempExtPerc.quente, TempIntRoupa.normal): Climatizacao.desligado,
                    (TempExtPerc.quente, TempIntRoupa.quente): Climatizacao.arNormal,
                    (TempExtPerc.quente, TempIntRoupa.muitoQuente): Climatizacao.arNormal,
                    (TempExtPerc.quente, TempIntRoupa.extremamenteQuente): Climatizacao.arMaximo,
                    (TempExtPerc.muitoQuente, TempIntRoupa.extremamenteFrio): Climatizacao.aquecMaximo,
                    (TempExtPerc.muitoQuente, TempIntRoupa.muitoFrio): Climatizacao.aquecNormal,
                    (TempExtPerc.muitoQuente, TempIntRoupa.frio): Climatizacao.desligado,
                    (TempExtPerc.muitoQuente, TempIntRoupa.normal): Climatizacao.desligado,
                    (TempExtPerc.muitoQuente, TempIntRoupa.quente): Climatizacao.arNormal,
                    (TempExtPerc.muitoQuente, TempIntRoupa.muitoQuente): Climatizacao.arMaximo,
                    (TempExtPerc.muitoQuente, TempIntRoupa.extremamenteQuente): Climatizacao.arMaximo,
                    (TempExtPerc.extremamenteQuente, TempIntRoupa.extremamenteFrio): very(Climatizacao.aquecNormal),
                    (TempExtPerc.extremamenteQuente, TempIntRoupa.muitoFrio): Climatizacao.aquecNormal,
                    (TempExtPerc.extremamenteQuente, TempIntRoupa.frio): Climatizacao.desligado,
                    (TempExtPerc.extremamenteQuente, TempIntRoupa.normal): Climatizacao.arNormal,
                    (TempExtPerc.extremamenteQuente, TempIntRoupa.quente): Climatizacao.arNormal,
                    (TempExtPerc.extremamenteQuente, TempIntRoupa.muitoQuente): Climatizacao.arMaximo,
                    (TempExtPerc.extremamenteQuente, TempIntRoupa.extremamenteQuente): very(Climatizacao.arMaximo),
                    })

def getClimatizacao(tempExtAp, tempIntRoupa):
    values = {TempExtPerc: tempExtAp, TempIntRoupa: tempIntRoupa}
    return regrasClimatizacao(values)


'''
Definindo variável de saída e regra para o último sistema CLIMATIZACAO_ACAO.
Nesse ponto, aplica-se o gosto pessoal sobre a decisão de ação tomada anteriormente.
'''

ClimaPersonal = Domain("Climatização personalizada", -0.01, 10.01)
ClimaPersonal.aquecMaximo = trapezoid(-0.01, 0, 2, 4)
ClimaPersonal.aquecMaximo = Climatizacao.aquecMaximo.normalized()
#ClimaPersonal.aquecMaximo.plot()
ClimaPersonal.aquecNormal = triangular(3, 5)
#ClimaPersonal.aquecNormal.plot()
ClimaPersonal.desligado = triangular(4, 6)
#ClimaPersonal.desligado.plot()
ClimaPersonal.arNormal = triangular(5, 7)
#ClimaPersonal.arNormal.plot()
ClimaPersonal.arMaximo = trapezoid(6, 8, 10, 10.1)
ClimaPersonal.arMaximo = Climatizacao.arMaximo.normalized()
#ClimaPersonal.arMaximo.plot()


regrasClimatizacaoPerson = Rule({
                                (Climatizacao.aquecMaximo, GostoPess.frio): ClimaPersonal.aquecNormal,
                                (Climatizacao.aquecMaximo, GostoPess.normal): ClimaPersonal.aquecMaximo,
                                (Climatizacao.aquecMaximo, GostoPess.quente): very(ClimaPersonal.aquecMaximo),
                                (Climatizacao.aquecNormal, GostoPess.frio): ClimaPersonal.desligado,
                                (Climatizacao.aquecNormal, GostoPess.normal): ClimaPersonal.aquecNormal,
                                (Climatizacao.aquecNormal, GostoPess.quente): ClimaPersonal.aquecMaximo,
                                (Climatizacao.desligado, GostoPess.frio): ClimaPersonal.arNormal,
                                (Climatizacao.desligado, GostoPess.normal): ClimaPersonal.desligado,
                                (Climatizacao.desligado, GostoPess.quente): ClimaPersonal.aquecNormal,
                                (Climatizacao.arNormal, GostoPess.frio): ClimaPersonal.arMaximo,
                                (Climatizacao.arNormal, GostoPess.normal): ClimaPersonal.arNormal,
                                (Climatizacao.arNormal, GostoPess.quente): ClimaPersonal.desligado,
                                (Climatizacao.arMaximo, GostoPess.frio): very(ClimaPersonal.arMaximo),
                                (Climatizacao.arMaximo, GostoPess.normal): ClimaPersonal.arMaximo,
                                (Climatizacao.arMaximo, GostoPess.quente): ClimaPersonal.arNormal
                                })

def getClimatizacaoPersonal(climatizacao, gostoPessoal):
    values = {Climatizacao: climatizacao, GostoPess: gostoPessoal}
    return regrasClimatizacaoPerson(values)


'''
Recebe como entrada:
    - temperatura externa
    - umidade externa
    - temperatura interna
    - umidade interna
    - gosto pessoal
    - densidade das roupas
'''
def getAcao(variaveis =(0, 0, 0, 0, 0)):
    #aproxima a senscao termica externa
    tempAparenteExterna = getTemExtApar(variaveis[0], variaveis[1])
    #aproxima a sensacao termica interna
    tempAparenteInterna = getTemIntApar(variaveis[2], variaveis[3])
    #aproxima a sensacao termica interna considerando roupas
    tempInternaRoupas = getTempIntRoupa(tempAparenteInterna, variaveis[5])
    #decide entre aquecer ou resfriar a partir das temperaturas internas e externas
    climatizacao = getClimatizacao(tempAparenteExterna, tempInternaRoupas)
    #personaliza a acao para um gosto pessoal configurado
    acaoPersonalizada = getClimatizacaoPersonal(climatizacao, variaveis[4])
    
    acao = ClimaPersonal(acaoPersonalizada)
    return acao

