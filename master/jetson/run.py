import tensorflow as tf
from keras.models import *
from keras.layers import *
from keras.losses import *
from keras.optimizers import *
import numpy as np
import math
from utilities import *
import time

try:
    #Check if NVIDIA GPU CUDA is connected
    physical_devices = tf.config.list_physical_devices('GPU')
    tf.config.experimental.set_memory_growth(physical_devices[0], True)
except:
    print("No GPU devices detected. Running on CPU")

img_size = (512, 512)
epochs = 5
batch_size = 4

model = load_model("master/jetson/model.h5")
model.summary()

prev_frame_time = 0
new_frame_time = 0

cap = cv2.VideoCapture("rtsp://admin:admin123456@172.20.129.23:10700/cam/realmonitor?channel=1&subtype=0")

if (cap.isOpened()== False): 
    print("Error opening video stream or file")

while cap.isOpened():
    #INEFFICIENT! This code uses the cv2 cpu, which is not what we want as the processing speed
    #CUDA cv2 is what we want, but theres barely any time to write it
    ret, frame = cap.read()
    
    if ret == True:
        frame = cv2.resize(frame, img_size)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        X_test = np.reshape(frame, (-1, img_size[0], img_size[1], 3))
        preds = model.predict(X_test)
        pred = np.reshape(preds, (img_size[0], img_size[1]))

        pred_uint8 = pred * 255
        pred_uint8 = pred_uint8.astype(np.uint8)
        bw = img_threshold(pred_uint8)

        filled_contour = draw_filled_contour(bw, img_size)
        feed_percentage = calc_whitepixels(filled_contour)

        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        contour = draw_contour(bw, frame)

        new_frame_time = time.time()
        fps = 1 / (new_frame_time - prev_frame_time)
        prev_frame_time = new_frame_time
        fps = str(int(fps))
        cv2.putText(contour, f"FPS: {fps}", (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 238, 0), 2, cv2.LINE_AA)
        cv2.putText(contour, f"Feed % {math.ceil(feed_percentage)}", (5, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 238, 0), 2, cv2.LINE_AA)

        cv2.imshow('Video', contour)
        firebase(math.ceil(feed_percentage))
        time.sleep(1)
        # Press Q on keyboard to  exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else: 
        break

cap.release()
cv2.destroyAllWindows()