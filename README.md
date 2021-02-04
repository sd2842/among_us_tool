# among_us_tool
2021 / 02 / 03 初回  
2021 / 02 / 04 修正＆マップ追加のアップデートを行いました。ver1.1  

among usの初心者向け推理支援ツールver1.1です。
以下目次です。  
  
 0. ver1.0からアップデートする方のみお読みください
 1. 最初のお読みください
 2. 環境の準備
 3. 使用方法
 4. 最後に

## 0. ver1.0からアップデートする方へ
当初からお使いいただきありがとうございます。  
もうすでにツールを持っている方で、マップの追加を行いたい場合は、「among_us_tool」のフォルダの中（Report_halfとかAdmin_halfがある場所）に、  
MIRA_HQ_easy_half  
MIRA_HQ_half  
POLUS_half  
POLUS_easy_half  
SKELD_easy_half  
を右クリックで保存してください。  
さらに実行するもととなるファイルの  
among_us_tool.py  
を保存してください。（**上書き保存で**保存してください。）  
ツールを起動した際、右端にマップ名が記載されたボタンが表示されていれば成功です。

## 1. 最初にお読みください
　この度はamong usの初心者向け推理支援ツールの使用を検討していただきありがとうございます。
以下、諸注意です。

### 1.1. 使用時の注意事項
　自由に使っていただいてかまいません。  
 まだ至らぬところも多いため、少々使いにくい点が目立ちますが、ご容赦ください。  
 不定期のアップデートで操作性の向上を目指します。  
 無言での使用で全く問題ありませんが、よろしければ**使用いただく際にtwitterにて@amongus_tsunaに連絡をくださると励み**になります。
 
### 1.2. プログラムの改変の注意事項
　個人に合わせてプログラムの改変をして頂いても特にかまいません。  
 ただ、プログラムの改変したものを外部にアップロード・公開する際は、<font color="Red">**事前にtwitterにて@amongus_tsunaに連絡・許可を得たのち、ツイートの一部に私のユーザー名をご記載**</font>ください。
 
### 1.3. SNSへのアップロードの注意事項
　使用時の様子等をSNSにアップロードしていただけると励みになります。  
 **その際は@amongus_tsunaを書くよう**お願いいたします。
  
  
## 2. 環境の準備
　使用する環境はanacondaです。  
 anacondaはプログラムを動かすために必要な仮想の環境です。  
 とりあえず順を追って読んでいただければどなたでも問題ないかと思います。  
 ご存じの方、導入済みの方は「2.1.ツールのインストール」の後、「2.4. 必要モジュールのインストール」まで飛ばし読みで大丈夫です。

### 2.1. ツールのインストール
　githubのこのページの「Code」から、「Download Zip」でデスクトップに保存してください。  
 「among_us_tool-main」というZipファイルで保存されるので右クリックをし展開をしてください。  
 その後、クリックを進めていくと、「among_us_tool」というフォルダと「README」という文書ファイルの２つがあるところまでいったら、「among_us_tool」をコピーして再び**デスクトップに**貼り付けてください。  
 そして、デスクトップに「among_us_tool」というフォルダが表示されていたら完了です！

### 2.2. anacondaのダウンロード
　以下のサイトからダウンロードしてください。  
https://www.anaconda.com/products/individual  
windowsの場合は[64-Bit Graphical Installer]をダウンロードしてください。  
  
ただ、ここまで書いた時点で分かりやすく環境構築を説明してくださっているサイトがありましたので以下をご参考ください。  
（私のPCではもう環境でできてしまっていて…すみません…）  
以下のサイトでは**「コマンドライン環境の設定」の上まで**をおこなっていただければ大丈夫です。  
https://www.python.jp/install/anaconda/windows/install.html  
  
### 2.3. 直前準備
　今からは「among_us_toolのあるフォルダに移動する」という動作を行います。  
 おそらく、今現在anaconda promptに  
   
 (base) C:\Users\----自分のアカウント名--->  
   
 が表示されている状態だと思います。  
 この状態で  
   
 cd desktop  
   
 とうって、enterを押して実行。  
 すると  
   
 (base) C:\Users\----自分のアカウント名---\Desktop>  
   
 となったと思います。  
その後にさらに  
   
 cd among_us_tool  
   
 と打って実行。  
 すると  
   
 (base) C:\Users\----自分のアカウント名---\Desktop\among_us_tool>  
   
 となったと思います。「フォルダが見つからない」ようなエラーが出たら、「2.1 ツールのインストール」のコピー＆貼り付け作業でミスをしている可能性があるとおもいます。  
 これで直前準備はokです。  
 
### 2.4. 必要モジュールのインストール
実行に必要なライブラリをインストールします。  
   
 pip install pillow  
   
と打って実行。  
これで少し読み込んでるような文字が出たらokです。（ここが一番エラーが起きやすいかもしれないので、その際はご連絡ください）

### 2.5. 実行
いよいよ実行です。あとは  
  
python among_us_tool.py  
  
と打って実行すれば、表示できるはずです。
 
 ## 3. 使用方法
 　おそらく直観でできると思います。~~説明がめんどくさくなってしまったとはいえない~~  
  マウスの左クリック、右クリック、ホイールの押し込みで描画、crewの配置、crewの死体の配置ができます。  
  グレー、白置き、黒置きは少し操作方法が異なります。  
  ctrl + cでツールを終了できます。  
  
 ## 4. 最後に
 　この度はamong us toolを使用していただき、ありがとうございます。  
  プログラミング初心者が作ったものですので、クオリティは幾分問題があるとは思いますが、少しでもamong usの楽しむための糧となれば幸いです。  
  
 
 
