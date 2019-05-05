import pandas as pd


def to_usd(input):


	result = "${0:,.2f}".format(input)


	return result



def get_top_sellers(worked_data):

	#deal with item list


	counter = 0
	item_list = []
	sales_list = []
	total_sale = 0
	overall_total_sales = 0

	for index, row in worked_data.iterrows():

		overall_total_sales = overall_total_sales + row["sales price"]

		counter = counter + 1

		if(counter <= 7) or (counter == len(worked_data) - 2):
			#total_sale_item = float(row["sales price"])
			#changed for revisit
			#total_sale_item ='${:,.2f}'.format(total_sale_item)
			total_sale_item = (float(row["sales price"]))
			total_sale = total_sale + total_sale_item
			total_sale_item = to_usd(total_sale_item)

			print(str(counter) + ") " + str(index) + ": " + str(total_sale_item))



			item_list.append(str(index))
			#item_list.append(str(row['Name:']))
			#item_list.append(str(row["product"]))
			#changed for revisit
			#sale_format = '${:,.2f}'.format(float(row["sales price"]))
			#sale_format = to_usd(float(row["sales price"]))

			sales_list.append(total_sale_item)

	sales_dataframe = pd.DataFrame(
		{
		'item_list': item_list,
		'sales_list': sales_list,
		'total_sale': total_sale,
		'total_overall_sale': overall_total_sales
		})



	return sales_dataframe



if __name__ == "__main__":
	print("main")