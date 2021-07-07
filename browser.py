import sys
import typing

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget

URL = "https://medium.com/predict/this-long-awaited-technology-may-finally-change-the-world-ec3023a30af2"
# URL = "https://duckduckgo.com/"


def loadFinished() -> None:
    print("finished")


def main() -> None:
    application = QApplication([])  # sys.argv
    view = QWebEngineView()
    view.loadStarted.connect(loadFinished)

    view.load(QUrl(URL))
    view.show()

    # TODO: Wait for JS (smartly?)
    # TODO: Extract page content
    # TODO: Stdout or html2org?

    sys.exit(application.exec_())


if __name__== "__main__":
    main()