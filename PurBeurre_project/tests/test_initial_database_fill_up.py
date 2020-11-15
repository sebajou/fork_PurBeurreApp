import pytest
from database_handler_app.initial_database_fill_up import fill_up_diet
from database_handler_app.models import Diet


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
