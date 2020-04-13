import os
import pandas as pd

cities_data = pd.read_csv(os.path.join('Resources', 'cities.csv'))
cities_data.to_html('example.html', index=False, classes=['table', 'table-striped', 'table-hover'])