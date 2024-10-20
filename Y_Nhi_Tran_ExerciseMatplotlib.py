# Y Nhi Tran
# Exercise Matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in Co2.html - ignore first 2 lines of the file
co2 = pd.read_html('Co2.html', header=2)[0]

# Read in SeaLevel.csv - ignore the lines have '#'
sea_level = pd.read_csv("SeaLevel.csv", comment='#', sep=',')
sea_level['year'] = sea_level['year'].apply(lambda x: int(x))
# print(co2)

# Calculate the average of the 'average' column for each year
co2_avg = co2.groupby(['year']).mean().reset_index()
co2_avg.rename(columns={'average': 'CO2'}, inplace=True)
co2_avg2 = co2_avg[["year", "CO2"]]
# print(co2_avg2)

# Calculate the average of the 'TOPEX' column for each year
sea_level_avg = sea_level.groupby(['year']).mean().reset_index()
sea_level_avg = sea_level_avg.fillna(0)
sea_level_avg.rename(columns={'TOPEX/Poseidon': 'Sea_Level'}, inplace=True)
sea_level_avg2 = sea_level_avg[["year", "Sea_Level"]]
# print(sea_level_avg2)

# Merge the two dataframes on the 'year' column
result = pd.merge(co2_avg2, sea_level_avg2, how='outer', on='year')

# Print out the result
print(result.to_string())

# Display the data in ONE plot/graph instead of two.
n_groups = len(result)

means_CO2 = result.loc[:, "CO2"]
means_sea_level = result.loc[:, "Sea_Level"]

index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, means_CO2,
                 bar_width,
                 alpha=opacity,
                 color='b',
                 error_kw=error_config,
                 label='CO2')

rects2 = plt.bar(index + bar_width, means_sea_level,
                 bar_width,
                 alpha=opacity,
                 color='r',
                 error_kw=error_config,
                 label='Sea Level')

plt.xlabel('Total carbon emissions and mean sea level anomaly global ocean')
plt.ylabel('Years')
plt.title('TOTAL CARBON EMISSIONS AND MEAN SEA LEVEL ANOMALY GLOBAL OCEAN 1959-2019')
plt.xticks(index + bar_width / 2, result.loc[:, "year"], rotation='vertical')
plt.legend()

plt.tight_layout()
plt.show()
