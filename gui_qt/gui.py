import sys
from PySide6.QtCore import Qt
# from core import api
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

from core import api

class GuiQt:
    def __init__(self, api):
        
        loader = QUiLoader()
        self.window = loader.load("main.ui")
        # self.window.btn_home.clicked.connect(lambda: self.set_page(0))
        # self.window.btn_mod.clicked.connect(lambda: self.set_page(1))
        self.window.quit_btn.clicked.connect(self.close_app)
        # self.window.gameList.itemClicked.connect() # (self.api.launch_game)
        # self.show_games()
        self.window.show()
        

    def close_app(self):
      self.window.close()
    
    def show_games(self):
      games = api.load_games()
      for game in games:
        item = self.window.gameList.addItem(game["name"])
        item = self.window.gameList.item(self.window.gameList.count() - 1)
        item.setData(Qt.ItemDataRole.UserRole, game)

if __name__ == "__main__":
  app = QApplication(sys.argv)
  client = GuiQt()
  sys.exit(app.exec())


def run_gui(api):
    app = QApplication(sys.argv)
    client = GuiQt(api)
    sys.exit(app.exec())
