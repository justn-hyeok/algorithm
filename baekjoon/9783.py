message = input()
result = []

for char in message:
    if char.islower():  # 소문자
        result.append(f"{ord(char) - ord('a') + 1:02d}")
    elif char.isupper():  # 대문자
        result.append(f"{ord(char) - ord('A') + 27:02d}")
    elif char.isdigit():  # 숫자
        result.append(f"#{char}")
    else:  # 그 외 문자
        result.append(char)

print("".join(result))
