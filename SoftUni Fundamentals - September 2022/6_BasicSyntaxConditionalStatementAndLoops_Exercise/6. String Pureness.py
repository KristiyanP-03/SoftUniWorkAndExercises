inputs = int(input())
for each_input in range(inputs):
    word = input()
    if "," in word or "." in word or "_" in word:
        print(f"{word} is not pure!")
    else:
        print(f"{word} is pure.")