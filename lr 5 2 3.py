with open('text.txt', 'r') as file:
    content = file.read()  # Читает весь файл
    words = content.split() 
    
    print("Слов в вашем файле: " + str(len(words)))  возвращение длины строки