
from bs4 import BeautifulSoup as b
import requests 
import tkinter 
from tkinter import scrolledtext
from tkinter import messagebox
import os
import webbrowser 

class TechScrap():
  def __init__(s):
      s.root=tkinter.Tk()
      s.src=tkinter.IntVar()
      s.no=tkinter.StringVar()
      s.src.set(1)
      s.color="#5cda99"
      s.root.wm_resizable(0,0)
      s.root.geometry("630x650+320+30")
      s.root.configure(bg=s.color)
      s.root.title("TechScrap")
      s.label_intro=tkinter.Label(s.root,text="Select The Website Number  \n".upper(),font=("arieal",8,"bold"),bg=s.color)
      s.label_intro.place(x=10,y=150)
      #image
      s.image=tkinter.PhotoImage(file=os.path.join(os.getcwd(),"image","web scrap.png"))
      s.label_img=tkinter.Label(s.root,image=s.image,height=130,width=600,bg="white").pack()

      s.label1=tkinter.Label(s.root,text="1.house of bots \n".upper(),font=("arieal",8,"bold"),bg=s.color)
      s.label1.place(x=10,y=180)
      
      s.labe2_intro=tkinter.Label(s.root,text="2.fossbytes\n".upper(),font=("arieal",8,"bold"),bg=s.color)
      s.labe2_intro.place(x=10,y=200)

      s.labe3_intro=tkinter.Label(s.root,text="3.hackernews\n".upper(),font=("arieal",8,"bold"),bg=s.color)
      s.labe3_intro.place(x=10,y=220)

      s.labe4_intro=tkinter.Label(s.root,text="4.pcmag\n".upper(),font=("arieal",8,"bold",),bg=s.color)
      s.labe4_intro.place(x=10,y=240)
      
      s.label5=tkinter.Label(s.root,text="Enter your choice:",font=("arieal",8,"bold"),bg=s.color)
      s.label5.place(x=10,y=260)
      
      s.enter_webno=tkinter.Entry(s.root,font=("arieal",8,"bold"),relief="sunken",textvariable=s.src)
      s.enter_webno.place(x=140,y=260,height=20,width=100)

      s.convert_button=tkinter.Button(s.root,text="Enter",command=lambda:s.start(),fg="red",relief="raised")
      s.convert_button.place(x=250,y=260,height=20,width=70)

      s.image1=tkinter.PhotoImage(file=os.path.join(os.getcwd(),"image","cse world.png"))
       
      s.label_img1=tkinter.Label(s.root,image=s.image1,bg="white",height=120,width=230).place(x=320,y=140)
      
      s.label6=tkinter.Label(s.root,text="Enter the numbers:",font=("arieal",8,"bold"),bg=s.color)
      s.label6.place(x=20,y=600)
  
      s.text = scrolledtext.ScrolledText(s.root,height=20,width=90,wrap=tkinter.WORD,bg="#ff7188",fg="#000000",font=("garamond",10,"bold"),border=5)
      s.text.place(x=10,y=280)

      s.enter_headingno=tkinter.Entry(s.root,font=("arieal",8,"bold"),relief="raised",textvariable=s.no)
      s.enter_headingno.place(x=160,y=600,height=20,width=100)
      
      
      s.exit_button=tkinter.Button(s.root,text="Finished",command=lambda:s.quit(),fg="red",relief="raised")
      s.exit_button.place(x=400,y=600,height=20,width=75)

      s.root.mainloop()
 
  def pcmag(s):
         s.text.delete("1.0",tkinter.END)
         s.enter_headingno.delete(0,tkinter.END)
         s.enter_webno.delete(0,tkinter.END)
         try:
           s.p=requests.get("https://www.pcmag.com").text
           s.soup=b(s.p,features="html.parser")   
         except:
          messagebox.showinfo("ERROR","Plse Make Sure You Have Internet Connection ")

         length=1
         s.heading1=[]
         s.link1=[]
         s.text.insert(tkinter.INSERT,"\t\tThe contents  in pcmag are  \n \n".upper())
         for i in s.soup.find_all("h2"):
           if i.find("a")!=None:
               s.heading1.append(i.text)
               s.text.insert(tkinter.INSERT,str(length)+"."+i.text+"\n\n")
               s.link1.append(i.find("a").get("href"))
               length+=1
         s.sumbit_button=tkinter.Button(s.root,text="Open",command=lambda:s.dispaly(s.link1),fg="red",relief="raised")
         s.sumbit_button.place(x=300,y=600,height=20,width=70)

      
  
  def houseofbots(s):
         s.text.delete("1.0",tkinter.END)
         s.enter_webno.delete(0,tkinter.END)
         try:
           s.p=requests.get("https://www.houseofbots.com").text
           s.soup=b(s.p,features="html.parser")
         except:
            messagebox.showinfo("ERROR","Plse Make Sure You Have Internet Connection ")
         length=1
         s.heading1=[]
         s.link2=[]
         s.text.insert(tkinter.INSERT,"\t\tThe contents  in house of bots are \n \n".upper())
         for i in s.soup.find_all("li"):
            if i.find("h4")!=None:
              s.heading1.append(i.find("h4").text)
              s.text.insert(tkinter.INSERT,str(length)+"."+i.find("h4").text+"\n\n")
              s.link2.append(i.find("a").get("href"))
              length+=1
         s.sumbit_button=tkinter.Button(s.root,text="Open",command=lambda:s.dispaly(s.link2),fg="red",relief="sunken")
         s.sumbit_button.place(x=300,y=600,height=20,width=70)
        
         
  def fossbytes(s):
      
       s.text.delete("1.0",tkinter.END)
       s.enter_webno.delete(0,tkinter.END)
       try:
         s.p=requests.get("https://fossbytes.com").text
         s.soup=b(s.p,features="html.parser")
       except:
          messagebox.showinfo("ERROR","Plse Make Sure You Have Internet Connection ")
       length=1
       s.link3=[]
       s.heading1=[]
       s.text.insert(tkinter.INSERT,"\t\tThe contents  in fossbytes are \n\n".upper())
       for i in s.soup.find_all("h3"):
          s.text.insert(tkinter.INSERT,str(length)+"."+i.text+"\n\n")
          s.heading1.append(i.text)
          s.link3.append(i.find("a").get("href"))
          length+=1
       s.sumbit_button=tkinter.Button(s.root,text="Open",command=lambda:s.dispaly(s.link3),fg="red",relief="sunken")
       s.sumbit_button.place(x=300,y=600,height=20,width=70)
     
          
  def hackernews(s):
        #cleaning the dispaly
        s.text.delete("1.0",tkinter.END)
        s.enter_webno.delete(0,tkinter.END)
        try:
          s.p=requests.get("https://thehackernews.com").text
          s.soup=b(s.p,features="html.parser")
        except:
          messagebox.showinfo("ERROR","Plse Make Sure You Have Internet Connection ")
        length=1
        s. heading1=[]
        s. link4=[]
        s.text.insert(tkinter.INSERT,"\t\tThe contents  in hacker news are\n \n".upper())
        for i in s.soup.find_all("h2"):
             s.text.insert(tkinter.INSERT,str(length)+"."+i.text+"\n\n")
             s.heading1.append(i.text)
             length+=1
        length=0 
        for i in s.soup.find_all("a",class_='story-link'):
           s.link4.append(i.get("href"))
           length+=1
        s.sumbit_button=tkinter.Button(s.root,text="Open",command=lambda:s.dispaly(s.link4),fg="red",relief="sunken")
        s.sumbit_button.place(x=300,y=600,height=20,width=70)
  def dispaly(s,link):
      s.text.delete("1.0",tkinter.END)
      s.enter_webno.delete(0,tkinter.END)
      link_no=s.no.get()
      print(link_no)
      try:
          if(len(link_no)>1):
                #iterate each number if user has more input
                for i in link_no.split(","):
                  #opening web browser
                  webbrowser.open_new_tab(str(link[int(i)-1]))
          else:
                  webbrowser.open(str(link[int(link_no)-1]))
      except:
            messagebox.showinfo("ERROR","Enter A Valid  Number Plse")
      s.text.delete("1.0",tkinter.END)
      s.enter_headingno.delete(0,tkinter.END)
      s.enter_webno.delete(0,tkinter.END)
      s.text["state"]="disabled"
         
  def start(s):
    try:
     c=s.src.get()
     if(c==1):
        s.houseofbots()
     elif(c==2):
        s.fossbytes()
     elif(c==3):
      s.hackernews()
     elif(c==4):
        s.pcmag()
     else:
      messagebox.showinfo("ERROR","Choose Valid Option Plse")
    except:
        messagebox.showinfo("ERROR","Enter A Valid Number Plse")  
  def quit(s):
    s.root.withdraw()

    
def main():
         obj=TechScrap()
main()
    
       


