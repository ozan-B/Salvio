from mac.vendor import Vendors



ozan = input("Enter Mac Address = ")
example = Vendors()
example.get_by_single(ozan)
print(example.response)