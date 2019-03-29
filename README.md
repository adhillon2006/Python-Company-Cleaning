## Cleaning Company Names with FuzzyWuzzy
FuzzyWuzzy is a python library that helps to provide the user a probability of matching a specific word using Levenshtein Distance. This
means you are able to find typos and spelling mistakes alot easier.

For more information: https://github.com/seatgeek/fuzzywuzzy

## Current Problem
In several system having a free text field can result in many similar company name. For example, you can have Intel with multiple
abbreviations like Intel Corp, Intel Americas, Intel Inc, and etc. This could make it difficult to complete an analysis. 

## Solution
Use FuzzyWuzzy and utilize the fuzz.token_set_ration() function in the library that is not case sensitive. Also I would suggest
using company names without any Inc or Corp at the end to help improve accuracy of the library. In addition, companies with short names
could have false positives. 

# Future Project
Looking to webscrape all the subsidaries using Google
