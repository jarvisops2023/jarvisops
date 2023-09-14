import sys
import json

def main():
    payload = json.loads(sys.stdin.read())
    content = payload.get("content", "No content provided")
    print(f"Keyword Alert: {content}")

if __name__ == "__main__":
    main()

