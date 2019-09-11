##pdf merger for AICHE Resume Web scraper
# the purpose of this script is to merge The PDF resumes into one PDF booklet
from PyPDF2 import PdfFileMerger
import os
# Function to rename multiple files
########################################################################################################################
# since the folder Co-op already sorts the resumes in alphabetical order as they are getting pulled This section
# just moves the resumes into a new folder called 'Co-op processed' and renames the pdf files with the name 'file#'

i = 0
for filename in os.listdir("C:/Users/andre/Documents/AICHEWebScraper/Attachments/Co-op"):
    dst = "file" + str(i) + ".pdf"
    src = 'C:/Users/andre/Documents/JimWebScraper/Attachments/Co-op/' + filename
    dst = 'C:/Users/andre/Documents/JimWebScraper/Attachments/Co-op processed/' + dst
    os.rename(src, dst)
    i += 1

#list maker from number of files in Co-op processed
########################################################################################################################
#creates a list for the total amount of resumes so its easy to run though a for loop and merge all of the folders
pdf_files= list(range(i))
n=0
print(pdf_files)
for n in range(0,i):
    pdf_files[n]="file"+str(n)+'.pdf'
print(pdf_files)

# merges the PDF files
##################################################################
# merges on pdf after another, this code utilizes the list made by the code on lines 21-26
#the if not statement keeps the prior merged files which is helpful when a freshman send in a corrupted PDF file by accident
path='C:/Users/andre/Documents/AICHEWebScraper/Attachments/Co-op processed/'

merger = PdfFileMerger()
for files in pdf_files:
    merger.append(path+files)
if not os.path.exists(path+ 'Coop list Merged.pdf'):
    merger.write(path+"Coop listMerged.pdf")
merger.close()
################################################################
