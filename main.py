import pandas as pd

url_name_basics = "https://datasets.imdbws.com/name.basics.tsv.gz"
name_basics = pd.read_csv(url_name_basics, sep='\t')

url_title_akas = "https://datasets.imdbws.com/title.akas.tsv.gz"
title_akas = pd.read_csv(url_title_akas, sep='\t')

url_title_basics = "https://datasets.imdbws.com/title.basics.tsv.gz"
title_basics = pd.read_csv(url_title_basics, sep='\t')

url_title_crew = "https://datasets.imdbws.com/title.crew.tsv.gz"
title_crew = pd.read_csv(url_title_crew, sep='\t')

url_title_episode = "https://datasets.imdbws.com/title.episode.tsv.gz"
title_episode = pd.read_csv(url_title_episode, sep='\t')

url_title_principal = "https://datasets.imdbws.com/title.principals.tsv.gz"
title_principal = pd.read_csv(url_title_principal, sep='\t')

url_title_ratings = "https://datasets.imdbws.com/title.ratings.tsv.gz"
title_ratings = pd.read_csv(url_title_ratings, sep='\t')