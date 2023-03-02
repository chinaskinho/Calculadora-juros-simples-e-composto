import math
# *Para encontrar o valor desejado, basta deixa-lo igual a 0 na formula
# * Infelizmente o valor do tempo na formula de juros composto não está retornando corretamente mesmo eu tendo colocado a unica formula que encontrei

def jurosS(capital,tempo,taxa, montante = 0):
    if montante == 0:
        juros = (capital * (taxa/100))*tempo
        return f'Juros: R$ {juros} \nMontante: R$ {capital + juros}'
    elif capital == 0:
        capital = montante/ 1 + tempo*(taxa/100)
        return f'Capital: R$ {capital}'
    elif taxa == 0:
        taxa = ((montante/capital-1)/tempo)*100
        return f'Taxa: R$ {taxa}%'
    elif tempo == 0:
        tempo = (montante/capital-1)*taxa
        return f'Tempo: `{tempo}'


def jurosC(capital= 0,tempo= 0,taxa = 0, montante = 0):
    if montante == 0:
        montante = capital * (1 + (taxa / 100)) ** tempo
        return 'Juros: R$ %.2f \nMontante: R$ %.2f' % (montante - capital, montante)
    elif capital == 0:
        capital = montante / (1 + (taxa / 100)) ** tempo
        return 'Capital: R$ %.2f' % capital
    elif taxa == 0:
        taxa = ((montante / capital) ** (1/tempo)-1) * 100
        return 'Taxa: %.2f%%' % taxa
    elif tempo == 0:
        tempo = math.log(montante/capital)/math.log(1+taxa)
        return f'Tempo: `{tempo}'














