import yagmail

receiver = "your@gmail.com" #Receiver's gmail address
body = "Hello there from Yagmail"
filename = "document.pdf"

yag = yagmail.SMTP("my@gmail.com")#Your gmail address
yag.send(
    to=receiver,
    subject="Yagmail test (attachment included",
    contents=body, 
    attachments=filename,
)
