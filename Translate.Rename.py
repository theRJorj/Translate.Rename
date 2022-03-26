from PyQt5 import QtCore, QtGui, QtWidgets
import os
import datetime
from googletrans import Translator
import tkinter as tk
from tkinter import filedialog
import re
import shutil
import threading


lang = [
    "afrikaans",
    "albanian",
    "amharic",
    "arabic",
    "armenian",
    "azerbaijani",
    "basque",
    "belarusian",
    "bengali",
    "bosnian",
    "bulgarian",
    "catalan",
    "cebuano",
    "chichewa",
    "chinese (simplified)",
    "chinese (traditional)",
    "corsican",
    "croatian",
    "czech",
    "danish",
    "dutch",
    "english",
    "esperanto",
    "estonian",
    "filipino",
    "finnish",
    "french",
    "frisian",
    "galician",
    "georgian",
    "german",
    "greek",
    "gujarati",
    "haitian creole",
    "hausa",
    "hawaiian",
    "hebrew",
    "hindi",
    "hmong",
    "hungarian",
    "icelandic",
    "igbo",
    "indonesian",
    "irish",
    "italian",
    "japanese",
    "javanese",
    "kannada",
    "kazakh",
    "khmer",
    "korean",
    "kurdish (kurmanji)",
    "kyrgyz",
    "lao",
    "latin",
    "latvian",
    "lithuanian",
    "luxembourgish",
    "macedonian",
    "malagasy",
    "malay",
    "malayalam",
    "maltese",
    "maori",
    "marathi",
    "mongolian",
    "myanmar (burmese)",
    "nepali",
    "norwegian",
    "pashto",
    "persian",
    "polish",
    "portuguese",
    "punjabi",
    "romanian",
    "russian",
    "samoan",
    "scots gaelic",
    "serbian",
    "sesotho",
    "shona",
    "sindhi",
    "sinhala",
    "slovak",
    "slovenian",
    "somali",
    "spanish",
    "sundanese",
    "swahili",
    "swedish",
    "tajik",
    "tamil",
    "telugu",
    "thai",
    "turkish",
    "ukrainian",
    "urdu",
    "uzbek",
    "vietnamese",
    "welsh",
    "xhosa",
    "yiddish",
    "yoruba",
    "zulu",
    "Filipino",
    "Hebrew",
]
lang_dict = {
    "afrikaans": "af",
    "albanian": "sq",
    "amharic": "am",
    "arabic": "ar",
    "armenian": "hy",
    "azerbaijani": "az",
    "basque": "eu",
    "belarusian": "be",
    "bengali": "bn",
    "bosnian": "bs",
    "bulgarian": "bg",
    "catalan": "ca",
    "cebuano": "ceb",
    "chichewa": "ny",
    "chinese (simplified)": "zh-cn",
    "chinese (traditional)": "zh-tw",
    "corsican": "co",
    "croatian": "hr",
    "czech": "cs",
    "danish": "da",
    "dutch": "nl",
    "english": "en",
    "esperanto": "eo",
    "estonian": "et",
    "filipino": "tl",
    "finnish": "fi",
    "french": "fr",
    "frisian": "fy",
    "galician": "gl",
    "georgian": "ka",
    "german": "de",
    "greek": "el",
    "gujarati": "gu",
    "haitian creole": "ht",
    "hausa": "ha",
    "hawaiian": "haw",
    "hebrew": "iw",
    "hindi": "hi",
    "hmong": "hmn",
    "hungarian": "hu",
    "icelandic": "is",
    "igbo": "ig",
    "indonesian": "id",
    "irish": "ga",
    "italian": "it",
    "japanese": "ja",
    "javanese": "jw",
    "kannada": "kn",
    "kazakh": "kk",
    "khmer": "km",
    "korean": "ko",
    "kurdish (kurmanji)": "ku",
    "kyrgyz": "ky",
    "lao": "lo",
    "latin": "la",
    "latvian": "lv",
    "lithuanian": "lt",
    "luxembourgish": "lb",
    "macedonian": "mk",
    "malagasy": "mg",
    "malay": "ms",
    "malayalam": "ml",
    "maltese": "mt",
    "maori": "mi",
    "marathi": "mr",
    "mongolian": "mn",
    "myanmar (burmese)": "my",
    "nepali": "ne",
    "norwegian": "no",
    "pashto": "ps",
    "persian": "fa",
    "polish": "pl",
    "portuguese": "pt",
    "punjabi": "pa",
    "romanian": "ro",
    "russian": "ru",
    "samoan": "sm",
    "scots gaelic": "gd",
    "serbian": "sr",
    "sesotho": "st",
    "shona": "sn",
    "sindhi": "sd",
    "sinhala": "si",
    "slovak": "sk",
    "slovenian": "sl",
    "somali": "so",
    "spanish": "es",
    "sundanese": "su",
    "swahili": "sw",
    "swedish": "sv",
    "tajik": "tg",
    "tamil": "ta",
    "telugu": "te",
    "thai": "th",
    "turkish": "tr",
    "ukrainian": "uk",
    "urdu": "ur",
    "uzbek": "uz",
    "vietnamese": "vi",
    "welsh": "cy",
    "xhosa": "xh",
    "yiddish": "yi",
    "yoruba": "yo",
    "zulu": "zu",
    "Filipino": "fil",
    "Hebrew": "he",
    "Auto": "Auto detect",
}


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Translate.Rename Bulk")
        MainWindow.resize(581, 648)
        MainWindow.setMinimumSize(QtCore.QSize(581, 648))
        MainWindow.setMaximumSize(QtCore.QSize(581, 648))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(108, 108, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 138, 138))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 136, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)

        gradient2 = QtGui.QLinearGradient(0.512, 0.597045, 1, 1)
        gradient2.setSpread(QtGui.QGradient.PadSpread)
        gradient2.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QtGui.QColor(0, 0, 0, 255))
        gradient2.setColorAt(1, QtGui.QColor(0, 82, 122, 255))
        brush5 = QtGui.QBrush(gradient2)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush5)

        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)

        gradient3 = QtGui.QLinearGradient(0.512, 0.597045, 1, 1)
        gradient3.setSpread(QtGui.QGradient.PadSpread)
        gradient3.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QtGui.QColor(0, 0, 0, 255))
        gradient3.setColorAt(1, QtGui.QColor(0, 82, 122, 255))
        brush6 = QtGui.QBrush(gradient3)

        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush6)

        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.target = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.tfolder()
        )

        self.target.setEnabled(True)
        self.target.setGeometry(QtCore.QRect(460, 30, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.target.sizePolicy().hasHeightForWidth())
        self.target.setSizePolicy(sizePolicy)
        self.target.setObjectName("target")
        self.pre = QtWidgets.QLineEdit(self.centralwidget)
        self.pre.setEnabled(False)
        self.pre.setGeometry(QtCore.QRect(150, 320, 311, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pre.sizePolicy().hasHeightForWidth())
        self.pre.setSizePolicy(sizePolicy)
        self.pre.setObjectName("pre")
        self.L1 = QtWidgets.QComboBox(self.centralwidget)
        self.L1.setEnabled(False)
        self.L1.setGeometry(QtCore.QRect(150, 180, 81, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L1.sizePolicy().hasHeightForWidth())
        self.L1.setSizePolicy(sizePolicy)
        self.L1.setObjectName("L1")
        self.error_name_ch = QtWidgets.QLabel(self.centralwidget)
        self.error_name_ch.setEnabled(True)
        self.error_name_ch.setGeometry(QtCore.QRect(90, 460, 461, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.error_name_ch.sizePolicy().hasHeightForWidth()
        )
        self.error_name_ch.setSizePolicy(sizePolicy)
        self.error_name_ch.setText("")
        self.error_name_ch.setObjectName("error_name_ch")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setEnabled(True)
        self.label_11.setGeometry(QtCore.QRect(150, 470, 261, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.dest = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.dfolder()
        )
        self.dest.setEnabled(True)
        self.dest.setGeometry(QtCore.QRect(460, 70, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dest.sizePolicy().hasHeightForWidth())
        self.dest.setSizePolicy(sizePolicy)
        self.dest.setObjectName("dest")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(90, 190, 47, 13))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.suffix = QtWidgets.QCheckBox(self.centralwidget)
        self.suffix.setEnabled(True)
        self.suffix.setGeometry(QtCore.QRect(30, 480, 70, 17))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.suffix.sizePolicy().hasHeightForWidth())
        self.suffix.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.suffix.setFont(font)
        self.suffix.setObjectName("suffix")
        self.translat = QtWidgets.QCheckBox(self.centralwidget)
        self.translat.setEnabled(True)
        self.translat.setGeometry(QtCore.QRect(30, 160, 81, 17))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.translat.sizePolicy().hasHeightForWidth())
        self.translat.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.translat.setFont(font)
        self.translat.setObjectName("translat")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(90, 320, 47, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.chang = QtWidgets.QCheckBox(self.centralwidget)
        self.chang.setEnabled(True)
        self.chang.setGeometry(QtCore.QRect(30, 410, 70, 17))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chang.sizePolicy().hasHeightForWidth())
        self.chang.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.chang.setFont(font)
        self.chang.setObjectName("chang")
        self.add = QtWidgets.QCheckBox(self.centralwidget)
        self.add.setEnabled(True)
        self.add.setGeometry(QtCore.QRect(30, 260, 70, 17))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
        self.add.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setEnabled(True)
        self.label_9.setGeometry(QtCore.QRect(150, 160, 331, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.error_start = QtWidgets.QLabel(self.centralwidget)
        self.error_start.setEnabled(True)
        self.error_start.setGeometry(QtCore.QRect(30, 610, 521, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_start.sizePolicy().hasHeightForWidth())
        self.error_start.setSizePolicy(sizePolicy)
        self.error_start.setText("")
        self.error_start.setObjectName("error_start")
        self.error_translate = QtWidgets.QLabel(self.centralwidget)
        self.error_translate.setEnabled(True)
        self.error_translate.setGeometry(QtCore.QRect(90, 250, 461, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.error_translate.sizePolicy().hasHeightForWidth()
        )
        self.error_translate.setSizePolicy(sizePolicy)
        self.error_translate.setText("")
        self.error_translate.setObjectName("error_translate")
        self.date = QtWidgets.QCheckBox(self.centralwidget)
        self.date.setEnabled(False)
        self.date.setGeometry(QtCore.QRect(90, 280, 70, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date.sizePolicy().hasHeightForWidth())
        self.date.setSizePolicy(sizePolicy)
        self.date.setObjectName("date")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setGeometry(QtCore.QRect(290, 280, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.radioButton_2.sizePolicy().hasHeightForWidth()
        )
        self.radioButton_2.setSizePolicy(sizePolicy)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setEnabled(True)
        self.label_10.setGeometry(QtCore.QRect(150, 405, 301, 21))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.error_name_add = QtWidgets.QLabel(self.centralwidget)
        self.error_name_add.setEnabled(True)
        self.error_name_add.setGeometry(QtCore.QRect(90, 390, 461, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.error_name_add.sizePolicy().hasHeightForWidth()
        )
        self.error_name_add.setSizePolicy(sizePolicy)
        self.error_name_add.setText("")
        self.error_name_add.setObjectName("error_name_add")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(90, 500, 61, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.L2 = QtWidgets.QComboBox(self.centralwidget)
        self.L2.setEnabled(False)
        self.L2.setGeometry(QtCore.QRect(150, 220, 81, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L2.sizePolicy().hasHeightForWidth())
        self.L2.setSizePolicy(sizePolicy)
        self.L2.setObjectName("L2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(90, 230, 47, 13))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setEnabled(False)
        self.label_8.setGeometry(QtCore.QRect(90, 440, 51, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setEnabled(False)
        self.label_5.setGeometry(QtCore.QRect(90, 360, 51, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setEnabled(False)
        self.radioButton.setGeometry(QtCore.QRect(160, 280, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setObjectName("radioButton")
        self.Start_b = QtWidgets.QPushButton(
            self.centralwidget,
            clicked=lambda: threading.Thread(target=self.check).start(),
        )
        self.Start_b.setEnabled(True)
        self.Start_b.setGeometry(QtCore.QRect(-10, 570, 601, 41))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Start_b.sizePolicy().hasHeightForWidth())
        self.Start_b.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Start_b.setFont(font)
        self.Start_b.setAutoFillBackground(False)
        self.Start_b.setStyleSheet(
            "\n"
            "QPushButton {\n"
            "    color: rgb(247, 244, 255);\n"
            "    border: 2px solid rgb(183, 200, 208);\n"
            "    border-radius: 4px;    \n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.534, x2:1, y2:1, stop:0.477273 rgba(53, 105, 131, 255), stop:1 rgba(110, 87, 121, 255));\n"
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(47, 186, 255, 255), stop:1 rgba(121, 128, 171, 255));\n"
            "    border: 2px solid rgb(61, 70, 86);\n"
            "}\n"
            "QPushButton:pressed {    \n"
            "    background-color: rgb(203, 187, 236);\n"
            "    border: 2px solid rgb(43, 50, 61);\n"
            "}"
        )
        self.Start_b.setDefault(False)
        self.Start_b.setObjectName("Start_b")
        self.post = QtWidgets.QLineEdit(self.centralwidget)
        self.post.setEnabled(False)
        self.post.setGeometry(QtCore.QRect(150, 360, 311, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.post.sizePolicy().hasHeightForWidth())
        self.post.setSizePolicy(sizePolicy)
        self.post.setObjectName("post")
        self.change = QtWidgets.QLineEdit(self.centralwidget)
        self.change.setEnabled(False)
        self.change.setGeometry(QtCore.QRect(150, 430, 311, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.change.sizePolicy().hasHeightForWidth())
        self.change.setSizePolicy(sizePolicy)
        self.change.setObjectName("change")
        self.suff = QtWidgets.QLineEdit(self.centralwidget)
        self.suff.setEnabled(False)
        self.suff.setGeometry(QtCore.QRect(150, 500, 61, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.suff.sizePolicy().hasHeightForWidth())
        self.suff.setSizePolicy(sizePolicy)
        self.suff.setObjectName("suff")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 540, 181, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 431, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 70, 431, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.sort = QtWidgets.QComboBox(self.centralwidget)
        self.sort.setEnabled(False)
        self.sort.setGeometry(QtCore.QRect(460, 430, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sort.sizePolicy().hasHeightForWidth())
        self.sort.setSizePolicy(sizePolicy)
        self.sort.setObjectName("sort")
        self.sort.addItem("")
        self.sort.addItem("")
        self.sort.addItem("")
        self.sort.addItem("")
        self.filter = QtWidgets.QCheckBox(self.centralwidget)
        self.filter.setEnabled(True)
        self.filter.setGeometry(QtCore.QRect(30, 110, 81, 17))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filter.sizePolicy().hasHeightForWidth())
        self.filter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.filter.setFont(font)
        self.filter.setObjectName("filter")
        self.filterbox = QtWidgets.QComboBox(self.centralwidget)
        self.filterbox.setEnabled(False)
        self.filterbox.setGeometry(QtCore.QRect(150, 120, 81, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterbox.sizePolicy().hasHeightForWidth())
        self.filterbox.setSizePolicy(sizePolicy)
        self.filterbox.setObjectName("filterbox")
        self.filterbox.addItem("")
        self.filterbox.addItem("")
        self.filterbox.addItem("")
        self.filterbox.addItem("")
        self.filtertext = QtWidgets.QLineEdit(self.centralwidget)
        self.filtertext.setEnabled(False)
        self.filtertext.setGeometry(QtCore.QRect(230, 120, 231, 31))
        self.filtertext.setObjectName("filtertext")
        self.filterbox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.filterbox_2.setEnabled(False)
        self.filterbox_2.setGeometry(QtCore.QRect(460, 120, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )

        self.link = QtWidgets.QLabel(self.centralwidget)

        self.link.setGeometry(QtCore.QRect(430, 550, 130, 21))
        self.link.setObjectName("link")
        self.link.setOpenExternalLinks(True)

        self.link.setText(
            "<a href='https://github.com/theRJorj'style='color:white;' >By: Github.com/theRJorj</a>"
        )
        self.L1.addItem("Auto")
        self.L2.addItem("Select")
        self.L1.addItems(lang)
        self.L2.addItems(lang)

        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterbox_2.sizePolicy().hasHeightForWidth())
        self.filterbox_2.setSizePolicy(sizePolicy)
        self.filterbox_2.setObjectName("filterbox_2")
        self.filterbox_2.addItem("")
        self.filterbox_2.addItem("")

        self.filterbox.currentIndexChanged.connect(self.filter_hint)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.date.clicked["bool"].connect(self.radioButton.setEnabled)  # type: ignore
        self.date.clicked["bool"].connect(self.radioButton_2.setEnabled)  # type: ignore
        self.add.clicked["bool"].connect(self.date.setEnabled)  # type: ignore
        self.translat.clicked["bool"].connect(self.L1.setEnabled)  # type: ignore
        self.translat.clicked["bool"].connect(self.L2.setEnabled)  # type: ignore
        self.filter.clicked["bool"].connect(self.filterbox.setEnabled)  # type: ignore
        self.filter.clicked["bool"].connect(self.filtertext.setEnabled)  # type: ignore
        self.filter.clicked["bool"].connect(self.filterbox_2.setEnabled)  # type: ignore
        self.add.clicked["bool"].connect(self.pre.setEnabled)  # type: ignore
        self.add.clicked["bool"].connect(self.post.setEnabled)  # type: ignore
        self.chang.clicked["bool"].connect(self.change.setEnabled)  # type: ignore
        self.chang.clicked["bool"].connect(self.sort.setEnabled)  # type: ignore
        self.suffix.clicked["bool"].connect(self.suff.setEnabled)  # type: ignore
        self.add.clicked["bool"].connect(self.label_4.setEnabled)  # type: ignore
        self.add.clicked["bool"].connect(self.label_5.setEnabled)  # type: ignore
        self.chang.clicked["bool"].connect(self.label_8.setEnabled)  # type: ignore
        self.suffix.clicked["bool"].connect(self.label_3.setEnabled)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.target.setText(_translate("MainWindow", "Open folder"))
        self.label_11.setText(
            _translate("MainWindow", "Be cautious about changing suffixes")
        )
        self.dest.setText(_translate("MainWindow", "Open folder"))
        self.label_6.setText(_translate("MainWindow", "From"))
        self.suffix.setText(_translate("MainWindow", "Suffix"))
        self.translat.setText(_translate("MainWindow", "Translate"))
        self.label_4.setText(_translate("MainWindow", "Pre name"))
        self.chang.setText(_translate("MainWindow", "Change"))
        self.add.setText(_translate("MainWindow", "Add"))
        self.label_9.setText(
            _translate(
                "MainWindow",
                "Please note that it is just Google translate and it is not Accurate!",
            )
        )
        self.date.setText(_translate("MainWindow", "Date"))
        self.radioButton_2.setText(_translate("MainWindow", "End"))
        self.label_10.setText(
            _translate("MainWindow", "Fully renames and adds numbers _1,_2,...")
        )
        self.label_3.setText(_translate("MainWindow", 'Without "."'))
        self.label_7.setText(_translate("MainWindow", "To"))
        self.label_8.setText(_translate("MainWindow", "New name"))
        self.label_5.setText(_translate("MainWindow", "Post name"))
        self.radioButton.setText(_translate("MainWindow", "Beginnig"))
        self.Start_b.setText(_translate("MainWindow", "Start"))
        self.checkBox.setText(_translate("MainWindow", "Backup (Recommended)"))
        self.sort.setItemText(0, _translate("MainWindow", "Sort by"))
        self.sort.setItemText(1, _translate("MainWindow", "Name"))
        self.sort.setItemText(2, _translate("MainWindow", "Date"))
        self.sort.setItemText(3, _translate("MainWindow", "Size"))
        self.filter.setText(_translate("MainWindow", "Filter"))
        self.filterbox.setItemText(0, _translate("MainWindow", "By Text"))
        self.filterbox.setItemText(1, _translate("MainWindow", "By Date"))
        self.filterbox.setItemText(2, _translate("MainWindow", "By Size"))
        self.filterbox.setItemText(3, _translate("MainWindow", "By Type"))
        self.filterbox_2.setItemText(0, _translate("MainWindow", "Only"))
        self.filterbox_2.setItemText(1, _translate("MainWindow", "Sub"))
        self.lineEdit.setText(_translate("MainWindow", "Target folder"))
        self.lineEdit_2.setText(
            _translate(
                "MainWindow",
                "Destination folder: Must be in the SAME DRIVE as target folder",
            )
        )

    def filter_hint(self):
        self.filtertext.clear()
        if self.filterbox.currentIndex() == 1:
            self.filtertext.setText("(ex: 2020-05-15) Up to given date")
        if self.filterbox.currentIndex() == 2:
            self.filtertext.setText("(ex: 15) Up to given size by KB")
        if self.filterbox.currentIndex() == 3:
            self.filtertext.setText("(ex: .png)")

    def tfolder(self):

        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        mainfolder1 = filedialog.askdirectory()
        self.lineEdit.setText(mainfolder1)

    def dfolder(self):
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        dest_folder = filedialog.askdirectory()
        self.lineEdit_2.setText(dest_folder)

    def backup(self):

        np = os.path.normpath(self.lineEdit.text())
        npd = os.path.normpath(self.lineEdit_2.text())
        checkBox = "tr_Backup"
        bpath = os.path.join(npd, checkBox)

        shutil.copytree(os.path.join(np), os.path.join(bpath))

    def filters(self):
        np = os.path.normpath(self.lineEdit.text())
        npd = os.path.normpath(self.lineEdit_2.text())
        if self.filter.isChecked():
            unfiltered_files_list = os.listdir(np)
            if self.filterbox.currentIndex() == 0:
                files_list = []
                for i in unfiltered_files_list:
                    filename = os.path.splitext(i)[0]
                    if (
                        re.search(rf"{self.filtertext.text()}", filename) != None
                        and self.filterbox_2.currentIndex() == 0
                    ):
                        files_list.append(i)
                    elif (
                        re.search(rf"{self.filtertext.text()}", filename) == None
                        and self.filterbox_2.currentIndex() == 1
                    ):
                        files_list.append(i)
            elif self.filterbox.currentIndex() == 1:
                files_list = []
                filterdate = datetime.datetime.strptime(
                    self.filtertext.text(), "%Y-%m-%d"
                )
                for j in unfiltered_files_list:
                    filedate = datetime.datetime.fromtimestamp(
                        os.stat(os.path.join(np, j)).st_mtime
                    ).strftime("%Y-%m-%d")
                    filedate = datetime.datetime.strptime(filedate, "%Y-%m-%d")
                    if filedate >= filterdate and self.filterbox_2.currentIndex() == 0:
                        files_list.append(j)
                    elif (
                        filedate <= filterdate and self.filterbox_2.currentIndex() == 1
                    ):
                        files_list.append(j)
            elif self.filterbox.currentIndex() == 2:
                files_list = []
                filtersize = int(self.filtertext.text())
                for s in unfiltered_files_list:
                    if (
                        os.stat(os.path.join(np, s)).st_size // 1024
                    ) <= filtersize and self.filterbox_2.currentIndex() == 0:
                        files_list.append(s)
                    elif (
                        os.stat(os.path.join(np, s)).st_size // 1024
                    ) >= filtersize and self.filterbox_2.currentIndex() == 1:
                        files_list.append(s)
            elif self.filterbox.currentIndex() == 3:
                files_list = []
                filtertype = self.filtertext.text()
                for t in unfiltered_files_list:
                    filetype = os.path.splitext(t)[1]
                    if filtertype == filetype and self.filterbox_2.currentIndex() == 0:
                        files_list.append(t)
                    elif (
                        filtertype != filetype and self.filterbox_2.currentIndex() == 1
                    ):
                        files_list.append(t)

            return files_list
        else:
            files_list = os.listdir(np)
            return files_list

    def trans(self, files_list):
        c1 = 0
        c2 = 0
        c3 = 0

        np = os.path.normpath(self.lineEdit.text())
        npd = os.path.normpath(self.lineEdit_2.text())

        translator = Translator()

        suffix = [os.path.splitext(res)[1] for res in files_list]

        folder = [os.path.splitext(filename)[0] for filename in files_list]

        f = open(r"f.text", "w", encoding="utf-8")

        for i in folder:
            f.write(i + "\n")
            c1 += 1

        f.close()
        f = open(r"f.text", "r", encoding="utf-8")

        m = f.read()
        print(len(m))
        if len(m) <= 14000:
            pass
        else:
            len_error = "Too much characters! the limit is 15k"
            print(len_error)

        l1 = lang_dict[self.L1.currentText()]
        l2 = lang_dict[self.L2.currentText()]
        if l1 == "Auto detect":
            result = translator.translate(m, dest=l2)
        else:
            result = translator.translate(m, src=l1, dest=l2)

        result = result.text
        result = (
            result.replace('"', "")
            .replace(":", "")
            .replace("|", "")
            .replace("*", "")
            .replace("/", "")
            .replace("<", "")
            .replace(">", "")
            .replace("?", "")
        )
        result = result.split("\n")

        for filename, r, s in zip(folder, result, suffix):
            c2 += 1

            try:
                os.rename(os.path.join(np, filename + s), os.path.join(npd, r + s))
            except WindowsError:
                c3 += 1

                os.rename(
                    os.path.join(np, filename + s), os.path.join(npd, r + str(c3) + s)
                )

        f.close()

    def adds(self, files_list):

        self.error_name_add.setText("")
        pre_add = self.pre.text()
        pra = re.search(r"[\\\/\:\*\?\"\<\>\|]", pre_add)
        post_add = self.post.text()
        psa = re.search(r"[\\\/\:\*\?\"\<\>\|]", post_add)
        if pra is not None:
            self.error_name_add.setText(
                'Name cannot contain any of these characters: \/:*?"<>|'
            )
        elif psa is not None:
            self.error_name_add.setText(
                'Name cannot contain any of these characters: \/:*?"<>|'
            )
        else:
            pass

        np = os.path.normpath(self.lineEdit.text())
        npd = os.path.normpath(self.lineEdit_2.text())

        date_add_post = ""
        date_add_pre = ""
        if self.date.isChecked():
            if self.radioButton.isChecked():
                date_add_pre = datetime.date.today()
            elif self.radioButton_2.isChecked():
                date_add_post = datetime.date.today()
            else:
                pass

        suffix = [os.path.splitext(res)[1] for res in files_list]

        folder = [os.path.splitext(filename)[0] for filename in files_list]
        result = []
        for i in folder:
            result.append(
                str(date_add_pre) + pre_add + i + post_add + str(date_add_post)
            )

        for filename, r, s in zip(folder, result, suffix):

            try:
                os.rename(os.path.join(np, filename + s), os.path.join(npd, r + s))
            except:
                os.replace(os.path.join(np, filename + s), os.path.join(npd, r + s))

    def change_all(self, files_list):
        np = os.path.normpath(self.lineEdit.text())
        npd = os.path.normpath(self.lineEdit_2.text())
        c = 1

        new_name = self.change.text()

        nn = re.search(r"[\\\/\:\*\?\"\<\>\|]", new_name)
        if nn is not None:
            self.error_name_ch.setText(
                'Name cannot contain any of these characters: \/:*?"<>|'
            )

        else:
            pass

        if self.sort.currentIndex() in (0, 1):
            suffix = [os.path.splitext(res)[1] for res in files_list]
            folder = [os.path.splitext(filename)[0] for filename in files_list]

        elif self.sort.currentIndex() == 2:
            files = os.listdir(np)
            files_list = [os.path.join(np, f) for f in files]
            files_list.sort(key=lambda x: os.path.getmtime(x))

            suffix = [os.path.splitext(res)[1] for res in files_list]
            folder = [os.path.splitext(filename)[0] for filename in files_list]

        elif self.sort.currentIndex() == 3:

            files_list = os.listdir(np)
            files_list = sorted(
                files_list, key=lambda x: os.stat(os.path.join(np, x)).st_size
            )
            suffix = [os.path.splitext(res)[1] for res in files_list]
            folder = [os.path.splitext(filename)[0] for filename in files_list]

        result = []
        for i in folder:
            i = ""
            result.append(i + new_name + "_" + str(c))
            c += 1

        for filename, r, s in zip(folder, result, suffix):

            try:
                os.rename(os.path.join(np, filename + s), os.path.join(npd, r + s))
            except:
                pass

    def change_suffix(self, files_list):

        np = os.path.normpath(self.lineEdit.text())
        npd = os.path.normpath(self.lineEdit_2.text())

        new_suffix = self.suff.text()

        suffix = [os.path.splitext(res)[1] for res in files_list]

        folder = [os.path.splitext(filename)[0] for filename in files_list]
        result = []
        for i in folder:
            result.append(i + "." + new_suffix)

        for filename, r, s in zip(folder, result, suffix):

            try:
                os.rename(os.path.join(np, filename + s), os.path.join(npd, r))
            except:
                pass

    def check(self):
        try:
            self.error_start.setText("Started...")
            files_list = self.filters()

            if self.checkBox.isChecked() == True:
                files_list = self.filters()
                self.backup()
            else:
                pass

            if self.translat.isChecked() == True:
                files_list = self.filters()
                self.trans(files_list)
            else:
                pass

            if self.add.isChecked() == True:
                files_list = self.filters()
                self.adds(files_list)
            else:
                pass

            if self.chang.isChecked() == True:
                files_list = self.filters()
                self.change_all(files_list)
            else:
                pass

            if self.suffix.isChecked() == True:
                files_list = self.filters()
                self.change_suffix(files_list)
            else:
                pass
            if (
                self.suffix.isChecked() == False
                and self.chang.isChecked() == False
                and self.add.isChecked() == False
                and self.translat.isChecked() == False
                and self.checkBox.isChecked() == False
            ):
                self.error_start.setText("Please choose an Option!")
                return

            else:
                pass
            self.error_start.setText("Done!")
        except WindowsError:
            self.error_start.setText("Please specify Target and Destination folder")
        except TypeError:
            self.error_start.setText("Too Many Characters")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
