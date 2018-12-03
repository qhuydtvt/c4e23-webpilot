import pyexcel
from collections import OrderedDict

# int()

#2 Prepare data
data = [
  OrderedDict({
    "Name": "Quan",
    "Age": 24,
  }),
  OrderedDict({
    "Name": "H.Duc",
    "Age": 23,
  }),
  OrderedDict({
    "Name": "Chi",
    "Age": 17,
  }),
]

# List comprehension

#3 Save file using save_as()
pyexcel.save_as(records=data, dest_file_name="sample.xlsx")