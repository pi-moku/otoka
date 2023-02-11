[english](README.md)
# otoka
<img src="Untitled.png"><br /><br />
## 1. ガイド
otoka は、特定の「開発元」をなくすための Python で書かれたソフトウェアです。  
プロジェクトを支援するには、現在otokaには「開発元」がある状況なので、さまざまな方法でotokaを実装するか、自分のWebサイトでotokaを紹介してください。  
### 1.1. 始める
#### 1.1.1. otokaのインストール
コマンド(wsl2で検証していますがメインがlinuxでも大丈夫だと思います):  
```
git clone https://github.com/pi-moku/otoka.git  
cd otoka  
```  
#### 1.1.2. load.txtに書く内容
load.txt には、読み込みたい URL とパスを上から順に記述します。 (改行区切りで書く必要があります)  
例(load.txt):  
```  
https://pi-moku.github.io/  
```    
#### 1.1.3 実行
「python3 otoka.py filename」をシェルで実行します。(filename は書き込みたいファイルのパスです)  
例:  
```
python3 otoka.py program.py
```
次に、otoka プログラムは load.txt を読み取り、url とパスの内容を読み取り、指定されたファイルに書き込みます。  
(例では https://pi-moku.github.io の内容を「program.py」に書き込んでいます。)  
## 2. エラー
実行してエラーが発生した場合は、まず load.txt を確認してください。  
改行を入れて書いていますか？  
あなたが書いているURLまたはパスは存在しますか？  
(フルパスを推奨)  
確認して存在する場合は、次に実行方法を確認しましょう。  
引数を指定していますか？  
それでも指定されている場合は、otokaのバグの可能性があります。 バグの場合は、このリポジトリで問題を報告してください。  
## 3. otoka五つの理念
1.シンプルであれ  
2.自由万歳  
3.権威主義は悪である  
4.分散万歳  
5,プログラマーはユーザーを尊重する必要がある  
## 4. ライセンス
GNU General Public License v3.0ライセンスです。  
## 4.注意
[english](README.md)
