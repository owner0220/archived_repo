def func():
    print("function a.py")

print("여긴 A의 함수 밖입니다. (top-level)")

if __name__ == "__main__":
    print("if문 안쪽입니다.")
else:
    print("import a.py")
    print(__name__)
