# XOR
def xor(a, b):
    return ['0' if bit_a == bit_b else '1' for bit_a, bit_b in zip(a, b)]
# AND
def and_bits(a, b):
    return ['1' if bit_a == '1' and bit_b == '1' else '0' for bit_a, bit_b in zip(a, b)]
#NOT
def not_bits(bits):
    return ['0' if bit == '1' else '1' for bit in bits]

# SHIFT
def right_shift(line, position):
    return ['0'] * position + line[:-position]

#SIGMA 0 - Expansion
def a0(line):
    # ROTATE PARA OS PRIMEIROS 7 BITS
    ultimos = line[-7:]
    primeiros= line[:-7]
    rotate7 = ultimos + primeiros

    # ROTATE PARA OS PRIMEIROS 18 BITS
    ultimos = line[-18:]
    primeiros = line[:-18]
    rotate18 = ultimos + primeiros

    # RIGHT SHIFT USANDO FUNÇÃO
    shift = right_shift(line, 3)

    # XOR
    temp = xor(rotate7, rotate18)
    result = xor(temp, shift)
    return result

# SIGMA 1 - Expansion
def a1(line):
    # ROTATE PARA OS PRIMEIROS 17 BITS
    ultimos = line[-17:]
    primeiros = line[:-17]
    rotate17 = ultimos + primeiros

    # ROTATE PARA OS PRIMEIROS 19 BITS
    ultimos = line[-19:]
    primeiros = line[:-19]
    rotate19 = ultimos + primeiros

    # RIGHT SHIFT USANDO FUNÇÃO
    shift = right_shift(line, 10)

    # XOR
    temp = xor(rotate17, rotate19)
    result = xor(temp, shift)
    return result


# SIGMA 0 - Compression
def e0(line):
    # RIGHT ROTATE 2
    ultimos = line[-2:]
    primeiros= line[:-2]
    rotate2 = ultimos + primeiros

    # RIGHT ROTATE 13
    ultimos = line[-13:]
    primeiros = line[:-13]
    rotate13 = ultimos + primeiros

    # RIGHT ROTATE 22
    ultimos = line[-22:]
    primeiros = line[:-22]
    rotate22 = ultimos + primeiros

    # XOR
    temp = xor(rotate2, rotate13)
    result = xor(temp, rotate22)
    return result

# SIGMA 1 - Compression
def e1(line):
    # RIGHT ROTATE 6
    ultimos = line[-6:]
    primeiros= line[:-6]
    rotate6 = ultimos + primeiros

    # RIGHT ROTATE 11
    ultimos = line[-11:]
    primeiros = line[:-11]
    rotate11 = ultimos + primeiros

    # RIGHT ROTATE 22
    ultimos = line[-25:]
    primeiros = line[:-25]
    rotate25 = ultimos + primeiros

    # XOR
    temp = xor(rotate6, rotate11)
    result = xor(temp, rotate25)
    return result

def choice(e, f, g):
    stepOne = and_bits(e, f)
    stepTwo = not_bits(e)
    stepTre = and_bits(stepTwo, g)
    return xor(stepOne , stepTre)

def majority(a, b, c):
    ab = and_bits(a, b)
    ac = and_bits(a, c)
    bc = and_bits(b, c)

    abc = xor(ab, ac)
    result = xor(abc, bc)

    return result

def soma(v1, v2, v3, v4, v5, parametros):
    bits_a = "".join(v1)
    bits_b = "".join(v2)
    int_a = int(bits_a, 2)
    int_b = int(bits_b, 2)
    valor = int_a + int_b

    # QUANDO FOR PASSADO 4 PARAMETROS ELE FAZ A SOMA COM 4 ELEMENTOS
    if parametros == 4:
        bits_c = "".join(v3)
        bits_d = "".join(v4)
        int_c = int(bits_c, 2)
        int_d = int(bits_d, 2)
        valor = int_a + int_b + int_c + int_d

    # QUANDO FOR PASSADO 5 PARAMETROS ELE FAZ A SOMA COM 5 ELEMENTOS
    if parametros == 5:
        bits_c = "".join(v3)
        bits_d = "".join(v4)
        bits_e = "".join(v5)
        int_c = int(bits_c, 2)
        int_d = int(bits_d, 2)
        int_e = int(bits_e, 2)
        valor = int_a + int_b + int_c + int_d + int_e

    soma_bits = valor & 0xFFFFFFFF
    resultado = list(format(soma_bits, '032b'))

    return resultado

def recostruir(hash):
    # MAPA - BASE64
    char_map = {
        i: char for i, char in enumerate(
            [
                *map(chr, range(65, 91)),  # A-Z (0-25)
                *map(chr, range(97, 123)),  # a-z (26-51)
                *map(str, range(0, 10)),  # 0-9 (52-61)
                '+',  # 62
                '/'   # 63
            ]
        )
    }

    numeros = []  # Recebe os valores numericos do hash

    inverse_map = {v: k for k, v in char_map.items()}
    update = [char for char in hash if char != '=']
    newhash = [char for char in update if char != '==']

    for c in newhash:
        numeros.append(inverse_map[c])

    lista_bits = [format(num, '06b') for num in numeros]

    string_bits = ''.join(lista_bits)

    bits8 = [string_bits[i:i + 8] for i in range(0, len(string_bits), 8)]

    ascs = [int(byte, 2) for byte in bits8]

    palavra = [chr(asc) for asc in ascs]

    return palavra

def verificar(palavra):
    # Inserção Manual das constantes(k)
    constants = [
        list("01000010100010100010111110011000"),
        list("01110001001101110100010010010001"),
        list("10110101110000001111101111001111"),
        list("11101001101101011101101110100101"),
        list("00111001010101101100001001011011"),
        list("01011001111100010001000111110001"),
        list("10010010001111111000001010100100"),
        list("10101011000111000101111011010101"),
        list("11011000000001111010101010011000"),
        list("00010010100000110101101100000001"),
        list("00100100001100011000010110111110"),
        list("01010101000011000111110111000011"),
        list("01110010101111100101110101110100"),
        list("10000000110111101011000111111110"),
        list("10011011110111000000011010100111"),
        list("11000001100110111111000101110100"),
        list("11100100100110110110100111000001"),
        list("11101111101111100100011110000110"),
        list("00001111110000011001110111000110"),
        list("00100100000011001010000111001100"),
        list("00101101111010010010110001101111"),
        list("01001010011101001000010010101010"),
        list("01011100101100001010100111011100"),
        list("01110110111110011000100011011010"),
        list("10011000001111100101000101010010"),
        list("10101000001100011100011001101101"),
        list("10110000000000110010011111001000"),
        list("10111111010110010111111111000111"),
        list("11000110111000000000101111110011"),
        list("11010101101001111001000101000111"),
        list("00000110110010100110001101010001"),
        list("00010100001010010010100101100111"),
        list("00100111101101110000101010000101"),
        list("00101110000110110010000100111000"),
        list("01001101001011000110110111111100"),
        list("01010011001110000000110100010011"),
        list("01100101000010100111001101010100"),
        list("01110110011010100000101010111011"),
        list("10000001110000101100100100101110"),
        list("10010010011100100010110010000101"),
        list("10100010101111111110100010100001"),
        list("10101000000110100110011001001011"),
        list("11000010010010111000101101110000"),
        list("11000111011011000101000110100011"),
        list("11010001100100101110100000011001"),
        list("11010110100110010000011000100100"),
        list("11110100000011100011010110000101"),
        list("00010000011010101010000001110000"),
        list("00011001101001001100000100010110"),
        list("00011110001101110110110000001000"),
        list("00100111010010000111011101001100"),
        list("00110100101100001011110010110101"),
        list("00111001000111000000110010110011"),
        list("01001110110110001010101001001010"),
        list("01011011100111001100101001001111"),
        list("01101000001011100110111111110011"),
        list("01110100100011111000001011101110"),
        list("01111000101001010110001101101111"),
        list("10000100110010000111100000010100"),
        list("10001100110001110000001000001000"),
        list("10010000101111101111111111111010"),
        list("10100100010100000110110011101011"),
        list("10111110111110011010001111110111"),
        list("11000110011100010111100011110010")
    ]
    # Registradores
    h0 = list('01101010000010011110011001100111')
    h1 = list('10111011011001111010111010000101')
    h2 = list('00111100011011101111001101110010')
    h3 = list('10100101010011111111010100111010')
    h4 = list('01010001000011100101001001111111')
    h5 = list('10011011000001010110100010001100')
    h6 = list('00011111100000111101100110101011')
    h7 = list('01011011111000001100110100011001')

    padding = []  # 16 linhas de 32 bits
    matriz = []  # 32 bits por linha
    byts = []  # Separa em 8 bits
    bits = []  # Todos os 512 bits
    aux = []  # Soma os pares de bits
    valores = ''  # Valores Temporarios

    char = list(palavra)

    ## String inserida é trasformada em char, a função é responsavel por fazer a conversão de char para bits
    for i in char:
        byts.append(format(ord(i), '08b'))
    i = 0
    ## Bits 0 até o 488
    while i in range(56):
        if i == len(byts):
            padding.append('10000000')
        elif i < len(byts):
            padding.append(byts[i])
        else:
            padding.append('00000000')
        i += 1
    i = 0
    ## O tamanho total da palavra é inserido no final
    for i in range(7):
        padding.append('00000000')
    palavra = len(char) * 8
    padding.append(format(palavra, '08b'))

    i = 0
    ## 512 bits em uma matriz, 32 bits em cada linha... 32*16 = 512
    for by in padding:
        if i == 4:
            valores += aux[0]
            valores += aux[1]
            valores += aux[2]
            valores += aux[3]
            matriz.append(list(valores))
            i = 0
            valores = ''
            aux.clear()
        aux.append(by)
        i += 1

    ## Finals Bits
    valores += aux[0]
    valores += aux[1]
    valores += aux[2]
    valores += aux[3]
    matriz.append(list(valores))

    # ROTATION -------------------------------------------------------------------------------------------------------------
    # Matriz com 64 linhas, 48 novas linhas para ser preenchida com a rotação
    for _ in range(48):
        matriz.append([0] * 32)  # ARRUMAR TALVEZ

    # Expasão da mensagem -> Linha 15 a 63
    for elements in range(len(matriz)):
        if elements + 1 < len(matriz):
            r0 = a0(matriz[elements + 1])
        if elements + 14 < len(matriz):
            r1 = a1(matriz[elements + 14])
        if elements + 16 < len(matriz):
            matriz[elements + 16] = soma(matriz[elements], matriz[elements + 9], r0, r1, '', 4)
    i = 0
    # ----------------------------------------------------------------------------------------------------------------------
    # iniciar variavel
    a = h0
    b = h1
    c = h2
    d = h3
    e = h4
    f = h5
    g = h6
    h = h7

    # temp1 = h + E1 + choice + k0 + w0 | temp2 = E0 +  major
    for elements in range(len(matriz)):
        temp1 = soma(h, e1(e), choice(e, f, g), constants[elements], matriz[elements], 5)
        temp2 = soma(e0(a), majority(a, b, c), '', '', '', 2)

        # Update valores
        h = g
        g = f
        f = e
        e = soma(d, temp1, '', '', '', 2)
        d = c
        c = b
        b = a
        a = soma(temp1, temp2, '', '', '', 2)

    h0 = soma(h0, a, '', '', '', 2)
    h1 = soma(h1, b, '', '', '', 2)
    h2 = soma(h2, c, '', '', '', 2)
    h3 = soma(h3, d, '', '', '', 2)
    h4 = soma(h4, e, '', '', '', 2)
    h5 = soma(h5, f, '', '', '', 2)
    h6 = soma(h6, g, '', '', '', 2)
    h7 = soma(h7, h, '', '', '', 2)

    h0 = hex(int(''.join(h0), 2))[2:].zfill(8)
    h1 = hex(int(''.join(h1), 2))[2:].zfill(8)
    h2 = hex(int(''.join(h2), 2))[2:].zfill(8)
    h3 = hex(int(''.join(h3), 2))[2:].zfill(8)
    h4 = hex(int(''.join(h4), 2))[2:].zfill(8)
    h5 = hex(int(''.join(h5), 2))[2:].zfill(8)
    h6 = hex(int(''.join(h6), 2))[2:].zfill(8)
    h7 = hex(int(''.join(h7), 2))[2:].zfill(8)
    return f"{h0}{h1}{h2}{h3}{h4}{h5}{h6}{h7}"
def base64(char):
    # MAPA - BASE64
    char_map = {
        i: char for i, char in enumerate(
            [
                *map(chr, range(65, 91)),  # A-Z (0-25)
                *map(chr, range(97, 123)),  # a-z (26-51)
                *map(str, range(0, 10)),  # 0-9 (52-61)
                '+',  # 62
                '/'  # 63
            ]
        )
    }

    six = []     ## 6 BITS POR LINHA
    asc = []     ## ASC FINAL
    byts = []    ## 8 BITS EM CADA LISTA
    matriz = []  ## 24 BITS POR LINHA
    result = []  ## VALOR FINAL
    bits = ''    ## SEPARA OS BITS
    count = 0    ## CONTROLE
    padding = 0  ## VALOR DO PADDING

    ## TRANSFORMA A STRING EM BYTS E ADICIONA A LISTA
    for i in char:
        byts.append(format(ord(i), '08b'))

    ## MATRIZ RECEBE 24 BITS, CADA LINHA VAI TER 3 BYTS
    i = 0
    for elements in byts:
        count = 0
        bits += elements
        if i == 2:
            matriz.append(list(bits))
            bits = ''
            i = 0
            count = 1
        i += 1

    if count == 0:  ## SE CASO NÃO ENTRAR NO IF DO FOR ELE COMPLETA
        matriz.append(list(bits))

    # PADDING
    for lines in range(len(matriz)):
        if len(matriz[lines]) == 8:
            bits = matriz[lines]
            bits += '00000000'
            bits += '00000000'
            matriz[lines] = list(bits)
            padding = 2
        if len(matriz[lines]) == 16:
            bits = matriz[lines]
            bits += '00000000'
            padding = 1
            matriz[lines] = list(bits)

    # SEPARAÇÃO
    #  6 BITS POR LINHA
    for lines in matriz:
        for i in range(0, len(lines), 6):
            bloco = lines[i:i + 6]
            six.append(bloco)
    # CONVERSION
    for elements in six:
        # LISTA PARA STRING
        bits_str = ''.join(str(bit) for bit in elements)
        # CONVERSÃO PARA DECIMAL
        decimal = int(bits_str, 2)
        asc.append(decimal)

    # RESULT
    for num in asc:
        result.append(char_map[num])

    # PADDING
    if padding == 2:
        result.append('==')
    if padding == 1:
        result.append('=')
    # END
    return result


# Insert
string = input("Informe o texto: ")
char = list(string)
retorno = base64(char)

print(f"Retorno do Base64: {retorno}")


while True:
    print("[1] - Reconstruir o conteúdo original ")
    print("[2] - Verificar a autenticidade da mensagem ")
    print("[3] - Exit ")
    opcode = input("Informe um numero de acordo com as opcoes: ")
    if opcode == "1":
        recostrucao = recostruir(retorno)
        valor = ''.join(recostrucao)
        print(f"Conteudo Original: {valor}")
    if opcode == "2":
        recostrucao = recostruir(retorno)
        valor = ''.join(recostrucao)
        if verificar(string) == verificar(valor):
            print("as palavras são semelhantes!")
        else:
            print("a palavra original e o retorno da reconstrucao são diferentes")
    if opcode == "3":
        print("Saindo!")
        break
