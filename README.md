<h3 align="center"><b>✅ checkTEST</b></h3>
<p align="center">
テスト結果を作成・出力
</p> 

## ✨ 特徴
- たった１行の関数でテストの結果を作成できます。
- 必要に応じてテキストファイルを出力可能。

<br>

## 🌱 なぜ作ったのか?
自分自身が受験生で、テストの結果を簡単にまとめたいと思っていたので作成。

<br>

## ✏️ 書き方
- Pythonファイルにインポート
```python
from checktest import CT
```
- 関数にデータを挿入
```python
CT (
    <タイトル:str>,
    <科目数:int>, 
    [
        [<科目名:str>, <点数:int>], 
        [<科目名:str>, <点数:int>], 
        [<科目名:str>, <点数:int>]
    ], 
    <ファイルの出力:bool>
)
```

<br>

## 📝 ライセンス
MIT