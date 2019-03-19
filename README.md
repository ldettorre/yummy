# Yummy- An online recipe book.
A Data Centric Development(C.R.U.D.) Project.

Welcome to Yummy, my free online recipe book. "Yummy" is a C.R.U.D.(Create, Read, Update, Delete) application I've built using technologies I've studied in the Data Centric Development Module with Code Institute. The theme of the site is a simple recipe book where users can easily and freely find new recipes posted by other users aswell as create, edit and delete their own. Users can also decide whether or not to publish recipes for all to see or to keep them private. 


Click [here](https://data-centric-development.herokuapp.com/) to view Yummy live!


## UI & UX 

###### User Stories
The below user stories are catered for on this recipe book site.
* As a user, I want to browse recipies freely by cuisine, so I may find recipies based on the cuisine I'm in the mood for.
* As a user I want to browse all recipes publicly available on the site, so I may browse all the options at once.
* As a user, I want to post my own recipes to Yummy, so that other people can make use of them.
* As a user, I want to store my recipies privately for my own use.
* As a user, I want to see all my recipes on my own profile page.



## Technologies used for this project
* HTML
* CSS
* Bootstrap Version 3.3.7
* Python 3.4.3
* Flask 1.0.2
* MongoDB
* Google Fonts 
* Balsamiq for wiregframing and mock-ups.


## Features

### Existing Features
* Responsive layout and navigation bar.
* Users can create a free account with just a username.
* Users can create, update/edit and delete recipes they have submitted.
* Users can cho0se to post their recipies publicly or keep it private on their userpage.
* Only logged in users may add recipes to the site.
* Users can locate all their own recipes on their userpage.
* Any user can sort by Cuisine
* Any user can sort by Author


### Future Features
Some features can be implemented with more time such as a breakfast, lunch and dinner filter. For other features I would rather move the site over to Django and use AWS (Amazon Web Services) as it is very well equipped for allot of what is mentioned below.

* Allow users to leave comments on recipes and post photos of their attempts.
* Password integration for user accounts.
    * I've made a previous attempt at adding a hashed password feature with no success. However I believe Django would be much better suited for this. 
* Foul language filter for any text input by users.
    * I'd like to revisit Javascript and create something that splits the text a user is inputting into words based on white space, and loop it through a .txt file to check for matches of foul words. If it returns 0 matches it will pass, if it returns one or more then I would code something notifying the user.
* Popularity features such as 'likes' or 'upvotes'
* Further categorization such as breakfast,lunch and dinner.
    * This would be a done in a similar fashion to the current filter for cuisine and author by utilizing for loops and if statements searching for the value matching breakfast, lunch or dinner and rendering it to a template,
* Integration with AWS to allow for image uploading.
* View counter per recipe and a follower system for users.
* Recipe review in the form of stars out of 5 and a displayed average.
* Detailed footer with external links and an 'About page'. 


## Testing

### Responsiveness
I have used Chrome DevTools and [ResponsiveDesignChecker](https://responsivedesignchecker.com/) to test responsiveness of Yummy across a wide variety of emulated resoloutions.  The site performs very well across the range from 1920x 1080 with the content being well spaced out all the way down to the iPhone 6s at 414 x 736 where the content fits the narrow resoloution well. As with all my projects, I wanted to ensure some form of coverage by incorporating some physical hardware in my testing. 

For physical hardware testing, the site was tested on a Samsung Galaxy S8+, Dell and Asus 15.4 inch 1080p laptops and also in 4k using a Sony tv. 

While the content responded very well in all scenarios, at the lower resoloutions the recipies seemed quite cramped and overly 'busy' with lots of text. I think in future utilizing Javascript to split up the lengthy ingredients and instructions would create a much easier reading experience.

### User Interaction
The following has also been manually tested.
* All navigation bar buttons bring the user to the intended section of the site.
* The navbar buttons change to a single dropdown option when below 768 pixel width.
* Users cannot create an account if a username has already been taken.
* Users cannot log in unless the username has first been registered.
* Flashing messages work as intended should users attempt the 2 steps above.
* Only logged in users can create recipies, those who are not logged in will receive a flashing message on the index page.

To test the site I've also created a dummy account called 'tester' and ran through the expected uses of a typical user. To show where the tester account has interacted, I've used 'tester' as the text input where possible. In situations where there was an alternate form of input required, I've just selected random options.
* Created a new user called 'tester'.
* Created a new cuisine called 'tester'.
* Created a new recipe titled 'tester'.
* I've located this new recipe on the recipes page, under the tester cuisine section and also under the author name 'tester'.
* Upon clicking 'My profile' in the top corner, I was brought to a page with my posted recipe and name rendered in the greeting.
* I've tested the edit feature by clicking the edit button on my userpage for tester, changing the 'I want this recipe to be available:' from 'public' to 'private' and hitting 'submit recipe'.
* I can confirm this feature works as it is unavailable on the recipies page, and the cuisine and author pages show the expected message for recipes with the 'private' status.
* In order to test the remove recipe option, I've created a new recipe using the same method as above however using the word ' delete' and then hit the remove recipe button. The 'delete' recipe was removed and upon further inspection of my database using MLab, the tester recipe was available and the delete recipe was not.

## User Stories


