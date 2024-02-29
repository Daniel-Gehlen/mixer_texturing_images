import cv2

def apply_perspective(texture1, texture2):
    # Convertendo a primeira textura para escala de cinza
    texture1_gray = cv2.cvtColor(texture1, cv2.COLOR_BGR2GRAY)

    # Convertendo a segunda textura para escala de cinza
    texture2_gray = cv2.cvtColor(texture2, cv2.COLOR_BGR2GRAY)

    # Calculando a diferença absoluta entre as texturas em escala de cinza
    texture_diff = cv2.absdiff(texture1_gray, texture2_gray)

    # Aplicando a diferença como máscara na textura principal
    mixed_texture_with_relief = cv2.bitwise_and(texture1, texture1, mask=texture_diff)

    return mixed_texture_with_relief
