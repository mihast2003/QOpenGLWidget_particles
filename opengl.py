import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL import GL


class GLWidget(QOpenGLWidget):
    def initializeGL(self):
        """Called once at the start, after OpenGL context is created"""
        GL.glClearColor(0.2, 0.3, 0.4, 1.0)  # background color

    def resizeGL(self, w: int, h: int):
        """Called on resize"""
        GL.glViewport(0, 0, w, h)

    def paintGL(self):
        """Called every frame to draw"""
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)  # clear screen to background color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minimal QOpenGLWidget Example")
        self.resize(640, 480)
        self.gl_widget = GLWidget(self)
        self.setCentralWidget(self.gl_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
