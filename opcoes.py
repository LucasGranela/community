tiposOcorrencia = ["Criminal","Estrutural"]
subtiposOcorrencia = ["Falta de luz","Vazamento de agua","Roubo","Diversos"]
subtiposOcorrenciaCriminal = ["Roubo","Diversos"]
subtiposOcorrenciaCriminalValues = [2,3]
subtiposOcorrenciaEstrutural = ["Falta de luz","Vazamento de agua","Diversos"]
subtiposOcorrenciaEstruturalValues = [0,1,3]

estadosOcorrencia = ["Nao verificado","Em andamento","Verificado"]

def terminalSelect(opcoes,opcoesValue = None,nullOption = False):
        
    opcaoEscolhida = None

    while(True):
        count = 1
        for opcao in opcoes:
            print(str(count),"-",opcao)
            count += 1
        
        try:
            opcaoEscolhida = input("Entre com o numero da opcao:")
            if((opcaoEscolhida == None or opcaoEscolhida == "") and nullOption):
                return ""
            
            opcaoEscolhida = int(opcaoEscolhida)
        except:
            
            print("Opcao inválida!")
            continue
        
        print("")


        
        if(opcaoEscolhida <= 0 or opcaoEscolhida> len(opcoes)):
            print("Opcao inválida!")
            continue

        if(opcoesValue != None):
            return opcoesValue[opcaoEscolhida - 1]    
        return opcaoEscolhida - 1