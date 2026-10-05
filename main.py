import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print("welcome to langchain-course")
    print(os.environ.get("OPENAI_API_KEY"))


if __name__ == "__main__":
    main()
