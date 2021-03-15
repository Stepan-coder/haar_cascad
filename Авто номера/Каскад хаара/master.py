import cv2

def get_numberplace(input_img, k):
    haar_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
    dim = (int(input_img.shape[1]*k), int(input_img.shape[0] * k))
    resized_img = cv2.resize(input_img, dim, interpolation = cv2.INTER_AREA)
    gray_scale_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
    pictures = haar_cascade.detectMultiScale(gray_scale_img, scaleFactor=1.40, minNeighbors=15, minSize=(20, 20))
    recognized = []
    for (x, y, w, h) in pictures:
        cv2.rectangle(resized_img, (x, y), (x + w, y + h), (255, 0, 0), 2) # визуализация работы
        recognized.append(resized_img[y:y + h, x:x + w])
    cv2.imshow("now", resized_img)
    return recognized


 # img = cv2.imread("ru2530478.jpg")
# cam = cv2.VideoCapture(0)
# while(1):
#     ret, frame = cam.read()
#     images = get_numberplace(frame, 0.95)
#     if len(images) > 0:
#         cv2.imshow('rec', images[0])
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cam.release()
# cv2.destroyAllWindows()


img = cv2.imread('ru2530478.jpg')
images = get_numberplace(img, 0.9)
if len(images) > 0:
    for i in range(len(images)):
        cv2.imshow(str(i), images[i])
cv2.waitKey(0)
cv2.destroyAllWindows()