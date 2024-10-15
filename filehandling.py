# #program of read a file
# f = open("esay.txt")

# print(f.read())

# #program to read a file if file is located in different location 
# # s=open("C:\Users\91701\Desktop\Rise of Artificial Intelligence rajit.docx")

# # print(s.read())

# #program to read first num elements of file
# k=open("esay.txt")

# print(k.read(7))

# #program to read one line of a file
# l=open("esay.txt")

# print(l.readline())
# #by calling two times we can print the next line
# print(l.readline())
# print(l.readline())


# #By looping through the lines of the file, you can read the whole file, line by line:
# x=open("esay.txt")
# for i in x:
#     print(i)

# #close the file when you are done with it
# j=open("esay.txt")
# print(j.readline())
# j.close()

# #program to write a file and read it
# n=open("esay.txt","a")
# n.write("my hometown name is amb")
# n.close()
# n=open("esay.txt")
# print(n.read())

# #program to overwrite the content
# m=open("esay.txt","w")
# m.write("hello welcome again")
# m.close()
# m=open("esay.txt","r")
# print(m.read())

# #program to make a new file and give error if file name exist
# e=open("myfile.txt","x")


# #create a file if the specified file does not exist
# f = open("myfile.txt", "w")
# f.write("my content")
# f.close()

# #remove a file or delete a file
# import os
# os.remove("myfile.txt")

# #check if file exists then delete it
# import os
# if os.path.exists("myfile.txt"):
#     os.remove("myfile.txt")
# else:
#     print("file does not exist")

# #program for remove a folder
# import os
# os.rmdir("myfolder")


# s=open(r"C:\Users\91701\Desktop\Rise of Artificial Intelligence rajit.docx")
# print(s)

#open file from other path 
# from docx import Document
# # Open the .docx file
# doc = Document(r"C:\Users\91701\Desktop\Rise of Artificial Intelligence rajit.docx")
# # Read and print the content of the document
# for paragraph in doc.paragraphs:
#     print(paragraph.text)


# from docx import Document
# x=Document(r"C:\Users\91701\Desktop\Research Paper-Gaming Industry in India.docx")
# for i in x.paragraphs:
#     print(i.text)



# import fitz  # PyMuPDF

# # Open the PDF file
# pdf_document = fitz.open(r"C:\Users\91701\Desktop\Rise of Artificial Intelligence rajit.pdf")

# # Iterate through each page
# for page_num in range(len(pdf_document)):
#     page = pdf_document.load_page(page_num)
#     text = page.get_text()
#     print(f"Page {page_num + 1} content:\n{text}")

# # Close the PDF document
# pdf_document.close()


# import fitz 
# a=fitz.open(r"C:\Users\91701\Desktop\Nano Technology.pdf")
# for i in range(len(a)):
#     page=a.load_page(i)
#     text=page.get_text()
#     print(f"Page {i+1} content:\n{text}")

# a.close()



