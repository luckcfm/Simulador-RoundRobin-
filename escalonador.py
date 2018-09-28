#coding: utf-8
import sys
import time


#O processo terá apenas 2s para ser executado
#Seguindo a logica do R-R, o processo deve ser removido da execucao quando
#O mesmo exaurir seu quantum.
#Se o mesmo terminar a sua execução antes do fim, deve-se incluir
#outro processo para ser executado.


class processo:
    def __init__(self,id,tempo):
        self.id = id
        self.tempo = tempo
    def reduzTempo(self):
        self.tempo = self.tempo - 1;
        #Se o processo estiver terminado a execução ele tem que sair da fila
        if(self.tempo == 0):
            print("O processo %s terminou a sua execução" % (self.id))
            return False
        return True
    def getTempo(self):
        print "O processo %s tem: %s\n" % (self.id, self.tempo)

processos = []


#Vamos iniciar aqui o contador do quantunss
def iniciaExecucao(quantum,processo):
    timer=quantum
    #Enquanto existir timer.
    while timer > 0:
        #vamos iniciar o timer para o processo
        if(processo.reduzTempo()):
            time.sleep(1)
            timer = timer - 1
            processo.getTempo()
        else:
            #Ele vai retornar true somente se o processo terminar a execucao
            return True
    return False



#Aqui criamos alguns procesos para simulação
#NÃO ESTAMOS LEVANDO EM CONSIDERAÇÃO PAUSAS PARA I/O
processo1 = processo(10,50)
processo2 = processo(4,10)
processo3 = processo(11,20)
processo4 = processo(12,11)
processos.append(processo1)
processos.append(processo2)

#soh uma flag para podermos adicionar mais processos à frente.
flag_adicao = 0

while True:
    tmpProcesso = processos.pop(0)
    if(iniciaExecucao(2,tmpProcesso)):
        print "Removendo processo %s do array pois terminou a execucao" % tmpProcesso.id
        if flag_adicao == 0:
            processos.append(processo3)
            processos.append(processo4)
            flag_adicao = 1
    else:
        #Devemos adicionar o processo ao final da fila
        print "Voltando processo %s para a fila" %tmpProcesso.id
        processos.append(tmpProcesso)




#Projeto realizado com a ajuda de: https://en.wikipedia.org/wiki/Round-robin_scheduling

