import sys
from MemoriaCache import MemoriaCache

CPU_DEBUG = True

registrador_cp = 0x00
registrador_ax = 0x00
registrador_bx = 0x00
registrador_cx = 0x00
registrador_dx = 0x00

flag_zero = False

# memoria = MemoriaCache('arquivos_memoria/mov_mov_add.bin')
memoria = MemoriaCache('arquivos_memoria/inc_dec.bin')
#memoria = MemoriaCache('arquivos_memoria/todas_instrucoes.bin')
#memoria = MemoriaCache('arquivos_memoria/programa_simples.bin')
#memoria = MemoriaCache('arquivos_memoria/fibonacci_10.bin')

def buscarEDecodificarInstrucao():
    instrucao = memoria.getValorMemoria(registrador_cp)

    print(instrucao)

    # mov_mov_add
    if instrucao == 0x40:
        print('MOV Reg, Byte')
        return 40
    elif instrucao == 0x01:
        print('return ADD reg, Reg')
        return 1
    # inc_dec
    elif instrucao == 0x10:
        print('INC Reg')
        return 10
    elif instrucao == 0x20:
        print('DEC Reg')
        return 20

    return -1

def lerOperadoresExecutarInstrucao(idInstrucao):
    global registrador_ax
    global registrador_bx
    global registrador_cx
    global registrador_dx

    # mov_mov_add
    if idInstrucao == 40:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)

        if operador1 == 0x02:
            print('executou mov')
            registrador_ax = operador2
        elif operador1 == 0x03:
            registrador_bx = operador2

    elif idInstrucao == 1:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)

        if operador1 == 0x02:
            if operador2 == 0x02:
                registrador_ax += registrador_ax
            elif operador2 == 0x03:
                registrador_ax += registrador_bx
            elif operador2 == 0x04:
                registrador_ax += registrador_cx
            elif operador2 == 0x05:
                registrador_ax += registrador_dx

    # inc_dec
    elif idInstrucao == 10:
        operador = memoria.getValorMemoria(registrador_cp + 1)

        if operador == 0x02:
            print('INC AX')
            registrador_ax += 1
        elif operador == 0x03:
            print('INC BX')
            registrador_bx += 1
        elif operador == 0x04:
            print('INC CX')
            registrador_cx += 1
        elif operador == 0x05:
            print('INC DX')
            registrador_dx += 1
    
    elif idInstrucao == 20:
        operador = memoria.getValorMemoria(registrador_cp + 1)

        if operador == 0x02:
            print('DEC AX')
            registrador_ax -= 1
        elif operador == 0x03:
            print('DEC BX')
            registrador_bx -= 1
        elif operador == 0x04:
            print('DEC CX')
            registrador_cx -= 1
        elif operador == 0x05:
            print('DEC DX')
            registrador_dx -= 1
    
    print ('Implementar a lerOperadoresExecutarInstrucao')

def calcularProximaInstrucao(idInstrucao):

    global registrador_cp

    if idInstrucao == 40:
        registrador_cp += 3
    elif idInstrucao == 1:
        registrador_cp += 3
    elif idInstrucao == 10 or idInstrucao == 20:
        registrador_cp += 2
    
    print ('Implementar a calcularProximaInstrucao')

def dumpRegistradores():
    if CPU_DEBUG:
        print(f'CP[{registrador_cp:02X}] \
            AX[{registrador_ax:02X}]  \
            BX[{registrador_bx:02X}]  \
            CX[{registrador_cx:02X}]  \
            DX[{registrador_dx:02X}]  \
            ZF[{flag_zero}] ')

if __name__ == '__main__':
    while (True):
        #Unidade de Controle
        idInstrucao = buscarEDecodificarInstrucao()

        #ULA
        lerOperadoresExecutarInstrucao(idInstrucao)  

        dumpRegistradores() 

        #Unidade de Controle
        calcularProximaInstrucao(idInstrucao)

        #apenas para nao ficar em loop voce pode comentar a linha abaixo =)
        sys.stdin.read(1)
    
