

Analysis Questions
1. Discover user cohorts who are more likely to be retained.
2. Does the frequency and/or volume of daily activity relate to a user’s likelihood to
survive?

## Analysis Techniques

**Simple Correlation**

Looks like `has_extension` explains 96% of variance (.983**2)

In [309]: d.corrwith(d.survived)
Out[309]:
id                 0.005369
hhi                0.005283
age                0.188981
survived           1.000000
programming       -0.007271
health             0.032463
shopping           0.015879
news               0.007890
travel            -0.015264
uses_spaces       -0.001979
uses_recipes       0.038003
uses_home         -0.005853
has_extension      0.983454
has_app            0.586517
avg_ctr           -0.019852
avg_num_queries    0.005742
dtype: float64


## Exploration and Issues.

Missing data
- is it missing at random?

(pwd now: ~/gits/Neeva)
❯ wc *csv
   10001   10001  452044 demographic.csv
    8055    8055  581059 product.csv
   10001   10001  336638 query_intent.csv
   28057   28057 1369741 total
❯ less product.csv






Retained is "survived"

So:  
Obvious things:

- logistic regression with all variables.
- model selection

Or:
decision tree


In interest of time, skipping:
- cleaning

Dumbest


```
In [305]: d.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 8054 entries, 0 to 8053
Data columns (total 19 columns):
 #   Column           Non-Null Count  Dtype
---  ------           --------------  -----
 0   id               8054 non-null   int64
 1   job              8054 non-null   object
 2   gender           8054 non-null   object
 3   hhi              8054 non-null   int64
 4   age              8054 non-null   int64
 5   region           8054 non-null   object
 6   survived         8054 non-null   bool
 7   programming      8054 non-null   bool
 8   health           8054 non-null   bool
 9   shopping         8054 non-null   bool
 10  news             8054 non-null   bool
 11  travel           8054 non-null   bool
 12  uses_spaces      8054 non-null   bool
 13  uses_recipes     8054 non-null   bool
 14  uses_home        8054 non-null   bool
 15  has_extension    8054 non-null   bool
 16  has_app          8054 non-null   bool
 17  avg_ctr          8054 non-null   float64
 18  avg_num_queries  8054 non-null   float64
dtypes: bool(11), float64(2), int64(3), object(3)
memory usage: 652.8+ KB
```



#