import pandas as pd
from exec_dash_revisited import to_usd, get_top_sellers


def test_to_usd():

	test_passed = False
	input = 10000
	result = to_usd(input)



	if(result[0] == '$' and result[3] == ',' and result[-1] == '0' and result[-2] == '0'):
		test_passed = True


	assert test_passed == True

	#reset for next test
	#testing now with trailing decimals
	test_passed = False

	result = to_usd(10.99999999)

	if(result == "$11.00"):
		test_passed = True

	assert test_passed == True

	#reset for next test
	#testing with fewer decimals

	test_passed = False
	result = to_usd(1.1)
	if(result == "$1.10"):
		test_passed = True

	assert test_passed == True



def test_top_sellers():
	#in order to test the usage of the get top sellers function, must transform data read from csv into expected



	#reads data in
	data = pd.read_csv("test_csv/test.csv")
	data = pd.DataFrame(data)
	product_index_list = []

	#sets the index as the product, is done outside of this function
	for item in data['product']:
		product_index_list.append(item)
	data.set_index([product_index_list])




	worked_data = data.groupby(['product']).sum()
	#https://stackoverflow.com/questions/10373660/converting-a-pandas-groupby-object-to-dataframe
	worked_data = worked_data.sort_values(['sales price'], ascending = False)
	worked_data = pd.DataFrame(worked_data)



	#invokes the function
	results = get_top_sellers(worked_data)




	#asserts the first item in the list is the expected value
	assert results['sales_list'][0] == "$150.00"

	#asserts that the sales list should be in string format
	assert type(results['sales_list'][0]) == str

	#asserts value of the total sale of all items from that month and the total sale of the top 7 items
	#these two values should be different in the case of the test.csv
	assert results['total_overall_sale'][0] == 196
	assert results['total_sale'][0] == 192

	#asserts naming has been done properly, product names are used as indices
	assert results['item_list'][6] == "test4"

	#should only be 7 items on the list of top products
	assert len(results) == 7



