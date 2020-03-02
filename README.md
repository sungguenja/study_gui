# README.MD

this repo is record that I study gui with python

I'll use for this pygame and tkinter. if I need other thing I'll add more library like pyQt and otherthing

ty 4 watching and I hope that it will help u or u help me :laughing:



## 200226

> I setup tkinter and I make some widget use tkinter
>
> and I buy some book for following guide
>
> :airplane: I need more more study and guide
>
> I have no time but I have many thing about study like algorithm or python or Web.....
>
> holly jesus......
>
> :man_facepalming:



## 200227

> I study widget and menubar
>
> I have question about making shortcut
>
> I'll know that.... must.....



## 200228

> what is control variable?
>
> it is relative with widget and there are many widget and control variable (like indicatoron or onvalue)
>
> we can use widget value with .set or .get
>
> `Menubutton` object is different with `Menu` object
>
> `smenu.add_radiobutton(label='복사하기',variable=v,value=1, command= selected)`
>
> ㄴ like this we can give some value in v
>
> and we can attain submenu in menu or button in LabelFrame
>
> if you want to make sacle u can use `Scale` method
>
> ​	
>
> what is ttk.Combobox?
>
> we can make entrywidget or dropdown menu with ttk.Combobox
>
> ​	
>
> if u want to use `for` . u must have more think
>
> but u can use that it make ur code shorter
>
> ​	
>
> trace?
>
> this is method that you can call function that u want when u want



## 200301

> listbox can't use `append`
>
> only can use insert
>
> ​	
>
> tkinter can read file
>
> ​	
>
> and we can get data to use `curselction`
>
> like this 
>
> ```python
> sel = lst.curselection()
> one=lst.get(sel)   # we can save data into one
> ```
>
> ​	
>
> and tkinter can `tag`
>
> if we use tag we can adnubustrate more effucuently.
>
> also if we use `tag_bind` we can check mouse action or keyboard action



## 200302

> today I learn event hendling
>
> we can bind event to use `bind` method
>
> ```python
> # like this
> def c_h(hendler):
>     #function
> 
> txt1.bind('k', c_h)  # press k event c_h will happen
> ```
>
> if we want to generate event press two key just write like this `bind('ab', function)`
>
> or if you want to generate event two case (ex. 'a' or 'b') just bind two times
>
> and we want to generate other event with same handler just add '+' like
>
> ​	
>
> values is printed on gui