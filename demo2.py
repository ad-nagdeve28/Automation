import fitz

pdf_path = r"D:\invoice\invoice 3.pdf"

doc = fitz.open(pdf_path)
text = ""
for page in doc:
    text+=page.get_text()
# print(text)


print(type(text))

for s in text:
    if("Total" == s):
        print(s)


# Start
infn = r"C:\Users\Aditya.Nagdeve\Desktop\demo\input.txt"
outfn = 'out.txt'
text_search = 'Example Phrase'










# def mysearcher(infn, outfn, text_search):
#     """
#     Read infn file and find text_search, if found write the the 2 lines below it, to outfn file.
#     """   
#     found = 0  # counter if text_search is found
#     ret = []  # temp storage

#     with open(outfn, 'w') as w:  # open file for writing overwrite mode
#         with open(infn, 'r') as f:  # open file for reading
#             for lines in f:
#                 line = lines.rstrip()

#                 if found:
#                     ret.append(line)  # add new line in the ret list

#                     # Write to output if ret list has two elements.
#                     if len(ret) == 2:
#                         w.write(f'{ret[0]}:{ret[1]}\n')  # write to output

#                         # Update ret and found counter.                        
#                         found -= 1
#                         if found == 0:
#                             ret = []  # reset
#                         else:
#                             # Don't reset ret, there is successive text_search found.
#                             ret.pop(0)  # just remove the first element

#                 if text_search in line:
#                     found += 1


# mysearcher(infn, outfn, text_search)