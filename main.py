
# write in file using with()function
with open('file.txt', 'w') as file:
  file.write("Sup. I'm a capybara and I'm better than everybody in this stupid room.")
  file.close()

  # split file into words
  with open('file.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are...")
    for line in data:
      word = line.split()
      print(word)
      file.close()
      