buah = ("apel", "jeruk", "ceri", "durian", "apel", "mangga")

print(buah[2:5])
convert = list(buah)
convert.pop(3)
convert.insert(2,"manggis")
result = tuple(convert)
print(result)