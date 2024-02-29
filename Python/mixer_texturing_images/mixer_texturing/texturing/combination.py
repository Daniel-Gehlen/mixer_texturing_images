import cv2

def mix_textures(texture1_path, texture2_path):
    # Carregando as texturas
    texture1 = cv2.imread(texture1_path)
    if texture1 is None:
        print(f"Falha ao carregar a textura: {texture1_path}")
        return None

    texture2 = cv2.imread(texture2_path)
    if texture2 is None:
        print(f"Falha ao carregar a textura: {texture2_path}")
        return None

    # Redimensionando a segunda textura para ter o mesmo tamanho da primeira
    texture2_resized = cv2.resize(texture2, (texture1.shape[1], texture1.shape[0]))

    # Misturando as texturas
    mixed_texture = cv2.addWeighted(texture1, 0.5, texture2_resized, 0.5, 0)

    return mixed_texture
