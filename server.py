import subprocess
from fastmcp import FastMCP

mcp = FastMCP("Simple Subprocess Server")

@mcp.tool
def run_command(command: str) -> str:
    """Execute a shell command using subprocess and return the output"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30  # 30秒でタイムアウト
        )
        
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error (exit code {result.returncode}): {result.stderr}"
    
    except subprocess.TimeoutExpired:
        return "Error: Command timed out after 30 seconds"
    except Exception as e:
        return f"Error executing command: {str(e)}"

if __name__ == "__main__":
    mcp.run()