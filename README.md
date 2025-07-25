# Simple Subprocess MCP Server

シェルコマンドを実行するシンプルなModel Context Protocol (MCP) サーバー

## 概要

このMCPサーバーは、LLMアプリケーションから任意のシェルコマンドを安全に実行できるツールを提供します。FastMCPフレームワークを使用して構築されており、subprocessモジュールを通じてコマンドを実行します。

## 機能

- 任意のシェルコマンドの実行
- 30秒のタイムアウト設定
- エラーハンドリング
- 標準出力とエラー出力の取得

## 必要条件

- Python 3.11+
- uv (パッケージマネージャー)

## インストール

```bash
# 依存関係をインストール
uv sync
```

## 使用方法

### 1. サーバーの起動

```bash
# 直接実行
uv run python server.py

# または fastmcp コマンドを使用
uv run fastmcp run server.py
```

### 2. テストクライアントの実行

```bash
uv run python test_client.py
```

### 3. LLMアプリケーションとの統合

Claude Desktop等のMCP対応アプリケーションで使用する場合、設定ファイルにサーバーのパスを追加してください。

## API

### `run_command(command: str) -> str`

指定されたシェルコマンドを実行し、結果を返します。

**パラメータ:**
- `command`: 実行するシェルコマンド（文字列）

**戻り値:**
- 成功時: コマンドの標準出力
- エラー時: エラーメッセージ（終了コードとエラー出力を含む）

**例:**

```python
# ファイル一覧を取得
result = await client.call_tool("run_command", {"command": "ls -la"})

# Webサイトから連絡先情報を抽出
result = await client.call_tool("run_command", {
    "command": "curl -sL \"[URL]\" | grep -i contact"
})
```

## セキュリティ考慮事項

⚠️ **注意**: このサーバーは任意のシェルコマンドを実行できるため、信頼できる環境でのみ使用してください。

### 推奨される対策

1. **サンドボックス環境での実行**
2. **コマンドフィルタリングの実装**
3. **実行権限の制限**
4. **ログ監視の実装**

## ファイル構造

```
simple-subprocess/
├── server.py          # MCPサーバーのメイン実装
├── test_client.py     # テスト用クライアント
├── pyproject.toml     # プロジェクト設定
├── uv.lock           # 依存関係ロックファイル
└── README.md         # このファイル
```

## 実装例

### Webスクレイピング

```bash
curl -sL "[URL]" | grep -i -E "(contact|お問い合わせ|連絡|メール|mail|email|tel|電話)"
```

### ファイル操作

```bash
# ディレクトリ内容の確認
ls -la

# ファイルの検索
find . -name "*.py" -type f

# テキストファイルの内容確認
cat README.md
```

### システム情報の取得

```bash
# システム情報
uname -a

# ディスク使用量
df -h

# プロセス一覧
ps aux
```

## トラブルシューティング

### タイムアウトエラー

コマンドの実行時間が30秒を超える場合、タイムアウトエラーが発生します。長時間実行されるコマンドの場合は、server.pyの`timeout`値を調整してください。

### パーミッションエラー

実行権限が不足している場合は、適切な権限を付与するか、sudo を使用してください（ただし、セキュリティリスクを考慮してください）。

## ライセンス

MIT License

## 貢献

プルリクエストやイシューの報告を歓迎します。