import cv2


face_cascade = cv2.CascadeClassifier("face_detector/haarcascade_frontalface_default.xml") # Добавляю шаблон поиска лиц в переменную

img = cv2.imread('face_detector/news.jpg') # read img as color
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Конвертируем в чб (для лучшего распознования)

# объект, который хранит координаты верхней левой точки прямоугольника лица и длины его сторон. 
# minNeighbors - мин количество соседних искать вокруг лица
# scaleFactor=1.05 - чем больше тем хуже но быстрее ищет лица 
faces = face_cascade.detectMultiScale(gray_img, 
scaleFactor=1.05, 
minNeighbors=5)  

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 200, 200), 3) # Вверхняя левая координата, нижняя правая, BGR, ширина прямоугольника

print(type(faces))
print(faces)

resized =cv2.resize(img, (img.shape[1]//3, img.shape[0]//3))

cv2.imshow("gray", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()