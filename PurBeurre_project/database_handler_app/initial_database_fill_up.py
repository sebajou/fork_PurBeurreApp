from database_handler_app.models import Diet, Allergen


def fill_up_diet():
    diet_list = ['omnivore', 'végétarien', 'végétalien', 'carnivore', 'anthropophage', 'pesco-végétarien', 'crudivore']
    for diet_type in diet_list:
        if Diet.objects.filter(diet_name=diet_type):
            print(diet_type)
        else:
            Diet.objects.create(diet_name=diet_type)
            print(diet_type)


def fill_up_allergen():
    allergen_list = ['Pas d\'allergies']
    for allergen_type in allergen_list:
        if Allergen.objects.filter(allergen_name=allergen_type):
            print(allergen_type)
        else:
            Allergen.objects.create(allergen_name=allergen_type)
            print(allergen_type)

