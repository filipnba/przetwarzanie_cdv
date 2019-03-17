word = input("Podaj liczbê: ")
numberOfElements = len(word)

result = ""
i=0

while i < numberOfElements:
  if word[i] == "0":
    result = result + "zero "
  elif word[i] == "1":
    result = result + "jeden "
  elif word[i] == "2":
    result = result + "dwa "
  elif word[i] == "3":
    result = result + "trzy "
  elif word[i] == "4":
    result = result + "cztery "
  elif word[i] == "5":
    result = result + "piêæ "
  elif word[i] == "6":
    result = result + "szeœæ "
  elif word[i] == "7":
    result = result + "siedem "
  elif word[i] == "8":
    result = result + "osiem "
  elif word[i] == "9":
    result = result + "dziewiêæ "
  i = i + 1

print(result)