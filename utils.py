import pandas as pd
from scipy import stats as st


def locate_genres(df: pd.DataFrame, genre1: str, genre2: str):
  return df.loc[df["Genre"] == genre1, "Critic_Score"], df.loc[df["Genre"] == genre2, "Critic_Score"]


def check_hypothesis(series_1: pd.Series, series_2: pd.Series, alpha=0.001) -> str:
  series_1.dropna(inplace=True)
  series_2.dropna(inplace=True)
  equal_var = False
  print(series_1)
  print(series_2)
  if series_1.std() == series_2.std():
    equal_var = True
  print('std of series1: ', series_1.std(), 'mean of series1:', series_1.mean())
  print('std of series2: ', series_2.std(), 'mean of series2:', series_2.mean())
  results = st.ttest_ind(series_1, series_2, equal_var=equal_var)
  if results.pvalue < alpha:
    return 'decline zero hypothesis'
  return 'its impossible to decline zero hypothesis'