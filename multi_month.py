#imports packages
import os
import pandas as pd



import plotly as py
import plotly.tools as tls
import plotly.graph_objs as go





#https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/os.md
print("Welcome to Graham's ~Multi-Month~ Executive Dashboard!")
current_files = os.listdir("data/")
current_files = pd.DataFrame(current_files)


print("Which files from your data folder would you like to examine? (enter number)")

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

        print("Enter the first series: ")
        user_selection = input()
        user_selection = int(user_selection)
        user_selection = user_selection - 1
        

#accounts for index starting at 0
#selects the filename from list of files
        filename = str(current_files.iloc[user_selection,0])


        #filename = "sales-201803.csv"
        data = pd.read_csv("data/" + str(filename))

        
        print("Enter the second series: ")
        user_selection = input()
        user_selection = int(user_selection)
        user_selection = user_selection - 1

        filename2 = str(current_files.iloc[user_selection,0])
        data2 = pd.read_csv("data/" + str(filename2))




        print("Enter the third series: ")
        user_selection = input()
        user_selection = int(user_selection)
        user_selection = user_selection - 1

        filename3 = str(current_files.iloc[user_selection,0])
        data3 = pd.read_csv("data/" + str(filename3))


        #exploration challenge #1
        #https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
        #https://stackoverflow.com/questions/19482970/get-list-from-pandas-dataframe-column-headers
        header_list = ["date","product","unit price","units sold","sales price"]
        detected_header_list = list(data)
        detected_header_list2 = list(data2)
        detected_header_list3 = list(data3)
        if (detected_header_list != header_list) or (detected_header_list2 != header_list) or (detected_header_list3 != header_list):
            print("File Headers do not match")
            raise Exception
        break
    except:
        pass
    
    print("Try again! Enter file selection:")




print("-----------------------")


data_sets = [data, data2, data3]
filename_list = [filename, filename2, filename3]


#adapted from Prof. Rosetti's filename solution
def month_lookup(month):
    year_month={'01':'January','02':'February','03':'March','04':'April',
    '05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
    '11':'November', '12':'December'}
    return year_month[month]


filename_counter = 0


print("-----------------------")
print("CRUNCHING THE DATA...")
print("-----------------------")


multi_sales_list = []
period_names_list = []
total_sales_list = []

def sortSecond(val): 
    return val[1]  

#https://stackoverflow.com/questions/44630805/pandas-loop-through-list-of-data-frames-and-change-index?rq=1
for index, data_item in enumerate(data_sets):


    
    monthstr = filename_list[filename_counter][-6:-4]
    year_lookup = filename_list[filename_counter][6:10]

    filename_counter = filename_counter + 1

    month = month_lookup(monthstr) 
    year = int(year_lookup)
    month_year = str(month) + " " + str(year)
    period = "Period: " + month_year



    period_names_list.append(month_year)
    
    print("-----------------------")
    print("-----------------------")    
    print(period)



    #finds the sum of the monthly sales 
    total_sales = data_sets[index]["sales price"].sum()
    #https://stackoverflow.com/questions/8183146/two-dimensional-array-in-python

    #formats the data
    total_sales ='${:,.2f}'.format(total_sales)

    total_sales_list.append([])
    total_sales_list[index].append(filename_list[index])
    total_sales_list[index].append(total_sales)
    total_sales_list[index].append(month_year)


    #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html

    worked_data = data_item.groupby(['product']).sum()


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
    multi_sales_list.append(sales_list)


print("_____________________________________")
#https://www.geeksforgeeks.org/python-list-sort/
total_sales_list.sort(key = sortSecond)



print("Top Selling Period: " + str(total_sales_list[2][2]) + ", Sales: " + str(total_sales_list[2][1]))
print("Lowest Selling Period: " + str(total_sales_list[0][2]) + ", Sales: " + str(total_sales_list[0][1]))


#code left in for further developement 
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


trace1 = go.Bar(
    x=item_list,
    y=multi_sales_list[0],
    name=period_names_list[0]
)


trace2 = go.Bar(
    x=item_list,
    y=multi_sales_list[1],
    name=period_names_list[1]
)


trace3 = go.Bar(
    x=item_list,
    y=multi_sales_list[2],
    name=period_names_list[2]
)


data = [trace1, trace2, trace3]


layout = go.Layout(
    title='Top Products',
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
    ),
    barmode = 'group'
)
    

figure = go.Figure(data=data, layout=layout)
py.offline.plot(figure, filename="bar-chart-multi.html", auto_open=True)







