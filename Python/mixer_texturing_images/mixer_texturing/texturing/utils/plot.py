import matplotlib.pyplot as plt
import cv2

def plot_images(image1, image2, transformed_image):
    # Cria a figura para plotagem
    plt.figure(figsize=(12, 6))

    # Plota a primeira imagem
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
    plt.title('Imagem 1 (random)')
    plt.axis('off')

    # Plota a segunda imagem
    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
    plt.title('Imagem 2 (random2)')
    plt.axis('off')

    # Plota a terceira imagem transformada
    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(transformed_image, cv2.COLOR_BGR2RGB))
    plt.title('Imagem Transformada')
    plt.axis('off')

    # Mostra as imagens
    plt.tight_layout()
    plt.show()
