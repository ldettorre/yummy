# Yummy- An online recipe book.
A Data Centric Development(C.R.U.D.) Project.

Welcome to Yummy, my free online recipe book. "Yummy" is a C.R.U.D.(Create, Read, Update, Delete) application I've built using technologies I've studied in the Data Centric Development Module with Code Institute. The theme of the site is a simple recipe book where users can easily and freely find new recipes posted by other users aswell as create, update and delete their own. Users can also decide whether or not to publish recipes for all to see or to keep them private. 


Click [here](https://data-centric-development.herokuapp.com/) to view Yummy live!


## UI & UX 
The Idea for Yummy came from having always watched the Tasty videos that plague my Facebook news feed but not having anywhere easy to store them.  The fact that the "Tasty" recipes always seemed so simple, it made me want to create an equally simple to use site to store them. Although the site is minimalistic in features right now, it provides the user with an easy to navigate User Interface where there is no fear of being lost on the site. The experience is also very user friendly with everything being easy to read on desktop and also comfortable enough on mobile screens.


###### User Stories
The below user stories are catered for on this recipe site.
* As a user I want to browse all recipes publicly available.
* As a user, I want to sort recipes by cuisine.
* As a user, I want to sort recipes by author.
* As a user, I want to post recipes to Yummy publicly, so that other users may view them.
* As a user, I want to post recipes to Yummy privately, so that I can store them there for my own personal use.
* As a user, I want a profile page where I can view all of my recipes both public and private, so that I can locate just my own submissions.



## Technologies used for this project
* HTML
* CSS
* Bootstrap Version 3.3.7
* Python 3.4.3
* Flask 1.0.2
* MongoDB and mLab
* Google Fonts 
* Balsamiq for wiregframing and mock-ups.


## Features

### Existing Features
* Responsive layout and navigation bar.
* Users can create a free account with just a username.
* Users can create, update/edit and delete recipes they have submitted.
* Users can choose to post their recipes publicly or keep it private on their own userpage.
* Only logged in users may add recipes to the site.
* Users can locate all their own recipes on their userpage.
* Any user can sort by Cuisine
* Any user can sort by Author


### Future Features To Implement
Some features can be implemented with more time such as a breakfast, lunch and dinner filter. For other features I would rather move the site over to Django and use AWS (Amazon Web Services) as it is very well equipped for allot of what is mentioned below as opposed to continue with Flask. However, as learning experience I would like to attempt what I can with Flask to better my knowledge on it.

* Allow users to leave comments on recipes and post photos of their attempts.
* Password integration for user accounts.
    * I've made a previous attempt at adding a hashed password feature with no success. However I believe Django would be much better suited for this. 
* Foul language filter for any text input by users.
    * I'd like to revisit Javascript and create something that splits the text a user is inputting into words based on white space, and loop it through a .txt file to check for matches of foul words. If it returns 0 matches it will pass, if it returns one or more then I would code something notifying the user.
* Popularity features such as 'likes' or 'upvotes'
* Further categorization such as breakfast,lunch and dinner.
    * This would be a done in a similar fashion to the current filter for cuisine and author by utilizing for loops and if statements searching for the value matching breakfast, lunch or dinner and rendering it to a template,
* Integration with AWS to allow for image uploading, storage and rendering.
* View counter per recipe and a follower system for users.
* Recipe review in the form of stars out of 5 and a displayed average.
* Detailed footer with external links to social media and an 'About page'. 


## Testing

### Responsiveness
I have used Chrome DevTools and [ResponsiveDesignChecker](https://responsivedesignchecker.com/) to test responsiveness of Yummy across a wide variety of emulated resoloutions.  The site performs very well across the range from 1920x 1080 with the content being well spaced out all the way down to the iPhone 6s at 414 x 736 where the content fits the narrow resoloution well. As with all my projects, I wanted to ensure some form of coverage by incorporating some physical hardware in my testing. 

For physical hardware testing, the site was tested on a Samsung Galaxy S8+, Dell and Asus 15.4 inch 1080p laptops and also in 4k using a Sony tv. 

While the content responded very well in all scenarios, at the lower resoloutions the recipes seemed quite cramped and overly 'busy' with lots of text. I think in future utilizing Javascript to split up the lengthy ingredients and instructions would create a much easier reading experience.

### User Interaction
The following has also been manually tested.
* All navigation bar buttons bring the user to the intended section of the site.
* The navbar buttons change to a single dropdown option when below 768 pixel width.
* Users cannot create an account if a username has already been taken.
* Users cannot log in unless the username has first been registered.
* Flashing messages work as intended should users enter a name that's already registered, log in with a name that has not been registered or add a cuisine that already exists.
* Only logged in users can create recipes, those who are not logged in will receive a flashing message on the index page.

To test the site I've also created a dummy account called 'tester' and ran through the expected uses of a typical user. To show where the tester account has interacted, I've used 'tester' as the text input where possible. In situations where there was an alternate form of input required, I've just selected random options.
* Created a new user called 'tester'.
* Created a new cuisine called 'tester'.
* Created a new recipe titled 'tester'.
* I've located this new recipe on the recipes page, under the tester cuisine section and also under the author name 'tester'.
* Upon clicking 'My profile' in the top corner, I was brought to a page with my posted recipe and name rendered in the greeting.
* I've tested the edit feature by clicking the edit button on my userpage for tester, changing the 'I want this recipe to be available:' from 'public' to 'private' and hitting 'submit recipe'. I can confirm this feature works as it is unavailable on the recipes page, and the cuisine and author pages show the expected message for recipes with the 'private' status.
* In order to test the remove recipe option, I've created a new recipe using the same method as above however using the word ' delete' and then hit the remove recipe button. The 'delete' recipe was removed and upon further inspection of my database using MLab, the tester recipe was available and the delete recipe was not.

## Deployment

### Local
This site was deployed to Heroku. For instructions on how to replicate what I've done to get it running locally, follow the steps below.

1. After you set up a fresh workspace on Cloud9,  clone the app from my GitHub by entering the following into the terminal. 
 
    `git clone https://github.com/ldettorre/yummy.git`
2. Next, enter the following code into the terminal which is needed to change directory.
    
    ` cd yummy`
3. The required installations are then installed with the following code.
    
    `sudo pip3 install -r requirements.txt`
4. If you then try run the app using `python3 recipes.py` you will get the following error:
    
~~~~
"You must specify a URI or set the MONGO_URI Flask config variable"
ValueError: You must specify a URI or set the MONGO_URI Flask config variable 
~~~~

5. The next step is to get your own MongoDB URI and Name set up using mLab with the following steps:
    * Create and account or sign into [mLab](https://mlab.com/).
    * Click on the "+ create new" button.
    * For Cloud9 provider, I've select Amazon Web Services. For plan type, select sandbox and proceed using "Continue" on the bottom.
    * Now from the options available , select one closest to you. For me it's Ireland, then hit "Continue".
    * You now need to name your database, continue on to review the details and hit the order or confirm button.
    * Now you can see the database but need to make a user. Click "User" and then hit "add database user".
    * Fill in the details however as a tip, do not use special characters.
    * You have now set up a database and user to access it.

6. Once you've done all that, take the URI string at the top of the page in mLab and copy it into your recipes.py file as seen below.
    ~~~~
    app.config["MONGO_URI"] = Place your URI string here inside quotes
    app.config["MONGO_DBNAME"] = Place your db name here inside quotes
    ~~~~
7. Now save the file, type `python3 recipes.py` into your terminal and open the app in your browser. You can perform a test by entering a new cuisine and trying the other features such as user and recipe creation. Once you've tested the site, reload your mLab database page to see the collections appear with documents inside.

Your database is now connected succesfully and the site is running locally.

### Heroku Deployment

1. I've gone to [Heroku](https://www.heroku.com/) and set up a free account.
2. On my dashboard, I clicked on "New" and then "Create a new app".
3. Entered a name, selected a region and hit "Create app".
4. For Deployment Method, I chose GitHub then searched for my repository.
5. I've enabled deploying from the master branch then hit "Deploy Branch".
6. Once the app is ready, you can hit "View" to see it live.


## Credits

### Acknowledgements
* Credit to Michael Park for spotting my flash messages rendering incorrect information during development.
* I'd also like to acknowledge Yoni Lavi for his mentoring during this project.

### Media
* I sourced photos and fonts for this site from:
     * [Pexels.com](https://www.pexels.com/)
     * [Pixabay.com](https://pixabay.com/en/)
    * [Google Fonts](https://fonts.google.com/)

### Content
* Recipe information and other descriptions were taken from [Wikipedia](https://en.wikipedia.org/wiki/Main_Page) and [BBC Good Food](https://www.bbcgoodfood.com/).

