from django.conf import settings
import pytest
import requests
from schema import Schema, Use
from request_api_app.search_engine import PopDBFromJsonWithCategories


# @pytest.mark.smoketest
# def test_api_json_format():
#     """
#     Verifies that the Open Fact Foods is returning json data with an expected structure
#     """
#     # Get in variable the json data format from Open Fact Foods API
#     pop = PopDBFromJsonWithCategories()
#     choucroute_json = pop.json_from_api("choucroute")
#
#     # Structure of API json
#     schema = Schema({
#                   "type": "object",
#                   "required": [],
#                   "properties": {
#                     "count": {
#                       "type": "number"
#                     },
#                     "page": {
#                       "type": "number"
#                     },
#                     "products": {
#                       "type": "array",
#                       "items": {
#                         "type": "object",
#                         "required": [],
#                         "properties": {
#                           "images": {
#                             "type": "object",
#                             "required": [],
#                             "properties": {
#                               "1": {
#                                 "type": "object",
#                                 "required": [],
#                                 "properties": {
#                                   "uploader": {
#                                     "type": "string"
#                                   },
#                                   "uploaded_t": {
#                                     "type": "string"
#                                   },
#                                   "sizes": {
#                                     "type": "object",
#                                     "required": [],
#                                     "properties": {
#                                       "100": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "h": {
#                                             "type": "number"
#                                           },
#                                           "w": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "400": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "w": {
#                                             "type": "number"
#                                           },
#                                           "h": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "full": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "h": {
#                                             "type": "number"
#                                           },
#                                           "w": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       }
#                                     }
#                                   }
#                                 }
#                               },
#                               "2": {
#                                 "type": "object",
#                                 "required": [],
#                                 "properties": {
#                                   "sizes": {
#                                     "type": "object",
#                                     "required": [],
#                                     "properties": {
#                                       "100": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "w": {
#                                             "type": "number"
#                                           },
#                                           "h": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "400": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "w": {
#                                             "type": "number"
#                                           },
#                                           "h": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "full": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "w": {
#                                             "type": "number"
#                                           },
#                                           "h": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       }
#                                     }
#                                   },
#                                   "uploaded_t": {
#                                     "type": "string"
#                                   },
#                                   "uploader": {
#                                     "type": "string"
#                                   }
#                                 }
#                               },
#                               "3": {
#                                 "type": "object",
#                                 "required": [],
#                                 "properties": {
#                                   "uploaded_t": {
#                                     "type": "number"
#                                   },
#                                   "uploader": {
#                                     "type": "string"
#                                   },
#                                   "sizes": {
#                                     "type": "object",
#                                     "required": [],
#                                     "properties": {
#                                       "100": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "w": {
#                                             "type": "number"
#                                           },
#                                           "h": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "400": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "w": {
#                                             "type": "number"
#                                           },
#                                           "h": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "full": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "h": {
#                                             "type": "number"
#                                           },
#                                           "w": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       }
#                                     }
#                                   }
#                                 }
#                               },
#                               "front_fr": {
#                                 "type": "object",
#                                 "required": [],
#                                 "properties": {
#                                   "x1": {
#                                     "type": "string"
#                                   },
#                                   "angle": {
#                                     "type": "string"
#                                   },
#                                   "y2": {
#                                     "type": "string"
#                                   },
#                                   "geometry": {
#                                     "type": "string"
#                                   },
#                                   "y1": {
#                                     "type": "string"
#                                   },
#                                   "normalize": {
#                                     "type": "string"
#                                   },
#                                   "imgid": {
#                                     "type": "string"
#                                   },
#                                   "sizes": {
#                                     "type": "object",
#                                     "required": [],
#                                     "properties": {
#                                       "100": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "h": {
#                                             "type": "number"
#                                           },
#                                           "w": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "200": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "w": {
#                                             "type": "number"
#                                           },
#                                           "h": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "400": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "w": {
#                                             "type": "number"
#                                           },
#                                           "h": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "full": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "h": {
#                                             "type": "number"
#                                           },
#                                           "w": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       }
#                                     }
#                                   },
#                                   "x2": {
#                                     "type": "string"
#                                   },
#                                   "rev": {
#                                     "type": "string"
#                                   },
#                                   "white_magic": {
#                                     "type": "string"
#                                   }
#                                 }
#                               },
#                               "ingredients": {
#                                 "type": "object",
#                                 "required": [],
#                                 "properties": {
#                                   "imgid": {
#                                     "type": "string"
#                                   },
#                                   "sizes": {
#                                     "type": "object",
#                                     "required": [],
#                                     "properties": {
#                                       "100": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "w": {
#                                             "type": "number"
#                                           },
#                                           "h": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "200": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "w": {
#                                             "type": "number"
#                                           },
#                                           "h": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "400": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "h": {
#                                             "type": "number"
#                                           },
#                                           "w": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "full": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "w": {
#                                             "type": "number"
#                                           },
#                                           "h": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       }
#                                     }
#                                   },
#                                   "normalize": {
#                                     "type": "string"
#                                   },
#                                   "geometry": {
#                                     "type": "string"
#                                   },
#                                   "rev": {
#                                     "type": "string"
#                                   },
#                                   "white_magic": {
#                                     "type": "string"
#                                   }
#                                 }
#                               },
#                               "nutrition": {
#                                 "type": "object",
#                                 "required": [],
#                                 "properties": {
#                                   "geometry": {
#                                     "type": "string"
#                                   },
#                                   "white_magic": {
#                                     "type": "string"
#                                   },
#                                   "rev": {
#                                     "type": "string"
#                                   },
#                                   "sizes": {
#                                     "type": "object",
#                                     "required": [],
#                                     "properties": {
#                                       "100": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "w": {
#                                             "type": "number"
#                                           },
#                                           "h": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "200": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "w": {
#                                             "type": "number"
#                                           },
#                                           "h": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "400": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "w": {
#                                             "type": "number"
#                                           },
#                                           "h": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "full": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "h": {
#                                             "type": "number"
#                                           },
#                                           "w": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       }
#                                     }
#                                   },
#                                   "imgid": {
#                                     "type": "string"
#                                   },
#                                   "normalize": {
#                                     "type": "string"
#                                   }
#                                 }
#                               },
#                               "nutrition_fr": {
#                                 "type": "object",
#                                 "required": [],
#                                 "properties": {
#                                   "geometry": {
#                                     "type": "string"
#                                   },
#                                   "white_magic": {
#                                     "type": "string"
#                                   },
#                                   "rev": {
#                                     "type": "string"
#                                   },
#                                   "imgid": {
#                                     "type": "string"
#                                   },
#                                   "normalize": {
#                                     "type": "string"
#                                   },
#                                   "sizes": {
#                                     "type": "object",
#                                     "required": [],
#                                     "properties": {
#                                       "100": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "h": {
#                                             "type": "number"
#                                           },
#                                           "w": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "200": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "h": {
#                                             "type": "number"
#                                           },
#                                           "w": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "400": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "h": {
#                                             "type": "number"
#                                           },
#                                           "w": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "full": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "h": {
#                                             "type": "number"
#                                           },
#                                           "w": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       }
#                                     }
#                                   }
#                                 }
#                               },
#                               "ingredients_fr": {
#                                 "type": "object",
#                                 "required": [],
#                                 "properties": {
#                                   "imgid": {
#                                     "type": "string"
#                                   },
#                                   "sizes": {
#                                     "type": "object",
#                                     "required": [],
#                                     "properties": {
#                                       "100": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "w": {
#                                             "type": "number"
#                                           },
#                                           "h": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "200": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "w": {
#                                             "type": "number"
#                                           },
#                                           "h": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "400": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "h": {
#                                             "type": "number"
#                                           },
#                                           "w": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "full": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "h": {
#                                             "type": "number"
#                                           },
#                                           "w": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       }
#                                     }
#                                   },
#                                   "normalize": {
#                                     "type": "string"
#                                   },
#                                   "white_magic": {
#                                     "type": "string"
#                                   },
#                                   "rev": {
#                                     "type": "string"
#                                   },
#                                   "geometry": {
#                                     "type": "string"
#                                   }
#                                 }
#                               },
#                               "front": {
#                                 "type": "object",
#                                 "required": [],
#                                 "properties": {
#                                   "normalize": {
#                                     "type": "string"
#                                   },
#                                   "sizes": {
#                                     "type": "object",
#                                     "required": [],
#                                     "properties": {
#                                       "100": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "h": {
#                                             "type": "number"
#                                           },
#                                           "w": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "200": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "w": {
#                                             "type": "number"
#                                           },
#                                           "h": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "400": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "w": {
#                                             "type": "number"
#                                           },
#                                           "h": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       },
#                                       "full": {
#                                         "type": "object",
#                                         "required": [],
#                                         "properties": {
#                                           "w": {
#                                             "type": "number"
#                                           },
#                                           "h": {
#                                             "type": "number"
#                                           }
#                                         }
#                                       }
#                                     }
#                                   },
#                                   "imgid": {
#                                     "type": "string"
#                                   },
#                                   "geometry": {
#                                     "type": "string"
#                                   },
#                                   "white_magic": {
#                                     "type": "string"
#                                   },
#                                   "rev": {
#                                     "type": "string"
#                                   }
#                                 }
#                               }
#                             }
#                           },
#                           "traces_imported": {
#                             "type": "string"
#                           },
#                           "ingredients_percent_analysis": {
#                             "type": "number"
#                           },
#                           "product_name_fr_debug_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "categories_properties": {
#                             "type": "object",
#                             "required": [],
#                             "properties": {
#                               "ciqual_food_code:en": {
#                                 "type": "string"
#                               },
#                               "agribalyse_food_code:en": {
#                                 "type": "string"
#                               },
#                               "agribalyse_proxy_food_code:en": {
#                                 "type": "string"
#                               }
#                             }
#                           },
#                           "countries_imported": {
#                             "type": "string"
#                           },
#                           "emb_codes_orig": {
#                             "type": "string"
#                           },
#                           "nutriments": {
#                             "type": "object",
#                             "required": [],
#                             "properties": {
#                               "salt_100g": {
#                                 "type": "number"
#                               },
#                               "fat_value": {
#                                 "type": "number"
#                               },
#                               "saturated-fat": {
#                                 "type": "number"
#                               },
#                               "sodium_serving": {
#                                 "type": "number"
#                               },
#                               "salt": {
#                                 "type": "number"
#                               },
#                               "saturated-fat_serving": {
#                                 "type": "number"
#                               },
#                               "energy_value": {
#                                 "type": "number"
#                               },
#                               "energy-kj_100g": {
#                                 "type": "number"
#                               },
#                               "carbohydrates_value": {
#                                 "type": "number"
#                               },
#                               "fruits-vegetables-nuts-estimate-from-ingredients_100g": {
#                                 "type": "string"
#                               },
#                               "energy-kj": {
#                                 "type": "number"
#                               },
#                               "energy_unit": {
#                                 "type": "string"
#                               },
#                               "proteins_100g": {
#                                 "type": "number"
#                               },
#                               "carbon-footprint-from-known-ingredients_100g": {
#                                 "type": "number"
#                               },
#                               "energy": {
#                                 "type": "number"
#                               },
#                               "sodium_value": {
#                                 "type": "number"
#                               },
#                               "proteins_unit": {
#                                 "type": "string"
#                               },
#                               "fat_serving": {
#                                 "type": "number"
#                               },
#                               "sodium": {
#                                 "type": "number"
#                               },
#                               "saturated-fat_100g": {
#                                 "type": "number"
#                               },
#                               "nova-group": {
#                                 "type": "number"
#                               },
#                               "salt_unit": {
#                                 "type": "string"
#                               },
#                               "proteins_value": {
#                                 "type": "number"
#                               },
#                               "energy-kj_value": {
#                                 "type": "number"
#                               },
#                               "carbohydrates_unit": {
#                                 "type": "string"
#                               },
#                               "nutrition-score-fr": {
#                                 "type": "number"
#                               },
#                               "carbon-footprint-from-meat-or-fish_serving": {
#                                 "type": "number"
#                               },
#                               "energy_100g": {
#                                 "type": "number"
#                               },
#                               "salt_value": {
#                                 "type": "number"
#                               },
#                               "nova-group_serving": {
#                                 "type": "number"
#                               },
#                               "saturated-fat_unit": {
#                                 "type": "string"
#                               },
#                               "sugars_value": {
#                                 "type": "number"
#                               },
#                               "carbon-footprint-from-known-ingredients_product": {
#                                 "type": "number"
#                               },
#                               "sugars_unit": {
#                                 "type": "string"
#                               },
#                               "proteins_serving": {
#                                 "type": "number"
#                               },
#                               "nutrition-score-fr_100g": {
#                                 "type": "number"
#                               },
#                               "sodium_100g": {
#                                 "type": "number"
#                               },
#                               "nova-group_100g": {
#                                 "type": "number"
#                               },
#                               "carbon-footprint-from-meat-or-fish_100g": {
#                                 "type": "number"
#                               },
#                               "sugars_100g": {
#                                 "type": "number"
#                               },
#                               "carbohydrates_100g": {
#                                 "type": "number"
#                               },
#                               "carbon-footprint-from-known-ingredients_serving": {
#                                 "type": "number"
#                               },
#                               "carbon-footprint-from-meat-or-fish_product": {
#                                 "type": "number"
#                               },
#                               "sugars_serving": {
#                                 "type": "number"
#                               },
#                               "fat_100g": {
#                                 "type": "number"
#                               },
#                               "energy-kj_unit": {
#                                 "type": "string"
#                               },
#                               "sodium_unit": {
#                                 "type": "string"
#                               },
#                               "fat_unit": {
#                                 "type": "string"
#                               },
#                               "fat": {
#                                 "type": "number"
#                               },
#                               "sugars": {
#                                 "type": "number"
#                               },
#                               "energy-kj_serving": {
#                                 "type": "number"
#                               },
#                               "carbohydrates": {
#                                 "type": "number"
#                               },
#                               "proteins": {
#                                 "type": "number"
#                               },
#                               "saturated-fat_value": {
#                                 "type": "number"
#                               },
#                               "salt_serving": {
#                                 "type": "number"
#                               },
#                               "energy_serving": {
#                                 "type": "number"
#                               },
#                               "carbohydrates_serving": {
#                                 "type": "number"
#                               }
#                             }
#                           },
#                           "quantity": {
#                             "type": "string"
#                           },
#                           "states": {
#                             "type": "string"
#                           },
#                           "brands_imported": {
#                             "type": "string"
#                           },
#                           "debug_param_sorted_langs": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "ingredients": {
#                             "type": "array",
#                             "items": {
#                               "type": "object",
#                               "required": [],
#                               "properties": {
#                                 "rank": {
#                                   "type": "number"
#                                 },
#                                 "text": {
#                                   "type": "string"
#                                 },
#                                 "id": {
#                                   "type": "string"
#                                 },
#                                 "has_sub_ingredients": {
#                                   "type": "string"
#                                 },
#                                 "percent": {
#                                   "type": "string"
#                                 }
#                               }
#                             }
#                           },
#                           "completed_t": {
#                             "type": "number"
#                           },
#                           "no_nutrition_data": {
#                             "type": "string"
#                           },
#                           "labels_prev_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "brands": {
#                             "type": "string"
#                           },
#                           "nutrition_grades": {
#                             "type": "string"
#                           },
#                           "emb_codes_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "ingredients_text_with_allergens_fr": {
#                             "type": "string"
#                           },
#                           "created_t": {
#                             "type": "number"
#                           },
#                           "emb_codes_debug_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "countries_lc": {
#                             "type": "string"
#                           },
#                           "data_quality_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "image_nutrition_thumb_url": {
#                             "type": "string"
#                           },
#                           "nutriscore_score": {
#                             "type": "number"
#                           },
#                           "nutrition_data": {
#                             "type": "string"
#                           },
#                           "nova_groups": {
#                             "type": "string"
#                           },
#                           "lang": {
#                             "type": "string"
#                           },
#                           "ingredients_from_palm_oil_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "last_modified_t": {
#                             "type": "number"
#                           },
#                           "additives_old_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "serving_size_imported": {
#                             "type": "string"
#                           },
#                           "image_front_url": {
#                             "type": "string"
#                           },
#                           "editors": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "nutrition_data_prepared_per_imported": {
#                             "type": "string"
#                           },
#                           "ingredients_that_may_be_from_palm_oil_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "ingredients_text_fr_imported": {
#                             "type": "string"
#                           },
#                           "countries_hierarchy": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "serving_quantity": {
#                             "type": "string"
#                           },
#                           "id": {
#                             "type": "string"
#                           },
#                           "minerals_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "image_thumb_url": {
#                             "type": "string"
#                           },
#                           "lc": {
#                             "type": "string"
#                           },
#                           "known_ingredients_n": {
#                             "type": "number"
#                           },
#                           "ingredients_text_fr": {
#                             "type": "string"
#                           },
#                           "labels_hierarchy": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "pnns_groups_2_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "packaging": {
#                             "type": "string"
#                           },
#                           "ingredients_original_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "last_edit_dates_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "stores_imported": {
#                             "type": "string"
#                           },
#                           "nova_group_debug": {
#                             "type": "string"
#                           },
#                           "categories_hierarchy": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "additives_prev_original_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "nutrient_levels_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "ingredients_analysis_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "purchase_places": {
#                             "type": "string"
#                           },
#                           "packaging_debug_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "complete": {
#                             "type": "number"
#                           },
#                           "nutrition_score_warning_no_fiber": {
#                             "type": "number"
#                           },
#                           "unique_scans_n": {
#                             "type": "number"
#                           },
#                           "states_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "labels": {
#                             "type": "string"
#                           },
#                           "traces_debug_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "traces_from_user": {
#                             "type": "string"
#                           },
#                           "manufacturing_places": {
#                             "type": "string"
#                           },
#                           "vitamins_prev_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "languages_hierarchy": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "_id": {
#                             "type": "string"
#                           },
#                           "product_name": {
#                             "type": "string"
#                           },
#                           "link": {
#                             "type": "string"
#                           },
#                           "completeness": {
#                             "type": "number"
#                           },
#                           "code": {
#                             "type": "string"
#                           },
#                           "codes_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "pnns_groups_2": {
#                             "type": "string"
#                           },
#                           "owner_fields": {
#                             "type": "object",
#                             "required": [],
#                             "properties": {
#                               "sugars": {
#                                 "type": "number"
#                               },
#                               "quantity": {
#                                 "type": "number"
#                               },
#                               "energy": {
#                                 "type": "number"
#                               },
#                               "serving_size": {
#                                 "type": "number"
#                               },
#                               "countries": {
#                                 "type": "number"
#                               },
#                               "carbohydrates": {
#                                 "type": "number"
#                               },
#                               "traces": {
#                                 "type": "number"
#                               },
#                               "stores": {
#                                 "type": "number"
#                               },
#                               "salt": {
#                                 "type": "number"
#                               },
#                               "data_sources": {
#                                 "type": "number"
#                               },
#                               "ingredients_text_fr": {
#                                 "type": "number"
#                               },
#                               "nutrition_data_prepared_per": {
#                                 "type": "number"
#                               },
#                               "brands": {
#                                 "type": "number"
#                               },
#                               "lc": {
#                                 "type": "number"
#                               },
#                               "energy-kj": {
#                                 "type": "number"
#                               },
#                               "categories": {
#                                 "type": "number"
#                               },
#                               "nutrition_data_per": {
#                                 "type": "number"
#                               },
#                               "product_name_fr": {
#                                 "type": "number"
#                               }
#                             }
#                           },
#                           "traces_from_ingredients": {
#                             "type": "string"
#                           },
#                           "last_image_dates_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "ingredients_hierarchy": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "nutrition_grade_fr": {
#                             "type": "string"
#                           },
#                           "generic_name_fr_debug_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "amino_acids_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "nutrition_data_per_imported": {
#                             "type": "string"
#                           },
#                           "max_imgid": {
#                             "type": "string"
#                           },
#                           "compared_to_category": {
#                             "type": "string"
#                           },
#                           "ingredients_text_fr_debug_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "popularity_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "nutrition_score_warning_fruits_vegetables_nuts_estimate_from_ingredients_value": {
#                             "type": "string"
#                           },
#                           "product_name_fr_imported": {
#                             "type": "string"
#                           },
#                           "last_editor": {
#                             "type": "string"
#                           },
#                           "fruits-vegetables-nuts_100g_estimate": {
#                             "type": "string"
#                           },
#                           "carbon_footprint_from_meat_or_fish_debug": {
#                             "type": "string"
#                           },
#                           "ingredients_text_with_allergens": {
#                             "type": "string"
#                           },
#                           "misc_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "image_url": {
#                             "type": "string"
#                           },
#                           "generic_name": {
#                             "type": "string"
#                           },
#                           "data_quality_errors_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "ingredients_that_may_be_from_palm_oil_n": {
#                             "type": "string"
#                           },
#                           "nutrition_score_warning_fruits_vegetables_nuts_estimate_from_ingredients": {
#                             "type": "number"
#                           },
#                           "product_quantity": {
#                             "type": "string"
#                           },
#                           "nutriscore_data": {
#                             "type": "object",
#                             "required": [],
#                             "properties": {
#                               "sugars_value": {
#                                 "type": "number"
#                               },
#                               "is_cheese": {
#                                 "type": "string"
#                               },
#                               "score": {
#                                 "type": "number"
#                               },
#                               "saturated_fat_ratio": {
#                                 "type": "number"
#                               },
#                               "proteins_points": {
#                                 "type": "number"
#                               },
#                               "sodium_points": {
#                                 "type": "number"
#                               },
#                               "positive_points": {
#                                 "type": "number"
#                               },
#                               "sugars": {
#                                 "type": "number"
#                               },
#                               "saturated_fat": {
#                                 "type": "number"
#                               },
#                               "energy_points": {
#                                 "type": "number"
#                               },
#                               "fruits_vegetables_nuts_colza_walnut_olive_oils": {
#                                 "type": "string"
#                               },
#                               "is_beverage": {
#                                 "type": "string"
#                               },
#                               "fiber_points": {
#                                 "type": "string"
#                               },
#                               "saturated_fat_ratio_points": {
#                                 "type": "number"
#                               },
#                               "fiber": {
#                                 "type": "string"
#                               },
#                               "proteins": {
#                                 "type": "number"
#                               },
#                               "negative_points": {
#                                 "type": "number"
#                               },
#                               "fruits_vegetables_nuts_colza_walnut_olive_oils_points": {
#                                 "type": "string"
#                               },
#                               "saturated_fat_ratio_value": {
#                                 "type": "number"
#                               },
#                               "is_fat": {
#                                 "type": "string"
#                               },
#                               "energy_value": {
#                                 "type": "number"
#                               },
#                               "saturated_fat_points": {
#                                 "type": "number"
#                               },
#                               "is_water": {
#                                 "type": "string"
#                               },
#                               "sodium": {
#                                 "type": "number"
#                               },
#                               "grade": {
#                                 "type": "string"
#                               },
#                               "energy": {
#                                 "type": "number"
#                               },
#                               "sodium_value": {
#                                 "type": "number"
#                               },
#                               "proteins_value": {
#                                 "type": "number"
#                               },
#                               "fruits_vegetables_nuts_colza_walnut_olive_oils_value": {
#                                 "type": "string"
#                               },
#                               "fiber_value": {
#                                 "type": "string"
#                               },
#                               "sugars_points": {
#                                 "type": "string"
#                               },
#                               "saturated_fat_value": {
#                                 "type": "number"
#                               }
#                             }
#                           },
#                           "nutriscore_grade": {
#                             "type": "string"
#                           },
#                           "image_nutrition_url": {
#                             "type": "string"
#                           },
#                           "countries_debug_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "correctors_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "brands_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "selected_images": {
#                             "type": "object",
#                             "required": [],
#                             "properties": {
#                               "front": {
#                                 "type": "object",
#                                 "required": [],
#                                 "properties": {
#                                   "thumb": {
#                                     "type": "object",
#                                     "required": [],
#                                     "properties": {
#                                       "fr": {
#                                         "type": "string"
#                                       }
#                                     }
#                                   },
#                                   "display": {
#                                     "type": "object",
#                                     "required": [],
#                                     "properties": {
#                                       "fr": {
#                                         "type": "string"
#                                       }
#                                     }
#                                   },
#                                   "small": {
#                                     "type": "object",
#                                     "required": [],
#                                     "properties": {
#                                       "fr": {
#                                         "type": "string"
#                                       }
#                                     }
#                                   }
#                                 }
#                               },
#                               "nutrition": {
#                                 "type": "object",
#                                 "required": [],
#                                 "properties": {
#                                   "thumb": {
#                                     "type": "object",
#                                     "required": [],
#                                     "properties": {
#                                       "fr": {
#                                         "type": "string"
#                                       }
#                                     }
#                                   },
#                                   "display": {
#                                     "type": "object",
#                                     "required": [],
#                                     "properties": {
#                                       "fr": {
#                                         "type": "string"
#                                       }
#                                     }
#                                   },
#                                   "small": {
#                                     "type": "object",
#                                     "required": [],
#                                     "properties": {
#                                       "fr": {
#                                         "type": "string"
#                                       }
#                                     }
#                                   }
#                                 }
#                               },
#                               "ingredients": {
#                                 "type": "object",
#                                 "required": [],
#                                 "properties": {
#                                   "display": {
#                                     "type": "object",
#                                     "required": [],
#                                     "properties": {
#                                       "fr": {
#                                         "type": "string"
#                                       }
#                                     }
#                                   },
#                                   "small": {
#                                     "type": "object",
#                                     "required": [],
#                                     "properties": {
#                                       "fr": {
#                                         "type": "string"
#                                       }
#                                     }
#                                   },
#                                   "thumb": {
#                                     "type": "object",
#                                     "required": [],
#                                     "properties": {
#                                       "fr": {
#                                         "type": "string"
#                                       }
#                                     }
#                                   }
#                                 }
#                               }
#                             }
#                           },
#                           "traces": {
#                             "type": "string"
#                           },
#                           "pnns_groups_1_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "other_nutritional_substances_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "sortkey": {
#                             "type": "number"
#                           },
#                           "allergens_from_ingredients": {
#                             "type": "string"
#                           },
#                           "countries": {
#                             "type": "string"
#                           },
#                           "image_nutrition_small_url": {
#                             "type": "string"
#                           },
#                           "net_weight_value": {
#                             "type": "string"
#                           },
#                           "ingredients_ids_debug": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "_keywords": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "languages": {
#                             "type": "object",
#                             "required": [],
#                             "properties": {
#                               "en:french": {
#                                 "type": "number"
#                               }
#                             }
#                           },
#                           "entry_dates_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "owners_tags": {
#                             "type": "string"
#                           },
#                           "lc_imported": {
#                             "type": "string"
#                           },
#                           "languages_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "stores_debug_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "product_name_fr": {
#                             "type": "string"
#                           },
#                           "rev": {
#                             "type": "number"
#                           },
#                           "categories_imported": {
#                             "type": "string"
#                           },
#                           "labels_prev_hierarchy": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "nutrition_score_beverage": {
#                             "type": "string"
#                           },
#                           "ingredients_n_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "emb_codes_20141016": {
#                             "type": "string"
#                           },
#                           "languages_codes": {
#                             "type": "object",
#                             "required": [],
#                             "properties": {
#                               "fr": {
#                                 "type": "number"
#                               }
#                             }
#                           },
#                           "traces_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "quantity_debug_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "ingredients_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "data_quality_info_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "origins_debug_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "vitamins_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "nova_group": {
#                             "type": "number"
#                           },
#                           "nutrient_levels": {
#                             "type": "object",
#                             "required": [],
#                             "properties": {
#                               "saturated-fat": {
#                                 "type": "string"
#                               },
#                               "sugars": {
#                                 "type": "string"
#                               },
#                               "salt": {
#                                 "type": "string"
#                               },
#                               "fat": {
#                                 "type": "string"
#                               }
#                             }
#                           },
#                           "stores": {
#                             "type": "string"
#                           },
#                           "allergens_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "purchase_places_debug_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "expiration_date": {
#                             "type": "string"
#                           },
#                           "amino_acids_prev_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "scans_n": {
#                             "type": "number"
#                           },
#                           "image_ingredients_url": {
#                             "type": "string"
#                           },
#                           "expiration_date_debug_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "lang_debug_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "data_sources_imported": {
#                             "type": "string"
#                           },
#                           "owner": {
#                             "type": "string"
#                           },
#                           "image_front_thumb_url": {
#                             "type": "string"
#                           },
#                           "photographers_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "informers_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "labels_lc": {
#                             "type": "string"
#                           },
#                           "categories_lc": {
#                             "type": "string"
#                           },
#                           "allergens_hierarchy": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "image_ingredients_small_url": {
#                             "type": "string"
#                           },
#                           "link_debug_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "sources": {
#                             "type": "array",
#                             "items": {
#                               "type": "object",
#                               "required": [],
#                               "properties": {
#                                 "fields": {
#                                   "type": "array",
#                                   "items": {
#                                     "type": "string"
#                                   }
#                                 },
#                                 "import_t": {
#                                   "type": "number"
#                                 },
#                                 "url": {
#                                   "type": "string"
#                                 },
#                                 "id": {
#                                   "type": "string"
#                                 },
#                                 "manufacturer": {
#                                   "type": "string"
#                                 },
#                                 "images": {
#                                   "type": "array",
#                                   "items": {
#                                     "type": "string"
#                                   }
#                                 },
#                                 "name": {
#                                   "type": "string"
#                                 }
#                               }
#                             }
#                           },
#                           "unknown_nutrients_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "last_modified_by": {
#                             "type": "string"
#                           },
#                           "allergens": {
#                             "type": "string"
#                           },
#                           "traces_hierarchy": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "net_weight_unit": {
#                             "type": "string"
#                           },
#                           "generic_name_fr": {
#                             "type": "string"
#                           },
#                           "interface_version_modified": {
#                             "type": "string"
#                           },
#                           "states_hierarchy": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "editors_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "carbon_footprint_from_known_ingredients_debug": {
#                             "type": "string"
#                           },
#                           "ciqual_food_name_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "ingredients_from_or_that_may_be_from_palm_oil_n": {
#                             "type": "string"
#                           },
#                           "interface_version_created": {
#                             "type": "string"
#                           },
#                           "quantity_imported": {
#                             "type": "string"
#                           },
#                           "countries_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "cities_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "nucleotides_prev_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "last_image_t": {
#                             "type": "number"
#                           },
#                           "nucleotides_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "minerals_prev_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "image_front_small_url": {
#                             "type": "string"
#                           },
#                           "new_additives_n": {
#                             "type": "number"
#                           },
#                           "origins": {
#                             "type": "string"
#                           },
#                           "ingredients_debug": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "additives_old_n": {
#                             "type": "number"
#                           },
#                           "data_sources_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "purchase_places_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "unknown_ingredients_n": {
#                             "type": "number"
#                           },
#                           "url": {
#                             "type": "string"
#                           },
#                           "nutrition_grades_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "data_quality_bugs_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "additives_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "popularity_key": {
#                             "type": "number"
#                           },
#                           "checkers_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "packaging_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "stores_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "ingredients_text": {
#                             "type": "string"
#                           },
#                           "manufacturing_places_debug_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "allergens_from_user": {
#                             "type": "string"
#                           },
#                           "data_quality_warnings_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "categories": {
#                             "type": "string"
#                           },
#                           "manufacturing_places_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "additives_debug_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "creator": {
#                             "type": "string"
#                           },
#                           "emb_codes": {
#                             "type": "string"
#                           },
#                           "additives_original_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "nutrition_data_per_debug_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "serving_size_debug_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "image_small_url": {
#                             "type": "string"
#                           },
#                           "labels_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "serving_size": {
#                             "type": "string"
#                           },
#                           "additives_n": {
#                             "type": "number"
#                           },
#                           "pnns_groups_1": {
#                             "type": "string"
#                           },
#                           "categories_properties_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "ingredients_text_debug": {
#                             "type": "string"
#                           },
#                           "category_properties": {
#                             "type": "object",
#                             "required": [],
#                             "properties": {
#                               "ciqual_food_name:en": {
#                                 "type": "string"
#                               },
#                               "ciqual_food_name:fr": {
#                                 "type": "string"
#                               }
#                             }
#                           },
#                           "carbon_footprint_percent_of_known_ingredients": {
#                             "type": "number"
#                           },
#                           "nutrition_data_per": {
#                             "type": "string"
#                           },
#                           "image_ingredients_thumb_url": {
#                             "type": "string"
#                           },
#                           "nova_groups_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "categories_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "origins_tags": {
#                             "type": "array",
#                             "items": {
#                               "type": "string"
#                             }
#                           },
#                           "update_key": {
#                             "type": "string"
#                           },
#                           "nutrition_data_prepared_per": {
#                             "type": "string"
#                           },
#                           "ingredients_n": {
#                             "type": "number"
#                           },
#                           "data_sources": {
#                             "type": "string"
#                           },
#                           "ingredients_from_palm_oil_n": {
#                             "type": "string"
#                           }
#                         }
#                       }
#                     },
#                     "skip": {
#                       "type": "string"
#                     },
#                     "page_size": {
#                       "type": "number"
#                     }
#                   }
#                 })
#
#     assert schema.is_valid(choucroute_json)
