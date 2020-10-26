import pytest
from request_api_app.search_engine import PopDBFromJsonWithCategories
import json
import pickle


class TestsPopDBFromJsonWithCategories:

    def setup_method(self):
        # Open the choucroute_json_data
        with open("bonbons.json", "r") as read_file:
            bonbons_json = json.load(read_file)
        self.json_for_test = bonbons_json

        with open("dictionary_bonbon.json", "r") as read_file:
            dictionary_bonbon_json = json.load(read_file)
        self.dictionary_for_test = dictionary_bonbon_json

    # def tests_json_from_api(self):
    #     """Call the API to get json file for one food."""
    #     json_of_test = self.json_for_test
    #     # Food name requested for test
    #     food_for_test = "choucroute"
    #     pop = PopDBFromJsonWithCategories()
    #     get_json = pop.json_from_api(food_for_test)
    #     assert get_json == json_of_test

    def test_variables_from_foods_json(self):
        """Extract useful data from json and stock it in variables"""
        dictionary_test = self.dictionary_for_test
        pop = PopDBFromJsonWithCategories()
        dictionary_from_json = pop.variables_from_foods_json(data_category_json=self.json_for_test, name_category="bonbon")
        # Go through the loop of dictionary from json and dictionary for test
        for products_test in dictionary_test["products"]:
            for products_from_foo in dictionary_from_json["products"]:
                for element_test in products_test:
                    for element_from_foo in products_from_foo:
                        assert element_test == element_from_foo

    @pytest.mark.django_db(transaction=True)
    def tests_pop_db(self):
        """Populate the database with the json file."""
        pass

    @pytest.mark.django_db(transaction=True)
    def pop_db_with_categories(self):
        """Use json_from_api and pop_db for 30 differents categories of foods. """
        pass
