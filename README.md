# MLB Win Prediction Model

This project uses a linear regression model to predict how many games a Major League Baseball team will win in a season, based on how many runs it scored and allowed per game.

I used the Lahman Baseball Database. I queried the team data in MySQL Workbench, finished cleaning it with pandas and NumPy, and built the model with scikit-learn. The model uses team seasons from 1990 onward. I left out the 1994, 1995, and 2020 seasons due to the strikes and the COVID year. Although the wins are a season total, the inputs are per game, so those seasons threw off the predictions. Removing them raised R² from 0.782 to 0.892.

The model takes two inputs, runs scored per game and runs allowed per game, and predicts total wins. I trained it on most of the data and kept a portion aside to test it on teams it hadn't seen. On that test data it got an R² of 0.892, a mean absolute error of 2.86 wins, and a root mean squared error of 3.62 wins. In other words, it explains about 89% of the differences in team wins, and a typical prediction is off by less than 3 wins.

The fitted equation is roughly: wins = 82.8 + 16.1 x (runs scored per game) - 16.4 x (runs allowed per game). Scoring one more run per game adds about 16 wins over a season, and allowing one more run per game costs about 16. That lines up with the baseball rule of thumb that about 10 runs equals one win.

The model only describes a season using that same season's runs. It does not forecast future seasons, and it ignores things like defense, injuries, and schedule strength. Inputs also have to be per game, so season totals need to be divided by games played first.

To run it, install pandas, Numpy, Matplotlib, and Scikit-learn, then run `python finalizer.py`. It prints the coefficients and error numbers and shows a graph of predicted wins vs. actual wins.

Data source: Lahman Baseball Database (https://sabr.org/lahman-database/)
