# Pur Beurre Application

This ***application*** allow the user to find a 
*healthy substitute* aliment from **any aliment**. 

___

![Pur Beurre logo](PurBeurre_project/media/pur_beurre.ico)

*Pur Beurre logo*

## I - How to run  
Go to https://stormy-earth-30718.herokuapp.com/

Or:
1. Clone the project from [Github](https://github.com/sebajou/PurBeurreApp) 
2. Change DEBUG to True in setting.py.
3. Create an environment then install the same requirements then in requirements.txt. 
4. Go at the same directory level then manage.py. 
5. In your bash launch the command "./manage.py migrate".
6. Pre-populate your database with function in initial_database_fill_up.py.
7. In your bash launch the command "./manage.py runserver".
7. Open the localhost in your favorite navigator. 

## II - Data base
This app use a PostgreySQL database. 
Migrate command allow to create tables. 

List of Tables: 
+ MyUsers (user profile data)
+ Foodlist (food information pick up on OpenFactFoods API)
+ Allergen (List of allergen find in json from OpenFactFoods)
+ Diet (list of diet type fill by initial_database_fill_up.py)
+ Favorites (list of user's favorites food id)

Some many to many relationship:
+ Allergen with Foodlist
+ Allergen with MyUsers
+ Diet with MyUsers

> For many to many relationship this application use the Django ManyToManyField. 
This allow to not directly create junction table. Django do it for use thanks to django ORM. 

## III - Code and directory organisation
The code is organize in three app:
+ database_handler_app:
    + Contain model, module, view and template for manage relationship with model.  
+ request_api_app
    + Contain module and view which interact with OpenFactFoods API. 
+ user_app
    + Contain form, view and template with concern user functionalities.
Other main directory:
+ PurBeurre_project:
    + Contain setting.py main url.py and Django stuff. 
+ htmlcov:
    + Test coverage. 
+ media:
    + Files storage for local use with DEBUG = True. 
+ staticfiles: 
    + Obtain after collectstatic Django command. 
+ tests:  
    + Contain test modules. 

## IV - Back End functionalities

### Zoom on search_engine module
This module contain the main application functionality:
+ Collect json from OpenFactFoods API then fill Foodlist database table. 
+ Parse the input from user (the aliments request). 
+ Search foods substitute in database from parsed user input.
    + Inside a home made search engine with a system of matching score 
    to sort the better results. 

            for element_key_words in list_key_words:
                list_food_name = [x.lower() for x in dict_in_foodlist['food_name'].split(' ')]
                if element_key_words.lower() in list_food_name:
                    score += 1
                list_category = [x.lower() for x in dict_in_foodlist['category'].split(' ')]
                if element_key_words.lower() in list_category:
                    score += 2
                else:
                    pass
## IV - Front End functionalities

### Zoom on Django tag for template
Two tag is used in this application. 
#### Tag route_to_page_anchor function in custom_tags module
This function allow the use of # in url. Which is normally not possible in Django. 
#### Tag replace_underscore_space 
This home made tag to what the function title say in template. 

### Django form usage
This application use the Django class form (in user_app sign_up_form.py module). 