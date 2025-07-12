import asyncio
from fastmcp import Client

async def main():
    # サーバーファイルに接続
    client = Client("server.py")
    
    async with client:
        # 利用可能なツールを表示
        tools = await client.list_tools()
        print("Available tools:")
        for tool in tools:
            print(f"- {tool.name}: {tool.description}")
        
        print("\n" + "="*50)
        
        # テストコマンド実行
        test_commands = [
            "echo 'Hello World'",
            "ls -la",
            "curl -sL 'https://example.com' | grep -i contact"
        ]
        
        for cmd in test_commands:
            print(f"\nExecuting: {cmd}")
            print("-" * 30)
            result = await client.call_tool("run_command", {"command": cmd})
            print(result.content[0].text)

if __name__ == "__main__":
    asyncio.run(main())