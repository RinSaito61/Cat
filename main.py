#表示範囲の指定
from kivy.config import Config
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

from kivy.app import App

#要素の総省が「ウィジェット(Widget)」
#下でインポートした要素を引き継ぐことで自分で設定できる
from kivy.uix.widget import Widget

from kivy.properties import StringProperty

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

from random import randint

resource_add_path('C:\Windows\Fonts')
LabelBase.register(DEFAULT_FONT,'HGRPP1.TTC') #日本語フォントの指定

resource_add_path('./images')

#ウィジェットを継承して新たな処理を作成
class ImageWidget(Widget):
    source = StringProperty('./images/neko01.jpg')

    def __init__(self, **kwargs):
        super(ImageWidget, self).__init__(**kwargs)
        pass
    #初めに戻るボタン
    def buttonStarted(self):
        #デフォルトのsourceの値を変更
        self.source= './images/neko01.jpg'
    #ランダムに表示するボタン
    def buttonRandom(self):
        #/imageは上に追加しているため、書かなくていい
        self.source= f'neko0{randint(1,9)}.jpg'

class CatApp(App):
    def __init__(self, **kwargs):
        super(CatApp, self).__init__(**kwargs)
        #アプリのタイトル
        self.title = 'ネコ画像表示'

#呼び出しがコンソールからなら実行（だったはず）
if __name__ == '__main__':
    catap = CatApp()
    catap.run()