import random
def gerarCampo(matrizUsuario, linhas, colunas, matriz, x, y,vitorias):
    win = True
    if matriz[x][y] == -1:
        matrizUsuario[x][y] = matriz[x][y]
        for i in range(len(matrizUsuario)):
            for j in range(0, len(matrizUsuario)):
                row = i
                col = j
                print(f'| {matrizUsuario[row][col]} ', end="")
            print("|")          
        win = False
        return win
    elif matriz[x][y] != -1 and matrizUsuario[x][y] == "X":
        matrizUsuario[x][y] = matriz[x][y]
        vitorias +=1
        for i in range(len(matrizUsuario)):
            for j in range(0, len(matrizUsuario)):
                row = i
                col = j
                print(f'| {matrizUsuario[row][col]} ', end="")
            print("|")   
        return vitorias
    elif matriz[x][y] != -1 and matrizUsuario[x][y] != "X":
        for i in range(len(matrizUsuario)):
            for j in range(0, len(matrizUsuario)):
                row = i
                col = j
                print(f'| {matrizUsuario[row][col]} ', end="")
            print("|")
        print("Você já escolheu essa casa, escolha outra!\n")
def gerarBombas(matriz, linhas, colunas, bombas):
    while bombas > 0:
        aleatLine = random.randint(0, linhas-1)
        aleatCol = random.randint(0, colunas-1)
        if matriz[aleatLine][aleatCol] != -1:
            matriz[aleatLine][aleatCol] = -1
            bombas -= 1
            
def verificadorBombas(matriz, linhas, colunas):
    for a in range(0, linhas):
        for b in range(0, colunas):
            if matriz[a][b] == -1:
                continue
            cont_minas_adj = 0
            for c in range(a - 1 if a > 0 else 0, a + 2 if a < linhas - 1 else linhas):
                for d in range(b - 1 if b > 0 else 0, b + 2 if b < colunas - 1 else colunas):
                    if matriz[c][d] == -1:
                        cont_minas_adj += 1
            matriz[a][b] = str(cont_minas_adj)
    return matriz 
def main():
    while True:
        
        print("-"*10,"CAMPO MINADO","-"*10)
        print("Escolha a dificuldade que deseja jogar:")
        print("1 - Fácil\n2 - Médio\n3 - Difícil")
        lvl = int(input("Nível:"))
        if lvl == 1:
            linhas = 4
            colunas = 4
            bombas = 5
        elif lvl == 2:
            linhas = 6
            colunas = 6
            bombas = 10
        elif lvl == 3:
            linhas =8
            colunas = 8
            bombas = 20
        matriz = [["-" for i in range(colunas)] for j in range(linhas)]
        matrizUsuario = [["X" for i in range(colunas)] for j in range(linhas)]
        gerarBombas(matriz, linhas, colunas, bombas)
        vitorias = 0
        while True:
            print("Escolha a posição que deseja jogar:")
            x = int(input("Linha: "))-1
            y = int(input("Coluna: "))-1
            verificadorBombas(matriz, linhas, colunas)
            
            print("-"*10,"TABULEIRO","-"*10)
            for i in range(0, linhas):
                print(" ",i+1,end=" ")
            print()
            win = gerarCampo(matrizUsuario, linhas, colunas, matriz, x, y, vitorias)
            
            if win == False:
                print("Você perdeu!")
                break;
            else:
                vitorias += 1
                if vitorias >= (linhas * colunas - bombas):
                    print("Parabéns! Você venceu o jogo! :)")
                    break;
        try:
            play = input("Deseja jogar novamente?(y/n): ")
            if play == "n" or "no" or "não":
                break
            if play == "y" or "yes" or "sim":
                print("Então vamos jogar novamente!")
                continue
        except ValueError:
            print("Por favor insira um valor válido")
    
main()