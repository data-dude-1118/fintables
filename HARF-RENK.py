# -*- coding: utf-8 -*-
"""
Created on Fri May 16 10:10:20 2025

@author: engin
"""

import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLabel,
    QVBoxLayout, QPushButton, QHBoxLayout
)
from PyQt5.QtCore import Qt

class ColorLetterGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Renk Harf Oyunu")
        self.setGeometry(100, 100, 600, 700)

        self.color_letters = {
            "M": "blue",    # Mavi
            "Y": "green",   # Yeşil
            "K": "red",     # Kırmızı
            "S": "yellow"   # Sarı
        }

        self.letters = list(self.color_letters.keys())
        self.colors = list(self.color_letters.values())

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.grid_layout = QGridLayout()
        self.main_layout.addLayout(self.grid_layout)

        # Butonlar için yatay kutu
        button_layout = QHBoxLayout()
        self.main_layout.addLayout(button_layout)

        self.black_button = QPushButton("Siyah Harfli Oyun")
        self.black_button.clicked.connect(self.generate_black_game)
        button_layout.addWidget(self.black_button)

        self.color_button = QPushButton("Karışık Renkli Harfli Oyun")
        self.color_button.clicked.connect(self.generate_colored_game)
        button_layout.addWidget(self.color_button)

        self.generate_black_game()  # Başlangıçta siyah harfli oyun

    def clear_grid(self):
        while self.grid_layout.count():
            child = self.grid_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def generate_black_game(self):
        self.clear_grid()

        for row in range(8):  # 8 satır
            for col in range(4):  # 4 sütun
                letter = random.choice(self.letters)
                label = QLabel(letter)
                label.setAlignment(Qt.AlignCenter)
                label.setStyleSheet("color: black; font-size: 40px; font-weight: bold;")
                self.grid_layout.addWidget(label, row, col)

    def generate_colored_game(self):
        self.clear_grid()

        for row in range(8):
            for col in range(4):
                letter = random.choice(self.letters)
                true_color = self.color_letters[letter]
                other_colors = [color for color in self.colors if color != true_color]
                font_color = random.choice(other_colors)

                label = QLabel(letter)
                label.setAlignment(Qt.AlignCenter)
                label.setStyleSheet(f"color: {font_color}; font-size: 40px; font-weight: bold;")
                self.grid_layout.addWidget(label, row, col)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ColorLetterGame()
    window.show()
    sys.exit(app.exec_())
