from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowIcon(QIcon('faa9f6cb4fd03e4cc602f513b796566c.jpg'))
        self.setWindowTitle('BROWSER TEST')
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('<', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        reload_btn =QAction('Reload',self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        forward_btn = QAction('>' , self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.urlbar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))
    def navigate_to_url(self):
        url = self.urlbar.text()
        self.browser.setUrl(QUrl(url))
    def update_url(self,site):
        self.urlbar.setText(site.toString())




app = QApplication(sys.argv)
window = MainWindow()
window.showMaximized()
QApplication.setApplicationName('BROWSER TEST')
app.exec_()