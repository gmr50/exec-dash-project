# TODO: import some modules and/or packages here

# TODO: write some Python code here to produce the desired functionality...


#products=sales['product'].unique()
import os
import pandas as pd



filename = "sales-201803.csv"
data = pd.read_csv(filename)





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





print("************************")
worked_data = worked_data.sort_values(['sales price'], ascending = False)




worked_data = pd.DataFrame(worked_data)



print("************************")


#prints the top items

counter = 0
for index, row in worked_data.iterrows():

	counter = counter + 1
	total_sale_item = float(row["sales price"])
	total_sale_item ='${:,.2f}'.format(total_sale_item)
	print(str(counter) + ") " + str(index) + ": " + str(total_sale_item))

    #print(index + ") " + str(row["product"]) + str(row["sales price"]))


print("************************")

print("TOTAL MONTHLY SALES: " + str(total_sales))



print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")

