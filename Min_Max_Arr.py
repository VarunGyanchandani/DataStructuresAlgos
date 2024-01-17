
def getMin(arr, n):
	res = arr[0]
	for i in range(1,n):
		res = min(res, arr[i])
	return res

def getMax(arr, n):
	res = arr[0]
	for i in range(1,n):
		res = max(res, arr[i])
	return res

arr = [12, 5620, 45, 67, 3]
n = len(arr)
print ("Minimum element of array:", getMin(arr, n))
print ("Maximum element of array:", getMax(arr, n))
