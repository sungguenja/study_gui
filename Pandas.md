# Pandas.md

> I will record my learning about pandas



## 200304

> we can save data with using pandas
>
> 1. list
>
>    ```python
>    import pandas as pd
>    data = [['mike',50,60,70],
>           ['luara',70,20,90],
>           ['ranya',70,70,70],
>           ['cammy',80,60,70]]
>    df = pd.DataFrame(data, columns=['name','math','eng','phy'])
>    ```
>
> 2. dict
>
>    ```python
>    import pandas as pd
>    data = {'name':['mike','luara','ranya','cammy'],
>           'math':[50,70,70,80],
>           'eng':[60,20,70,60],
>           'phy':[70,90,70,70]}
>    df=pd.DataFrame(data)
>    ```
>
> 3. read file
>
>    ​	
>
> and we can see what we choose data
>
> ```python
> df.head(2) # we can see mike, luara
> df.tail(3) # we can see luara~cammy
> ```
>
> ​	
>
> we can add column like using below
>
> ```python
> df['sum'] = df['math'] + df['eng'] + df['phy']
> df['avg'] = df['sum']/3
> # if u want to see 2number behind . df.round(2)
> ```
>
> 

