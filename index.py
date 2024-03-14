import json

d1={'name':'Gaurav','age':22}

json_data=json.dumps(d1)

print(json_data)

p_data=json.loads(json_data)
print(p_data)



# models ======================================>serilization=================================>json
# models<=======================================deserilization <=============================== json






# ====================================================================================================================================================





# Api
# api is intermediatary that alllows two or more application to talk to each other 





# =====================================================================================================








# types of api

# private-used within orgAanization 

# partner-use within buisness partner 

# public - use with third party developers







# ================================================================================================================




# web api
# an api which is interface for web is called api
# it may be consist of one or more endpoints to define request and response 


# how web api works

# android application    webapi        web application



# client makes HTTP request to api 

# api willcommunicate to web application 
# web application database provides required data to api



# =============================================================================================================







# REST :

# architactural guideline to develop web api

# api which is developed using rest is rest api

# how rest web api works :
#         androd      ------------------> web api------------------->web application



# ==========================================================================================================================================



# CRUD operation 

# operation                                       HTTP Method                                    desc 
# ------------------------------------------------------------------------------------------------------------------
# create                                          POST                                         create  /post/insert data
# read                                           GET                                           reading /getting /retriving data
# update                                         put/patch                                     updating data  complete data -put   , partial -patch
# delete                                         delete                                        delete Data
# -----------------------------------------------------------------------------------------------------------------------------------------









# serilization

# # in django Rest framework Serilizer are the responsible for converting thr complex data such as queryset ad model 
# # instance to native pyhton datatype that can be them 
# # easily renderd into json ,xml

# # types which is understable by front end