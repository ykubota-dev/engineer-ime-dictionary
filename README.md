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

1. リポジトリを取得する（Git clone または GitHub の **Code → Download ZIP**）。
2. Python 3.10 以降を使用して、リポジトリのルートで以下を実行する。

   ```powershell
   python scripts/build_dictionary.py
   ```

3. `dist/engineer_dictionary.txt` が生成されたことを確認する。
4. タスクバーの「あ」または「A」を右クリックし、**ユーザー辞書ツール** を開く。
5. **ツール → テキストファイルからの登録** で `dist/engineer_dictionary.txt` を選択する。
6. `ふぁすと` などを入力して変換候補を確認する。

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
