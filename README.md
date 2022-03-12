# ideal-func

3 datasets:
Train: x, y1-y4
Test: x,y
Ideal: x, y1-y50

## Criteria

- Ideal function: minimize the sum of all y-deviation
- Test case: existing max deviation of the calculated regression doesn't exceed the largest deviation between training and ideal functions chosen of it more than sqrt(2)Test case: existing max deviation of the calculated regression doesn't exceed the largest deviation between training and ideal functions chosen of it more than sqrt(2)

## objectives

- Load train and ideal CSV datasets into an SQLite database using sqlalchemy
- The final table must consist 4 columns: x,y, ideal-function,deviation


## Resources

- least squared method - [Youtube Link](https://www.youtube.com/watch?v=P8hT5nDai6A)
