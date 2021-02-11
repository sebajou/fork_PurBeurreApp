import pytest
from request_api_app.search_engine import PopDBFromJsonWithCategories, FindSubstitute, Parser
from request_api_app.search_engine import pop_db_with_categories
import json
from schema import Schema, And
from database_handler_app.models import FoodList, Allergen
import ast

import pytest


class TestsPopDBFromJsonWithCategories:

    def setup_method(self):
        # Open the bonbons_json_data
        with open("bonbons3.json", "r") as read_file:
            self.json_for_test = json.load(read_file)
        # Build json schema for test variable from json
        self.schema = Schema([{
            "food_name": And(str),
            "category": And(str),
            "scora_nova_group": And(int),
            "nutri_score_grad": And(str),
            "food_url": And(str),
            "image_src": And(str),
            "allergen_list": And(str),
            "labels_list": And(list),
            "ingredients_tags": And(list),
            "nutriments_100g": And(dict),
        }])

        # Dictionary like dictionary made with variable_from_json function
        with open("variables_bonbons4.json", "r") as read_file:
            self.dictionary_from_json_bonbon = read_file.read()
            self.dictionary_from_json_bonbon = ast.literal_eval(self.dictionary_from_json_bonbon)

    def test_variables_from_foods_json(self):
        """Control Extract useful data from json and stock it in variables corespond to schema"""
        pop = PopDBFromJsonWithCategories()
        data_category_json = self.json_for_test
        data_category_json = [data_category_json]
        self.dictionary_build_with_json = pop.variables_from_foods_json(data_category_json=data_category_json,
                                                                        name_category="bonbon")
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
            assert str(product_from_model["labels_tags"])
            assert str(product_from_model["ingredients_tags"])
            assert str(product_from_model["image_src"])
            assert int(product_from_model["id"])


@pytest.mark.api_request
@pytest.mark.django_db(transaction=True)
def test_pop_db_with_categories():
    given_categories_name = 'bonbon'
    pop_db_with_categories(given_categories_name)
    dictionary_from_model = FoodList.objects.values()
    category_list_model = []
    for product_from_model in dictionary_from_model:
        category_list_model.append(product_from_model["category"])
    assert given_categories_name in category_list_model


@pytest.mark.api_request
@pytest.mark.django_db(transaction=True)
def test_pop_db_with_categories_without_argument():
    pop_db_with_categories()
    category_list_test = {'pizza', 'pate a tartiner', 'gateau', 'choucroute', 'bonbon', 'cassoulet', 'compote',
                          'cookies', 'tartiflette', 'bolognaise', 'chips', 'brioche', 'bolognaise', 'biscuit',
                          'croissants', 'pesto', 'couscous', 'confiture', 'biscuit', 'chocolat', 'croissant',
                          'yahourt', 'soda', 'céréales pour petit-déjeuner', 'biscotte', 'patte', 'riz',
                          'lentille', 'pâtes feuilletées', 'pâtes brisées', 'pâte sablée', 'saucisse',
                          'jambon', 'saucissons', 'poissons', 'tofu', 'fromages', 'mayonnaise'}
    dictionary_from_model = FoodList.objects.values()
    category_list_model = []
    for product_from_model in dictionary_from_model:
        category_list_model.append(product_from_model["category"])
    category_list_model = list(set(category_list_model))
    for category_element_test in category_list_test:
        assert category_element_test in category_list_model


class TestsParser:

    def setup_method(self):
        self.sentence_to_parse1 = "Je voudrais un bonbon à la fraise"
        self.sentence_to_parse2 = ""
        self.sentence_to_parse3 = "qsdazg!eraeeg dbz 35T@#31!5zb sN?dg"

    def test_parse_message_empty(self):
        sentence_to_parse = self.sentence_to_parse2
        parse = Parser()
        list_parsed_sentence = parse.parse_message_from_front(sentence_to_parse)
        assert list_parsed_sentence == []

    def test_parse_message_absurd(self):
        sentence_to_parse = self.sentence_to_parse3
        parse = Parser()
        list_parsed_sentence = parse.parse_message_from_front(sentence_to_parse)
        assert list_parsed_sentence == ['qsdazg!eraeeg', 'dbz', '35t@#31!5zb', 'sn?dg']

    def test_parse_message_from_front(self):
        sentence_to_parse = self.sentence_to_parse1
        parse = Parser()
        list_parsed_sentence = parse.parse_message_from_front(sentence_to_parse)
        assert list_parsed_sentence == ["bonbon", "fraise"]


class TestsFindSubstitute:

    def setup_method(self):
        self.key_sentence1 = "Bonbon à la fraises"
        self.key_sentence2 = ""
        self.key_sentence3 = "goudoubouz à la brimiritif gaudoisiate"
        self.category = "bonbon"
        # Schema of dictionay of substitute values from database
        self.schema2 = Schema({
            "id": And(int),
            "labels_tags": And(str),
            "ingredients_tags": And(str),
            "food_name": And(str),
            "category": And(str),
            "scora_nova_group": And(int),
            "nutri_score_grad": And(str),
            "food_url": And(str),
            "image_src": And(str),
            "nutriments_100g": And(str),
        })
        self.id_food_from_search_choose = 662
        self.id_food_for_substitute = 1550

    @pytest.mark.django_db(transaction=True)
    def test_database_search_and_find(self, django_db_setup):
        key_word_for_test = self.key_sentence1
        find = FindSubstitute()
        list_id_food_from_search = find.database_search_and_find(key_word_for_test)
        for element_id in list_id_food_from_search:
            assert int(element_id)
        # Verify that element of list is distinct
        assert len(list_id_food_from_search) == len(set(list_id_food_from_search))
        # Verify that element of list exist in foodlist id
        list_existing_id_in_food_list = FoodList.objects.values_list('id', flat=True)
        for element_id in list_id_food_from_search:
            assert element_id in list_existing_id_in_food_list
        # verifier d'autre attribut dans le dictionnaire
        # verifier les limites

    @pytest.mark.django_db(transaction=True)
    def test_database_search_and_find_empty_sentence(self, django_db_setup):
        key_word_for_test = self.key_sentence2
        find = FindSubstitute()
        list_id_food_from_search = find.database_search_and_find(key_word_for_test)
        for element_id in list_id_food_from_search:
            assert element_id == "-µ-empty-µ-"

    @pytest.mark.django_db(transaction=True)
    def test_database_search_and_find_absurd_sentence(self, django_db_setup):
        key_word_for_test = self.key_sentence3
        find = FindSubstitute()
        list_id_food_from_search = find.database_search_and_find(key_word_for_test)
        for element_id in list_id_food_from_search:
            assert element_id == '-µ-absurd-µ-'

    @pytest.mark.django_db()
    def test_healthy_substitute(self):
        id_food = self.id_food_for_substitute
        dictionary_schema = self.schema2
        find = FindSubstitute()
        dic_healthy_substitute_from_categories = find.healthy_substitute(id_food)
        assert dictionary_schema.is_valid(dic_healthy_substitute_from_categories[0])
