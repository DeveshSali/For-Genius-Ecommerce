from product.models import Product, Features
from user.errors import InputError
from user.models import Admin
from product.products import get_product_features
from user.models import User, Search_history
from user.errors import InputError

# return the search list from the chosen search key and sorting algothirms
def get_search_result(email, search, sorting):
    # check is the sorting algothirms are invalid
    if sorting != "price_low" and sorting != "price_high" and sorting != "best_sell" and sorting != "a_to_z" and sorting != "z_to_a" and sorting != "relevance":
        raise InputError("The sorting is invalid")
    
    # check if the search word is valid
    if search == "":
        raise InputError("The search word in empty")
    
    # add the search to user's search history
    if email != "":
        try:
            user_email = User.objects.get(pk=email)
        except User.DoesNotExist:
            raise InputError('User not exist')

        search_save = Search_history(user_email=user_email, search=search)
        search_save.save()
    
    
    search = search.lower().split()
    data = Product.objects.filter()
    result = get_products(search, data, 1)
    if len(result) == 0:
        result = get_products(search, data, 2)
        if len(result) == 0:
            result = get_products(search, data, 3)
   
    
    # sort the result list with chosen method
    result_list = sort_help(sorting, result, search)
    return_list = []
    # output the product in the result list 
    for product in result_list:
        item = {
            "product_id" : product.product_id,
            "name" : product.name,
            "description" : product.description[:30],
            "sales_data" : product.sales_data,
            "price" : round(float(product.price), 2),
            "picture" : product.picture,
            "features" : get_product_features(product.product_id) 
        }
        return_list.append(item)
        
    return return_list

def get_products(search, data, level):
    result = []
     # choose the relevant products from the database
    for product in data:
        add = False
        for search_word in search:
            if add == True:
                break
            # if the search word in the product name or desription
            word = " " + search_word + " "
            if word in product.name.lower():
                result.append(product)
                add = True
                continue
            
            # check the first word
            
            name = product.name.lower().split( )
            if search_word == name[0]:
                result.append(product)
                add = True
                continue
            
             # check the last word
            
            if search_word == name[len(name) - 1]:
                result.append(product)
                add = True
                continue
            
            
            
            if level >= 3:
                if search_word in product.name.lower():
                    result.append(product)
                    add = True
                    continue
            
            
            # if the search word in the product feature
            features = Features.objects.filter(product_id = product.product_id)
            for feature in features:
                # if there are many words in the feature, split them and check if same
                if "_" in feature.feature:
                    words = feature.feature.lower().split('_')
                    for feature_word in words:
                        if feature_word == search_word and add != True:
                            result.append(product)
                            add = True
                            break
                    
                    if level >=2:
                        if search_word in feature.feature.lower():
                            result.append(product)
                            add = True
                            break
                    
                    if add == True:
                        break
                    
                
                if search_word == feature.feature.lower():
                    result.append(product)
                    add = True
                    break
                
                if level >= 2:
                    if search_word in feature.feature.lower():
                        result.append(product)
                        add = True
                        break
                
    return result
    
# the helper function for sorting
def sort_help(sorting, list, search):
    result = []
    return recursion_help(result, list, search, sorting)

# the helper function for recursion        
def recursion_help(result, list, search_list, sorting):
    if len(list) == 0:
        return result
    first = 0
    # choose the chosen method based on the sorting
    for j in range(0, len(list)):
        if (sorting == "price_low"):
            if list[j].price < list[first].price:
                first = j
        if (sorting == "price_high"):
            if list[j].price > list[first].price:
                first = j
        if (sorting == "best_sell"):
            if list[j].sales_data > list[first].sales_data:
                first = j
        if (sorting == "a_to_z"):
            if list[j].name < list[first].name:
                first = j
        if (sorting == "z_to_a"):
            if list[j].name > list[first].name:
                first = j
        # using the optional method in the relevance sorting 
        if (sorting == "relevance"):
            val1 , val2 = 0.0, 0.0
            product_j = Product.objects.get(product_id = list[j].product_id)
            product_first = Product.objects.get(product_id = list[first].product_id)
            for search in search_list:
                if search in product_j.name.lower():
                    val1 += 1.0
                    
                if search in product_first.name.lower():
                    val2 += 1.0
                    
                if search in product_j.description.lower():
                    val1 += 0.1
                    
                if search in product_first.description.lower():
                    val2 += 0.1  
                           
                # if the search word in the product feature
                featuresj = Features.objects.filter(product_id = product_j.product_id)
                for feature in featuresj:
                    if search == feature.feature.lower():
                        val1 += 1.0
                    if search in feature.feature.lower():
                        val1 += 1.0   
                                     
                features = Features.objects.filter(product_id = product_first.product_id)
                for feature in features:
                    if search == feature.feature.lower():
                        val2 += 1.0
                    if search in feature.feature.lower():
                        val2 += 1.0     
            
            if val1 > val2:
                first = j
                      
            if val1 == val2 and list[j].sales_data > list[first].sales_data:
                first = j

    # add the most optinal one in the result lists and start next recursion.
    result.append(list[first])
    list.remove(list[first])
    return recursion_help(result, list, search_list, sorting)
