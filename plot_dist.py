import pandas as pd
import matplotlib.pyplot as plt


df_products = pd.read_csv('data/special_products_list.csv')

ax = plt.gca()
df_products.plot.scatter(x="sold_in_distinct_parcels", y="marked_has_battery_pct", ax=ax, color='red')
df_products.plot.scatter(x="sold_in_distinct_parcels", y="marked_has_sensitive_pct", ax=ax, color='grey')
df_products.plot.scatter(x="sold_in_distinct_parcels", y="marked_has_liquid_pct", ax=ax, color='cyan')
ax.set_xlim([0, 100])
plt.show()
