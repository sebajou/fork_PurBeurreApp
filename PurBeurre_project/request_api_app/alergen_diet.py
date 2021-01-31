from database_handler_app.models import FoodList, Allergen
import ast


class IsFood:
    """
    Methode which return boolean to caracterise food from foodlist table.
    """

    @staticmethod
    def is_allergen(allergen_list, id_food):
        """Determine is a food from id_food contain an allergen in allergen_list. """
        # Obtain allergen list from id_food through many to many relationship
        allergen_list_from_id = Allergen.objects.filter(foodlist__id=id_food).values()
        print('allergen_list_from_id => ', allergen_list_from_id)
        # allergen_list_from_id = allergen_list_from_id[0]['allergen_list']
        bool_is_allergen = False
        for allergen_from_id in allergen_list_from_id:
            for allergen in allergen_list:
                print("allergen_from_id['allergen_name'] => ", allergen_from_id['allergen_name'])
                if allergen == allergen_from_id['allergen_name']:
                    bool_is_allergen = True

        return bool_is_allergen

    @staticmethod
    def is_diet(diet_type, id_food):
        """Determine is a food from id_food respect a diet from diet_type. """
        # Extract data of label_tags (halal, vegan, vegetalian...) from id_food foodlist in label_list
        dico_food = FoodList.objects.filter(id=id_food).values()
        print(dico_food)
        # Extract the list of ingredients from id_food in foodlist.
        # ingredients = FoodList.objects.filter()
        bool_is_diet = False
        # Loop inside the both list and condition. If find label corresponding to diet_type bool_is_diet = True
        for labels in dico_food:
            for label in ast.literal_eval(labels["labels_tags"]):
                if label == diet_type:
                    print(label)
                    bool_is_diet = True
        # In some ingredients is not coherent with diet_type bool_is_diet = False

        return bool_is_diet
