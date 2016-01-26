# GyazoへのCounting画像アップロードサーバー

あらかじめ指定しておいたCounting画像をGyazoにアップロードし、そのURLをレスポンスとして返す。  
画面のスクリーンショットを取り、ImageMagicで指定した部分を切り抜いて処理する。

## 設定ファイル
setting.confとして以下のように設定する。

```
[Gyazo]
access_token = Gyazo URL

[Counting]
url = Counting URL

[Slack]
url = hook URL
```
