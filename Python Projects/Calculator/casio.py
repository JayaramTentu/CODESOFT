import tkinter as tk

calculation=" "

def add(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evalute():
      global calculation
      try:
          calculation=str(eval(calculation))
          text_result.delete(1.0,"end")
          text_result.insert(1.0,calculation)
      except:
         clear()
         text_result.insert(1.0,"Error")
         

def clear():
     global calculation
     calculation=" "
     text_result.delete(1.0,"end")
     


root=tk.Tk()
root.geometry("300x500")
text_result=tk.Text(root , height=5, width=16,font=("Arial",24))
text_result.grid(columnspan=5)

btn_Clear=tk.Button(root,text="C",command=clear,width=5,font=("Arial",14))
btn_Clear.grid(row=2,column=0)

btn_Delete=tk.Button(root,text="√",command=lambda:add('√'),width=5,font=("Arial",14))
btn_Delete.grid(row=2,column=1)

btn_Modulo=tk.Button(root,text="%",command=lambda:add('%'),width=5,font=("Arial",14))
btn_Modulo.grid(row=2,column=2)

btn_Divide=tk.Button(root,text="/",command=lambda:add('/'),width=5,font=("Arial",14))
btn_Divide.grid(row=2,column=3)



btn_1=tk.Button(root,text="7",command=lambda:add(7),width=5,font=("Arial",14))
btn_1.grid(row=3,column=0)

btn_2=tk.Button(root,text="8",command=lambda:add(8),width=5,font=("Arial",14))
btn_2.grid(row=3,column=1)

btn_3=tk.Button(root,text="9",command=lambda:add(9),width=5,font=("Arial",14))
btn_3.grid(row=3,column=2)

btn_product=tk.Button(root,text="X",command=lambda:add('X'),width=5,font=("Arial",14))
btn_product.grid(row=3,column=3)


btn_4=tk.Button(root,text="4",command=lambda:add(4),width=5,font=("Arial",14))
btn_4.grid(row=4,column=0)

btn_5=tk.Button(root,text="5",command=lambda:add(5),width=5,font=("Arial",14))
btn_5.grid(row=4,column=1)

btn_6=tk.Button(root,text="6",command=lambda:add(6),width=5,font=("Arial",14))
btn_6.grid(row=4,column=2)

btn_Minus=tk.Button(root,text="-",command=lambda:add('-'),width=5,font=("Arial",14))
btn_Minus.grid(row=4,column=3)



btn_7=tk.Button(root,text="1",command=lambda:add(1),width=5,font=("Arial",14))
btn_7.grid(row=5,column=0)

btn_8=tk.Button(root,text="2",command=lambda:add(2),width=5,font=("Arial",14))
btn_8.grid(row=5,column=1)

btn_9=tk.Button(root,text="3",command=lambda:add(3),width=5,font=("Arial",14))
btn_9.grid(row=5,column=2)

btn_sum=tk.Button(root,text="+",command=lambda:add('+'),width=5,font=("Arial",14))
btn_sum.grid(row=5,column=3)




btn_10=tk.Button(root,text="0",command=lambda:add(0),width=5,font=("Arial",14))
btn_10.grid(row=6,column=0)

btn_11=tk.Button(root,text="00",command=lambda:add(00),width=5,font=("Arial",14))
btn_11.grid(row=6,column=1)

btn_13=tk.Button(root,text=".",command=lambda:add('.'),width=5,font=("Arial",14))
btn_13.grid(row=6,column=2)

btn_equals=tk.Button(root,text="=",command=evalute,width=5,font=("Arial",14))
btn_equals.grid(row=6,column=3)


root.mainloop()
