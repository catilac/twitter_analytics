How to get it started:
========================

Install packages: 

`pip install -r requirements.txt`

There are 3 migrations which need to be run:

    python init_twitter_employees.py # Gets all users into the database
    python get_klout_scores.py # Saves the klout scores for the users.
    python get_tweets.py # Gets 100k tweets. 

Afterwards, just run `python dashboard.py` and go to `localhost:5000/`




This was a fun problem, and now I have a dataset. Unfortunately I don't have enough time
to make things perfect, or go for my custom bonus item of doing sentiment analysis.

Luckily, thats something I'm interested in and I'll do that in my free time.


 * The graphs are really ugly, and I need to display more detailed information in
  a window when hovering over a point.

 * The top users graph is weird as a scatter plot. The interesting users have a lot of favs
  or a lot of RTs. There aren't many users with both. Also some users seem to be going into the millions? I would look at some users with less than 10k RTs and Favs. I think there is
  something there.

 * I chose a bad mongodb python lib. I used mongo. pypi said it held a lot of weight,
  but I should have started with pymongo. The worst part is that for actual web app, I
  went with pymongo. If I had more time, I'd change that, since it's something that would
  drive me crazy. It is driving me crazy.

 * I used python. I'm really loving it, but there are some things that I need to do research
  on:

    - Package management: I want to use something like bundler for ruby. I am using X libraries, each with X_i version number and with a command it'll install all of them.

    - Idiomattic python. Could be useful. I'm sure there are nicer ways to do things.
    I'm not too unhappy because I think the code is readable
