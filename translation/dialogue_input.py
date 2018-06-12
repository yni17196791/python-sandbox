# モジュールのインポート
import os, tkinter, tkinter.filedialog, tkinter.messagebox
# ファイル選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()
fTyp = [("","*.txt")]
iDir = os.path.abspath(os.path.dirname(__file__))
tkinter.messagebox.showinfo('Google翻訳API','処理するテキストファイルを選択してください。\n一行あたり2000文字が翻訳の上限です。')
file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
# 処理ファイル名の出力
tkinter.messagebox.showinfo('Google翻訳API',file)
