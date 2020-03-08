import cv2

def DisplayCamera():
    cap = cv2.VideoCapture(0)

    def rescale_frame(frame, percent=25):
        width = int(frame.shape[1] * percent/ 100)
        height = int(frame.shape[0] * percent/ 100)
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

        while True:
            rect, frame = cap.read()
            frame25 = rescale_frame(frame, percent=25)
            cv2.imshow('frame75', frame25)

            cv2.waitKey(10000)

