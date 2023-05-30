class WaveletTree:
	def __init__(self, arr, low, high):
		self.low = low
		self.high = high
		self.freq = []

		# If there is only one element, create a list with a single element
		if low == high:
			self.freq = [0]
			for i in range(len(arr)):
				self.freq.append(self.freq[i] + 1)
			return

		# Split the input array into two based on the midpoint of the range
		mid = (low + high) // 2
		self.freq = [0]
		left_arr = []
		right_arr = []
		for i in range(len(arr)):
			if arr[i] <= mid:
				left_arr.append(arr[i])
				self.freq.append(self.freq[i] + 1)
			else:
				right_arr.append(arr[i])
				self.freq.append(self.freq[i])

		# Recursively create Wavelet Trees for the left and right arrays
		self.l = WaveletTree(left_arr, low, mid)
		self.r = WaveletTree(right_arr, mid + 1, high)


# Driver code
size = 5
high = -float('inf')
arr = [1, 5, 2, 6, 4, 4]

# Object of class wavelet tree
obj = WaveletTree(arr, min(arr), max(arr))
print(obj.r.r.freq)