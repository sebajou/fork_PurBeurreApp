import pytest
from request_api_app.alergen_diet import IsFood


class TestIsFood:

    def setup_method(self):
        self.allergen_list = ['en:fish', 'en:eggs']
        self.diet_type = 'en:vegan'
        self.id_food = 555
        self.id_food_two = 612
        self.food_list = []
        self.food_list_without_allergen = []
        self.food_list_without_diet = []
        self.id_user = 1

    @pytest.mark.django_db(transaction=True)
    def test_is_allergen(self):
        allergens = self.allergen_list
        a_food = self.id_food
        is_or_not = IsFood()

        bool_is_allergen = is_or_not.is_allergen(allergen_list=allergens, id_food=a_food)

        assert bool_is_allergen

    @pytest.mark.django_db(transaction=True)
    def test_is_diet(self):
        a_food = self.id_food_two
        a_diet = self.diet_type
        is_or_not = IsFood()

        bool_is_diet = is_or_not.is_diet(diet_type=a_diet, id_food=a_food)

        assert not bool_is_diet

    def test_remove_food_from_allergen(self):
        with_allergen = self.food_list
        without_allergen = self.food_list_without_allergen
        user = self.id_user
        remove_from_list = IsFood()

        calc_list_without_allergen = remove_from_list.remove_food_from_allergen(food_list=with_allergen, user_id=user)

        assert calc_list_without_allergen in without_allergen

    def test_remove_food_from_diet(self):
        with_diet = self.food_list
        without_diet = self.food_list_without_diet
        user = self.id_user
        remove_from_list = IsFood()

        calc_list_without_diet = remove_from_list.remove_food_from_diet(food_list=with_diet, user_id=user)

        assert calc_list_without_diet in without_diet
