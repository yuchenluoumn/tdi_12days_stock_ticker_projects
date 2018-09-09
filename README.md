# Flask on Heroku

The Heroku link of this project can be seen here:
https://agile-escarpment-32727.herokuapp.com/
How to use the app:
First blank input stock ticker
Second blank input starting date
Thrid blank input ending date

It only support the close price for now.

Some note for me:
## Step 1: Setup and deploy
links: For windows system how to deploy: http://www.gtlambert.com/blog/deploy-flask-app-to-heroku
only thing needs to change from the tutorial 
heroku create --buildpack https://github.com/kennethreitz/conda-buildpack.git
instead of just heroku create. It will let the heroku know the version of python used in the app.
If not used, the error future = 3.2.0 cannot find will appear

When the heroku apps reaches the maximum, should delete some of the existing ones. by heroku apps:destroy appName

When heroku remote does not show the repository, 
first: git remote rm heroku
then: git remote add heroku https://git.heroku.com/appname.git

how to add existing project to github using command line: 
https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/

## Step 2: Get data from API and put it in pandas
- Use the `requests` library to grab some data from a public API. This will
  often be in JSON format, in which case `simplejson` will be useful.
- Build in some interactivity by having the user submit a form which determines which data is requested.
- Create a `pandas` dataframe with the data.
- when the range of date is input from the user, the backend trys to find the records fall in this period, using a for loop. It is not very efficient, can be optimized using some other more clever command. Will update if I figure out.

## Step 3: Use Bokeh to plot pandas data
- Create a Bokeh plot from the dataframe.
- Consult the Bokeh [documentation](http://bokeh.pydata.org/en/latest/docs/user_guide/embed.html)
  and [examples](https://github.com/bokeh/bokeh/tree/master/examples/embed).
- Make the plot visible on your website through embedded HTML or other methods - this is where Flask comes in to manage the interactivity and display the desired content.
- Some good references for Flask: [This article](https://realpython.com/blog/python/python-web-applications-with-flask-part-i/), especially the links in "Starting off", and [this tutorial](https://github.com/bev-a-tron/MyFlaskTutorial).

