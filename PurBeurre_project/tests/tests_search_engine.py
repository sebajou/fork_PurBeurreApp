import pytest
from request_api_app.search_engine import PopDBFromJsonWithCategories
import json
from schema import Schema, And, Use, Optional
from database_handler_app.models import FoodList, Allergen
import ast


class TestsPopDBFromJsonWithCategories:

    def setup_method(self):
        # Open the bonbons_json_data
        with open("bonbons.json", "r") as read_file:
            self.json_for_test = json.load(read_file)
            # string_json_for_test = read_file.read()
            # self.json_for_test = json.loads(string_json_for_test)
        # Build json schema for test variable from json
        self.schema = Schema([{
            "food_name": And(str),
            "category": And(str),
            "scora_nova_group": And(int),
            "nutri_score_grad": And(str),
            "food_url": And(str),
            "image_src": And(str),
            "allergen_list": And(str),
        }])
        # Dictionary like dictionary made with variable_from_json function
        with open("variables_bonbons.json", "r") as read_file:
            self.dictionary_from_json_bonbon = read_file.read()
            self.dictionary_from_json_bonbon = ast.literal_eval(self.dictionary_from_json_bonbon)

    def test_variables_from_foods_json(self):
        """Control Extract useful data from json and stock it in variables corespond to schema"""
        pop = PopDBFromJsonWithCategories()
        data_category_json = self.json_for_test
        self.dictionary_build_with_json = pop.variables_from_foods_json(data_category_json=data_category_json, name_category="bonbon")
        dictionary_schema = self.schema
        dictionary_from_json = self.dictionary_build_with_json
        print('dictionary_from_json => ', dictionary_from_json)
        # Loop on dictionary extract from json to assert schema of for each products
        for products_num_dict in dictionary_from_json:
            assert dictionary_schema.is_valid(products_num_dict)

    @pytest.mark.django_db(transaction=True)
    def tests_pop_db(self):
        """Verify that database is populate with the dictionary from json file."""
        dictionary_from_json = self.dictionary_from_json_bonbon
        # Populate the database with dictionary from json
        pop = PopDBFromJsonWithCategories()
        pop.pop_db(dictionary_from_json=dictionary_from_json)
        # Stoke data from model in dictionary
        dictionary_from_model = FoodList.objects.values()
        # Loop to assert that data from dictionary_from_json are stock in the database
        for product_from_model in dictionary_from_model:
            assert str(product_from_model["food_name"])
            assert str(product_from_model["category"])
            assert int(product_from_model["scora_nova_group"])
            assert str(product_from_model["nutri_score_grad"])
            assert str(product_from_model["food_url"])
            assert str(product_from_model["image_src"])
            # Verify the many to many relation between FoodList and Allergen)
            # allergen_from_model = Allergen.objects.filter(foodlist__id=product_from_model["id"]).values()
            # for allergen_in_product_model in allergen_from_model:
            #     assert str(allergen_in_product_model['allergen_name'])
            # Verify that food_list item contain an id
            assert int(product_from_model["id"])

