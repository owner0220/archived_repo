import a

print("top-level: b.py")
a.func()

if __name__ == "__main__":
    print("b.py를 직접 실행")
else:
    print("import b.py")
