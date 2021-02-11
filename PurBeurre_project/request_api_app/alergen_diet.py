from database_handler_app.models import FoodList, Allergen, Diet
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
            if allergen_from_id['allergen_name'] in allergen_list:
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
        # Take ingredients of a given food in a list
        for ele in dico_food:
            for ingredient in ast.literal_eval((ele["ingredients_tags"])):
                if diet_type == 'végétalien' and \
                        (ingredient == 'en:egg' or ingredient == 'en:milk' or ingredient == 'en:meat'):
                    bool_is_diet = False
                if diet_type == 'végétarien' and \
                        (ingredient == 'en:fish' or ingredient == 'en:meat'):
                    bool_is_diet = False
                if diet_type == 'pesco-végétarien' and \
                        (ingredient == 'en:meat'):
                    bool_is_diet = False

        return bool_is_diet

    def remove_food_from_allergen(self, food_dict, user_id=None, list_allergen_of_user=[]):
        """
        This function remove foods from a list of food if this food is not in adequation with allergen of a user.
        This list of allergen is determinated with is_allergen function which give a boolean.
        """
        # Obtain list of allergen and diet of the current user.
        # Remove food with user's allergen from dict_healthy_substitute.
        food_dict = list(food_dict)

        if user_id:
            dict_allergen_of_user = Allergen.objects.filter(myusers__id=user_id).values()
            for allergen in dict_allergen_of_user:
                list_allergen_of_user.append(allergen['allergen_name'])

        food_not_allergen = []
        for food_id in food_dict:
            print("food_id = > ", food_id)
            is_allergen = self.is_allergen(allergen_list=list_allergen_of_user, id_food=food_id['id'])
            print('is_allergen => ', is_allergen)
            if not is_allergen:
                food_not_allergen.append(food_id)

        return food_not_allergen

    def remove_food_from_diet(self, food_dict, user_id=None, diet_of_user=None):
        """
        This function remove foods from a list of food if this food is not in adequation with diet of a user.
        Foods adequation with diet is determine with is_allergen function.
        """
        # Remove food not adequate with user diet from list_id.
        food_dict = list(food_dict)

        if user_id:
            diet_of_user = Diet.objects.filter(myusers__id=user_id).values()
            diet_of_user = diet_of_user[0]['diet_name']
            print("diet_of_user => ", diet_of_user)

        j = 0
        for food_id in food_dict:
            is_diet = self.is_diet(diet_type=diet_of_user[0], id_food=food_id['id'])
            if not is_diet:
                del food_dict[j]
            j += 1

        return food_dict
