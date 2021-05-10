import geonamescache
import twint
import nest_asyncio
nest_asyncio.apply()


def get_tweets_by_city(city):
    cfg = twint.Config()
    cfg.Search = 'inDriver'
    cfg.Custom['tweet'] = ['date', 'user_id', 'tweet']
    cfg.Limit = 1000000
    cfg.Near = city.lower()
    cfg.Since = '2021-04-08'
    cfg.Filter_retweets = True
    cfg.Store_csv = True
    cfg.Output = f'inDriver_brazil_{city}.csv'
    twint.run.Search(cfg)


cities_list = [_val['name'] for _val in geonamescache.GeonamesCache().get_cities().values() if _val['countrycode'] == 'BR']
for c in cities_list:
    get_tweets_by_city(c)
