
from exec_dash_revisited import to_usd


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