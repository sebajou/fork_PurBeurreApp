from database_handler_app.models import Diet


def fill_up_diet():
    diet_list = ['omnivore', 'végétarien', 'végétalien', 'carnivore', 'anthropophage', 'pesco-végétarien', 'crudivore']
    for diet_type in diet_list:
        if Diet.objects.filter(diet_name=diet_type):
            print(diet_type)
        else:
            Diet.objects.create(diet_name=diet_type)
            print(diet_type)

