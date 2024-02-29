from mixer_texturing.utils.io import download_image
from mixer_texturing.combination import mix_textures
from mixer_texturing.transformation import apply_perspective
from mixer_texturing.utils.plot import plot_images

# URL das imagens
cat_image_url = 'https://unsplash.com/photos/AaEQmoufHLk/download'
car_image_url = 'https://unsplash.com/photos/3Ww7_CoLHFA/download'

# Caminhos para salvar as imagens
cat_image_path = '/content/cat_image.jpg'
car_image_path = '/content/car_image.jpg'

# Baixa as imagens
download_image(cat_image_url, cat_image_path)
download_image(car_image_url, car_image_path)

# Carrega as imagens
cat_image = cv2.imread(cat_image_path)
car_image = cv2.imread(car_image_path)

# Mistura as texturas
mixed_texture = mix_textures(cat_image_path, car_image_path)
if mixed_texture is not None:
    # Aplica a perspectiva
    mixed_texture_with_relief = apply_perspective(mixed_texture, cv2.imread(cat_image_path))

    # Plota as imagens
    plot_images(cat_image, car_image, mixed_texture_with_relief)
