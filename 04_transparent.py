import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QSurfaceFormat
from OpenGL import GL


class GLWidget(QOpenGLWidget):
    def initializeGL(self):
        GL.glClearColor(0.0, 0.0, 0.0, 0.0)  # transparent

    def paintGL(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setAttribute(Qt.WA_TransparentForMouseEvents) # type: ignore

        # Frameless
        self.setWindowFlags(Qt.FramelessWindowHint|    # type: ignore
                            Qt.WindowStaysOnTopHint)   # pyright: ignore[reportAttributeAccessIssue]

        # Transparent
        self.setAttribute(Qt.WA_TranslucentBackground) # pyright: ignore[reportAttributeAccessIssue]

        self.setCentralWidget(GLWidget(self))

        # Fullscreen
        self.showFullScreen()


if __name__ == "__main__":
    # Enable alpha channel
    fmt = QSurfaceFormat()
    fmt.setAlphaBufferSize(8)
    QSurfaceFormat.setDefaultFormat(fmt)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
