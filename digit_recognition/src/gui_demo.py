from tkinter import *
import psycopg2 as db
import pandas as pd
from tkinter.filedialog import askopenfilename

body = Tk('Test')


def message_show():
    filename = askopenfilename()
    connect = db.connect(database="postgres", user="postgres", password="root", host="127.0.0.1", port="5432")
    cur = connect.cursor()
    insert_sql = 'insert into stock_prices(date,symbol,open,close,low,high,volume) values(%s, %s, %s, %s, %s, %s, %s);'
    data_set = pd.read_csv(filename)
    print(len(data_set))
    print(filename)
    stocks = data_set.iloc[0:851265, 0:7].values
    for stock in stocks:
        s_date = stock[0]
        s_symbol = stock[1]
        s_open = stock[2]
        s_close = stock[3]
        s_low = stock[4]
        s_high = stock[5]
        s_volume = stock[6]
        cur.execute(insert_sql, (s_date, s_symbol, s_open, s_close, s_low, s_high, s_volume))

    connect.commit()
    cur.close()


B = Button(body, text="Choose file", command=message_show)
B.place(x=50, y=50)
body.mainloop()

print("data saved .. successfully")
