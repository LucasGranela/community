def criarOpcoe(texto,acao = None):
    return {
        'texto':texto,
        'acao':acao
    }
    

class Tela:
    def __init__(self,opcoes,back,textoComeco = "", forcarFechamento = None):
        self.opcoes = opcoes
        self.back = back
        self.textoComeco = textoComeco
        self.forcarFechamento =  forcarFechamento
    
        
    def show(self):
        while(True):

            if(self.forcarFechamento != None):
                if(self.forcarFechamento()):
                    break

            print("")

            if(self.textoComeco != None):
                print(self.textoComeco)
                print("")
            
            count = 1
            for opcao in self.opcoes:
                print(str(count),"-",opcao['texto'])
                count += 1
            print("0 -",self.back['texto'])
            
            opcaoEscolhida= None
            try:
                opcaoEscolhida = int(input("Entre com sua opcao:"))
            except:
                print("Opcao inválida!")
                continue
            
            print("")

            if(opcaoEscolhida == 0):
                if(self.back['acao'] != None):
                    self.back['acao']()
                break

            elif(opcaoEscolhida < 0 or opcaoEscolhida> len(self.opcoes)):
                print("Opcao inválida!")
                continue

            self.opcoes[opcaoEscolhida-1]['acao']()
                    

              



            