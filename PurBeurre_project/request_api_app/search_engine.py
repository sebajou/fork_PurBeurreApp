import requests
import json
from database_handler_app.models import FoodList, Allergen
import string
import pickle
import re


class PopDBFromJsonWithCategories:
    """
    This class allow to populate the application's database with data from Open Fact Foods.
    One function (json_from_api) call the API to get json file for one food.
    A second function load json useful data in dictionary.
    A third function (pop_db) populate the database with the json file.
    Another function (pop_db_with_categories) call the two precedent function to populate database
    with foods from up to 30 different categories of foods.
    """

    @staticmethod
    def json_from_api(name_category):
        """Call the API to get json file for one food."""
        pass
        payload = {
            'action': 'process', 'tagtype_0': 'categories',
            'tag_contains_0': 'contains', 'tag_0': "\'" + name_category + "\'",
            'sort_by': 'unique_scans_n', 'page_size': '100',
            'axis_x': 'energy', 'axis_y': 'products_n', 'json': '1'
        }
        req = requests.get(
            "https://fr.openfoodfacts.org/cgi/search.pl?", params=payload
        )
        print('Json did')
        data_category_json = req.json()
        return data_category_json, name_category

    @staticmethod
    def variables_from_foods_json(data_category_json, name_category):
        """Extract useful data from json and stock it in variables"""
        # Loop through data_category_json and stock useful data in dictionary_from_json
        dictionary_from_json = []
        for data in data_category_json[0]['products']:
            try:
                if data['product_name_fr'] == '':
                    food_name = name_category
                else:
                    food_name = data['product_name_fr']
                food_url = data['url']
                scora_nova_group = data['nova_group']
                nutri_score_grad = data['nutriscore_grade']
                image_src = data['image_url']
                allergen_list = data['allergens']
                # Take labels from labels_tags
                labels_list = data['labels_tags']
                print("labels_tags => ", labels_list)
                ingredients_tags = data['ingredients_tags']
                print("ingredients_tags => ", ingredients_tags)
                # labels_list = []
                # for label in data['labels_tags']:
                #     labels_list.append(label)
                # print(labels_list)
                # Capt data from data['nutriments']
                nutriments_100g = data['nutriments']
                # Add to dictionary only appropriate nutriments for 100g
                exclude_list = ['nova-group_100g', 'carbon-footprint-from-known-ingredients_100g',
                                'nutrition-score-fr_100g', 'carbon-footprint-from-meat-or-fish_100g']
                selected_nutriments_100g = {}
                for key, value in nutriments_100g.items():
                    # Filter only good element from nutriments_100g dictionary
                    if key not in exclude_list:
                        match = re.search(r"_100g", key)
                        if match:
                            selected_nutriments_100g[key] = value
                # Add get data in returned  dictionary
                dictionary_from_json.append([{"food_name": food_name,
                                              "category": name_category,
                                              "scora_nova_group": scora_nova_group,
                                              "nutri_score_grad": nutri_score_grad,
                                              "food_url": food_url,
                                              "image_src": image_src,
                                              "labels_list": labels_list,
                                              "ingredients_tags": ingredients_tags,
                                              "allergen_list": allergen_list,
                                              "nutriments_100g": selected_nutriments_100g}])
            except (TypeError, KeyError):
                print("One loop through the data_category_json doesn't work")
        return dictionary_from_json

    @staticmethod
    def pop_db(dictionary_from_json):
        """Populate the database with the dictionary_from_json file."""
        for inside_dictionary in dictionary_from_json:
            for product_from_json in inside_dictionary:
                # Populate columns
                if FoodList.objects.filter(food_name=product_from_json["food_name"]):
                    food_values_list = FoodList.objects.values_list('food_name', flat=True)
                else:
                    food_list = FoodList(food_name=product_from_json["food_name"],
                                         category=product_from_json["category"],
                                         scora_nova_group=int(product_from_json["scora_nova_group"]),
                                         nutri_score_grad=product_from_json["nutri_score_grad"],
                                         food_url=product_from_json["food_url"],
                                         image_src=product_from_json["image_src"],
                                         nutriments_100g=product_from_json["nutriments_100g"],
                                         ingredients_tags=product_from_json["ingredients_tags"],
                                         labels_tags=product_from_json["labels_list"])
                    food_list.save()
                    # Stock allergens tag in list
                    data_allergens = product_from_json["allergen_list"]
                    # Add list of allergens from json in allergens_list
                    allergens = []
                    allergens_list = []
                    for allergens_raw in data_allergens.split(','):
                        # List all allergens in each product
                        allergens.append(allergens_raw)
                        # List of allergens without double
                        allergens_list = set(allergens)

                    # Add allergen from allergen_list in database if not present in database
                    for allergen in allergens_list:
                        if Allergen.objects.filter(allergen_name=allergen):
                            aller = Allergen.objects.get(allergen_name=allergen)
                            food_list.allergen_list.add(aller)
                        else:
                            aller = Allergen(allergen_name=allergen)
                            aller.save()
                            food_list.allergen_list.add(aller)

    def pop_db_all_foo(self, name_category):
        """Use json_from_api and pop_db for up to 30 different categories of foods. """
        # Fill with name_category from outside function
        if name_category:
            data_category_json_var = self.json_from_api(name_category)
            dictionary_from_json_var = self.variables_from_foods_json(name_category=name_category,
                                                                      data_category_json=data_category_json_var)
            self.pop_db(dictionary_from_json_var)


def pop_db_with_categories(given_categories_name=None):
    """
    Contain the list of category and organise the database fill up
    with method from PopDBFromJsonWithCategories class.
    """
    categories_list = ['pizza', 'pate a tartiner', 'gateau', 'choucroute', 'bonbon', 'cassoulet', 'compote',
                       'cookies', 'tartiflette', 'bolognaise', 'chips', 'brioche', 'bolognaise', 'biscuit',
                       'croissants', 'pesto', 'couscous', 'confiture', 'biscuit', 'chocolat', 'croissant',
                       'yahourt', 'soda', 'céréales pour petit-déjeuner', 'biscotte', 'patte', 'riz',
                       'lentille', 'pâtes feuilletées', 'pâtes brisées', 'pâte sablée', 'saucisse',
                       'jambon', 'saucissons', 'poissons', 'tofu', 'fromages', 'mayonnaise', 'fromages',
                       'beurre', 'sushis', 'produits à tartiner', 'yaourts']
    pop = PopDBFromJsonWithCategories()
    if given_categories_name is not None:
        pop.pop_db_all_foo(given_categories_name)
    else:
        for categories_name in categories_list:
            pop.pop_db_all_foo(categories_name)
            print('categories_name done => ', categories_name)


class Parser:
    """ This class parse message from front input from user."""

    def __init__(self):
        """Initial attribute for Parser. """
        with open('fr_stop_word_data', 'rb') as fr_stop_word_file:
            my_unpickler = pickle.Unpickler(fr_stop_word_file)
            self.fr_stop_word = my_unpickler.load()
        # List of piece of word, for target french verb.
        self.list_pattern_beginning = ['part', 'all', 'veu', 'part', 'voul', 'voudr', 'ir']
        self.list_pattern_end = ['ons', 'ez', 'ent', 'x', 't', 'ais', 'ai', 'ait', 'us', 'ut',
                                 'ûmes', 'ûtes', 'urent', 'é', 'ir']

    @staticmethod
    def format_message(message_from_front):
        """Format message from front user input. """
        # Parse input message
        try:
            message_from_front = message_from_front.lower()
            message_from_front = message_from_front.strip(string.punctuation)
            message_from_front = message_from_front.replace("\'", " ")
            message_from_front = message_from_front.replace(",", "")
            message_from_front = message_from_front.replace(".", "")
            message_from_front = message_from_front.strip()
            message_from_front = message_from_front.split(" ")
            return message_from_front
        except AttributeError as NoTy:
            return ""

    def format_verb(self, message_from_front):
        """Format message from front user input by removing verb. """
        list_verb_pattern = []
        for pattern_beginning in self.list_pattern_beginning:
            for pattern_end in self.list_pattern_end:
                pattern = pattern_beginning + pattern_end
                list_verb_pattern.append(pattern)

        # Remove list_message_from_front from message_from_front
        list_message_from_front = [word for word in message_from_front if word not in list_verb_pattern]

        return list_message_from_front

    def parse_message_from_front(self, message_from_front):
        """
        Parse the message from front user input,
        return parse message for API by using method from Parser class.
        """
        # Use method from Parser class
        list_message_from_front = self.format_message(message_from_front)
        parse_message_of_front = self.format_verb(list_message_from_front)

        # Remove stopWord from parse_message_from_front
        word = [word for word in parse_message_of_front if word not in self.fr_stop_word]

        return word


class FindSubstitute:
    """
    This class contain functions which allow User to search Food in database,
    then find a healthy substitute from Open Food Facts API.
    """

    @staticmethod
    def database_search_and_find(key_sentence):
        """This function allows User to find foods list in database from key word enter in search field"""
        # Use a parser.
        parser = Parser()
        list_key_words = parser.parse_message_from_front(message_from_front=key_sentence)
        if not list_key_words:
            return ['-µ-empty-µ-']
        print('list_key_words => ', list_key_words)
        # Collect in dictionary id, food name and category.
        list_dict_to_compare_foodlist = list(FoodList.objects.values('id', 'food_name', 'category',
                                                                     'image_src', 'nutri_score_grad',
                                                                     'food_url'))
        # Process on key words data => compare key words with category name and food_name in database
        # Give a score of matching between key words and each food id
        list_dict_with_score_foodlist = []
        for dict_in_foodlist in list_dict_to_compare_foodlist:
            score = 0
            for element_key_words in list_key_words:
                list_food_name = [x.lower() for x in dict_in_foodlist['food_name'].split(' ')]
                if element_key_words.lower() in list_food_name:
                    score += 1
                list_category = [x.lower() for x in dict_in_foodlist['category'].split(' ')]
                if element_key_words.lower() in list_category:
                    score += 2
                else:
                    pass
            dict_in_foodlist_with_score = {'id': dict_in_foodlist['id'],
                                           'food_name': dict_in_foodlist['food_name'],
                                           'category': dict_in_foodlist['category'],
                                           'image_src': dict_in_foodlist['image_src'],
                                           'nutri_score_grad': dict_in_foodlist['nutri_score_grad'],
                                           'food_url': dict_in_foodlist['food_url'],
                                           'score': score}
            list_dict_with_score_foodlist.append(dict_in_foodlist_with_score)

        # Display ordered list of food from score matching
        # or if not results display "Nous n'avons pas trouvé... "
        list_dict_with_score_foodlist = sorted(list_dict_with_score_foodlist, key=lambda i: i['score'], reverse=True)
        list_id = []
        for element_score in list_dict_with_score_foodlist:
            list_id.append(element_score['id'])

        # If all score of matching is 0, we consider the request absurd
        for element_id in list_dict_with_score_foodlist[:1]:
            if element_id['score'] == 0:
                return ['-µ-absurd-µ-']
        # Return the dictionary of the first search matching product
        return list_dict_with_score_foodlist[:1]

    @staticmethod
    def healthy_substitute(id_food_from_search_choose):
        """This function search a subsitute of food in Open Fact Food API"""
        # Find category associated with given id
        category_from_id = FoodList.objects.filter(id=id_food_from_search_choose).values()
        given_categories_name = category_from_id[0]['category']
        # Find better nutritional score food and associated id from database in this category
        top_scores = (FoodList.objects
                      .order_by('nutri_score_grad')
                      .values_list('nutri_score_grad', flat=True)
                      .distinct()
                      .filter(category=given_categories_name))
        dic_healthy_substitute_from_categories = (FoodList
                                                  .objects.order_by('nutri_score_grad')
                                                  .filter(nutri_score_grad__in=top_scores)
                                                  .filter(category=given_categories_name)
                                                  .values())
        return dic_healthy_substitute_from_categories
