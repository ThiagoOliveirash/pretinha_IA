class TeachingInterface:
    def __init__(self, ai):
        self.ai = ai

    def ensinar(self):
        """Método para ensinar a IA."""
        while True:
            entrada = input("Digite uma pergunta ou comando para ensinar a IA (ou 'sair' para encerrar): ")
            if entrada.lower() == 'sair':
                break
            resposta = input("Digite a resposta da IA: ")
            self.ai.aprender(entrada, resposta)
        self.ai.salvar_conhecimento()
        print("Conhecimento salvo com sucesso!")