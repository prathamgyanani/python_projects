'''import tkinter as tk
from tkcalendar import DateEntry

def get_selected_date():
    selected_date = cal.get_date()
    formatted_date = selected_date.strftime("%Y-%m-%d")  # Format the date as desired
    print("Selected Date:", formatted_date)

app = tk.Tk()
app.title("Date Picker Example")

# Create a DateEntry Widget
cal = DateEntry(app, selectmode='day')
cal.pack()
cal1 = DateEntry(app, selectmode='month')
cal1.pack()
cal2 = DateEntry(app, selectmode='year')
cal2.pack()
cal3 = DateEntry(app, selectmode='calendar')
cal3.pack()


# Create a Button to Get the Selected Date
get_date_button = tk.Button(app, text="Get Date", command=get_selected_date)
get_date_button.pack()

app.mainloop()'''
n=int(input())
a=[]
for i in range(n):
    b=int(input())
    a.append(b)
a.sort()
ans=0
th=0
for i in range(len(a)):
    if th
