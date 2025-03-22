#virtual mouse
import cv2 as cv
import mediapipe as mp
import pyautogui

cap = cv.VideoCapture(0)
detect_hand = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

index_y=0
index_x=0
clicked = False
while True:
    _, frame = cap.read()
    frame =  cv.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    output = detect_hand.process(rgb_frame)
    hand_landmarks = output.multi_hand_landmarks
    
    if hand_landmarks:
        for hand in hand_landmarks:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x=int(landmark.x*frame_width)
                y=int(landmark.y*frame_height)
                # print(x,y)
                if(id==8):
                    color = (255,0,0) if clicked else (0,0,0)
                    cv.circle(img = frame, center = (x,y), radius = 10, color = color, thickness = 3)
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x, index_y)

                if(id==4):
                    color = (255,0,0) if clicked else (0,0,255)
                    cv.circle(img = frame, center = (x,y), radius = 10, color = color, thickness = 3)
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    if( abs(thumb_y-index_y)<20):
                        clicked = True
                        pyautogui.click()
                        pyautogui.sleep(1)
                    else:
                        clicked = False

    cv.imshow('virtual mouse', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break