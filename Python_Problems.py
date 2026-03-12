# Problem 1:

# Task: Write code that counts how many times each word appears in this sentence:
# sentence = "the cat and the dog and the bird and the cat again"

sentence = "the cat and the dog and the bird and the cat again"
words=[]
words = sentence.split(" ")

unique_words=[]

for i in words:
    if i not in unique_words:
        unique_words.append(i)
print(unique_words)

for i in unique_words:
    count  = 0
    for j in words:
        if i==j:
            count+=1
    print(i,"appears",count,"times")
             
