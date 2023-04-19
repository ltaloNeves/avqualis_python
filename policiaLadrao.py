def can_reach_end(labirinto):
    # Posição inicial da polícia
    inicio = (0, 0)
    # Posição final dos ladrões
    fim = (4, 4)
    visited = set()
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    #verificando se a posição é valida

    def is_valid(x, y):
        if x < 0 or x > 4 or y < 0 or y > 4:
            return False
        if labirinto[x][y] == 1:
            return False
        return True

    #explorar os possiveis movimentos que podem ser feitos
    def dfs(x, y):
        visited.add((x, y))
        if (x, y) == fim:
            return True
        for move in moves:
            new_x, new_y = x + move[0], y + move[1]
            if is_valid(new_x, new_y) and (new_x, new_y) not in visited:
                if dfs(new_x, new_y):
                    return True
        return False

    
    #polica consegue alcançar o ladrão?
    if dfs(inicio[0], inicio[1]):
        return "COPS"
    else:
        return "ROBBERS"


#definindo o labirinto por meio do usuario
labirinto = []
for i in range(5):
    row = input("Digite a linha {} do labirinto (0's e 1's separados por espaço): ".format(i+1)).split()
    row = [int(x) for x in row]
    labirinto.append(row)

# Exibe o resultado para o labirinto definido pelo usuário
print(can_reach_end(labirinto))

'''
0 0 0 0 1
1 1 0 0 1
0 1 0 0 0
0 0 0 1 1
1 1 0 0 0
cops


0 0 0 0 1
1 1 0 0 1
0 1 0 0 0
0 0 1 1 1
1 1 0 0 0
robbers
'''
