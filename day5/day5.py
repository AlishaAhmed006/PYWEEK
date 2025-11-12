# import cv2

# # image reading
# image = cv2.imread("C:/Users/USER/Desktop/VS CODE/python-day1/venv/vk.jpg")

# cv2.imshow("VIRAT KOHLI - Original", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # convert to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("VIRAT KOHLI - Grayscale", gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # resized
# resized = cv2.resize(gray, (700, 700))
# cv2.imshow("VIRAT KOHLI ", resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #blur
# blur=cv2.GaussianBlur(resized,(7,7),3)
# cv2.imshow("VIRAT KOHLI", blur)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#video reading
import cv2
# cap=cv2.VideoCapture("cat.mp4")
# while True:
#     success,frame=cap.read()
#     if not success:
#         break
#     cv2.imshow("Cat Video",frame)
#     if cv2.waitKey(1)& 0xFF==ord("q"):
#         break
# cap.release()
# cv2.destroyAllWindows()

cap=cv2.VideoCapture(0)

while True:
    
    success,frame=cap.read()
    cv2.flip(frame,1,frame)
    if not success:
        break
    cv2.imshow("MyVideo",frame)
    if cv2.waitKey(1)& 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
