# # Problem 3:

# # Task: Write code that counts how many times each word appears in this sentence:
# # sentence = "the cat and the dog and the bird"
# # Create a dictionary where keys are words and values are the count of how many times they appear.
# # Expected Output:
# # python
# # {'the': 3, 'cat': 1, 'and': 2, 'dog': 1, 'bird': 1}

# sentence ="the cat and the dog and the bird"
# words=[]
# words = sentence.split(" ")
# print(words)

# unique_words={}

# for i in words:
#     if i in unique_words:
#         unique_words[i]+=1
#     else:
#         unique_words[i] = 1
# print(unique_words)