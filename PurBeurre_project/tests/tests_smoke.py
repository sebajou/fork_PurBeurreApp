import pytest
from request_api_app.search_engine import PopDBFromJsonWithCategories
from database_handler_app.models import FoodList, Allergen


@pytest.mark.smoketest
def test_api_json_format():
    """
    Verifies that the Open Fact Foods is returning json data with an expected structure
    """
    # Get in variable the json data format from Open Fact Foods API
    pop = PopDBFromJsonWithCategories()
    bonbons_json = pop.json_from_api("bonbon")

    # Check if json from API contain some json keys important for the application
    for product_bonbons_json in bonbons_json[0]['products']:
        assert 'product_name_fr' in product_bonbons_json
        assert 'url' in product_bonbons_json
        assert 'nova_group' in product_bonbons_json or 'nutriscore_grade' in product_bonbons_json
        assert 'image_url' in product_bonbons_json
        assert 'allergens' in product_bonbons_json


@pytest.mark.smoketest
@pytest.mark.django_db(transaction=True)
def tests_pop_db_all_foo():
    """Use json_from_api and pop_db for 30 different categories of foods. """
    # Get in variable the json data format from Open Fact Foods API
    pop = PopDBFromJsonWithCategories()
    bonbons_json = pop.json_from_api("bonbon")
    variables_bonbons = pop.variables_from_foods_json(data_category_json=bonbons_json, name_category="bonbon")
    # Populate the database with dictionary get on OFF API
    pop.pop_db(variables_bonbons)
    # Stoke data from model in dictionary
    dictionary_from_model = FoodList.objects.values()
    print('\n=========================================\n\n\n', 'dictionary_from_model', dictionary_from_model)
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
