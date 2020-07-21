# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'video.ui'
# Created by: PyQt5 UI code generator 5.5.1

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1272, 838)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1121, 631))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label.setObjectName("label")
        self.OpenVideo = QtWidgets.QPushButton(Form)
        self.OpenVideo.setGeometry(QtCore.QRect(1140, 20, 99, 27))
        self.OpenVideo.setObjectName("OpenVideo")
        self.OpenCamera = QtWidgets.QPushButton(Form)
        self.OpenCamera.setGeometry(QtCore.QRect(1140, 60, 99, 27))
        self.OpenCamera.setObjectName("OpenCamera")
        self.NumofObject = QtWidgets.QLineEdit(Form)
        self.NumofObject.setGeometry(QtCore.QRect(960, 790, 111, 31))
        self.NumofObject.setFocusPolicy(QtCore.Qt.NoFocus)
        self.NumofObject.setObjectName("NumofObject")
        self.Num = QtWidgets.QLabel(Form)
        self.Num.setGeometry(QtCore.QRect(960, 760, 111, 31))
        self.Num.setObjectName("Num")
        self.Position_x = QtWidgets.QLabel(Form)
        self.Position_x.setGeometry(QtCore.QRect(960, 710, 111, 31))
        self.Position_x.setObjectName("Position_x")
        self.Position_y = QtWidgets.QLabel(Form)
        self.Position_y.setGeometry(QtCore.QRect(960, 740, 111, 31))
        self.Position_y.setObjectName("Position_y")
        self.quitButton = QtWidgets.QPushButton(Form)
        self.quitButton.setGeometry(QtCore.QRect(1140, 790, 111, 31))
        self.quitButton.setObjectName("quitButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(490, 670, 401, 151))
        self.label_2.setObjectName("label_2")
        self.net_info_box = QtWidgets.QGroupBox(Form)
        self.net_info_box.setGeometry(QtCore.QRect(1140, 100, 131, 531))
        self.net_info_box.setObjectName("net_info_box")
        self.lineEdit_local_ip = QtWidgets.QLineEdit(self.net_info_box)
        self.lineEdit_local_ip.setGeometry(QtCore.QRect(0, 50, 113, 31))
        self.lineEdit_local_ip.setObjectName("lineEdit_local_ip")
        self.label_local_IP = QtWidgets.QLabel(self.net_info_box)
        self.label_local_IP.setGeometry(QtCore.QRect(0, 20, 81, 31))
        self.label_local_IP.setObjectName("label_local_IP")
        self.label_local_Port = QtWidgets.QLabel(self.net_info_box)
        self.label_local_Port.setGeometry(QtCore.QRect(0, 80, 81, 31))
        self.label_local_Port.setObjectName("label_local_Port")
        self.lineEdit_local_port = QtWidgets.QLineEdit(self.net_info_box)
        self.lineEdit_local_port.setGeometry(QtCore.QRect(0, 110, 113, 31))
        self.lineEdit_local_port.setObjectName("lineEdit_local_port")
        self.label_RSU_IP = QtWidgets.QLabel(self.net_info_box)
        self.label_RSU_IP.setGeometry(QtCore.QRect(0, 180, 81, 31))
        self.label_RSU_IP.setObjectName("label_RSU_IP")
        self.lineEdit_rsu_ip = QtWidgets.QLineEdit(self.net_info_box)
        self.lineEdit_rsu_ip.setGeometry(QtCore.QRect(0, 210, 113, 31))
        self.lineEdit_rsu_ip.setObjectName("lineEdit_rsu_ip")
        self.label_RSU_Port = QtWidgets.QLabel(self.net_info_box)
        self.label_RSU_Port.setGeometry(QtCore.QRect(0, 240, 81, 31))
        self.label_RSU_Port.setObjectName("label_RSU_Port")
        self.lineEdit_rsu_port = QtWidgets.QLineEdit(self.net_info_box)
        self.lineEdit_rsu_port.setGeometry(QtCore.QRect(0, 270, 113, 31))
        self.lineEdit_rsu_port.setObjectName("lineEdit_rsu_port")
        self.get_ip_Button = QtWidgets.QPushButton(self.net_info_box)
        self.get_ip_Button.setGeometry(QtCore.QRect(0, 150, 111, 31))
        self.get_ip_Button.setObjectName("get_ip_Button")
        self.lineEdit_cam_port = QtWidgets.QLineEdit(self.net_info_box)
        self.lineEdit_cam_port.setGeometry(QtCore.QRect(0, 390, 113, 31))
        self.lineEdit_cam_port.setObjectName("lineEdit_cam_port")
        self.label_Cam_IP = QtWidgets.QLabel(self.net_info_box)
        self.label_Cam_IP.setGeometry(QtCore.QRect(0, 300, 81, 31))
        self.label_Cam_IP.setObjectName("label_Cam_IP")
        self.lineEdit_cam_ip = QtWidgets.QLineEdit(self.net_info_box)
        self.lineEdit_cam_ip.setGeometry(QtCore.QRect(0, 330, 113, 31))
        self.lineEdit_cam_ip.setObjectName("lineEdit_cam_ip")
        self.label_Cam_Port = QtWidgets.QLabel(self.net_info_box)
        self.label_Cam_Port.setGeometry(QtCore.QRect(0, 360, 81, 31))
        self.label_Cam_Port.setObjectName("label_Cam_Port")
        self.openudpButton = QtWidgets.QPushButton(self.net_info_box)
        self.openudpButton.setGeometry(QtCore.QRect(0, 500, 111, 31))
        self.openudpButton.setObjectName("openudpButton")
        self.coordinate_Box = QtWidgets.QGroupBox(Form)
        self.coordinate_Box.setGeometry(QtCore.QRect(10, 650, 461, 171))
        self.coordinate_Box.setObjectName("coordinate_Box")
        self.label_y_2 = QtWidgets.QLabel(self.coordinate_Box)
        self.label_y_2.setGeometry(QtCore.QRect(300, 60, 31, 31))
        self.label_y_2.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_y_2.setFont(font)
        self.label_y_2.setStyleSheet("font: 57 italic 14pt \"Ubuntu\";\n"
"font: 57 italic 11pt \"Ubuntu\";\n"
"font: 57 italic 12pt \"Ubuntu\";\n"
"font: 57 12pt \"Ubuntu\";")
        self.label_y_2.setObjectName("label_y_2")
        self.label_y_3 = QtWidgets.QLabel(self.coordinate_Box)
        self.label_y_3.setGeometry(QtCore.QRect(300, 100, 31, 31))
        self.label_y_3.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_y_3.setFont(font)
        self.label_y_3.setStyleSheet("font: 57 italic 14pt \"Ubuntu\";\n"
"font: 57 italic 11pt \"Ubuntu\";\n"
"font: 57 italic 12pt \"Ubuntu\";\n"
"font: 57 12pt \"Ubuntu\";")
        self.label_y_3.setObjectName("label_y_3")
        self.LE_UL_x = QtWidgets.QLineEdit(self.coordinate_Box)
        self.LE_UL_x.setGeometry(QtCore.QRect(180, 20, 111, 31))
        self.LE_UL_x.setInputMethodHints(QtCore.Qt.ImhNone)
        self.LE_UL_x.setObjectName("LE_UL_x")
        self.label_x_4 = QtWidgets.QLabel(self.coordinate_Box)
        self.label_x_4.setGeometry(QtCore.QRect(140, 140, 31, 31))
        self.label_x_4.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_x_4.setFont(font)
        self.label_x_4.setStyleSheet("font: 57 italic 14pt \"Ubuntu\";\n"
"font: 57 italic 11pt \"Ubuntu\";\n"
"font: 57 italic 12pt \"Ubuntu\";\n"
"font: 57 12pt \"Ubuntu\";")
        self.label_x_4.setObjectName("label_x_4")
        self.LE_DL_y = QtWidgets.QLineEdit(self.coordinate_Box)
        self.LE_DL_y.setGeometry(QtCore.QRect(340, 100, 113, 31))
        self.LE_DL_y.setObjectName("LE_DL_y")
        self.upleftPoint = QtWidgets.QPushButton(self.coordinate_Box)
        self.upleftPoint.setGeometry(QtCore.QRect(0, 20, 131, 31))
        self.upleftPoint.setObjectName("upleftPoint")
        self.LE_DL_x = QtWidgets.QLineEdit(self.coordinate_Box)
        self.LE_DL_x.setGeometry(QtCore.QRect(180, 100, 111, 31))
        self.LE_DL_x.setObjectName("LE_DL_x")
        self.label_x_3 = QtWidgets.QLabel(self.coordinate_Box)
        self.label_x_3.setGeometry(QtCore.QRect(140, 100, 31, 31))
        self.label_x_3.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_x_3.setFont(font)
        self.label_x_3.setStyleSheet("font: 57 italic 14pt \"Ubuntu\";\n"
"font: 57 italic 11pt \"Ubuntu\";\n"
"font: 57 italic 12pt \"Ubuntu\";\n"
"font: 57 12pt \"Ubuntu\";")
        self.label_x_3.setObjectName("label_x_3")
        self.downleftPoint = QtWidgets.QPushButton(self.coordinate_Box)
        self.downleftPoint.setGeometry(QtCore.QRect(0, 100, 131, 31))
        self.downleftPoint.setObjectName("downleftPoint")
        self.LE_UR_x = QtWidgets.QLineEdit(self.coordinate_Box)
        self.LE_UR_x.setGeometry(QtCore.QRect(180, 60, 111, 31))
        self.LE_UR_x.setObjectName("LE_UR_x")
        self.downrightPoint = QtWidgets.QPushButton(self.coordinate_Box)
        self.downrightPoint.setGeometry(QtCore.QRect(0, 140, 131, 31))
        self.downrightPoint.setObjectName("downrightPoint")
        self.LE_DR_x = QtWidgets.QLineEdit(self.coordinate_Box)
        self.LE_DR_x.setGeometry(QtCore.QRect(180, 140, 111, 31))
        self.LE_DR_x.setObjectName("LE_DR_x")
        self.LE_DR_y = QtWidgets.QLineEdit(self.coordinate_Box)
        self.LE_DR_y.setGeometry(QtCore.QRect(340, 140, 113, 31))
        self.LE_DR_y.setObjectName("LE_DR_y")
        self.label_y_1 = QtWidgets.QLabel(self.coordinate_Box)
        self.label_y_1.setGeometry(QtCore.QRect(300, 20, 31, 31))
        self.label_y_1.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_y_1.setFont(font)
        self.label_y_1.setStyleSheet("font: 57 italic 14pt \"Ubuntu\";\n"
"font: 57 italic 11pt \"Ubuntu\";\n"
"font: 57 italic 12pt \"Ubuntu\";\n"
"font: 57 12pt \"Ubuntu\";")
        self.label_y_1.setObjectName("label_y_1")
        self.uprightPoint = QtWidgets.QPushButton(self.coordinate_Box)
        self.uprightPoint.setGeometry(QtCore.QRect(0, 60, 131, 31))
        self.uprightPoint.setObjectName("uprightPoint")
        self.LE_UL_y = QtWidgets.QLineEdit(self.coordinate_Box)
        self.LE_UL_y.setGeometry(QtCore.QRect(340, 20, 113, 31))
        self.LE_UL_y.setObjectName("LE_UL_y")
        self.label_x_1 = QtWidgets.QLabel(self.coordinate_Box)
        self.label_x_1.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_x_1.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_x_1.setFont(font)
        self.label_x_1.setStyleSheet("font: 57 italic 14pt \"Ubuntu\";\n"
"font: 57 italic 11pt \"Ubuntu\";\n"
"font: 57 italic 12pt \"Ubuntu\";\n"
"font: 57 12pt \"Ubuntu\";")
        self.label_x_1.setObjectName("label_x_1")
        self.LE_UR_y = QtWidgets.QLineEdit(self.coordinate_Box)
        self.LE_UR_y.setGeometry(QtCore.QRect(340, 60, 113, 31))
        self.LE_UR_y.setObjectName("LE_UR_y")
        self.label_x_2 = QtWidgets.QLabel(self.coordinate_Box)
        self.label_x_2.setGeometry(QtCore.QRect(140, 60, 31, 31))
        self.label_x_2.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_x_2.setFont(font)
        self.label_x_2.setStyleSheet("font: 57 italic 14pt \"Ubuntu\";\n"
"font: 57 italic 11pt \"Ubuntu\";\n"
"font: 57 italic 12pt \"Ubuntu\";\n"
"font: 57 12pt \"Ubuntu\";")
        self.label_x_2.setObjectName("label_x_2")
        self.label_y_4 = QtWidgets.QLabel(self.coordinate_Box)
        self.label_y_4.setGeometry(QtCore.QRect(300, 140, 31, 31))
        self.label_y_4.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_y_4.setFont(font)
        self.label_y_4.setStyleSheet("font: 57 italic 14pt \"Ubuntu\";\n"
"font: 57 italic 11pt \"Ubuntu\";\n"
"font: 57 italic 12pt \"Ubuntu\";\n"
"font: 57 12pt \"Ubuntu\";")
        self.label_y_4.setObjectName("label_y_4")
        self.downloadConfigButton = QtWidgets.QPushButton(Form)
        self.downloadConfigButton.setGeometry(QtCore.QRect(1140, 710, 111, 31))
        self.downloadConfigButton.setObjectName("downloadConfigButton")
        self.uploadConfigButton = QtWidgets.QPushButton(Form)
        self.uploadConfigButton.setGeometry(QtCore.QRect(1140, 750, 111, 31))
        self.uploadConfigButton.setObjectName("uploadConfigButton")
        self.Clear_XY = QtWidgets.QPushButton(Form)
        self.Clear_XY.setGeometry(QtCore.QRect(960, 670, 111, 31))
        self.Clear_XY.setObjectName("Clear_XY")
        self.SensorID = QtWidgets.QLineEdit(Form)
        self.SensorID.setGeometry(QtCore.QRect(560, 630, 221, 31))
        self.SensorID.setObjectName("SensorID")
        self.sensor_id = QtWidgets.QLabel(Form)
        self.sensor_id.setGeometry(QtCore.QRect(490, 630, 71, 31))
        self.sensor_id.setObjectName("sensor_id")
        self.coordinate_Box.raise_()
        self.label.raise_()
        self.OpenVideo.raise_()
        self.OpenCamera.raise_()
        self.NumofObject.raise_()
        self.Num.raise_()
        self.Position_x.raise_()
        self.Position_y.raise_()
        self.quitButton.raise_()
        self.label_2.raise_()
        self.net_info_box.raise_()
        self.downloadConfigButton.raise_()
        self.uploadConfigButton.raise_()
        self.Clear_XY.raise_()
        self.SensorID.raise_()
        self.sensor_id.raise_()

        Form.setFixedSize(1272, 838)
        Form.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        # 限制输入
        reg = QtCore.QRegExp("^(\-|\+)?[0-9]*\.[0-9]*$")
        validator = QtGui.QRegExpValidator(reg)
        self.LE_UL_x.setValidator(validator)
        self.LE_UL_y.setValidator(validator)
        self.LE_UR_x.setValidator(validator)
        self.LE_UR_y.setValidator(validator)
        self.LE_DR_x.setValidator(validator)
        self.LE_DR_y.setValidator(validator)
        self.LE_DL_x.setValidator(validator)
        self.LE_DL_y.setValidator(validator)
        sensor_id_reg = QtCore.QRegExp("^[a-zA-Z0-9_]{16}$")
        sensor_id_validator = QtGui.QRegExpValidator(sensor_id_reg)
        self.SensorID.setValidator(sensor_id_validator)
        self.lineEdit_local_ip.setInputMask('000.000.000.000')
        self.lineEdit_rsu_ip.setInputMask('000.000.000.000')
        self.lineEdit_cam_ip.setInputMask('000.000.000.000')
        reg_port = QtCore.QRegExp("[0-9]{10}$")
        validator_port = QtGui.QRegExpValidator(reg_port)
        self.lineEdit_local_port.setValidator(validator_port)
        self.lineEdit_rsu_port.setValidator(validator_port)
        self.lineEdit_cam_port.setValidator(validator_port)
        # Form.setCurrentIndex(0)
        # 将按键与事件相连
        self.OpenVideo.clicked.connect(Form.video_processing)
        self.OpenCamera.clicked.connect(Form.camera_processing)
        self.upleftPoint.clicked.connect(Form.addUL)
        self.uprightPoint.clicked.connect(Form.addUR)
        self.downleftPoint.clicked.connect(Form.addDL)
        self.downrightPoint.clicked.connect(Form.addDR)
        self.downloadConfigButton.clicked.connect(Form.down_load_config)
        self.uploadConfigButton.clicked.connect(Form.up_load_config)
        self.get_ip_Button.clicked.connect(Form.get_ip)
        self.openudpButton.clicked.connect(Form.udp_sender_switch)
        self.Clear_XY.clicked.connect(Form.clear_xy)
        self.quitButton.clicked.connect(Form.quit)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Detection"))
        self.label.setText(_translate("Form", "video_here"))
        self.OpenVideo.setText(_translate("Form", "OpenVideo"))
        self.OpenCamera.setText(_translate("Form", "OpenCamera"))
        self.NumofObject.setText(_translate("Form", "0"))
        self.Num.setText(_translate("Form", "NumofObject"))
        self.Position_x.setText(_translate("Form", "0"))
        self.Position_y.setText(_translate("Form", "0"))
        self.quitButton.setText(_translate("Form", "Quit"))
        self.label_2.setText(_translate("Form", "result_here"))
        self.net_info_box.setTitle(_translate("Form", "Net_Info"))
        self.lineEdit_local_ip.setText(_translate("Form", "127.0.0.1"))
        self.label_local_IP.setText(_translate("Form", "Local_IP"))
        self.label_local_Port.setText(_translate("Form", "Local_Port"))
        self.lineEdit_local_port.setText(_translate("Form", "10000"))
        self.label_RSU_IP.setText(_translate("Form", "RSU_IP"))
        self.lineEdit_rsu_ip.setText(_translate("Form", "127.0.0.1"))
        self.label_RSU_Port.setText(_translate("Form", "RSU_Port"))
        self.lineEdit_rsu_port.setText(_translate("Form", "10000"))
        self.get_ip_Button.setText(_translate("Form", "get_local_IP"))
        self.lineEdit_cam_port.setText(_translate("Form", "10000"))
        self.label_Cam_IP.setText(_translate("Form", "Cam_IP"))
        self.lineEdit_cam_ip.setText(_translate("Form", "127.0.0.1"))
        self.label_Cam_Port.setText(_translate("Form", "Cam_Port"))
        self.openudpButton.setText(_translate("Form", "Close UDP"))
        self.coordinate_Box.setTitle(_translate("Form", "Coordinate"))
        self.label_y_2.setText(_translate("Form", "lat ="))
        self.label_y_3.setText(_translate("Form", "lat ="))
        self.LE_UL_x.setText(_translate("Form", "0"))
        self.label_x_4.setText(_translate("Form", "lon ="))
        self.LE_DL_y.setText(_translate("Form", "150"))
        self.upleftPoint.setText(_translate("Form", "upleftPoint"))
        self.LE_DL_x.setText(_translate("Form", "0"))
        self.label_x_3.setText(_translate("Form", "lon ="))
        self.downleftPoint.setText(_translate("Form", "downleftPoint"))
        self.LE_UR_x.setText(_translate("Form", "400"))
        self.downrightPoint.setText(_translate("Form", "downrightPoint"))
        self.LE_DR_x.setText(_translate("Form", "400"))
        self.LE_DR_y.setText(_translate("Form", "150"))
        self.label_y_1.setText(_translate("Form", "lat ="))
        self.uprightPoint.setText(_translate("Form", "uprightPoint"))
        self.LE_UL_y.setText(_translate("Form", "0"))
        self.label_x_1.setText(_translate("Form", "lon ="))
        self.LE_UR_y.setText(_translate("Form", "0"))
        self.label_x_2.setText(_translate("Form", "lon ="))
        self.label_y_4.setText(_translate("Form", "lat ="))
        self.downloadConfigButton.setText(_translate("Form", "DownLoadCfg"))
        self.uploadConfigButton.setText(_translate("Form", "UpLoadCfg"))
        self.Clear_XY.setText(_translate("Form", "clear point"))
        self.SensorID.setText(_translate("Form", "SensorID_need_16"))
        self.sensor_id.setText(_translate("Form", "Sensor ID"))