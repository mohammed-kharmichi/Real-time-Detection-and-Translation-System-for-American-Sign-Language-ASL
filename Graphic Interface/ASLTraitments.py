
import cv2 # type: ignore
from PyQt5.QtGui import QImage, QPixmap # type: ignore
import numpy as np # type: ignore

# display the insertion elements
def displayInsertionElements(ui):
    # display the label insertion style
    ui.label_insertion.setStyleSheet(
    """
        #label_insertion {  background-color: #ffd55a;
                            border-top-left-radius: 40px;
                            border-top-right-radius: 40px;
                            color: white;   }

        #label_insertion:hover { background-color: #ffd55a;}
    """ )
    ui.body_insertion.show()

# display the real time elements
def displayRealTimeElements(ui):
    # display label real time style
    ui.label_realtime.setStyleSheet(
    """
        #label_realtime {  background-color: #ffd55a;
                            border-top-left-radius: 40px;
                            border-top-right-radius: 40px;
                            color: white;   }

        #label_realtime:hover { background-color: #ffd55a;}
    """ )

    # display the body
    ui.body.show()

# hide insertion elements
def hideInsertionElements(ui):
    # remove the style of the insertion label
    ui.label_insertion.setStyleSheet(
    """
        #label_insertion {   border-top-left-radius: 40px;
                            border-top-right-radius: 40px;
                            color: white;   }

        #label_insertion:hover {    background-color: #ffd55a;  }
    """ )

    # hidding body of insertion
    ui.body_insertion.hide()

# hide the real time elements
def hideRealTimeElements(ui):
    # remove the style of the real time label
    ui.label_realtime.setStyleSheet(
    """
        #label_realtime {   border-top-left-radius: 40px;
                            border-top-right-radius: 40px;
                            color: white;   }

        #label_realtime:hover {    background-color: #ffd55a;  }
    """ )

    # hidding body of real time
    ui.body.hide()

# read an image
def read_image(image_path):
    image = cv2.imread(image_path)
    return image

# SHow a frame 
def show_image(image_place, image):
    if image is not None:

        if len(image.shape) == 2:  # Grayscale image
            height, width = image.shape
            bytesPerLine = width * 1  # Grayscale image has only 1 channel
            qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_Grayscale8)
        elif len(image.shape) == 3:  # RGB image
            height, width, channel = image.shape
            bytesPerLine = width * channel
            qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)

        pixmap = QPixmap.fromImage(qImg)
        image_place.setPixmap(pixmap)

    
# extracting the land marks of the hand
def extract_landmarks(image, results, mpDraw, mpHands):
    # Extraction des dimensions de l'image
    h, w, c = image.shape
    # Initialisation du tableau pour stocker les coordonnées des landmarks
    landmarks_array = []
    
    # Vérification de la présence de landmarks pour plusieurs mains dans les résultats
    if results.multi_hand_landmarks:
        # Boucle à travers les landmarks de chaque main détectée
        for hand_landmarks in results.multi_hand_landmarks:
            
            # Extraction des coordonnées des landmarks
            landmarks = hand_landmarks.landmark
            landmarks_row = []
            
            # Boucle à travers chaque landmark
            for landmark in landmarks:
                # Stockage des coordonnées des landmarks dans le tableau
                landmarks_row.extend([landmark.x*w, landmark.y*h, landmark.z*c])
                
                # Dessin d'un cercle pour représenter chaque landmark sur l'image
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                cv2.circle(image, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                
            # Stockage des coordonnées des landmarks de la main dans le tableau principal
            landmarks_array.append(landmarks_row)
        
            # Dessin des connexions entre les landmarks de la main sur l'image
            mpDraw.draw_landmarks(image, hand_landmarks, mpHands.HAND_CONNECTIONS)
        
        # Traitement du nombre de mains détectées
        vector_landmarks = []
        nom_hands = len(results.multi_hand_landmarks)
        
        # Ajout d'informations supplémentaires au tableau des landmarks en fonction du nombre de mains détectées
        if nom_hands == 1:
            landmarks_array[0].append(0)
            landmarks_array.append([0] * 63)
        elif nom_hands == 2:
            landmarks_array[0].append(1)
            
        # Retour de l'image avec les landmarks dessinés et des coordonnées des landmarks
        return image,np.array([ landmarks_array[0]+landmarks_array[1] ]).flatten()
    else:
        # Si aucun landmark n'est détecté, retourne None
        return None

