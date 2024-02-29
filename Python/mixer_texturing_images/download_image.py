import requests

def download_image(url, save_path):
    # Baixa a imagem da URL
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Imagem baixada com sucesso: {save_path}")
    else:
        print(f"Falha ao baixar imagem: {url}")
