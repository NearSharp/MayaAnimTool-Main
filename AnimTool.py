#PRESS ALT + SHIFT + M
import maya.cmds as cmds
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit

class PlayblastWindow(QMainWindow):
    def __init__(self):
        super(PlayblastWindow, self).__init__()
        self.setWindowTitle("Playblast Settings")
        self.setFixedSize(300, 150)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        self.width_label = QLabel("Width:")
        self.layout.addWidget(self.width_label)
        
        self.width_input = QLineEdit()
        self.layout.addWidget(self.width_input)
        
        self.height_label = QLabel("Height:")
        self.layout.addWidget(self.height_label)
        
        self.height_input = QLineEdit()
        self.layout.addWidget(self.height_input)
        
        self.playblast_button = QPushButton("Make Playblast")
        self.playblast_button.clicked.connect(self.make_playblast)
        self.layout.addWidget(self.playblast_button)
        
    def make_playblast(self):
        width = int(self.width_input.text())
        height = int(self.height_input.text())
        
        # Set render resolution
        cmds.setAttr("defaultResolution.width", width)
        cmds.setAttr("defaultResolution.height", height)
        
        # Make playblast
        cmds.playblast(width=width, height=height, forceOverwrite=True)


def main():
    # Check if the window already exists, if so, delete it
    if cmds.window("playblastWindow", exists=True):
        cmds.deleteUI("playblastWindow", window=True)
    
    # Create Qt application
    app = QApplication.instance()
    if not app:
        app = QApplication([])
    
    # Create and show the window
    window = PlayblastWindow()
    window.show()
    
    # Execute the Qt application
    app.exec_()


if __name__ == "__main__":
    main()

