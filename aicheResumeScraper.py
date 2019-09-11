#file for AICHE resume scraper
#the purpose of this script is to pull the attatchments from emails and sort them into the groups Fulltime or Co-op

#The directions sent out by AICHE  to the students are as follows:
#save resume as a pdf file
#name format: LastnameFirstnameResume.pdf
#email to vtaicheresume@gmail.com with email subject as <Lastname>,<Firstname>:<Fulltime/Co-op>
#Jim Ownes example would be OwensJamesResume.pdf and the subject of email would be Owens, James : Co-op


import imaplib, email, os,re

#code for logging into gmail
ORG_EMAIL = '@gmail.com'
FROM_EMAIL ='sampleAccount@gmail.com'
FROM_PWD='password'
SMTP_SERVER = 'imap.gmail.com'
SMTP_PORT=993
attachment_dir='C:/Users/andre/Documents/AICHEWebScraper/Attachments'

##function for getting the body payload of an email, while not directly used in the code was useful in the command line
##when people would send emails with blank subjects
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)

## function for getting the attachments of the email
def get_attachments(msg):
    for part in msg.walk():
        if part.get_content_maintype()=='multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()

        if bool(fileName):
            filePath = os.path.join(attachment_dir,fileName)
            with open(filePath,'wb') as f:
                f.write(part.get_payload(decode=True))



## search function to help sift though the HTML code of the RAW email and find the subject line of an email
def search(key,value,con):
    result,data= con.search(None,key,'"{}"'.format(value))
    return data

con= imaplib.IMAP4_SSL(SMTP_SERVER)
con.login(FROM_EMAIL,FROM_PWD)
inboxTuple=con.select('INBOX')
# The inboxTuple give you the total amount of emails present in the Inbox of the email account in the form of the byte number
inboxMail=str(inboxTuple[1])



# this is essentially a round-about way of converting the byte code into a useable number for the for loop below
inboxRaw = re.search("b'(.+?)'", inboxMail)
if inboxRaw:
    foundInbox = int(inboxRaw.group(1))
    print (foundInbox)

#this is the loop of the code that does the actual sorting
bytecode=1
for bytecode in range(1,foundInbox):#end of range should be foundInbox
    index = bytes(str(bytecode),'utf-8')
    print(index)
##This selects the email from the inbox where the b'#' is the numbered email the resultant is HTML code
    con.select('INBOX')
    result, data= con.fetch(index,'(RFC822)')
    raw= email.message_from_bytes(data[0] [1])
    #print(raw)
    text= str(raw)

## for some reason I had difficulty pulling exact words directly from the subject line and the talent pool is
## having some extreme difficulty with following directions
## the logic works off of finding NoneNone and if it doesnt exist (returning and index of -1) a key word was found indicating the correct folder placement.

    subjectCoop1 = str(re.search('Subject: (.+?)op', text)) #this is for pulling full time or coop
    subjectCoop2 = str(re.search('Subject: (.+?)-', text))
    subjectCoop3 = str(re.search('Subject: (.+?)Intern', text))
    coopJoin=subjectCoop1 +subjectCoop2+subjectCoop3
    print(coopJoin)
    subjectFull1= str(re.search('Subject: (.+?)time', text))
    subjectFull2= str(re.search('Subject: (.+?)Time', text))
    fullJoin=subjectFull1 +subjectFull2
    print(fullJoin)


    coopIndex = coopJoin.find('NoneNoneNone')
    fullTimeIndex = fullJoin.find('NoneNone')

    if fullTimeIndex == -1:
        attachment_dir = 'C:/Users/andre/Documents/JimWebScraper/Attachments/Full time'
    elif coopIndex == -1:
        attachment_dir = 'C:/Users/andre/Documents/JimWebScraper/Attachments/Co-op'
    else:
        attachment_dir = 'C:/Users/andre/Documents/JimWebScraper/Attachments/Other'
#finds the attachment name and then renames the attachment to specified
    docRaw = re.search('filename="(.+?)"', text) #this is for pulling full time or coop
    if docRaw:
        foundDoc = docRaw.group(1)
        print (foundDoc)
    get_attachments(raw)
