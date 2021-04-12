import flask
import ArborRecipe
import ast
from ArborRecipe.api.invalid_usage import InvalidUsage
from flask import jsonify
from flask import request
import ast
import json

# fix lower case letter

@ArborRecipe.app.route('/api/i', methods=["GET"])
def get_recipe():

    print("get recipe")
    ingredients = [] 
    # saves sets of recipe id
    recipe_id_sets = []
    recipes_id = set()
    recipes_text = {}

    restr = request.args.get('restr')

    ingredients = request.args.get('ingredients').split(",")
    print(ingredients)
    connection = ArborRecipe.model.get_db()
    for ingredient in ingredients:
        cur = connection.execute(
            "SELECT recipe_id FROM ingredient_table WHERE ingredients = ?", [ingredient.lower()]
        ).fetchone()
        #catch if ingrridients not found
        print(cur)
        recipe_id_sets.append(ast.literal_eval(cur["recipe_id"]))
    

    print("recipe_id_sets", recipe_id_sets) 
    # find recipes 
    for set_id in recipe_id_sets:
        print(type(set_id), type(recipes_id))
        recipes_id = recipes_id | set_id

    number = 0 


    res_list = []
    for recipe in recipes_id:
        cur2 = connection.execute(
            "SELECT * FROM recipe_table WHERE recipe_id = ?", [recipe]
        ).fetchone()
        
        temp = {
            "recipe_id"  : cur2["recipe_id" ],
            "recipe_name" :  cur2["recipe_name"],
            "ingredients" : cur2["ingredients"],
            "instruction" :  cur2["instruction"] ,
            "cooking_time" :  cur2["cooking_time"],
            "prep_time" : cur2["prep_time"]
        }

        res_list.append(temp)
    #     recipes_text[number] = temp
    #     number+=1
    # print(json.dumps(recipes_text, indent=2))
    res_dict = {'recipe': res_list}
 
    return flask.jsonify(**res_dict)