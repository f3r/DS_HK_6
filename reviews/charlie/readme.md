Please find a first draft of my project here - https://github.com/Screengoose/DS_homework/blob/master/Final%20project%20analysis.ipynb

I’ve spent a lot of time doing EDA in order to come up with something to model.  And I think I have something!  I have split user pours into three buckets:

1. Tasters - this is where the user pours less than 10oz beer (but has money left on their card to pour more - over $6)
2. Full drinks - user pours over 10oz
3. Card balance finishers - when a user has less than $6 on their card

I am planning to build a model that predicts a user’s action after they have poured a “taster”.  My belief is that it might be possible, especially when taking the beer brand into account.

As a bit of guidance, which model would you suggest I use to attempt this?  Also, any ideas for other models would be welcomed!