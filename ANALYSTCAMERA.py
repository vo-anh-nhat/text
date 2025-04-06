import cv2

cap = cv2.VideoCapture("D:/PYTHON/VIDEOCAR.mp4")  # open the video
if not cap.isOpened():  # Check the video
    print("Can not open video!") 
    exit()

car_cascade = cv2.CascadeClassifier("D:/PYTHON/haarcascade_ca.xml")  # Model detect car by XML

detected_cars = []  #  Declare loop to not reset
selected_car = None  # Varriable save car was selected by clickmouse

def mouse_callback(event, x, y, flags, param):
    global selected_car  # Allow access global varriablevarriable

    if event == cv2.EVENT_LBUTTONDOWN:  # Kiểm tra nếu click chuột trái
        for (x1, y1, w, h) in detected_cars:
            if x1 <= x <= x1 + w and y1 <= y <= y1 + h:  # Check if click was in carcar
                selected_car = frame[y1:y1 + h, x1:x1 + w]  # Cut image carcar
                cv2.imshow("Selected Car", selected_car)  # Show image car was selectedselected
                print(f"Car was selected at: {x1, y1, w, h}") 
# Gán sự kiện click chuột vào cửa sổ chính
cv2.namedWindow("Car Detection")
cv2.setMouseCallback("Car Detection", mouse_callback)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error: can not read the video!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detected_cars = car_cascade.detectMultiScale(gray, 1.1, 3)  # detect car

    for (x, y, w, h) in detected_cars:  # Draw rectangle around car
        image = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)  # Viền đen
        height, width, _ = image.shape  # "_" bỏ qua kênh màu vì không cần dùng

        axis_color = (0, 0, 0)  # Màu đen vẽ trục
        thickness = 3 

        # Vẽ trục X và Y
        cv2.line(image, (0, height - 1), (width, height - 1), axis_color, thickness)  # Axis x
        cv2.line(image, (0, height - 1), (0, 0), axis_color, thickness)  # Axis y

    cv2.imshow("Car Detection", frame)  # Show frame

    if cv2.waitKey(25) & 0xFF == ord('f'):  # Nhấn 'f' để thoát
        break

cap.release()  # Free video
cv2.destroyAllWindows()
