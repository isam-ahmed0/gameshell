import sys
import os
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
# from core import api
from cli import logo
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

from core import api

class GuiQt:
    def __init__(self, api, ui_path=None):
        
        if not ui_path:
          ui_path = os.path.expanduser("~/Projects/learn-python/gameshell/gui_qt/main.ui")
        loader = QUiLoader()
        self.window = loader.load(ui_path)
        # self.window.btn_home.clicked.connect(lambda: self.set_page(0))
        # self.window.btn_mod.clicked.connect(lambda: self.set_page(1))
        mono_font = QFont("Monospace", 8)
        mono_font.setStyleHint(QFont.Monospace)
        self.window.Title.setFont(mono_font)
        self.window.Title.setText(logo.logo())
        self.window.quit_btn.clicked.connect(self.close_app)
        # self.window.gameList.itemClicked.connect(self.launch_game) # not needed now
        self.window.play_btn.clicked.connect(self.play_game)
        # self.window.games_btn.clicked.connect(self.show_games)
        self.show_games()
        self.window.show()
        

    def close_app(self):
      self.window.close()
    
    def show_games(self):
      games = api.load_games()
      for game in games:
        item = QtWidgets.QListWidgetItem(game["name"])
        item.setData(Qt.ItemDataRole.UserRole, game)
        self.window.gameList.addItem(item)

    def play_game(self, item):
      item = self.window.gameList.currentItem()
      game = item.data(Qt.ItemDataRole.UserRole)

      if game:
        api.launch(game)

    def launch_game(self, item): # also play_game works
      game = item.data(Qt.ItemDataRole.UserRole)
      if game:
        api.launch(game)

if __name__ == "__main__":
  app = QApplication(sys.argv)
  client = GuiQt()
  sys.exit(app.exec())


def run(api):
    app = QApplication(sys.argv)
    client = GuiQt(api)
    sys.exit(app.exec())
