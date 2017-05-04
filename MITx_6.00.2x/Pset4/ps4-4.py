from ps4 import *

### Begining of program
raw_data = Climate('data.csv')

# Problem 3
y = []
x = INTERVAL_1
for year in INTERVAL_1:
      y.append( np.mean( raw_data.get_yearly_temp('BOSTON', year) ) )

models = generate_models(x, y, [1])

evaluate_models_on_training(x, y, models)
