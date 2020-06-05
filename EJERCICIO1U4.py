#Inteligencia Artificial CARLOS EDUARDO CUPUL HAU

#Se importa la libreria de CV2
import cv2
#Ruta de la imagen
fileImage = "/home/AI/image.jpeg"
#Imagen en bits
image = cv2.imread(fileImage)
#Se visualiza la imagen original
cv2.imshow("Logo ITSVA ORIGINAL",image)
#Insertando la imagen a función de detección de bordes
imageBorder = cv2.Canny(image,100,200)
#Se visualiza la imagen con bordes
cv2.imshow("Logotipo ITSVA CON BORDES",imageBorder)
#Tiempo de espera para cerrar las imagenes
cv2.waitKey(0)

