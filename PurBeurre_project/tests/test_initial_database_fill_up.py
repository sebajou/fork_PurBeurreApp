import pytest
from database_handler_app.initial_database_fill_up import fill_up_diet, fill_up_allergen
from database_handler_app.models import Diet, Allergen


class TestFillUpDiet:

    @pytest.mark.django_db(transaction=True)
    def test_fill_up_diet(self):
        list_diet_type_test = ['omnivore', 'végétarien', 'végétalien', 'carnivore',
                          'anthropophage', 'pesco-végétarien', 'crudivore']
        fill_up_diet()
        dictionary_from_model = Diet.objects.values()
        list_diet_type_model = []
        for diet_dict in dictionary_from_model:
            list_diet_type_model.append(diet_dict['diet_name'])
        for diet_type in list_diet_type_model:
            assert diet_type in list_diet_type_test

    @pytest.mark.django_db(transaction=True)
    def test_fill_up_allergen(self):
        allergen_type_test = 'Pas d\'allergies'
        fill_up_allergen()
        dictionary_from_model = Allergen.objects.values()
        list_allergen_type_model = []
        for allergen_dict in dictionary_from_model:
            list_allergen_type_model.append(allergen_dict['allergen_name'])
        flag = 0
        for allergen_type in list_allergen_type_model:
            if allergen_type_test in allergen_type:
                flag += 1
        assert flag >= 1
