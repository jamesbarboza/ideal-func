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

# Setup

Python version: >= 3.10


```
git clone https://github.com/jamesbarboza/ideal-func.git
cd ideal-func
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

# run the app
python app.py --train ../datasets/train.csv --ideal ../datasets/ideal.csv --test  ../datasets/test.csv
```

## Resources

- least squared method - [Youtube Link](https://www.youtube.com/watch?v=P8hT5nDai6A)
- least squared method - blog - [link](https://www.edureka.co/blog/least-square-regression/)



## Validation

Ideal functions:
  1. training-25
  2. training-3
  3. training-22
  4. training-21
