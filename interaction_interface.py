class InteractionInterface:
    def __init__(self, ai):
        self.ai = ai

    def interagir(self):
        """Método para interagir com a IA."""
        print(f"Bem-vindo à {self.ai.nome}! Pergunte o que quiser (ou 'sair' para encerrar).")
        while True:
            pergunta = input("Você: ")
            if pergunta.lower() == 'sair':
                break
            resposta = self.ai.responder(pergunta)
            print(f"{self.ai.nome}: {resposta}")