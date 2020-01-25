# data import and manipulation
import pandas as pd

"""
inventors (PatentsView)
pi (FedRePORTER)
assignees (PatentsView)
organizations (FedRePORTER)
"""

# Load data
inventors = pd.read_csv('../Data/inventors_cleaned.csv')
pi = pd.read_csv('../Data/pi_cleaned.csv')
assignees = pd.read_csv('../Data/assignees_cleaned.csv')
organizations = pd.read_csv('../Data/organizations_cleaned.csv')

# Top universities by grant
organizations = organizations[organizations['org_name'].str.contains('university') |
                              organizations['org_name'].str.contains('college') |
                              organizations['org_name'].str.contains('institute')]

summary = organizations.copy()
summary['count'] = 1
summary = (summary.groupby(['org_name', 'state'])['count']
                  .count()
                  .reset_index()
                  .sort_values(by = 'count', ascending = False)
          )
print(summary.head(10))

# Top organizations by patent
summary = assignees.copy()
summary['count'] = 1
summary = (summary.groupby(['org_name'])['count']
                  .count()
                  .reset_index()
                  .sort_values(by = 'count', ascending = False)
          )
print(summary.head(10))

# Top PIs by grants
summary = pi.copy()
summary['count'] = 1
summary = (summary.groupby(['name_first', 'name_last', 'city', 'state'])['count']
                  .count()
                  .reset_index()
                  .sort_values(by = 'count', ascending = False)
          )
print(summary)

# Top inventors by patent
summary = inventors.copy()
summary['count'] = 1
summary = (summary.groupby(['name_first', 'name_last', 'state'])['count']
                  .count()
                  .reset_index()
                  .sort_values(by = 'count', ascending = False)
          )
print(summary)