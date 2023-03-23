import cv2 as cv 

def video_demo():
    capture = cv.VideoCapture("video1_Trim_2_original.mp4")
    flag = 1
    name_label = 1
    while True:
        ret, frame = capture.read()
        #cv.imshow("frame", frame)
        if (flag % 30 == 0) and (ret is True):
            cv.imshow("frame", frame)
            cv.imwrite("video1_Trim_2_original/" + "version_ma_original_" + str(name_label) + ".png", frame)
            name_label = name_label + 1
        flag = flag + 1
        if cv.waitKey(100) & 0xFF == ord('q'):
            break

video_demo()
cv.destroyAllWindows()
