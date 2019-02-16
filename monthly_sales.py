#imports packages
import os
import pandas as pd



import plotly as py
import plotly.tools as tls
import plotly.graph_objs as go





#https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/os.md
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
#https://stackoverflow.com/questions/9781373/a-try-catch-method-in-while-loop
while True:
    try:
        user_selection = input()
        user_selection = int(user_selection)
        user_selection = user_selection - 1
        

#accounts for index starting at 0
#selects the filename from list of files
        filename = str(current_files.iloc[user_selection,0])


        #filename = "sales-201803.csv"
        data = pd.read_csv("data/" + str(filename))

  

        #exploration challenge #1
        #https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
        #https://stackoverflow.com/questions/19482970/get-list-from-pandas-dataframe-column-headers
        header_list = ["date","product","unit price","units sold","sales price"]
        detected_header_list = list(data)
        if detected_header_list != header_list:
            print("File Headers do not match")
            raise Exception
        break
    except:
        pass
    
    print("Try again! Enter file selection:")




print("-----------------------")


#adapted from Prof. Rosetti's filename solution
def month_lookup(month):
    year_month={'01':'January','02':'February','03':'March','04':'April',
    '05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
    '11':'November', '12':'December'}
    return year_month[month]

month = month_lookup(filename[-6:-4]) 
year = int(filename[6:10])


period = "Period: " + str(month) + " " + str(year)
print(period)

print("-----------------------")
print("CRUNCHING THE DATA...")
print("-----------------------")

#finds the sum of the monthly sales 
total_sales = data["sales price"].sum()
#formats the data
total_sales ='${:,.2f}'.format(total_sales)





#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html

worked_data = data.groupby(['product']).sum()

#https://stackoverflow.com/questions/10373660/converting-a-pandas-groupby-object-to-dataframe

worked_data = worked_data.sort_values(['sales price'], ascending = False)


worked_data = pd.DataFrame(worked_data)





print("")
print("Top Selling Products:")
print("_____________________________________")


#prints the top items
#https://stackoverflow.com/questions/43968692/check-if-last-row-in-pandas-df-iterrows check if last row in dataframe
#cases when there aren't 7 products

counter = 0
item_list = []
sales_list = []

for index, row in worked_data.iterrows():

    counter = counter + 1

    if(counter <= 7) or (counter == len(worked_data) - 2):
        total_sale_item = float(row["sales price"])
        total_sale_item ='${:,.2f}'.format(total_sale_item)
        print(str(counter) + ") " + str(index) + ": " + str(total_sale_item))

        item_list.append(str(index))
        sale_format = '${:,.2f}'.format(float(row["sales price"]))
        sales_list.append(sale_format)



print("_____________________________________")

print("TOTAL MONTHLY SALES: " + str(total_sales))







# print("Press B for bar chart, P for pie char, or any key to quit")
# user_selection = input()

# if(user_selection == 'B' or user_selection == 'b'):
#     print("-----------------------")
#     print("VISUALIZING THE DATA...")

#     plt.bar(item_list, sales_list, align='center', alpha=0.5)
#     plt.title("Top 7 Sellers: " + str(month) + " " + str(year))
#     plt.show() # need to explicitly "show" the chart window

# elif(user_selection == 'P' or user_selection == 'p'):
#     fig1, ax1 = plt.subplots()
#     ax1.pie(sales_list, labels=item_list, autopct='%1.1f%%', shadow=True, startangle=90)
#     ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
#     plt.title("Top 7 Sellers: " + str(month) + " " + str(year))

#     plt.show() # need to explicitly "show" the chart window


# print("Thank you!")

#https://plot.ly/python/bar-charts/
#https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/plotly.md
#plots chart using plotly 
#https://plot.ly/python/figure-labels/

data = [go.Bar(
            x=item_list,
            y=sales_list,
            text=sales_list,
            textposition = 'auto',
            marker=dict(
                color='rgb(219, 73, 40)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5),
            ),
            opacity=0.6,

        )]


layout = go.Layout(
    title='Top ' + str(len(item_list)) + ' products for ' + period,
    xaxis=dict(
        title='Product',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Sales ($)',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
    

figure = go.Figure(data=data, layout=layout)
py.offline.plot(figure, filename="bar-char.html", auto_open=True)




#pie chart
#https://plot.ly/python/pie-charts/
fig = {
    'data': [
        {
        'labels': item_list,
        'values': sales_list,
        'type' : 'pie',
        'name' : 'Top Sellers'
    
        }
    ]
}


figure = go.Pie(labels=item_list, values=sales_list)

py.offline.plot(fig, filename="pie_chart.html", auto_open=True)




