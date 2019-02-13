# TODO: import some modules and/or packages here

# TODO: write some Python code here to produce the desired functionality...


#products=sales['product'].unique()
import os
import pandas as pd



import plotly.plotly as py
import plotly.tools as tls


import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt



print("***************")
print("Welcome to Graham's Executive Dashboard!")
current_files = os.listdir("data/")
current_files = pd.DataFrame(current_files)


print("Which file from your data folder would you like to examine? (enter number)")

#prints the file names
counter =0
for index, row in current_files.iterrows():

    counter = counter + 1
    detected_file_name = str(row[0])
    
    print(str(counter) + ") " + detected_file_name)





user_selection = 0


#gets user file selection

while True:
    try:
        user_selection = input()
        user_selection = int(user_selection)
        user_selection = user_selection - 1
        

# picked_file = str(current_files[user_selection])
#accounts for index starting at 0
#selects the filename from list of files
        filename = str(current_files.iloc[user_selection,0])

        break
    except:
        pass
    
    print("Try again! Enter file selection:")



#key error



#filename = "sales-201803.csv"
data = pd.read_csv("data/" + str(filename))



print("-----------------------")


#adapted from Prof. Rosetti's filename solution
def month_lookup(month):
    year_month={'01':'January','02':'February','03':'March','04':'April',
    '05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
    '11':'November', '12':'December'}
    return year_month[month]

month = month_lookup(filename[-6:-4]) 
year = int(filename[6:10])

print("Period: " + str(month) + " " + str(year))

print("-----------------------")
print("CRUNCHING THE DATA...")
print("-----------------------")

#finds the sum of the monthly sales 
total_sales = data["sales price"].sum()
#formats the data
total_sales ='${:,.2f}'.format(total_sales)






worked_data = data.groupby(['product']).sum()





worked_data = worked_data.sort_values(['sales price'], ascending = False)




worked_data = pd.DataFrame(worked_data)




print("")
print("Top 7 Selling Products:")
print("_____________________________________")


#prints the top items

counter = 0
item_list = []
sales_list = []

for index, row in worked_data.iterrows():

    counter = counter + 1

    if(counter <= 7):
        total_sale_item = float(row["sales price"])
        total_sale_item ='${:,.2f}'.format(total_sale_item)
        print(str(counter) + ") " + str(index) + ": " + str(total_sale_item))

        item_list.append(str(index))
        sales_list.append(float(row["sales price"]))


        #print(index + ") " + str(row["product"]) + str(row["sales price"]))


print("_____________________________________")

print("TOTAL MONTHLY SALES: " + str(total_sales))







print("Press B for bar chart, P for pie char, or any key to quit")
user_selection = input()

if(user_selection == 'B' or user_selection == 'b'):
    print("-----------------------")
    print("VISUALIZING THE DATA...")

    plt.bar(item_list, sales_list, align='center', alpha=0.5)
    plt.show() # need to explicitly "show" the chart window

elif(user_selection == 'P' or user_selection == 'p'):
    fig1, ax1 = plt.subplots()
    ax1.pie(sales_list, labels=item_list, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show() # need to explicitly "show" the chart window


print("Thank you!")





