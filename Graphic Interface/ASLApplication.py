from PyQt5 import QtCore, QtGui, QtWidgets # type: ignore

class Ui_principal_window(object):
    
    def setupUi(self, principal_window):

        # principal window
        principal_window.setObjectName("principal_window")
        principal_window.resize(1081, 610)
        self.principal_grid_layout = QtWidgets.QWidget(principal_window)
        self.principal_grid_layout.setStyleSheet("#principal_grid_layout {\n"
                                                "    background-color: #6dd47e;\n"
                                                "}")
        
        self.principal_grid_layout.setObjectName("principal_grid_layout")

        # virtical layout for the principal window
        self.verticalLayout = QtWidgets.QVBoxLayout(self.principal_grid_layout)
        self.verticalLayout.setContentsMargins(0, 0, 0, 45)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        # top part of the principal window
        self.top_part_layout = QtWidgets.QWidget(self.principal_grid_layout)
        self.top_part_layout.setStyleSheet("#top_part_layout {\n"
                                                "    max-height: 50px;\n"
                                                "}")
        self.top_part_layout.setObjectName("top_part_layout")

        # its horizantal layout
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_part_layout)
        self.horizontalLayout.setContentsMargins(20, 9, 20, 0)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # the left label of the top part of the principal window
        self.label_insertion = QtWidgets.QLabel(self.top_part_layout)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_insertion.setFont(font)
        self.label_insertion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_insertion.setStyleSheet("#label_insertion {\n"
                                                "    border-top-left-radius: 40px;\n"
                                                "    border-top-right-radius: 40px;\n"
                                                "    color: white;\n"
                                                "}\n"
                                                "\n"
                                                "#label_insertion:hover {\n"
                                                "    background-color: #ffd55a;\n"
                                                "}")
        self.label_insertion.setAlignment(QtCore.Qt.AlignCenter)
        self.label_insertion.setObjectName("label_insertion")
        self.horizontalLayout.addWidget(self.label_insertion)

        # label real time
        self.label_realtime = QtWidgets.QLabel(self.top_part_layout)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_realtime.setFont(font)
        self.label_realtime.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_realtime.setStyleSheet("#label_realtime {\n"
                                        "    background-color: #ffd55a;\n"
                                        "    border-top-left-radius: 40px;\n"
                                        "    border-top-right-radius: 40px;\n"
                                        "    color: white;\n"
                                        "}\n"
                                        "\n"
                                        "#label_realtime:hover {\n"
                                        "    background-color: #ffd55a;\n"
                                        "}")
        self.label_realtime.setAlignment(QtCore.Qt.AlignCenter)
        self.label_realtime.setObjectName("label_realtime")
        self.horizontalLayout.addWidget(self.label_realtime)

        # adding the top part to the vertical layout of the principal layout
        self.verticalLayout.addWidget(self.top_part_layout)

        # center part of the principal window
        self.body = QtWidgets.QWidget(self.principal_grid_layout)
        self.body.setStyleSheet("#body {\n"
                                "    border-top: 1px solid white;\n"
                                "    background-color: rgb(248, 244, 244);\n"
                                "    border-top-left-radius: 25px;\n"
                                "    border-top-right-radius: 25px;\n"
                                "}")
        self.body.setObjectName("body")

        # its layout
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.body)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 9)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # left side of the center part of the principal window
        self.body_left_side = QtWidgets.QWidget(self.body)
        self.body_left_side.setObjectName("body_left_side")

        # its layout
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.body_left_side)
        self.verticalLayout_3.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.body_left_top_part = QtWidgets.QWidget(self.body_left_side)
        self.body_left_top_part.setStyleSheet("#body_left_top_part {\n"
                                                "    border-bottom: 1px solid black;\n"
                                                "}")
        self.body_left_top_part.setObjectName("body_left_top_part")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.body_left_top_part)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.label_sentence_explication = QtWidgets.QLabel(self.body_left_top_part)
        self.label_sentence_explication.setStyleSheet("#label_sentence_explication {\n"
                                                        "    font-size: 14px;\n"
                                                        "}")
        self.label_sentence_explication.setObjectName("label_sentence_explication")

        self.verticalLayout_4.addWidget(self.label_sentence_explication, 0, QtCore.Qt.AlignBottom)

        self.verticalLayout_3.addWidget(self.body_left_top_part) #

        self.body_left_center_part = QtWidgets.QWidget(self.body_left_side)
        self.body_left_center_part.setObjectName("body_left_center_part")

        self.sentence_result = QtWidgets.QTextEdit(self.body_left_center_part)
        self.sentence_result.setEnabled(True)
        self.sentence_result.setGeometry(QtCore.QRect(20, 0, 451, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sentence_result.setFont(font)
        self.sentence_result.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sentence_result.setStyleSheet("#sentence_result {\n"
                                        "    font-size: 14px;\n"
                                        "    font-weight: bold;\n"
                                        "}")
        self.sentence_result.setObjectName("sentence_result")

        self.verticalLayout_3.addWidget(self.body_left_center_part) #

        self.body_left_bottom_part = QtWidgets.QWidget(self.body_left_side)
        self.body_left_bottom_part.setStyleSheet("#body_left_bottom_part{\n"
                                                "    border-top: 1px solid black;\n"
                                                "}")
        self.body_left_bottom_part.setObjectName("body_left_bottom_part")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.body_left_bottom_part)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.clear_text = QtWidgets.QPushButton(self.body_left_bottom_part)
        self.clear_text.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_text.setStyleSheet("#clear_text {\n"
                                                "    max-width: 150px;\n"
                                                "    height: 30px;\n"
                                                "    background-color: #ffd55a;\n"
                                                "    border: none;\n"
                                                "    border-radius: 5px;\n"
                                                "    color: white;\n"
                                                "    font-size:13px;\n"
                                                "}\n"
                                                "#clear_text:hover {\n"
                                                "    background-color: white;\n"
                                                "    color: #ffd55a;\n"
                                                "}")
        self.clear_text.setObjectName("clear_text")
        self.gridLayout_3.addWidget(self.clear_text, 0, 0, 1, 1)

        self.verticalLayout_3.addWidget(self.body_left_bottom_part) #

        self.horizontalLayout_2.addWidget(self.body_left_side)

        # right side of center part
        self.body_right_side = QtWidgets.QWidget(self.body)
        self.body_right_side.setStyleSheet("#body_right_side {\n"
                                        "    border-left: 1px solid black;\n"
                                        "}")
        self.body_right_side.setObjectName("body_right_side")

        # its layout
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.body_right_side)
        self.verticalLayout_2.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # its top part
        self.body_right_top_part = QtWidgets.QWidget(self.body_right_side)
        self.body_right_top_part.setStyleSheet("#body_right_top_part {\n"
                                                        "    max-height: 40px;\n"
                                                        "    border-bottom: 1px solid black\n"
                                                        "}")
        self.body_right_top_part.setObjectName("body_right_top_part")

        # the layout of its top part
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.body_right_top_part)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.label_current_sign_detected = QtWidgets.QLabel(self.body_right_top_part)
        self.label_current_sign_detected.setObjectName("label_current_sign_detected")
        self.horizontalLayout_4.addWidget(self.label_current_sign_detected, 0, QtCore.Qt.AlignHCenter)

        self.label_current_sign = QtWidgets.QLabel(self.body_right_top_part)
        self.label_current_sign.setObjectName("label_current_sign")
        self.horizontalLayout_4.addWidget(self.label_current_sign)

        self.verticalLayout_2.addWidget(self.body_right_top_part) # adding the top part of right side of center to the layout
        
        self.body_right_center_part = QtWidgets.QWidget(self.body_right_side)
        self.body_right_center_part.setObjectName("body_right_center_part")

        self.gridLayout = QtWidgets.QGridLayout(self.body_right_center_part)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

        self.image_place = QtWidgets.QLabel(self.body_right_center_part)
        self.image_place.setText("")
        # self.image_place.setPixmap(QtGui.QPixmap("camera.png"))
        self.image_place.setScaledContents(True)
        self.image_place.setObjectName("image_place")
        self.gridLayout.addWidget(self.image_place, 0, 0, 1, 1)

        self.verticalLayout_2.addWidget(self.body_right_center_part) # adding its center part to the layout

        self.body_right_bottom_part = QtWidgets.QWidget(self.body_right_side)
        self.body_right_bottom_part.setStyleSheet("#body_right_bottom_part {\n"
                                                        "    max-height: 60px;\n"
                                                        "    border-top: 1px solid black;\n"
                                                        "}")
        self.body_right_bottom_part.setObjectName("body_right_bottom_part")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.body_right_bottom_part)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.open_webcam = QtWidgets.QPushButton(self.body_right_bottom_part)
        self.open_webcam.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.open_webcam.setStyleSheet("#open_webcam {\n"
                                                "    max-width: 150px;\n"
                                                "    min-height: 30px;\n"
                                                "    background-color: #6dd47e;\n"
                                                "    font-size: 13px;\n"
                                                "    border: none;\n"
                                                "    color: white;\n"
                                                "    border-radius: 5px;\n"
                                                "}\n"
                                                "\n"
                                                "#open_webcam:hover {\n"
                                                "    background-color: white;\n"
                                                "    color: #6dd47e;\n"
                                                "}")
        self.open_webcam.setObjectName("open_webcam")
        self.horizontalLayout_3.addWidget(self.open_webcam)

        self.verticalLayout_2.addWidget(self.body_right_bottom_part) # adding its bottom part

        self.horizontalLayout_2.addWidget(self.body_right_side) # here we associate the horizantal layout to the center principal window 
        
        self.verticalLayout.addWidget(self.body)


        ###### insertion part ############

        
        self.body_insertion = QtWidgets.QWidget(self.principal_grid_layout)
        self.body_insertion.setStyleSheet("#body_insertion {\n"
"    border-top: 1px solid white;\n"
"    background-color: rgb(248, 244, 244);\n"
"    border-top-left-radius: 25px;\n"
"    border-top-right-radius: 25px;\n"
"}")
        self.body_insertion.setObjectName("body_insertion")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.body_insertion)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.body_insertion_top_part = QtWidgets.QWidget(self.body_insertion)
        self.body_insertion_top_part.setStyleSheet("#body_insertion_top_part {\n"
"    max-height: 40px;\n"
"    border-bottom: 1px solid black\n"
"}")
        self.body_insertion_top_part.setObjectName("body_insertion_top_part")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.body_insertion_top_part)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_predicted_sign_insertion = QtWidgets.QLabel(self.body_insertion_top_part)
        self.label_predicted_sign_insertion.setObjectName("label_predicted_sign_insertion")
        self.horizontalLayout_3.addWidget(self.label_predicted_sign_insertion, 0, QtCore.Qt.AlignHCenter)
        self.predicted_sign_insertion = QtWidgets.QLabel(self.body_insertion_top_part)
        self.predicted_sign_insertion.setObjectName("predicted_sign_insertion")
        self.horizontalLayout_3.addWidget(self.predicted_sign_insertion)
        self.verticalLayout_2.addWidget(self.body_insertion_top_part)
        self.body_insertion_center_part = QtWidgets.QWidget(self.body_insertion)
        self.body_insertion_center_part.setMaximumSize(QtCore.QSize(1500, 300))
        self.body_insertion_center_part.setStyleSheet("")
        self.body_insertion_center_part.setObjectName("body_insertion_center_part")
        self.gridLayout = QtWidgets.QGridLayout(self.body_insertion_center_part)
        self.gridLayout.setObjectName("gridLayout")
        self.image_insertion = QtWidgets.QLabel(self.body_insertion_center_part)
        self.image_insertion.setMaximumSize(QtCore.QSize(350, 300))
        self.image_insertion.setText("")
        # self.image_insertion.setPixmap(QtGui.QPixmap("file_explor.png"))
        self.image_insertion.setScaledContents(True)
        self.image_insertion.setObjectName("image_insertion")
        self.gridLayout.addWidget(self.image_insertion, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.body_insertion_center_part)
        self.body_insertion_bottom_part = QtWidgets.QWidget(self.body_insertion)
        self.body_insertion_bottom_part.setStyleSheet("#body_insertion_bottom_part {\n"
"    max-height: 60px;\n"
"    border-top: 1px solid black;\n"
"}")
        self.body_insertion_bottom_part.setObjectName("body_insertion_bottom_part")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.body_insertion_bottom_part)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.select_image = QtWidgets.QPushButton(self.body_insertion_bottom_part)
        self.select_image.setStyleSheet("#select_image {\n"
"    max-width: 150px;\n"
"    min-height: 30px;\n"
"    background-color: #ffd55a;\n"
"    font-size: 13px;\n"
"    border: none;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#select_image:hover {\n"
"    background-color: white;\n"
"    color: #ffd55a;\n"
"}")
        self.select_image.setObjectName("select_image")
        self.horizontalLayout_2.addWidget(self.select_image)
        self.verticalLayout_2.addWidget(self.body_insertion_bottom_part)
        self.verticalLayout.addWidget(self.body_insertion)
        self.body_insertion.hide()

        ###################################

        principal_window.setCentralWidget(self.principal_grid_layout)

        self.retranslateUi(principal_window)
        QtCore.QMetaObject.connectSlotsByName(principal_window)

    def retranslateUi(self, principal_window):
        _translate = QtCore.QCoreApplication.translate
        principal_window.setWindowTitle(_translate("principal_window", "American Sign Language"))
        self.label_insertion.setText(_translate("principal_window", "Insertion"))
        self.label_realtime.setText(_translate("principal_window", "Real Time"))
        self.label_sentence_explication.setText(_translate("principal_window", "Your Sentence Combination Of Your Predected Signs"))
        self.sentence_result.setHtml(_translate("principal_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14px; font-weight:600; font-style:normal;\">\n"
                                                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.clear_text.setText(_translate("principal_window", "Clear Text Zone"))
        self.label_current_sign_detected.setText(_translate("principal_window", "Current Sign Predected"))
        self.label_current_sign.setText(_translate("principal_window", "_"))
        self.open_webcam.setText(_translate("principal_window", "Open WebCam"))
        self.label_insertion.setText(_translate("principal_window", "Insertion"))
        self.label_realtime.setText(_translate("principal_window", "Real Time"))
        self.label_predicted_sign_insertion.setText(_translate("principal_window", "Predicted Sign"))
        self.predicted_sign_insertion.setText(_translate("principal_window", "_"))
        self.select_image.setText(_translate("principal_window", "Upload Image"))
        