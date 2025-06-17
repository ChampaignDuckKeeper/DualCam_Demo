# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hgui1.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGraphicsView, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1141, 691)
        MainWindow.setStyleSheet(u"background-color: #1e1e1e;")
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(16)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(15)
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.graphicsView = QGraphicsView(self.widget_5)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(7)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy2)
        self.graphicsView.setStyleSheet(u"background-color: #000000;")

        self.horizontalLayout_2.addWidget(self.graphicsView)


        self.verticalLayout.addWidget(self.widget_5)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(2)
        sizePolicy3.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy3)
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Info = QLabel(self.widget_4)
        self.Info.setObjectName(u"Info")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(10)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Info.sizePolicy().hasHeightForWidth())
        self.Info.setSizePolicy(sizePolicy4)
        self.Info.setMinimumSize(QSize(0, 20))
        self.Info.setStyleSheet(u"font-size: 18px; background-color: #3c3f41; color: #ffffff; padding-left: 10px;")

        self.gridLayout_3.addWidget(self.Info, 1, 0, 1, 1)

        self.fps_label = QLabel(self.widget_4)
        self.fps_label.setObjectName(u"fps_label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.fps_label.sizePolicy().hasHeightForWidth())
        self.fps_label.setSizePolicy(sizePolicy5)
        self.fps_label.setMinimumSize(QSize(0, 20))
        self.fps_label.setStyleSheet(u"font-size: 10px; background-color: #3c3f41; color: #ffffff; padding-left: 10px;")

        self.gridLayout_3.addWidget(self.fps_label, 1, 1, 1, 1)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy6)
        self.widget_6.setStyleSheet(u"background-color: #888888;")
        self.gridLayout = QGridLayout(self.widget_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(2)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy7)
        self.widget_8.setSizeIncrement(QSize(0, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.EN_AutoAF = QCheckBox(self.widget_8)
        self.EN_AutoAF.setObjectName(u"EN_AutoAF")
        self.EN_AutoAF.setChecked(True)

        self.horizontalLayout_3.addWidget(self.EN_AutoAF)


        self.gridLayout.addWidget(self.widget_8, 0, 0, 1, 1)

        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(10)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy8)
        self.widget_7.setSizeIncrement(QSize(0, 0))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.widget_7)
        self.label_7.setObjectName(u"label_7")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(1)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy9)
        self.label_7.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.s_TargetPL = QSlider(self.widget_7)
        self.s_TargetPL.setObjectName(u"s_TargetPL")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(8)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.s_TargetPL.sizePolicy().hasHeightForWidth())
        self.s_TargetPL.setSizePolicy(sizePolicy10)
        self.s_TargetPL.setMinimum(0)
        self.s_TargetPL.setMaximum(959)
        self.s_TargetPL.setValue(440)
        self.s_TargetPL.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_5.addWidget(self.s_TargetPL)

        self.t_TargetPL = QLineEdit(self.widget_7)
        self.t_TargetPL.setObjectName(u"t_TargetPL")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(1)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.t_TargetPL.sizePolicy().hasHeightForWidth())
        self.t_TargetPL.setSizePolicy(sizePolicy11)
        self.t_TargetPL.setStyleSheet(u"background-color: #ffffff;")

        self.horizontalLayout_5.addWidget(self.t_TargetPL)


        self.gridLayout.addWidget(self.widget_7, 0, 2, 1, 1)

        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy8.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy8)
        self.widget_9.setSizeIncrement(QSize(0, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.widget_9)
        self.label_6.setObjectName(u"label_6")
        sizePolicy9.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy9)
        self.label_6.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.s_Pose = QSlider(self.widget_9)
        self.s_Pose.setObjectName(u"s_Pose")
        sizePolicy10.setHeightForWidth(self.s_Pose.sizePolicy().hasHeightForWidth())
        self.s_Pose.setSizePolicy(sizePolicy10)
        self.s_Pose.setMinimum(200)
        self.s_Pose.setMaximum(1000)
        self.s_Pose.setValue(200)
        self.s_Pose.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_4.addWidget(self.s_Pose)

        self.t_Pose = QLineEdit(self.widget_9)
        self.t_Pose.setObjectName(u"t_Pose")
        sizePolicy11.setHeightForWidth(self.t_Pose.sizePolicy().hasHeightForWidth())
        self.t_Pose.setSizePolicy(sizePolicy11)
        self.t_Pose.setStyleSheet(u"background-color: #ffffff;")

        self.horizontalLayout_4.addWidget(self.t_Pose)


        self.gridLayout.addWidget(self.widget_9, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.widget_6, 0, 0, 1, 2)


        self.verticalLayout.addWidget(self.widget_4)


        self.horizontalLayout.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy12.setHorizontalStretch(2)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy12)
        self.widget_2.setStyleSheet(u"css\n"
"background-color: #000000;  /* \u80cc\u666f\u8272 */\n"
"border: 1px solid #555;     /* \u8fb9\u6846 */\n"
"border-radius: 5px;         /* \u5706\u89d2 */")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy13)
        self.label_4.setMinimumSize(QSize(0, 20))
        self.label_4.setStyleSheet(u"font-size: 18px; background-color: #3c3f41; color: #ffffff; padding-left: 10px;")

        self.gridLayout_2.addWidget(self.label_4, 11, 0, 1, 2)

        self.disp_Scene1 = QPushButton(self.widget_2)
        self.disp_Scene1.setObjectName(u"disp_Scene1")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(2)
        sizePolicy14.setHeightForWidth(self.disp_Scene1.sizePolicy().hasHeightForWidth())
        self.disp_Scene1.setSizePolicy(sizePolicy14)
        self.disp_Scene1.setStyleSheet(u"font-size: 16px; background-color: #4a4a4a; color: black;")

        self.gridLayout_2.addWidget(self.disp_Scene1, 1, 0, 1, 2)

        self.disp_Compare = QPushButton(self.widget_2)
        self.disp_Compare.setObjectName(u"disp_Compare")
        sizePolicy14.setHeightForWidth(self.disp_Compare.sizePolicy().hasHeightForWidth())
        self.disp_Compare.setSizePolicy(sizePolicy14)
        self.disp_Compare.setStyleSheet(u"font-size: 16px; background-color: #1b657c; color: black;")

        self.gridLayout_2.addWidget(self.disp_Compare, 3, 0, 1, 2)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy13.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy13)
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setStyleSheet(u"font-size: 18px; background-color: #3c3f41; color: #ffffff; padding-left: 10px;")

        self.gridLayout_2.addWidget(self.label_2, 6, 0, 1, 2)

        self.b_zoom_in = QPushButton(self.widget_2)
        self.b_zoom_in.setObjectName(u"b_zoom_in")
        sizePolicy15 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy15.setHorizontalStretch(2)
        sizePolicy15.setVerticalStretch(1)
        sizePolicy15.setHeightForWidth(self.b_zoom_in.sizePolicy().hasHeightForWidth())
        self.b_zoom_in.setSizePolicy(sizePolicy15)
        self.b_zoom_in.setStyleSheet(u"font-size: 14px; background-color: #4a4a4a; color: black;")

        self.gridLayout_2.addWidget(self.b_zoom_in, 7, 0, 1, 1)

        self.b_reset = QPushButton(self.widget_2)
        self.b_reset.setObjectName(u"b_reset")
        sizePolicy16 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy16.setHorizontalStretch(1)
        sizePolicy16.setVerticalStretch(1)
        sizePolicy16.setHeightForWidth(self.b_reset.sizePolicy().hasHeightForWidth())
        self.b_reset.setSizePolicy(sizePolicy16)
        self.b_reset.setStyleSheet(u"font-size: 14px; background-color: #4a4a4a; color: black;")

        self.gridLayout_2.addWidget(self.b_reset, 8, 0, 1, 2)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy13.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy13)
        self.label_3.setMinimumSize(QSize(0, 20))
        self.label_3.setStyleSheet(u"font-size: 18px; background-color: #3c3f41; color: #ffffff; padding-left: 10px;")

        self.gridLayout_2.addWidget(self.label_3, 9, 0, 1, 2)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy13.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy13)
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setStyleSheet(u"font-size: 18px; background-color: #3c3f41; color: #ffffff; padding-left: 10px;")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)

        self.disp_RAW = QPushButton(self.widget_2)
        self.disp_RAW.setObjectName(u"disp_RAW")
        sizePolicy14.setHeightForWidth(self.disp_RAW.sizePolicy().hasHeightForWidth())
        self.disp_RAW.setSizePolicy(sizePolicy14)
        self.disp_RAW.setStyleSheet(u"font-size: 16px; background-color: #751617; color: black;")

        self.gridLayout_2.addWidget(self.disp_RAW, 4, 0, 1, 2)

        self.disp_Scene2 = QPushButton(self.widget_2)
        self.disp_Scene2.setObjectName(u"disp_Scene2")
        sizePolicy14.setHeightForWidth(self.disp_Scene2.sizePolicy().hasHeightForWidth())
        self.disp_Scene2.setSizePolicy(sizePolicy14)
        self.disp_Scene2.setStyleSheet(u"font-size: 16px; background-color: #8a1d7b; color: black;")

        self.gridLayout_2.addWidget(self.disp_Scene2, 2, 0, 1, 2)

        self.b_zoom_out = QPushButton(self.widget_2)
        self.b_zoom_out.setObjectName(u"b_zoom_out")
        sizePolicy15.setHeightForWidth(self.b_zoom_out.sizePolicy().hasHeightForWidth())
        self.b_zoom_out.setSizePolicy(sizePolicy15)
        self.b_zoom_out.setStyleSheet(u"font-size: 14px; background-color: #4a4a4a; color: black;")

        self.gridLayout_2.addWidget(self.b_zoom_out, 7, 1, 1, 1)

        self.disp_MIS = QPushButton(self.widget_2)
        self.disp_MIS.setObjectName(u"disp_MIS")
        sizePolicy14.setHeightForWidth(self.disp_MIS.sizePolicy().hasHeightForWidth())
        self.disp_MIS.setSizePolicy(sizePolicy14)
        self.disp_MIS.setStyleSheet(u"font-size: 16px; background-color: #8c11a5; color: black;")

        self.gridLayout_2.addWidget(self.disp_MIS, 5, 0, 1, 2)

        self.B_Stream_on = QPushButton(self.widget_2)
        self.B_Stream_on.setObjectName(u"B_Stream_on")
        sizePolicy14.setHeightForWidth(self.B_Stream_on.sizePolicy().hasHeightForWidth())
        self.B_Stream_on.setSizePolicy(sizePolicy14)
        self.B_Stream_on.setStyleSheet(u"font-size: 16px; background-color: #606060; color: black;")

        self.gridLayout_2.addWidget(self.B_Stream_on, 12, 0, 1, 2)

        self.widget_10 = QWidget(self.widget_2)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy17 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy17.setHorizontalStretch(1)
        sizePolicy17.setVerticalStretch(2)
        sizePolicy17.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy17)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Capture_all = QPushButton(self.widget_10)
        self.Capture_all.setObjectName(u"Capture_all")
        sizePolicy18 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy18.setHorizontalStretch(4)
        sizePolicy18.setVerticalStretch(2)
        sizePolicy18.setHeightForWidth(self.Capture_all.sizePolicy().hasHeightForWidth())
        self.Capture_all.setSizePolicy(sizePolicy18)
        self.Capture_all.setStyleSheet(u"font-size: 18px; background-color: #395d39; color: black;")

        self.horizontalLayout_6.addWidget(self.Capture_all)

        self.Burst = QPushButton(self.widget_10)
        self.Burst.setObjectName(u"Burst")
        sizePolicy19 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy19.setHorizontalStretch(3)
        sizePolicy19.setVerticalStretch(2)
        sizePolicy19.setHeightForWidth(self.Burst.sizePolicy().hasHeightForWidth())
        self.Burst.setSizePolicy(sizePolicy19)
        font = QFont()
        self.Burst.setFont(font)
        self.Burst.setStyleSheet(u"font-size: 18px; background-color: #395d39; color: black;")

        self.horizontalLayout_6.addWidget(self.Burst)


        self.gridLayout_2.addWidget(self.widget_10, 10, 0, 1, 2)


        self.horizontalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.EN_AutoAF.setText(QCoreApplication.translate("MainWindow", u"AF/AEC", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Target\n"
"Brightness", None))
        self.t_TargetPL.setText(QCoreApplication.translate("MainWindow", u"126", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Focus", None))
        self.t_Pose.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.Info.setText(QCoreApplication.translate("MainWindow", u"Ready", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Display Mode", None))
        self.disp_Scene1.setText('RGB-AWB\n📷')
        self.disp_Scene2.setText('MIS-AWB\n🌈')
        self.disp_Compare.setText('Compare\n🔀')
        self.disp_MIS.setText('Channels\n🧬')
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Zoom", None))
        self.b_zoom_in.setText('In➕')
        self.b_zoom_out.setText('Out➖')
        self.b_reset.setText('Reset🔍')
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.Capture_all.setText('📸')
        self.Burst.setText('🎥')
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Stream", None))
        self.B_Stream_on.setText('Stream On\n▶️')
        self.disp_RAW.setText('RAW\n🧱')
