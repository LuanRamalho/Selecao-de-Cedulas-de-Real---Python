import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Links das imagens das cédulas
links_cedulas = {
    "1 Real": "https://filatelicavitoriaregia.com.br/wp-content/uploads/2023/12/cedula-1-real-2001-anverso.jpg",
    "2 Reais": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSs2Q34ho0mdpyG6uP9Kues39iDHTo-ynSRA&s",
    "5 Reais": "https://www.bcb.gov.br/novasnotas/assets/img/section/5/5_front.jpg",
    "10 Reais": "https://www.bcb.gov.br/novasnotas/assets/img/section/10/10_front.jpg",
    "20 Reais": "https://extra.globo.com/incoming/25533889-e67-697/w448/download.jpg",
    "50 Reais": "https://www.bcb.gov.br/novasnotas/assets/img/section/50/50_front.jpg",
    "100 Reais": "https://www.bcb.gov.br/novasnotas/assets/img/section/100/100_front.jpg"
}

# Função para carregar e exibir a imagem da cédula selecionada
def exibir_imagem(cedula):
    if cedula in links_cedulas:
        url = links_cedulas[cedula]
        try:
            response = requests.get(url, timeout=5)  # Define um tempo limite para a requisição
            response.raise_for_status()  # Verifica se houve algum erro na requisição
            image_data = response.content
            image = Image.open(BytesIO(image_data))
            image = image.resize((300, 150), Image.LANCZOS)  # Redimensiona a imagem
            photo = ImageTk.PhotoImage(image)
            imagem_label.config(image=photo)
            imagem_label.image = photo
            info_label.config(text=f"Você selecionou a cédula de {cedula}")
        except requests.RequestException:
            info_label.config(text="Erro ao carregar a imagem. Verifique o link.")
        except Exception as e:
            info_label.config(text=f"Erro inesperado: {e}")

# Configurações da janela principal
root = tk.Tk()
root.title("Seleção de Cédulas de Dinheiro")
root.geometry("500x500")
root.configure(bg="#DFF0E8")

# Label de Instrução
instrucoes_label = tk.Label(root, text="Escolha uma cédula de dinheiro:", font=("Helvetica", 14), bg="#DFF0E8")
instrucoes_label.pack(pady=10)

# Menu de Seleção de Cédulas
opcao_cedula = ttk.Combobox(root, values=list(links_cedulas.keys()), font=("Helvetica", 12))
opcao_cedula.pack(pady=10)
opcao_cedula.set("Selecione uma cédula")

# Botão para exibir a cédula selecionada
botao_exibir = tk.Button(root, text="Exibir Cédula", command=lambda: exibir_imagem(opcao_cedula.get()), bg="#68C3A3", fg="white", font=("Helvetica", 12))
botao_exibir.pack(pady=10)

# Label para exibir a imagem da cédula selecionada
imagem_label = tk.Label(root, bg="#DFF0E8")
imagem_label.pack(pady=10)

# Label para exibir informações sobre a cédula selecionada
info_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#DFF0E8")
info_label.pack(pady=5)

root.mainloop()
