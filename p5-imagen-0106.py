import cv2
# leer la imagen con cv = computer vision
img = cv2.imread('perrito.jpg')
# determinar el tipo de imagen numpy.ndarray
print(type(img))
# mostrar pixeles (276, 183, 3)
print(img.shape)
# mostrando imagen en ventana barra de titulo
cv2.imshow('perrito 0106', img)
## tiempo de espera
cv2.waitKey(0)
#destruir todas las ventanas
cv2.destroyAllWindows()