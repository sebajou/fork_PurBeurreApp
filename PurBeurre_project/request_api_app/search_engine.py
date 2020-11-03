import requests
import json
from database_handler_app.models import FoodList, Allergen


class PopDBFromJsonWithCategories:
    """
    This class allow to populate the application's database with data from Open Fact Foods.
    One function (json_from_api) call the API to get json file for one food.
    A second function load json useful data in dictionary.
    A third function (pop_db) populate the database with the json file.
    Another function (pop_db_with_categories) call the two precedent function to populate database
    with foods from 30 different categories of foods.
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
                # Add get data in returned  dictionary
                dictionary_from_json.append([{"food_name": food_name,
                                              "category": name_category,
                                              "scora_nova_group": scora_nova_group,
                                              "nutri_score_grad": nutri_score_grad,
                                              "food_url": food_url,
                                              "image_src": image_src,
                                              "allergen_list": allergen_list}])
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
                                         image_src=product_from_json["image_src"])
                    food_list.save()
                    # Stock allergens tag in list
                    data_allergens = product_from_json["allergen_list"]
                    # Add list of allergens from json in allergens_list
                    allergens = []
                    allergens_list = []
                    for allergens_raw in data_allergens.split(','):
                        # # Choose only english name allergens
                        # if allergens_raw[:3] == 'en:':
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
        """Use json_from_api and pop_db for 30 different categories of foods. """
        # Fill with name_category from outside function
        if name_category:
            data_category_json_var = self.json_from_api(name_category)
            dictionary_from_json_var = self.variables_from_foods_json(name_category=name_category,
                                                                      data_category_json=data_category_json_var)
            self.pop_db(dictionary_from_json_var)


def pop_db_with_categories():
    categories_list = ['pizza', 'pate a tartiner', 'gateau', 'choucroute', 'bonbon', 'cassoulet', 'compote',
                       'cookies', 'tartiflette', 'bolognaise', 'chips', 'brioche', 'bolognaise', 'biscuit',
                       'croissants', 'pesto', 'couscous', 'confiture', 'biscuit', 'chocolat', 'croissant',
                       'yahourt', 'soda', 'céréales pour petit-déjeuner', 'biscotte', 'patte', 'riz',
                       'lentille', 'pâtes feuilletées', 'pâtes brisées', 'pâte sablée', 'saucisse',
                       'jambon', 'saucissons', 'poissons', 'tofu', 'fromages']
    pop = PopDBFromJsonWithCategories()
    for categories_name in categories_list:
        pop.pop_db_all_foo(categories_name)

