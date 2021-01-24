import pytest
from request_api_app.alergen_diet import IsFood


class TestIsFood:

    def setup_method(self):
        self.allergen_list = ['en:fish', 'en:eggs']
        self.diet_type = 'végétalien'
        self.id_food = 555

    def test_is_allergen(self):
        allergens = self.allergen_list
        a_food = self.id_food
        is_or_not = IsFood()

        bool_is_allergen = is_or_not.is_allergen(allergen_list=allergens, id_food=a_food)

        assert bool_is_allergen

    def test_is_diet(self):
        a_food = self.id_food
        a_diet = self.diet_type
        is_or_not = IsFood()

        bool_is_diet = is_or_not.is_diet(diet_type=a_diet, id_food=a_food)

        assert bool_is_diet
