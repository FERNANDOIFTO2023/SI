import time
import os

def gerenciar_recurso():
    if not os.path.exists('status.txt'):
        with open('status.txt', 'w') as arquivo:
            arquivo.write('0')

    try:
    
            with open("status.txt", "r") as arquivo:
        valor = arquivo.read().strip()

    
        if valor == "0":
            print("Recurso disponível. Reservando recurso...")
            
            
            with open("status.txt", "w") as arquivo:
                arquivo.write("1")
            
            print("Utilizando recurso...")
            
            
            time.sleep(5) 
            
            print("Liberando recurso...")
            
            
            with open("status.txt", "w") as arquivo:
                arquivo.write("0")
            
            print("Recurso liberado com sucesso!")

        elif valor == "1":
            print("Recurso ocupado. Tente novamente mais tarde.")
            
       
        else:
            print("Valor inválido no arquivo")
            
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    gerenciar_recurso()