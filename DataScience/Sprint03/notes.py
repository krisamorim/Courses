#troubleshooting
# 1. Identify the delimeter (Although the file is a CSV, the delimiter is not always a comma, so identify the delimiter.)
# use the .head() method to check the first few rows of the file and identify the delimiter. For example, if the file is tab-delimited, you will see that the values are separated by tabs instead of commas.
# Use the sep= parameter so that the file import uses a different separator.

# → no parameter:
#   Afghanistan|Kajaki Hydroelectric Power Plant Afghanistan|33   0|32   322|65   119|Hydro|
# 0                                 Afghanistan|Kandahar DOG|10   0|31    67|65   795|Solar|
# 1                                 Afghanistan|Kandahar JOL|10   0|31   623|65   792|Solar|
# 2           Afghanistan|Mahipar Hydroelectric Power Plant ...   0|34   556|69  4787|Hydro|
# 3           Afghanistan|Naghlu Dam Hydroelectric Power Pla...   0|34   641|69   717|Hydro|
# 4           Afghanistan|Nangarhar (Darunta) Hydroelectric ...  55|34  4847|70  3633|Hydro|

# → using sep parameter: data = pd.read_csv('/datasets/gpp_modified.csv', sep='|')
#   Afghanistan       Kajaki Hydroelectric Power Plant Afghanistan   33,0   32,322   65,119  Hydro  Unnamed: 6
# 0  Afghanistan                                       Kandahar DOG   10,0    31,67   65,795  Solar         NaN
# 1  Afghanistan                                       Kandahar JOL   10,0   31,623   65,792  Solar         NaN
# 2  Afghanistan      Mahipar Hydroelectric Power Plant Afghanistan   66,0   34,556  69,4787  Hydro         NaN
# 3  Afghanistan   Naghlu Dam Hydroelectric Power Plant Afghanistan  100,0   34,641   69,717  Hydro         NaN
# 4  Afghanistan  Nangarhar (Darunta) Hydroelectric Power Plant ...  11,55  34,4847  70,3633  Hydro         NaN

# 2. handling the header

# → using header and name parameter
# header= None: this tells pandas that the file does not have a header row, so it will not treat the first row as column names.
# e.g.: data = pd.read_csv('/datasets/gpp_modified.csv', sep='|', header=None)

# → using name parameter: this allows you to specify the column names manually. You can provide a list of column names that correspond to the columns in the file.
# e.g.: 
# column_names = [
#     'country',
#     'name',
#     'capacity_mw',
#     'latitude',
#     'longitude',
#     'primary_fuel',
#     'owner'
# ]
# data = pd.read_csv('/datasets/gpp_modified.csv', sep='|', header=None, names=column_names)

# 3. handling supended points
# on read_csv() period is standard, lets use the dacimal parameter to specify that the decimal separator is a comma instead of a period.
# e.g.: data = pd.read_csv('/datasets/gpp_modified.csv', sep='|', header=None, names=column_names, decimal=',')