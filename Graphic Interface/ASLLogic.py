import sys
from PyQt5 import QtWidgets # type: ignore
from ASLApplication import Ui_principal_window
from ASLTraitments import *
import cv2 # type: ignore
import joblib # type: ignore
import mediapipe as mp # type: ignore
import numpy as np # type: ignore
import pandas as pd # type: ignore
from PyQt5.QtWidgets import QFileDialog # type: ignore

# loading the trained model
svm_model_loaded = joblib.load('./../asl_svm_model.pkl')

mpHands = mp.solutions.hands  # Importation du modèle de détection des mains
hands = mpHands.Hands()  # Initialisation du détecteur de mains
mpDraw = mp.solutions.drawing_utils  # Utilitaire pour dessiner les landmarks des mains


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_principal_window()
        self.ui.setupUi(self)

        # class variables
        self.cap = None
        self.sentence = ""
        self.previousLettre = ""

        # here we can add click events

        # click event of insertion
        self.ui.label_insertion.mousePressEvent = self.switchToInsertion

        # click event of real time
        self.ui.label_realtime.mousePressEvent = self.switchToRealTime

        # click event of openwebcam
        self.ui.open_webcam.clicked.connect(self.openWebCam)

        # click event of select image button
        self.ui.select_image.clicked.connect(self.upload_image)

        # delete the sentence
        self.ui.clear_text.clicked.connect(self.clearText)
    
    
    # functions to handle click events
    
    # handle click event of insrtion
    def switchToInsertion(self, event):
        print("insertion")
        displayInsertionElements(self.ui)
        hideRealTimeElements(self.ui)
        
        # Libération des ressources si on a déjà ouvrire le webcam
        if self.cap is not None:
            self.cap.release()
            cv2.destroyAllWindows()
            self.ui.image_place.clear()

    # handle click event of real time
    def switchToRealTime(self, event):
        print("real time")
        displayRealTimeElements(self.ui)
        hideInsertionElements(self.ui)

    
    # to handle open webcam
    def openWebCam(self, event):
        print("opening webcam")

        # Capture vidéo en direct à partir de la webcam (index 0)
        self.cap = cv2.VideoCapture(0)

        # Taille désirée pour la webcam
        webcam_width, webcam_height = 400, 400

        # Ajustement de la taille de la webcam
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, webcam_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, webcam_height)
        self.getFramesWithLandMarks(self.cap)


    # getting the webcam frames and extracting the landmarks than drawing them on the hand 
    def getFramesWithLandMarks(self, cap):

        while True:
            ret, frame = cap.read()  # Lecture d'une image de la webcam

            if not ret:
                break  # Sortir de la boucle si la lecture de la webcam échoue
                
            results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB).astype(np.uint8))  # Traitement de l'image pour détecter les mains

            if results.multi_hand_landmarks:  # Si des landmarks de main sont détectés
                print("extracting ")
                frame_marked, landmarks = extract_landmarks(frame, results, mpDraw, mpHands)  # Extraction et dessin des landmarks de la main
                
                header =[f'ld_1_{i}' for i in range(1, 64)] + ['o_h'] + [f'ld_2_{i}' for i in range(1, 64)]
                landmarks_dataframe = pd.DataFrame([landmarks], columns=header)  # Conversion des landmarks en DataFrame
                class_ = svm_model_loaded.predict(landmarks_dataframe)  # Prédiction de la classe du geste de la main
                
                # Affichage de la classe prédite en haut de l'image
                self.ui.label_current_sign.setText(class_[0])
                self.addLettre(class_[0])

                # resizing thee frame to be compatible with the interface
                frame_marked = cv2.resize(frame_marked, (300,300), interpolation=cv2.INTER_AREA)

                show_image(self.ui.image_place, frame_marked)
                
            else:
                # resizing thee frame to be compatible with the interface
                frame = cv2.resize(frame, (300,300), interpolation=cv2.INTER_AREA)

                # Affichage de _ en haut de l'image
                self.ui.label_current_sign.setText("_")
                show_image(self.ui.image_place, frame)

            # Quitter la boucle si la touche 'q' est enfoncée
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def clearText(self):
        print("clear text")
        self.sentence = ""
        self.ui.sentence_result.setText("")

    def addLettre(self,lettre):
        print("add lettre")
        if lettre != self.previousLettre:
            if lettre.lower() == "espace":
                self.sentence = self.sentence+" "
            else:
                self.sentence = self.sentence + lettre

            self.previousLettre = lettre
            self.ui.sentence_result.setText(self.sentence)
        
            
    def upload_image(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp *.tif)")
        file_dialog.setViewMode(QFileDialog.Detail)
        if file_dialog.exec_():
            original_image_path = file_dialog.selectedFiles()[0]
            original_image = read_image(original_image_path)

            results = hands.process(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB).astype(np.uint8))  # Traitement de l'image pour détecter les mains
            original_image, landmarks = extract_landmarks(original_image, results, mpDraw, mpHands)  # Extraction et dessin des landmarks de la main
            
            header =[f'ld_1_{i}' for i in range(1, 64)] + ['o_h'] + [f'ld_2_{i}' for i in range(1, 64)]
            landmarks_dataframe = pd.DataFrame([landmarks], columns=header)  # Conversion des landmarks en DataFrame
            class_ = svm_model_loaded.predict(landmarks_dataframe)  # Prédiction de la classe du geste de la main

            self.ui.predicted_sign_insertion.setText(class_[0])

            original_image = cv2.resize(original_image, (300,300), interpolation=cv2.INTER_AREA)
            show_image(self.ui.image_insertion,original_image)

# starting executing processus from here
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())