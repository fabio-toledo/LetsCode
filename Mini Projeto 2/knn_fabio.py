class Knn:
    def __init__(self, k):        
        '''
        Método construtor da Classe KNN que calcula
        as distâncias entre vários pontos de acordo 
        com o k escolhido
        '''
        self.k = k
                     
    def calcularDistancia(self, cartAtual, cartVizinho):
        '''
        Método que calcula as distâncias entre os pontos
        contidos na lista 'cartVizinho' em relação
        à lista informada em 'cartAtual'
        '''
        self.cartAtual = cartAtual
        self.cartVizinho = cartVizinho
        x=0
        for i in range(len(self.cartAtual)):
            x = x + (self.cartAtual[i] - self.cartVizinho[i])**2
        distancia = x**.5
        return distancia   
    
    def encontrarMaisProximos(self, k, pessoa, data):
        '''
        Método que calcula os vizinhos mais próximos
        baseado nas distâncias informadas no método calcularDistancia 
        e o fator k (que é o número de vizinhos desejados) 
        '''        
        self.k = k
        self.pessoa = pessoa
        self.data = data
        listProximos = []
        
        for v in range(len(self.data)):
            listProximos.append((self.data[v][1], self.calcularDistancia(self.pessoa[2], self.data[v][2])))
            if v >= self.k:
                listPerfisDistancias = list(zip(*listProximos))
                #print(listPerfisDistancias)
                idxMaior = listPerfisDistancias[1].index(max(listPerfisDistancias[1]))
                #print(idxMaior)
                listProximos.pop(idxMaior)
                #print(listProximos)
        return listProximos
    
    def definirPerfil(self, listPerfisProximos):
        '''
        Método que classifica todos os cpf´s
        contidos na base de não classificados
        'no_class' conforme a lista de perfis próximos
        '''
        self.listPerfisProximos = listPerfisProximos
        
        dicTotais = {
            'Conservador': 0,
            'Moderado': 0,
            'Agressivo': 0
        }
        # print(dicTotais)
        for perfil in self.listPerfisProximos:
            if perfil[0] == 'Conservador':
                dicTotais['Conservador'] += 1
            elif perfil[0] == 'Moderado':
                dicTotais['Moderado'] += 1
            else:
                dicTotais['Agressivo'] += 1
        print(dicTotais)
        totais = [dicTotais.get('Conservador'), dicTotais.get('Moderado'), dicTotais.get('Agressivo')]
        # print(totais)
        maior = max(totais)
        # print(maior)
        if (maior == dicTotais.get('Conservador')):
            return 'Conservador'
        elif (maior == dicTotais.get('Moderado')):
            return 'Moderado'
        else:
            return 'Agressivo'