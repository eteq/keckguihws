#!/usr/bin/env python
 
# Import PySide classes
import sys
from PySide.QtGui import QApplication, QLabel
 
 
# Create a Qt application
app = QApplication(sys.argv)
# Create a Label and show it
label = QLabel(("<font color=red size=40>Hello World</font>"))
label.show()
# Enter Qt application main loop
sys.exit(app.exec_())