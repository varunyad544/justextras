import requests
import bs4 as bs
from tkinter import *

def showanswer():
    url=e1.get()
    word=e2.get()
    page=requests.get(url).content
    unicode_str=page.decode('utf8')
    encoded_str=unicode_str.encode('ascii','ignore')
    soup=bs.BeautifulSoup(encoded_str,'lxml')
    count=0

    for string in soup.strings:
        if word in string:
            count+=1
    Label(root,text='Url:{} \ncontains {} occurrences of word {}'.format(url,count,word)).grid(row=5,column=1)

root =Tk()
root.title('No. of words in a website')
root.geometry('300x200')

Label(root,text='enter url:').grid(row=0)
Label(root,text='enter word:').grid(row=1)

e1=Entry(root)
e2=Entry(root)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
 
Button(root,text='Quit',command=root.quit).grid(row=3,column=0,sticky=W,pady=4)
Button(root,text='Show',command=showanswer).grid(row=3,column=1,sticky=W,pady=4)

root.mainloop()
