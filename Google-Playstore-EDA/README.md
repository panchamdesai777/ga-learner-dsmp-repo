### Project Overview

 **## Problem Statement**

Google Play Store serves as the official app store for the Android operating system, allowing users to browse and download applications. Success of an app is largely determined by its ratings.

But is there any particular pattern among high rated apps? Does size or genre of the app play a role in determining its high rating?

Conduct an EDA on the Google Play Store data and try to explore whether given the data, ratings of an can be predicted.

The dataset has details of 10841 apps with following 13 features

- Feature	                   -Description

- App	                   - Name of the app
- Category	           -Category the app broadly belongs to
- Rating	                   -Customer rating of the app
- Size	                    -Size of the app
- Installs	                   -Number of Installs done for the app
- Type	                   -Type of the app(Free/Paid)
- Price	                    -Price of the app(if any)
- Content Rating	    -What age group is the app appropriate for
- Genre	                    -What all genres the app belongs to
- Last Updated	    -Date on which the app was last updated
- Current Ver	            -Version of the app
- Android Ver	            -Android Version required by the device to the run the app


### Learnings from the project

 After completing this project, I now have a better understanding of certain methods of EDA and Data Preprocessing. 




### Approach taken to solve the problem

 - Data Loading
- Removal of  rows having rating more than 5
- Null Value Treatment
- Correlation between Rating vs Category
- Correlation between Installs vs Ratings
- Correlation between Price vs Ratings
- Correlation between Genres vs Ratings ( splitting genres and keeping only one genre per app in case of multiple genres)
- Correlation between Last Updated vs Ratings


 


