#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("OBS-Atom Futuristic Builder 🚀")
    window.resize(500, 300)

    layout = QVBoxLayout()

    label = QLabel("🦝 Greetings, traveler!\n\n"
                   "I am the Professor Raccoon from the future.\n"
                   "Today we test fireworks mode (UI launcher).")
    label.setStyleSheet("font-size: 16px; padding: 10px;")
    layout.addWidget(label)

    button = QPushButton("✨ Launch Fireworks ✨")
    button.setStyleSheet("font-size: 18px; background-color: black; color: gold; padding: 10px;")
    button.clicked.connect(lambda: label.setText("💥 BOOM! Fireworks are working!\n\nInstaller UI is alive."))
    layout.addWidget(button)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()

