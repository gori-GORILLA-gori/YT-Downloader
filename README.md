# YT-Downloader

YouTube動画を最高画質・音質でダウンロードし、MP4へ変換できるGUIツール（Python製）

## 🔧 特徴

- ✅ GUIによる簡単操作（Tkinter使用）
- ✅ yt-dlpにより最高画質＆音質を自動選択
- ✅ `cookies.txt` 対応（ログインが必要な動画もDL可能）

## 🌐 対応ブラウザ

以下のブラウザから `cookies.txt` を出力してログイン動画に対応可能：

- Google Chrome
- Microsoft Edge
- Mozilla Firefox
- Brave
- Opera
- Vivaldi
※ `cookies.txt` は、上記のような拡張機能で現在ログインしている状態のCookieを出力したテキストファイルです。プレミアム会員限定動画などのダウンロードに必要です。
　 `cookies.txt` は [Get cookies.txt](https://chromewebstore.google.com/detail/cclelndahbckbenkjhflpdbgdldlbecc?utm_source=item-share-cb) 等の拡張機能で取得できます。

## 📺 対応サイト

yt-dlpにより多数の動画サイトに対応。代表的な例：
<p>☑→動作確認済み</p>
<ul>
  <li>☑ YouTube</li>
  <li>☑ ニコニコ動画</li>
  <li>☑ bilibili</li>
  <li>&emsp;SoundCloud</li>
  <li>☑ Twitter / X（公開動画）</li>
  <li>☑ Twitch（アーカイブ）</li>
  <li>&emsp;Vimeo</li>
  <li>&emsp;Dailymotion</li>
  <li>&emsp;TikTok（非ログイン再生対応）</li>
  <li>&emsp;Facebook動画（公開範囲に依存）</li>
</ul>

👉 他にも数百のサイトに対応しています（完全なリストは [yt-dlp公式対応サイト一覧](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md) を参照）。

## 💻 使い方

1. GitHub右上の `Code` ボタンから `Download ZIP` を選択し、本リポジトリをダウンロード
2. ダウンロードしたZIPファイルを展開
3. 展開後に出てくる `YT-Downloader.zip` も解凍
4. `YT-Downloader` フォルダ内の `YT-Downloader.exe` を実行
5. 必要な情報を入力：
   - 動画のURL
   - 保存先フォルダ
   - ログを表示するか
   - Cookieを使うか（ログインが必要な動画用）
6. 「ダウンロード開始」ボタンを押して完了！

## 仕様
- ファイル名は動画のタイトルになります
- エラーを防ぐために日本語などの特殊文字はすべて`_`に変換されて保存されます
- MP4でダウンロードされます
- コーデック（例：HEVC/H.265など）の影響で、標準のメディアプレイヤーでは再生できない可能性があります（bilibiliで確認済み）。


## 📦 同梱ファイル

- [ffmpeg関連実行ファイル＆DLL（再配布許可済み）](https://github.com/BtbN/FFmpeg-Builds/releases)
- [yt-dlp.exe（MITライセンス）](https://github.com/yt-dlp/yt-dlp)

## 📁 ファイル構成


```
YT-Downloader
┣━Code
┃ ┣━YT-Downloader.py
┃ ┣━ffmpeg.exe
┃ ┣━ffplay.exe
┃ ┣━ffprobe.exe
┃ ┣━yt-dlp.exe
┃ ┗━ffmpegのdllファイル
┣━YT-Downloader.zip
┣━LICENSE
┗━README.md
```
## 📝 ライセンス

本ツールは MIT License で公開されています。  
同梱されている yt-dlp および ffmpeg もそれぞれ MIT または再配布可能な非制限ライセンスです。

## 🔗 作者

by [gori-GORILLA-gori](https://github.com/gori-GORILLA-gori)

