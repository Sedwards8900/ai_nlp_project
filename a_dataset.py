# Data collection for english tweets
import twint

c = twint.Config()


c.Search = ['hurricane ian']
c.Limit = 4000
c.Since = '2022-09-23 00:00:00'
# c.Until = '2022-10-03 00:00:00'
c.Lang = "en"
c.Store_csv = True
c.Output = "hurricane_ian.csv"
c.Translate = True
c.TranslateDest = "es"

twint.run.Search(c)



# # Data collection for spanish tweets
# import twint

# c = twint.Config()

# c.Search = ['huracan ian']
# c.Limit = 4000
# c.Since = '2022-09-23'
# c.Until = '2022-10-03'
# c.Lang = "es"
# c.Store_csv = True
# c.Output = "hurricane_ian_spanish2.csv"

# twint.run.Search(c)