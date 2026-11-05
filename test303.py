
import os

os.system('cls')

print()

#-------------------------------------------------
file_path = r"C:\Users\Mamun\Desktop\Python_Code\file1.txt"

with open(file_path, "r") as file:
    content = file.read().lower()

print(" Content of the file:   \n", content.lower())    

#-------------------------------------------------

word_list = list(content.upper().split())

print("\nWord List:", word_list)
print("Total Words:", len(word_list),"\n")

#-------------------------------------------------

unique_word_set =   set(word_list)
print("Unique Words (set):", unique_word_set)
print("Total Unique Words:", len(unique_word_set), "\n")

#-------------------------------------------------

unique_word_list = list(unique_word_set)
unique_word_list.sort()
word_list_unique_sorted =unique_word_list

print("Sorted Unique Words:", word_list_unique_sorted,'\n')

#-------------------------------------------------
i=1
for uw in word_list_unique_sorted:
     c=0
     for w in word_list:
         if (uw==w and uw != ''):
             c+=1   
            
     print(f"Word {i}: {uw}, Count: {c}")
     i+=1
print()    

#-------------------------------------------------



