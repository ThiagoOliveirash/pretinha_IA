import json
import os
import random

class AI:
    def __init__(self, nome="Pretinha"):
        self.nome = nome
        self.conhecimento = {}

    def aprender(self, entrada, resposta):
        """Método para ensinar a IA."""
        if entrada.lower() in self.conhecimento:
            self.conhecimento[entrada.lower()].append(resposta)
        else:
            self.conhecimento[entrada.lower()] = [resposta]

    def salvar_conhecimento(self, arquivo="conhecimento.json"):
        """Salva o conhecimento da IA em um arquivo JSON."""
        with open(arquivo, 'w') as file:
            json.dump(self.conhecimento, file, indent=4)

    def carregar_conhecimento(self, arquivo="conhecimento.json"):
        """Carrega o conhecimento da IA de um arquivo JSON."""
        if os.path.exists(arquivo):
            with open(arquivo, 'r') as file:
                self.conhecimento = json.load(file)

    def pesquisar_conhecimento(self, pergunta, diretorio="arquivos_texto"):
        """Método para pesquisar conhecimento em arquivos de texto."""
        if not os.path.exists(diretorio):
            return "Desculpe, não há arquivos de texto disponíveis para pesquisa."

        respostas_encontradas = []

        for arquivo in os.listdir(diretorio):
            caminho_arquivo = os.path.join(diretorio, arquivo)
            if os.path.isfile(caminho_arquivo) and arquivo.endswith(".txt"):
                with open(caminho_arquivo, 'r') as file:
                    conteudo_arquivo = file.read().lower()
                    if pergunta.lower() in conteudo_arquivo:
                        respostas_encontradas.append(conteudo_arquivo)

        if respostas_encontradas:
            return random.choice(respostas_encontradas)
        else:
            return "Desculpe, não encontrei informações relevantes para essa pergunta."