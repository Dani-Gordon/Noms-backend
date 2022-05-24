
<img width="1389" alt="Screen Shot 2022-05-20 at 22 30 17" src="https://user-images.githubusercontent.com/99892502/169635424-06839ff6-7b45-4b33-ac60-54e7a9bab040.png">

Noms was inspired by my Mom and allows users to search through recipes, enter their own recipes and save their favorite recipes to prepare for their weekly grocery list. Phase 2 of Noms will prepare the list for you based on your meals for the week. 

**This repo contains code for the backend server only; code for the frontend lives** [here](https://github.com/Dani-Gordon/Noms-frontend.git)

## Installation
Check out the live application [here](https://nomnomnoms.netlify.app/)! \
Feel free to register and then use your own login credentials, or try a demo using:
- Email: user10@user.com
- Password: Password!1

## Goals and Timeframe: 
- Build a full-stack application using a Python Django API (using Django REST Framework to serve your data from a Postgres database). Consume your API with a separate front-end built with React. Have multiple relationships and CRUD functionality for a few models. Implement thoughtful user stories/wireframes to develop your MVP and stretch goals. Have an entity relationship diagram showing the proposed database schema. Have a visually impressive design. Follow suggestions to be deployed online so it's publicly accessible.
- 13 days (solo project)

## Technologies Used:
React (JavaScript) | Sass | CSS | Bulma | Python | Django | PostgreSQL | Heroku | Netlify

# Site Overview
***

View of Noms as a non-registered user. Features include the ability to Register, Login and view the Recipe Book: 
> <img width="1000" alt="Screen Shot 2022-05-20 at 18 10 54" src="https://user-images.githubusercontent.com/99892502/169626395-a84abd70-0c2f-4486-afd3-6a488b6a0300.png">

> <img width="475" alt="Screen Shot 2022-05-20 at 18 12 27" src="https://user-images.githubusercontent.com/99892502/169637657-b14554cc-0511-40c4-981c-0c05cc9c67fc.png">  <img width="475" alt="Screen Shot 2022-05-20 at 18 12 55" src="https://user-images.githubusercontent.com/99892502/169637662-aeb6472b-ac23-4628-a361-6638a1217c90.png">


> <img width="1000" alt="Screen Shot 2022-05-20 at 23 59 03" src="https://user-images.githubusercontent.com/99892502/169638050-1af83758-dea4-4e56-8070-8f71d128e6f2.png">


As a registered & logged in user of Noms, accessible features include the ability to view the Recipe Book, like/unlike a recipe and save it to or remove it from your Noms Box, view your Noms Box (favorites page), as well as Add your own recipe and Sign Out:
> <img width="300" alt="Screen Shot 2022-05-20 at 23 54 25" src="https://user-images.githubusercontent.com/99892502/169637907-565553b2-2831-43fa-aed2-b2bf1acb3855.png"> <img width="600" alt="Screen Shot 2022-05-20 at 23 18 19" src="https://user-images.githubusercontent.com/99892502/169637797-7af81562-b3fb-4a19-bf84-68dc2bcbad5e.png">
> <img width="500" alt="Screen Shot 2022-05-20 at 23 18 51" src="https://user-images.githubusercontent.com/99892502/169637799-ed9fe800-fd56-44e2-a44d-8e83d5c9ef46.png"><img width="500" alt="Screen Shot 2022-05-20 at 23 19 19" src="https://user-images.githubusercontent.com/99892502/169637801-97d82631-e8f5-41f0-af97-8aaad346dbde.png">

# Project Overview
***

I had three ideas I presented to a TA to brainstorm which one made the most sense for Project 4 given the limited time and needed functionality. Once I solidified my idea, I began planning the basic functionality and drawing an entity relationship diagram (ERD) and basic wireframe for the project.

Database ERD: 

<img width="700" alt="Database ERD" src="https://user-images.githubusercontent.com/99892502/169673321-cfb3d1f6-2c8b-4679-9078-31324fc5aec1.png">

***Excalidraw Wireframe:*** 

<img width="700" alt="Noms" src="https://user-images.githubusercontent.com/99892502/169673690-b7c8764f-290c-4ad5-a1db-63a0f8faa1c1.png">

***More planning with a Miro board:*** 

<img width="500" alt="Screen Shot 2022-05-21 at 18 48 33" src="https://user-images.githubusercontent.com/99892502/169673727-27180ad6-2d4a-4760-9876-67fb9a701538.png">

# Backend
***

First, I created a simple ‘Hello World’ Django application and deployed it to Heroku. Then, I connected the app to a PostgreSQL database.

***Models, Views, Serializers & Urls***

I created a separate Django app for Recipes, wrote a basic Recipe serializer, a simple Recipe model (pictured below is the basic model plus what was added later - the initial model only had a name), a ListView with a GET request for all recipes and added the url path. I then created an app for jwt_auth and wrote the models, views and urls. I tested each route as I went using Django’s built-in admin site and Postman. In addition, I utilized TablePlus to test my connection and see tables/relationships within my PostgreSQL database.    

- Recipe Serializer 
  - I wrote the serializers, updating and/or adding more as needed             
<img width="417" alt="Screen Shot 2022-05-21 at 18 52 54" src="https://user-images.githubusercontent.com/99892502/169675020-4aa57fea-5724-4cb6-bbc2-ee4c25b4d002.png">

- Recipe Model
  - I added all of the models from the ERD I knew I needed right from the start, adding to them as information I wanted as part of each model changed. I made sure to have this portion wrapped up prior to implementing them on the frontend as changing models can be tricky when having to migrate the information down the road. As you can see, the Recipe Model also includes a ManyToMany relationship between Recipes and Ingredients. This relationship is through the RecipeIngredient Model and then used on the frontend when adding ingredients to recipes as recipes have many ingredients and a single ingredient could be part of many recipes.                  
<img width="417" alt="Screen Shot 2022-05-21 at 18 53 59" src="https://user-images.githubusercontent.com/99892502/169675028-99c45443-7398-427b-867c-930dc476ba3e.png"> 

The RecipeIngredient Model included a third component for quantity that was outside of the ManyToMany relationship as well since the quantity of an ingredient changes with each individual recipe.  
<img width="417" alt="Screen Shot 2022-05-21 at 18 53 59" src="https://user-images.githubusercontent.com/99892502/169678282-85641bf0-7cb4-40ee-a6a1-ce38df1e27a8.png">

- Class ListView(APIView)
  - I opted to use the Class view for most of the Views throughout this project as they allow for more functionality. I did utilize a few Generic models as well. 
<img width="417" alt="Screen Shot 2022-05-21 at 18 54 18" src="https://user-images.githubusercontent.com/99892502/169675133-122a247e-8aff-4dee-b0e1-962b07316dcc.png">

- URLs (Recipe App)
<img width="417" alt="Screen Shot 2022-05-21 at 19 26 50" src="https://user-images.githubusercontent.com/99892502/169675173-ec6e2ee8-ccd9-47ff-9777-869b758c42b6.png">  

## JWT_Auth

Once I had the models, views, serializers and urls for the Recipe App where I wanted them, I added register and login functionality through the jwt_auth app. I included a User Serializer with password confirmation. In addition to the Register, Login and Credentials View, I included a Current User View, Profile View and Profile List View in order for each logged in user to be able to access their Noms Box (favorites) page. The Profile View includes Authentication to identify which user is logged in so they can see their own favorited recipes. 
<img width="328" alt="Screen Shot 2022-05-21 at 21 29 53" src="https://user-images.githubusercontent.com/99892502/169677515-d04c2819-8992-4309-9425-e8ab5883ea80.png">

<img width="328" alt="Views" src="https://user-images.githubusercontent.com/99892502/169677519-a0658580-1f99-423a-93c4-9f28b48008b2.png">

In order to add the "liked" feature to each recipe and have it linked to the User, I created a Custom User Model within the jwt_auth app and registered the model in the admin.py file.

<img width="328" alt="CustomUser" src="https://user-images.githubusercontent.com/99892502/169677523-9b1ba40a-a2ec-455b-9e90-1ebc00f612b8.png">

- URLs (jwt_auth app)
 <img width="400" alt="Screen Shot 2022-05-21 at 20 06 23" src="https://user-images.githubusercontent.com/99892502/169675188-5ca729ca-53ed-4f14-9376-cb8302982bc3.png">

# Frontend
***

I worked on the frontend and backend simultaneously when I first got the frontend up and running. Being able to see some of the work I completed come to life on the frontend is a motivating factor and helps me to conceptualize what comes next. I imported Axios, connecting the frontend to the API (backend) with the deployed version herokuapp url and numerous axios endpoint requests. I utilized Postman to make sure each path worked as intended as I moved forward. 

![Screen Shot 2022-05-21 at 22 24 32](https://user-images.githubusercontent.com/99892502/169678564-7953afa6-bd43-4431-be13-93b85e274f87.png)

## Logged in vs Logged Out

The NavBar indicates whether someone is logged in or out based on the options available. If signed in, there is a Sign Out link available. Once signed out, the user's authentication token is removed and the user is taken back to the home page. 

![Screen Shot 2022-05-21 at 22 21 09](https://user-images.githubusercontent.com/99892502/169678624-3f9f187e-53ac-4e88-9a0a-1d1ff8aecb88.png)

## Create Your own Recipe

The form for adding your own recipe includes a section with checkboxes to add ingredients to your recipe. It does not currently include the ability to add your own or add the quantity of the ingredient, but this is on the list for future functionality! The ingredients currently listed on the form were input manually on the backend in the database, as they are ingredients included in the recipes available to view in the recipe book. Pulling the ingredients from the database was challenging as the ingredient itself was nested quite deep within the object. Below are snippets of code showing the checkboxes on the form as well as the functions for selecting ingredients. 

<img width="400" alt="CreateOwnRecipe" src="https://user-images.githubusercontent.com/99892502/169678920-6c1ff651-4a2f-4a0e-9b7b-ca3ac2469ee1.png">
<img width="400" alt="Checkboxes" src="https://user-images.githubusercontent.com/99892502/169678804-98e7cdcc-4d43-45d0-bcd1-5dcd276bd42f.png">

<img width="400" alt="IngredientForm" src="https://user-images.githubusercontent.com/99892502/169678797-492cb978-00ba-40fd-b961-8e6f4e11f843.png">

## Bugs: 

- No known bugs at this time! :)

## Challenges: 

- I really liked using Django on the backend as there were many built in functions already which made it easy to use. The challenging part of the whole project was just the overall amount of steps, code, and puzzle pieces that had to be put together bit by bit in such a short amount of time. 


## Wins:

- Getting the ingredients out of the database and into the form to add your own recipe was a win and a half! 

# Future Improvements/Features
***

Some additional features I would like to add to improve the app and create a more in-depth user experience:

- The ability for users to add their own ingredients and quantity of those ingredients into the create your own recipe form.
-	A weekly Meal Page that translates into a weekly grocery list, compiling all ingredients needed for each recipe chosen and if an ingredient is added to the list more than once, combining the quantity needed of that ingredient for all recipes it's included in that week.
-	A more responsive design for mobile/tablet use.
-	Error handling on the frontend registration/login pages displaying the error to the user. Right now, the error shows in the console only.


# Key Learnings
***

- I really enjoyed using Django on the backend as there were many built in functions that made it super easy to use. 
- Building a full-stack app from back to front independently and being able to see it all come together in the end was extremely satisfying. I learned a lot throughout the process that I may not have otherwise had I opted to work in a pair or group.




