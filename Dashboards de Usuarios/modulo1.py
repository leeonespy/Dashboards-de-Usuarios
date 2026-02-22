from datetime import datetime
import matplotlib.pyplot as plt
from cores import Cores
import csv, random

agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

class Usuario:
    def __init__(self, nome, emeil, data_criacao=agora):
        
        
        ID = 0
        exite = False
        with open("usuarios.csv", "r") as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                
                if linha["Usuario"] == nome:
                    exite = True
                    break
                if linha["Usuario"]:
                    ID +=1 
        if exite:
            print(Cores.vermelho + "Usuario ja existe" + Cores.resetar)
        else:
            dados = [{
            "Id": ID,
            "Usuario": nome,
            "E-meil": emeil,
            "Data": data_criacao
            }]
            self.add(dados)
                
                
        
    def add(self, dados):
        
        with open("usuarios.csv", "a", newline="", encoding="utf-8") as f:
            colunas = ["Id", "Usuario", "E-meil", "Data"]
            escritor = csv.DictWriter(f, fieldnames=colunas)
            f.seek(0, 2)
            if f.tell() == 0:
                escritor.writeheader()
            escritor.writerows(dados)
            
class Sistema:
    def __init__(self):
        pass
    
    def gerador_dados_aleatorios(self):
        dia = random.randint(1, 29)
        mes = random.randint(1, 12)
        ano = random.randint(2017, 2025)
        hora = random.randint(00, 23)
        minu = random.randint(00, 59)
        segun = random.randint(00, 59)
        
        data = (f"{dia}/{mes}/{ano} {hora}:{minu}:{segun}")
        
        letras = ["Leon", "Carl", "cecil", "lom", "tom"]
        nome = random.choice(letras)
        subre = random.choice(letras) 
        nomecomp = nome + subre
        emeil = (f"leones{random.randint(0, 100)}@gmail.com")
        ID = random.randint(1, 1000)
        
        dados = [{
            "Id": ID,
            "Usuario": nomecomp,
            "E-meil": emeil,
            "Data": data
            }]
        return dados
        
    def salvar_aleatorios(self):
        dados = self.gerador_dados_aleatorios()
        
        with open("usuarios.csv", "a", newline="", encoding="utf-8") as f:
            colunas = ["Id", "Usuario", "E-meil", "Data"]
            escritor = csv.DictWriter(f, fieldnames=colunas)
            f.seek(0, 2)
            if f.tell() == 0:
                escritor.writeheader()
            escritor.writerows(dados)
    
    def total_usuarios(self):
        Usuario = 0
        with open("usuarios.csv", "r") as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                Usuario += 1
                linha["Usuario"]
        catego = ["Quantidade de usuarios"]
        valores = [int(Usuario)]    
        plt.bar(catego, valores)
        plt.title("Total de Usuarios")
        plt.show()      
    
    def data_criacao(self):
        datas = []
        with open("usuarios.csv", "r") as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                datas.append(linha["Data"])
                
            data_convertida = [datetime.strptime(d, "%d/%m/%Y %H:%M:%S") for d in datas]
            
            maior = max(data_convertida)
            menor = min(data_convertida)
                
        catego = ["Data mais antiga", "Data mais recente"]
        valores = [menor, maior]    
        plt.bar(catego, valores)
        plt.title("Total de Usuarios")
        plt.show() 
           
    

