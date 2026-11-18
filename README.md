# Engineer IME Dictionary

Windows 11 / Microsoft IME 向けのエンジニア用ユーザー辞書です。技術用語・開発業務用語・日本語の定型文をまとめて登録できます。

## 収録内容

| ファイル | 件数 | 例 |
| --- | ---: | --- |
| `dictionary/technical.txt` | 70 | `ふぁすと → FastAPI`, `らんぐぐらふ → LangGraph` |
| `dictionary/business.txt` | 40 | `ようけん → 要件定義`, `きりもどし → 切り戻し` |
| `dictionary/templates.txt` | 40 | `おせ → お世話になっております。`, `ごかく → ご確認のほど、よろしくお願いいたします。` |
| **合計** | **150** | |

## 使い方（Windows 11 / Microsoft IME）

### 1. ZIPを展開する

GitHub の **Code → Download ZIP** からZIPをダウンロードし、エクスプローラーで右クリックして **すべて展開** を選択します。

展開したフォルダの中から、`README.md`・`dictionary`・`scripts` が並んでいるフォルダを開きます。このフォルダが **リポジトリのルートディレクトリ（実行ディレクトリ）** です。

例えばダウンロードフォルダに展開した場合、実際の場所は次のようになります（フォルダ名はダウンロードしたブランチにより異なります）。

```text
C:\Users\<ユーザー名>\Downloads\engineer-ime-dictionary-develop-basic-enginner-dectionary\
├── README.md
├── dictionary\
└── scripts\
    └── build_dictionary.py
```

### 2. PowerShellを開く

**Windows PowerShell または PowerShell** で実行できます。エクスプローラーで上記のルートディレクトリを開き、**アドレスバーに `powershell` と入力してEnter** を押してください。そのフォルダをカレントディレクトリとしてPowerShellが起動します。

PowerShellで以下を実行し、`README.md` と `scripts` が表示されることを確認します。

```powershell
Get-Location
Get-ChildItem
```

別の場所でPowerShellを開いた場合は、`cd "C:\Users\<ユーザー名>\Downloads\<展開したフォルダ名>"` でルートディレクトリに移動してください。パスは自分のPCに合わせて置き換えます。

### 3. Pythonで辞書を生成する

Python 3.10以降が必要です。まずインストール済みか確認します。

```powershell
python --version
```

`python` が認識されない場合、WindowsのPython Launcherが使える環境では `py --version` を試してください。両方使えない場合はPythonをインストールする必要があります。

**実行ディレクトリは `README.md` があるルートディレクトリです。** `scripts` ディレクトリに移動する必要はありません。

```powershell
python scripts/build_dictionary.py
```

`python` が使えず `py` が使える場合は、`py scripts/build_dictionary.py` を実行します。

成功すると `Generated dist/engineer_dictionary.txt (150 entries)` と表示され、ルートディレクトリ配下に `dist\engineer_dictionary.txt` が生成されます。

### 4. Microsoft IMEへ登録する

1. タスクバーの「あ」または「A」を右クリックし、**ユーザー辞書ツール** を開く。
2. **ツール → テキストファイルからの登録** を選択する。
3. 生成された `dist\engineer_dictionary.txt` を指定する。
4. `ふぁすと` などを入力し、変換候補に `FastAPI` が表示されるか確認する。

Microsoft IME の表示やメニュー名は環境・バージョンによって異なる場合があります。必要に応じて Windows の IME 設定からユーザー辞書ツールを開いてください。

**注意:** このファイルは入力候補を登録するためのものです。GitHub 上のデータを更新しても PC 側の辞書は自動的には更新されません。再生成と再登録が必要です。既存辞書は事前にバックアップしてください。再登録時に同じ単語が重複登録扱いになることがあります。

## 編集・追加方法

辞書の管理元は `dictionary/` 以下の UTF-8 テキストファイルです。1行につきタブ区切りの3列を記述します。

```text
読み<TAB>変換結果<TAB>品詞
ふぁすと<TAB>FastAPI<TAB>名詞
おせ<TAB>お世話になっております。<TAB>短縮よみ
```

`<TAB>` は文字列ではなく**実際のタブ文字**です。ヘッダー行は書かないでください。空行および `#` で始まるコメント行は無視されます。

品詞は `名詞` と `短縮よみ` の2種類をサポートします。ビルド時に列数・空欄・品詞・重複を検査します。エラーがある場合は出力せず終了コード1を返します。

生成ファイルは UTF-16（BOM付き）、Windows 改行（CRLF）です。Python の標準ライブラリだけを使うため追加パッケージは不要です。

## 構成

```text
engineer-ime-dictionary/
├── LICENSE
├── README.md
├── dictionary/
│   ├── technical.txt
│   ├── business.txt
│   └── templates.txt
├── scripts/
│   └── build_dictionary.py
└── dist/
    └── engineer_dictionary.txt  # スクリプトで生成
```

## ライセンス

MIT License（`LICENSE` 参照）
