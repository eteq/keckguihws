#!/usr/bin/env python
 
# Import PyQt4 classes
import sys
from PyQt4.QtGui import QApplication, QPushButton
 
def sayHello():
    print "Hello Keck!"
 
# Create the Qt Application
app = QApplication(sys.argv)
# Create a button, connect it and show it
button = QPushButton("Click me")
button.clicked.connect(sayHello)
button.show()
# Run the main Qt loop
sys.exit(app.exec_() )   