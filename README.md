# Sistema fuzzy para climatização residencial automática
O sistema considera quatro variáveis contínuas obtidas por sensores:
* Temperatura Interna
* Umidade Interna
* Temperatura Externa
* Umidade Externa

E mais duas variáveis discretas configuráveis:
* Gosto Pessoal
* Densidade das Roupas

A partir destas entradas, o sistema decide se é necessário aquecer ou resfriar o ambiente.

** Todo o sistema é baseado na toolbox de lógica fuzzy implementada por [Amogorkon](https://github.com/amogorkon/fuzzylogic) **