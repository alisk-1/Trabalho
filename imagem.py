import cv2

# Carrega uma imagem do disco
imagem = cv2.imread('minha_imagem.jpg')

# Exibe a imagem em uma janela
cv2.imshow('Minha Imagem Legal', imagem)

# Aguarda uma tecla ser pressionada e fecha a janela
cv2.waitKey(0)
cv2.destroyAllWindows()
