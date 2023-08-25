import csv
import time
import requests

# ================================================
Agency_Name_new = "UsmanAPItesting112"
Agency_Name = "AimalQA"
Agency_ID = "9"
Campaign_ID = "16042"
Buisiness_ID = "267473"
Client_id = "1874"
Keyword_name = "API TESTING"
# ================================================
business_name = "Red Royal Electric"
latitude = "27.9678923"
longitude = "-82.7962614"

# =========================

first_api_list = [
    
    # ====////Admin API////=======
    
    # {
    #     "url": f"http://50.28.76.71:7845/admin/apis/keywords/list/{Campaign_ID}",
    #     "method": "GET",
    #     "params": None
    # },
    # {
    #     "url": f"http://50.28.76.71:7845/admin/apis/business/categories/{Buisiness_ID}",
    #     "method": "GET",
    #     "params": None
    # },
    # {
    #     "url": "http://50.28.76.71:7845/admin/apis/update/keyword/values/serpapi/list/",
    #     "method": "PUT",
    #     "params":
    #         [
    #             {
    #                 "id": Campaign_ID,
    #                 "organic_results_link": "string",
    #                 "top_primary_categories": "string",
    #                 "has_map": 1
    #             }
    #         ]
    # },
    # {
    #     "url": "http://50.28.76.71:7845/admin/apis/update/keyword/values/all/list/",
    #     "method": "PUT",
    #     "params":
    #         [
    #             {
                
    #             "id": 16042,
    #             "page_score": 0,
    #             "keyword_in_url": 1,
    #             "keyword_in_page_title": 1,
    #             "keyword_in_h1": 1,
    #             "keyword_in_page_description": 1,
    #             "keyword_in_page_body": 1,
    #             "keyword_in_image_alt": 1,
    #             "keyword_in_body_content_score": 1,
    #             "geo_grid_keyword_id": "string",
    #             "grids_ranks": "string"
                
    #             }
    #         ]
    # },
    # {
    #     "url": "http://50.28.76.71:7845/admin/apis/update/keyword/values/all/list/serp/",
    #     "method": "PUT",
    #     "params":
    #         [
    #         {
            
    #         "organic_results_link": "string",
    #         "top_primary_categories": "string",
    #         "has_map": 1,
    #         "id": 15765,
    #         "page_score": 0,
    #         "keyword_in_url": 1,
    #         "keyword_in_page_title": 1,
    #         "keyword_in_h1": 1,
    #         "keyword_in_page_description": 1,
    #         "keyword_in_page_body": 1,
    #         "keyword_in_image_alt": 1,
    #         "keyword_in_body_content_score": 1
            
    #         }
    #         ]
    # },
    # {
    #     "url": "http://50.28.76.71:7845/admin/apis/update/keyword/analysis/categories/score/list/",
    #     "method": "PUT",
    #     "params":
    #         [
    #             {
            
    #         "id": 15765,
    #         "category_score": 0,
    #         "category_sub_score": 0
            
    #         }
    #         ]
    # },
    # {
    #     "url": "http://50.28.76.71:7845/admin/apis/update/keyword/analysis/all/list/",
    #     "method": "PUT",
    #     "params":
    #         [
    #             {
            
    #         "search_volume": 0,
    #         "count_per_click": 0,
    #         "website_score": 0,
    #         "proximity_score": 0,
    #         "map_rank": 0,
    #         "keyword_analysis_status": 5,
    #         "geo_grid_sub_score": 0,
    #         "on_page_sub_score": 0,
    #         "id": 15765
            
    #         }
    #             ]
    # },
    
    # {
    #     "url": "http://50.28.76.71:7845/admin/apis/call/procedure/manual/business/stats/",
    #     "method": "PUT",
    #     "params":
            
    #             {
    #             "business_id": 12752,
    #             "start_month": "2022-08-03",
    #             "end_month": "2022-08-03"
    #             }
            
    # },
    
    # # ====////Agency////=======
    
    # {
    #     "url": f"http://50.28.76.71:7845/agency/{Agency_ID}",
    #     "method": "GET",
    #     "params": None
    # },
    
    # {
    #     "url": "http://50.28.76.71:7845/agency/search/agencies/",
    #     "method": "GET",
    #     "params":{
    #         "search_query": Agency_Name,
    #         "page": 1,
    #         "size": 10
    #     }
    # },
    
    # {
    #     "url": f"http://50.28.76.71:7845/agency/update/{Agency_ID}",
    #     "method": "PUT",
    #     "params":
    #         {
    #         "is_full_reporting": 1
    #         }
            
    # },
    
    # {
    #     "url": "http://50.28.76.71:7845/agency/create/",
    #     "method": "POST",
    #     "params":
            
    #         {
    #         "agency_name": Agency_Name_new,
    #         "is_full_reporting": 1
    #          }
            
    # },
    # {
    #     "url": "http://50.28.76.71:7845/agency/agencies/list/?page=&size=",
    #     "method": "GET",
    #     "params":{
    #         "page": 1,
    #         "size": 50
    #     }
    # },
    # {
    #     "url": "http://50.28.76.71:7845/agency/agencies/list/all/",
    #     "method": "GET",
    #     "params": None
    # },
    # {
        
    #     "url": f"http://50.28.76.71:7845/agency/campaigns/{Campaign_ID}/?id=&campaign_status=&search_query=&offset=",
    #     "method": "GET",
    #     "params":{
    #             "id": Campaign_ID,
    #             "campaign_status": 0,
    #             "search_query": 1,
    #             "offset": 15,
    #             }
    # },
    # {
    #     "url": "http://50.28.76.71:7845/agency/agency-popup-data",
    #     "method": "GET",
    #     "params": None
    # },
    
#     # ====////Campaigns////=======
    
    
    # {
    #     "url": f"http://50.28.76.71:7845/campaigns/{Campaign_ID}",
    #     "method": "GET",
    #     "params": None
    # },
    # {
        
    #     "url": f"http://50.28.76.71:7845/campaigns/get/{business_name}/categories/{latitude}/serpapi/{longitude}/",
    #     "method": "GET",
    #     "params":None
    # },
    # {
    #     "url": f"http://50.28.76.71:7845/campaigns/full/{Campaign_ID}",
    #     "method": "GET",
    #     "params":None
    # },
    # {
    #     "url": "http://50.28.76.71:7845/campaigns/create/full/campaign/",
    #     "method": "POST",
    #     "params":{
    #             "business_name": "The tooth clinic",
    #             "business_website": None,
    #             "business_image": None,
    #             "business_gmb_cid": "1177042217874412191",
    #             "business_category_id": None,
    #             "business_category": "Dental clinic",
    #             "business_address": "Opposite Malik oil kolho, gohava morr, Bedian Rd, Lahore, 54000, Pakistan",
    #             "country_id": 162,
    #             "states_id": None,
    #             "states": None,
    #             "city": None,
    #             "zip_code": None,
    #             "longitude": 74.4195558,
    #             "latitude": 31.4843989,
    #             "place_id": "ChIJUU6nqiIPGTkRn9IKMqmxVRA",
    #             "business_id": 0,
    #             "campaign_name": "The TOOTH Clinic",
    #             "campaign_status": 1,
    #             "campaign_score": 0,
    #             "geo_grid_config_id": None,
    #             "is_updated": 1,
    #             "is_full_reporting": 0,
    #             "keywords_for_analysis": "Dental clinic",
    #             "user_id": 1,
    #             "agency_id": 9,
    #             "locafy_client_id": 0,
    #             "client_id": 10084
    #     }
    # },
    # {
    #     "url": "http://50.28.76.71:7845/campaigns/create/",
    #     "method": "POST",
    #     "params":
    #             {
    #                 "business_id": 267473,
    #                 "user_id": 1,
    #                 "agency_id": 1,
    #                 "client_id": 1,
    #                 "campaign_name": "API testing",
    #                 "campaign_status": 1,
    #                 "is_updated": 1,
    #                 "is_full_reporting": 1,
    #                 "is_gifs": 1,
    #                 "is_google_authorized": 1,
    #                 "is_monthly_reporting": 1,
    #                 "is_bmp_status": 1,
    #                 "quick_analysis": 0
    #                 }
    # },
    # {
    #     "url": "http://50.28.76.71:7845/campaigns/bpm/16045/1",
    #     "method": "PUT",
    #     "params": None
    # },

    # {
    #     "url": "http://50.28.76.71:7845/campaigns/bpm/update/map_ss/16045/",
    #     "method": "PUT",
    #     "params": 
    #             [
    #                 {
    #             "campaign_id": 16045,
                
    #             }
    #                 ]
    # },
    
    # {
    #     "url": "http://50.28.76.71:7845/campaigns/bpm/campaigns/average_ranks/",
    #     "method": "PUT",
    #     "params": 
    #                 {
    #                     "campaign_id": 16045,
    #                     "current_date": "string"
    #                     }
    # },

    # {
    #     "url": "http://50.28.76.71:7845/campaigns/bpm/kw/scores/",
    #     "method": "PUT",
    #     "params": 
                
    #                 {
    #                 "campaign_id": 16045
    #                 }
                
    # },
    # {
    #     "url": "http://50.28.76.71:7845/campaigns/bpm/kw/proximity_scores_history/",
    #     "method": "PUT",
    #     "params": 
            
    #                 {
    #                 "campaign_id": 16045
    #                 }
            
    # },
    # {
    #     "url": "http://50.28.76.71:7845/campaigns/bpm/compitators",
    #     "method": "POST",
    #     "params": 
    #                         {
    #         "b_id": [
    #             "null"
    #         ],
    #         "new_business_competitors": [
    #             "null"
    #         ],
    #         "competitors_record_keyword_analysis": [
    #             "null"
    #         ],
    #         "competitors_record": [
    #             "null"
    #         ],
    #         "campaign_id": [
    #             "null"
    #         ]
    #         }
    # },
    # {
    #     "url": "http://50.28.76.71:7845/campaigns/bpm/gifs/{id}/?date_to_store_gifs",
    #     "method": "PUT",
    #     "params":
    #             [
    #                 {
    #                 "business_name": "string",
    #                 "business_website": "string",
    #                 "business_image": "string",
    #                 "business_gmb_cid": "string",
    #                 "business_category_id": 0,
    #                 "business_category": "string",
    #                 "business_address": "string",
    #                 "country_id": 0,
    #                 "states_id": 0,
    #                 "states": "string",
    #                 "city": "string",
    #                 "zip_code": "string",
    #                 "longitude": 0,
    #                 "latitude": 0,
    #                 "place_id": "string",
    #                 "business_id": 0,
    #                 "campaign_name": "string",
    #                 "campaign_status": 5,
    #                 "geo_grid_config_id": "string",
    #                 "is_updated": 1,
    #                 "is_full_reporting": 0,
    #                 "locafy_client_id": "string",
    #                 "is_monthly_reporting": 0,
    #                 "is_gifs": 1,
    #                 "keywords_for_analysis": "string",
    #                 "user_id": 0,
    #                 "agency_id": 0,
    #                 "client_id": 0,
    #                 "sub_categories": "string"
    #                 }               
    #             ]
    # },
    # {
    #     "url": "http://50.28.76.71:7845/campaigns/update/status/16045",
    #     "method": "PUT",
    #     "params":
    #             {
    #             "campaign_status": 3
    #             }           
                
    # },
    # {
    #     "url": "http://50.28.76.71:7845/campaigns/update/reporting/type/16045/",
    #     "method": "PUT",
    #     "params":
                
    #                 {
    #                 "is_full_reporting": 1,
    #                 "is_monthly_reporting": 1,
    #                 "is_gifs": 1
    #                 }           
                
    # },
    # {
    #     "url": "http://50.28.76.71:7845/campaigns/update/is/full/reporting/16045/",
    #     "method": "PUT",
    #     "params":
                
    #                 {
    #                 "is_full_reporting": 1
    #                 }         
                
    # },
    # {
    #     "url": "http://50.28.76.71:7845/campaigns/update/is/full/reporting/16045/",
    #     "method": "PUT",
    #     "params":
                
    #                 {
    #                     "is_monthly_reporting": 1
    #                     }         
                
    # },
    # {
    #     "url": "http://50.28.76.71:7845/campaign/update/status/is/updated/16042",
    #     "method": "PUT",
    #     "params":
                
    #                 {
    #                 "campaign_status": 5,
    #                 "is_updated": 0
    #                 }       
                
    # },
    # {
    #     "url": "http://50.28.76.71:7845/campaigns/update/is/gifs/16042",
    #     "method": "PUT",
    #     "params":
                
    #                 {
    #                 "is_gifs": 1
    #                 }      
                
    # },
    # {
    #     "url": "http://50.28.76.71:7845/campaigns/update/configid/16042",
    #     "method": "PUT",
    #     "params":
                
    #                 {
    #                 "geo_grid_config_id": "string"
    #                 }      
                
    # },
    # {
    #     "url": "http://50.28.76.71:7845/campaigns/update/full/campaign/16042/43/",
    #     "method": "PUT",
    #     "params":
                
    #                 {
    #                 "campaign_name": "food12345",
    #                 "campaign_status": 5,
    #                 "is_full_reporting": 1,
                
    #                 "client_id": 1088,
    #                 "agency_id": 9,
                    
    #                 "added_keywords": [
    #                     "usman"
    #                 ],
    #                 }
                
    # },
    # {
    #     "url": "http://50.28.76.71:7845/campaigns/list/campaigns/",
    #     "method": "GET",
    #     "params": None
    # },
    # {
    #     "url": "http://50.28.76.71:7845/campaigns/list/live/campaigns/",
    #     "method": "GET",
    #     "params": None
    # },
    # {
    #     "url": "http://50.28.76.71:7845/campaigns/list/status/",
    #     "method": "GET",
    #     "params": None
    # },
    
#     # ====////Campaigns assignment////=======

    # {
    #     "url": "http://50.28.76.71:7845/campaign/assign/users/assignuser/",
    #     "method": "POST",
    #     "params": {
    #                 "campaign_id": 16045,
    #                 "assigned_user": 0
    #                 }
  
    # },
    # {
    #     "url": "http://50.28.76.71:7845/campaign/assign/users/update/campaigns/15765/user/1258",
    #     "method": "PUT",
    #     "params": {
    #                 "assigned_user": 226
    #                 }
  
    # },
    # {
    #     "url": "http://50.28.76.71:7845/campaign/assign/users/get/assigned/user/15765",
    #     "method": "GET",
    #     "params": None
  
    # },
    # {
    #     "url": "http://50.28.76.71:7845/campaign/assign/users/get/assigned/campaigns/list/224 =",
    #     "method": "GET",
    #     "params": None
  
    # },
    # {
    #     "url": "http://50.28.76.71:7845/campaign/assign/users/get/assigned/campaigns/list/224",
    #     "method": "GET",
    #     "params": None
  
    # },
    
# #==========Client=============
    
#     {
#     "url": "http://50.28.76.71:7845/clients/1074",
#     "method": "GET",
#     "params": None
# },

# {
#          "url": "http://50.28.76.71:7845/clients/get/details/status/db/?page=1&size=50",
#          "method": "GET",
#          "params": 
         
#             {
#                 "Page" : 1,
#                 "size" : 50
#             }
         
# },
# {
#          "url": "http://50.28.76.71:7845/clients/create/",
#          "method": "POST",
#          "params": 
#             {
                
#                 "user_id": 43,
#                 "agency_id": 9,
#                 "client_name": "11response1123",
#                 "is_active": 1  
#             }
#     },

# {
#         "url": "http://50.28.76.71:7845/clients/update/status/1063",
#         "method": "PUT",
#         "params":
            
#                 {
#                     "is_active": 0
#                 }
            
# },
# {
#         "url": "http://50.28.76.71:7845/clients/update/client/1063",
#         "method": "PUT",
#         "params":
            
#                 {
#                     "client_name": "Worldoftomorrow5"
#                 }
            
# },


# {
#     "url": "http://50.28.76.71:7845/clients/clients/list/",
#     "method": "GET",
#     "params": None
            
# },

# {
#         "url": "http://50.28.76.71:7845/clients/assignuser/",
#         "method": "POST",
#         "params":
           
#         {
#             "user_id": 192,
#             "client_id": 10078
#             }
        
# },

# {
#          "url": "http://50.28.76.71:7845/clients/search/client/?search_query=Abdullahbhai2.0",
#          "method": "GET",
#          "params": 
#             {
#                 "search_query" : "Abdullahbhai2.0",
#                 }
        
# },

# {
#         "url": "http://50.28.76.71:7845/clients/assign/team/1682",
#         "method": "PUT",
#         "params":
            
#                 {
#                     "team_id": 93,
#                     "user_id" : 590
#                 }
            
#     },


# {
#         "url": "http://50.28.76.71:7845/clients/campaigns/1118/?campaign_status=3",
#         "method": "GET",
#         "params": None
            
# }, 
#     # ====////Roles////=======
    
    # {
    #     "url": "http://50.28.76.71:7845/roles/2",
    #     "method": "GET",
    #     "params": None
  
    # },
    # {
    #     "url": "http://50.28.76.71:7845/roles/create/",
    #     "method": "POST",
    #     "params": {
    #                 "roles_name": "USMAN011245",
    #                 "roles_description": "Manger"
    #                 }
  
    # },
    # {
    #     "url": "http://50.28.76.71:7845/roles/list/all/",
    #     "method": "GET",
    #     "params": None
  
    # },
    # {
    #     "url": "http://50.28.76.71:7845/roles/list/all/below/",
    #     "method": "GET",
    #     "params": None
  
    # },
    
#     # ====////User////=======
    
    # {
    #     "url": "http://50.28.76.71:7845/user/roles/3",
    #     "method": "GET",
    #     "params": None
  
    # },
    # {
    #     "url": "http://50.28.76.71:7845/user/224",
    #     "method": "GET",
    #     "params": None
  
    # },
    # {
    #     "url": "http://50.28.76.71:7845/user/users/agency/1",
    #     "method": "GET",
    #     "params": None
  
    # },
    # {
    #     "url": "http://50.28.76.71:7845/user/get/list/103,114,108",
    #     "method": "GET",
    #     "params": None
  
    # },
    
    # {
    #     "url": "http://50.28.76.71:7845/user/name/testadminkhan sadadsa/",
    #     "method": "GET",
    #     "params":None
  
    # },
    # {
    #     "url": "http://50.28.76.71:7845/user/create/",
    #     "method": "POST",
    #     "params":{
    #             "role_id": 2,
    #             "agency_id": 8,
    #             "user_email": "string",
    #             "user_name": "stringfgdfhdfhfh",
    #             "user_password": "strhfghfghfging",
    #             "profile_image": "strifghfghgfng",
    #             "is_users_active": 1
    #             }
  
    # },
    # {
    #     "url": "http://50.28.76.71:7845/user/list/users/",
    #     "method": "GET",
    #     "params": None
  
    # },
    # {
    #     "url": "http://50.28.76.71:7845/user/users/me",
    #     "method": "GET",
    #     "params": None
  
    # },
    # {
    #     "url": "http://50.28.76.71:7845/user/list/users/1/teamid/",
    #     "method": "GET",
    #     "params": None
  
    # },
    # {
    #     "url": "http://50.28.76.71:7845/user/users/assign/team/8",
    #     "method": "PUT",
    #     "params": 
    #         {
    #         "user_ids": "225,193"
    #         }
        
  
    # },
    # {
    #     "url": "http://50.28.76.71:7845/user/managers/155/?page=1&size=20",
    #     "method": "GET",
    #     "params": {
    #         "Page": 1,
    #         "Size": 20
    #         }
  
    # },
    # {
    #     "url": "http://50.28.76.71:7845/user/users/155/?page=1&size=10",
    #     "method": "GET",
    #     "params": {
    #         "Page": 1,
    #         "Size": 10
    #         }
  
    # },
    # {
    #     "url": "http://50.28.76.71:7845/user/users/managers/12",
    #     "method": "GET",
    #     "params": None
  
    # },
    # {
    #     "url": "http://50.28.76.71:7845/user/campaigns/12/?campaign_status=4&search_query=string&offset=1",
    #     "method": "GET",
    #     "params":{
    #         "campaign_status": 4,
    #         "search_query": "string",
    #         "offset": 1
            
                  
    #               }
  
    # },
    # {
    #     "url": "http://50.28.76.71:7845/user/team/created/users/53/",
    #     "method": "GET",
    #     "params": None
  
    # },
    
# # //////Users Owners///////

    # {
    #     "url": "http://50.28.76.71:7845/user/owner/list/users/with/campaigns/?page=1&size=50",
    #     "method": "GET",
    #     "params": {
    #         "Page": 1,
    #         "Size": 50,
    #               }
    # },
    # {
    #     "url": "http://50.28.76.71:7845/user/owner/get/list/team/names/against/user/20/",
    #     "method": "GET",
    #     "params": None
    # },
    # {
    #     "url": "http://50.28.76.71:7845/user/owner/list/users/with/owner/",
    #     "method": "GET",
    #     "params": None
    # },
    # {
    #     "url": "http://50.28.76.71:7845/user/owner/assign/",
    #     "method": "POST",
    #     "params": 
    #         {
    #         "user_id": 0,
    #         "owner_id": 0
    #         }
    # },
    # {
    #     "url": "http://50.28.76.71:7845/user/owner/update/owner/43/user/221/",
    #     "method": "PUT",
    #     "params":
    #         {
    #         "user_id": 221
    #         }
    # },
    # {
    #     "url": "http://50.28.76.71:7845/user/owner/search/users/?search_query=Zulqarnain&page=1&size=50",
    #     "method": "GET",
    #     "params": 
    #         {
    #         "search_query": "Zulqarnain",
    #         "page": 1,
    #         "size": 50
    #         }
    # },
    # {
    #     "url": "http://50.28.76.71:7845/user/owner/search/teams/users/?search_query=siraj",
    #     "method": "GET",
    #     "params": 
    #         {
    #         "search_query": "Siraj",
    #         "page": 1,
    #         "size": 50
    #         }
    # },
    
#     # ///Notifications///////
    
    # {
    #     "url": "http://50.28.76.71:7845/notifications/create/",
    #     "method": "POST",
    #     "params": 
    #         {
    #         "user_id": 183,
    #         "notification": "string",
    #         "campaign_id": 16045,
    #         "is_seen": 0
    #         }
    # },
    # {
    #     "url": "http://50.28.76.71:7845/notifications/1/?page=1&size=10",
    #     "method": "GET",
    #     "params": 
    #         {
    #         "page": 1,
    #         "size": 10
    #         }
    # },
    # {
    #     "url": "http://50.28.76.71:7845/notifications/update/is_seen/3232",
    #     "method": "PUT",
    #     "params": 
            
    #             {
    #             "is_seen": 1
    #             }
            
    # },
    
    
    # # ///GMB API Users///////
    
    # {
    #     "url": "http://50.28.76.71:7845/gmb/api/users/4",
    #     "method": "GET",
    #     "params": None
    # },
    # {
    #     "url": "http://50.28.76.71:7845/gmb/api/users/11",
    #     "method": "GET",
    #     "params": None
    # },
    # {
    #     "url": "http://50.28.76.71:7845/gmb/api/users/create/",
    #     "method": "POST",
    #     "params": 
    #         {
    #         "user_email": "Zulqarnain001",
    #         "access_token": "stringone",
    #         "refresh_token": "string"
    #         }
    # },
    # {
    #     "url": "http://50.28.76.71:7845/gmb/api/users/update/access/token/12",
    #     "method": "PUT",
    #     "params": 
    #         [
    #             {
    #         "access_token": "string1"
    #         }
    #         ]
    # },
    # {
    #     "url": "http://50.28.76.71:7845/gmb/api/users/update/refresh/token/12",
    #     "method": "PUT",
    #     "params": 
    #         [
    #             {
    #             "refresh_token": "string02"
    #             }
    #         ]
    # },
    # {
    #     "url": "http://50.28.76.71:7845/gmb/api/users/update/tokens/12",
    #     "method": "PUT",
    #     "params": 
    #         [
    #             {
    #             "access_token": "strings",
    #             "refresh_token": "strings"
    #             }
    #         ]
    # },
    # {
    #     "url": "http://50.28.76.71:7845/gmb/api/users/all/list/",
    #     "method": "GET",
    #     "params": None
    # },
    # {
    #     "url": "http://50.28.76.71:7845/gmb/api/users/recent/added/",
    #     "method": "GET",
    #     "params": None
    # },
    
    
    
# #      # ///Grid Ranks///////
    
#     {
#         "url": "http://50.28.76.71:7845/api/grid-ranks/",
#         "method": "GET",
#         "params": None
#     },
#     {
#         "url": "http://50.28.76.71:7845/api/grid-ranks/",
#         "method": "POST",
#         "params": 
#                 [
                    # {
                    #     "campaign_id": 16042,
                    #     "keyword_analysis_id": 67865,
                    #     "grid_rank": "[[21, 21, 21, 21, 21, 21, 21], [21, 21, 21, 21, 21, 21, 21], [21, 21, 21, 21, 21, 21, 21], [21, 21, 21, 21, 21, 21, 21], [21, 21, 21, 21, 21, 21, 21], [21, 21, 21, 21, 21, 21, 21], [21, 21, 21, 21, 21, 21, 21]]",
                    #     "day_wise": "2023-08-16"
                    # }
                    # ]
#     },
#     {
#         "url": "http://50.28.76.71:7845/api/grid-ranks/keyword/35209",
#         "method": "GET",
#         "params": None
#     },
#     {
#         "url": "http://50.28.76.71:7845/api/grid-ranks/382/",
#         "method": "GET",
#         "params": None
#     },
    
    
    
#     # ---------Business--------
# # 01
# {
#     "url": "http://50.28.76.71:7845/business/get/{longitude}/id/{latitude}/?longitude&latitude",
#     "method": "GET",
#     "params":
#         {
#             "longitude": -97.8164856,
#             "latitude": 30.5046233
#         }


# },
# # 02
# {
#     "url": "http://50.28.76.71:7845/business/{id}/?id",
#     "method": "GET",
#     "params":
#         {
#             "id": 12922
#         }

# },

# # 03
# {
#     "url": "http://50.28.76.71:7845/business/{id}/?id",
#     "method": "PATCH",
#     "params":
#         {
#             "id": 12780
#         }

# },

# # 04
# {
#     "url": "http://50.28.76.71:7845/business/business/by/{cid}/?cid",
#     "method": "GET",
#     "params":
#         {
#             "cid": 10528117706918676785
#         }

# },


# # 05
# {
#     "url": "http://50.28.76.71:7845/business/byplace/{place_id}/?place_id",
#     "method": "GET",
#     "params":
#         {
#         "place_id": "ChIJ04sMDPnLj4ARXYmTqWeWRfY"
#         }

# },
# # 06
# {
#      "url": "http://50.28.76.71:7845/business/create/",
#      "method": "POST",
#      "params": 
    
#         {
#             "business_name": "string",
#             "business_website": "string",
#             "business_image": "string",
#             "business_gmb_cid": "string",
#             "business_category_id": 0,
#             "business_address": "string",
#             "country_id": 0,
#             "states_id": 0,
#             "states": "string",
#             "city": "string",
#             "zip_code": "string",
#             "longitude": 0,
#             "latitude": 0,
#             "place_id": "string",
#             "sub_categories": "string",
#             "is_updated": 0,
#             "is_google_authorized": 0,
#             "account_id": "string",
#             "location_id": "string",
#             "gmb_api_user_id": 0
#         }
    
# },
# # 07
# {
#     "url": "http://50.28.76.71:7845/business/update/201",
#     "method": "PUT",
#     "params":
#         [
#             {
#             "business_name": "string",
#             "business_website": "string",
#             "business_image": "string",
#             "business_category_id": 0,
#             "business_categories": "string",
#             "business_address": "string",
#             "country_id": 0,
#             "states_id": 0,
#             "states": "string",
#             "country": "string",
#             "city": "string",
#             "zip_code": "string",
#             "longitude": 0,
#             "latitude": 0,
#             "place_id": "string",
#             "sub_categories": "string",
#             "is_updated": 1
#             }
#         ]
# },
# # 08
# {
#     "url": "http://50.28.76.71:7845/business/update/is/updated/201",
#     "method": "PUT",
#     "params":
#         [
#             {
#             "is_updated": 1
#             }
#         ]
# },
# # 09
# {
#     "url": "http://50.28.76.71:7845/business/update/is/google/auth/201",
#     "method": "PUT",
#     "params":
#         [
#             {
#             "is_google_authorized": 1
#             }
#         ]
# },
# # 10
# {
#     "url": "http://50.28.76.71:7845/business/update/google/fields/201",
#     "method": "PUT",
#     "params":
#         [
#             {
#             "is_google_authorized": 1,
#             "account_id": "string",
#             "location_id": "string",
#             "gmb_api_user_id": 0
#             }
#         ]
# },
# # 11
# {
#     "url": "http://50.28.76.71:7845/business/get/business/update/by/{cid}/?cid",
#     "method": "GET",
#     "params":
#         {
#             "cid": 10528117706918676785
#         }

# },
# # 12
# {
#     "url": "http://50.28.76.71:7845/business/list/businesses/?gmb_cid &place_id",
#     "method": "GET",
#     "params":
#         {
#             "gmb_cid ": 3154498074408377883,
#             "place_id ": "ChIJ04sMDPnLj4ARXYmTqWeWRfY"
#         }

# },
# # 13
# {
#     "url": "http://50.28.76.71:7845/business/list/businesses/is/auth/",
#     "method": "GET",
#     "params": None
# },

# # ---------Business Stats--------

# # 01
# {
#     "url": "http://50.28.76.71:7845/businessstats/{id}/?id",
#     "method": "GET",
#     "params":
#         {
#             "id": 12948
#         }
# },

# # 02
# {
#     "url": "http://50.28.76.71:7845/businessstats/list/{business_id}/?business_id",
#     "method": "GET",
#     "params":
#         {
#             "business_id": 13295
#         }
# },

# # 03
# {
#     "url": "http://50.28.76.71:7845/businessstats/get/latest/{business_id}/?business_id",
#     "method": "GET",
#     "params":
#         {
#             "business_id": 13295
#         }
# },

# # 04
# {
#     "url": "http://50.28.76.71:7845/businessstats/get/latest/stats/{business_ids}/?business_ids",
#     "method": "GET",
#     "params":
#         {
#             "business_ids": 13295
#         }
# },
# # 05
# {
#     "url": "http://50.28.76.71:7845/businessstats/{business_id}/reporting/{month_wise}/?business_id&month_wise&campaign_id",
#     "method": "GET",
#     "params":
#         {
#             "business_id": 13299,
#             "month_wise" : 1,
#             "campaign_id": 15765
#         }
# },
# # 06
# {
#     "url": "http://50.28.76.71:7845/businessstats/{business_id}/reporting/{year_from}/year/{year_to}?business_id&year_from&year_to",
#     "method": "GET",
#     "params":
#         {
#             "business_id": 13297,
#             "year_from" : 1,
#             "year_to": 12
#         }
# },
# # 07
# {
#      "url": "http://50.28.76.71:7845/businessstats/create/",
#      "method": "POST",
#      "params": 
#         {
#             "business_id": 0,
#             "queries_direct": 0,
#             "queries_indirect": 0,
#             "views_search": 0,
#             "actions_website": 0,
#             "photos_views_merchant": 0,
#             "photos_views_customers": 0,
#             "photos_views_customer_merchant": 0,
#             "local_post_views_search": 0,
#             "actions_driving_directions": 0,
#             "actions_phone": 0,
#             "views_maps": 0,
#             "month_wise": "2022-08-04"
#         }
# },
# # 08

# {
#     "url": "http://50.28.76.71:7845/businessstats/list/stats/",
#     "method": "GET",
#     "params": None
# },

# # ---------Business Stats Graph--------
# # 01

# {
#     "url": "http://50.28.76.71:7845/businessstats/graph/list/{business_id}/?business_id",
#     "method": "GET",
#     "params":
#         {
#             "business_id": 13297
#         }
# },
# # 02
# {
#     "url": "http://50.28.76.71:7845/businessstats/graph/get/latest/{business_id}/?business_id",
#     "method": "GET",
#     "params":
#         {
#             "business_id": 13297
#         }
# },
# # 03
# {
#     "url": "http://50.28.76.71:7845/businessstats/graph/get/{business_id}/interval/{days}/?business_id&days&month",
#     "method": "GET",
#     "params":
#         {
#             "business_id": 13297,
#             "days": 10,
#             "month": 10
#         }
# },
# # 04
# {
#     "url": "http://50.28.76.71:7845/businessstats/graph/get/{business_id}/latest/partial/month/?business_id",
#     "method": "GET",
#     "params":
#         {
#             "business_id": 13297
#         }
# },
# # 05
# {
#     "url": "http://50.28.76.71:7845/businessstats/graph/list/single/{field}/{business_id}/interval/{days}/?business_id&days&field&month",
#     "method": "GET",
#     "params":
#         {
#             "business_id": 13297,
#             "days": 10,
#             "field": 10,
#             "month": 10
#         }
# },
# # 06
# {
#      "url": "http://50.28.76.71:7845/businessstats/graph/create/",
#      "method": "POST",
#      "params": 
#         {
#             "business_id": 0,
#             "queries_direct": 0,
#             "queries_indirect": 0,
#             "views_search": 0,
#             "actions_website": 0,
#             "photos_views_merchant": 0,
#             "photos_views_customers": 0,
#             "photos_views_customer_merchant": 0,
#             "local_post_views_search": 0,
#             "actions_driving_directions": 0,
#             "actions_phone": 0,
#             "views_maps": 0,
#             "day_wise": "2022-08-04"
#         }
# },
# # 07
# {
#      "url": "http://50.28.76.71:7845/businessstats/graph/create/multiple",
#      "method": "POST",
#      "params": 
#         [
#             {
#                 "business_id": 0,
#                 "queries_direct": 0,
#                 "queries_indirect": 0,
#                 "views_search": 0,
#                 "actions_website": 0,
#                 "photos_views_merchant": 0,
#                 "photos_views_customers": 0,
#                 "photos_views_customer_merchant": 0,
#                 "local_post_views_search": 0,
#                 "actions_driving_directions": 0,
#                 "actions_phone": 0,
#                 "views_maps": 0,
#                 "day_wise": "2022-08-04"
#             }
#         ]
# },
# # ---------Business Stats Graph APIs--------
# # 01
# {
#     "url": "http://50.28.76.71:7845/business/stats/graph/{id}/?id&field&days&month&last_year",
#     "method": "GET",
#     "params":
#         {
#             "id": 13297,
#             "field": 10,
#             "days": 10,
#             "month": 10,
#             "last_year": 10
#         }
# },
# # ---------Business Category--------
# # 01
# {
#      "url": "http://50.28.76.71:7845/businesscategory/create/",
#      "method": "POST",
#      "params": 
#         {
#             "category_name": "string",
#             "suggested_keywords": "string",
#             "nearby_keywords": "string",
#             "google_cid": "string",
#             "related_categories_url": "string"
#         }
# },
# # 02
# {
#     "url": "http://50.28.76.71:7845/businesscategory/1198/",
#     "method": "GET",
#     "params":None
# },
# # 03
# {
#     "url": "http://50.28.76.71:7845/businesscategory/get/id/Test Business 1/",
#     "method": "GET",
#     "params":None
# },
# # 04
# {
#     "url": "http://50.28.76.71:7845/businesscategory/get/id/by/Test Business 1/",
#     "method": "GET",
#     "params":None
# },
# # 05
# {
#     "url": "http://50.28.76.71:7845/businesscategory/list/categories/",
#     "method": "GET",
#     "params": None
# },

# ---------Business Stats Graph APIs--------
# 01
# {
#     "url": "http://50.28.76.71:7845/business/stats/graph/12618/?field=business_impressions_mobile_maps",
#     "method": "GET",
#     "params":
#         {
#             "field": "business_impressions_mobile_maps"
#         }
# }
  
#   # ---------Business Category--------
# # 01
# {
#      "url": "http://50.28.76.71:7845/businesscategory/create/",
#      "method": "POST",
#      "params": 
#         {
#             "category_name": "Zulqarnain002",
#             "suggested_keywords": "my business",
#             "nearby_keywords": "business one",
#             "google_cid": "10528117706918676785",
#             "related_categories_url": "https://pleper.com/index.php?do=tools&sdo=google_category_analyze&gcid=day_care_center"
#         }
# },
# # 02
# {
#     "url": "http://50.28.76.71:7845/businesscategory/282118",
#     "method": "GET",
#     "params": None
# },
# # 03
# {
#     "url": "http://50.28.76.71:7845/businesscategory/get/id/Zulqarnain001",
#     "method": "GET",
#     "params": None
# },
# # 04 we are not using this API
# # {
# #     "url": "http://50.28.76.71:7845/businesscategory/get/id/by/{categories}/?categories",
# #     "method": "GET",
# #     "params": None
# # },
# # 05
# {
#     "url": "http://50.28.76.71:7845/businesscategory/list/categories/",
#     "method": "GET",
#     "params": None
# }, 

# # ---------Business Stats--------

# # 01
# {
#     "url": "http://50.28.76.71:7845/businessstats/187/",
#     "method": "GET",
#     "params": None
# },
# # 02
# {
#     "url": "http://50.28.76.71:7845/businessstats/list/108/",
#     "method": "GET",
#     "params": None
# },
# # 03
# {
#     "url": "http://50.28.76.71:7845/businessstats/get/latest/108",
#     "method": "GET",
#     "params": None
# },
# # 04
# {
#     "url": "http://50.28.76.71:7845/businessstats/get/latest/stats/13294,13296/",
#     "method": "GET",
#     "params": None
# },
# # 05
# {
#     "url": "http://50.28.76.71:7845/businessstats/108/reporting/2021-08-01/",
#     "method": "GET",
#     "params": None
# },
# # 06
# {
#     "url": "http://50.28.76.71:7845/businessstats/108/reporting/2000/year/2023",
#     "method": "GET",
#     "params": None
# },
# # 07 Issue with this API
# {
#      "url": "http://50.28.76.71:7845/businessstats/create/",
#      "method": "POST",
#      "params": 
#         {
#             "business_id": 0,
#             "queries_direct": 0,
#             "queries_indirect": 0,
#             "views_search": 0,
#             "actions_website": 0,
#             "photos_views_merchant": 0,
#             "photos_views_customers": 0,
#             "photos_views_customer_merchant": 0,
#             "local_post_views_search": 0,
#             "actions_driving_directions": 0,
#             "actions_phone": 0,
#             "views_maps": 0,
#             "month_wise": "2022-08-03"
#         }
# }, 


#  # ---------Business Stats Graph--------
# # 01
# {
#     "url": "http://50.28.76.71:7845/businessstats/graph/list/108/",
#     "method": "GET",
#     "params": None
# },
# # 02
# {
#     "url": "http://50.28.76.71:7845/businessstats/graph/get/latest/108/",
#     "method": "GET",
#     "params": None
# },
# # 03
# {
#     "url": "http://50.28.76.71:7845/businessstats/graph/get/108/interval/90",
#     "method": "GET",
#     "params": None
# },
# # 04
# {
#     "url": "http://50.28.76.71:7845/businessstats/graph/get/108/latest/partial/month/",
#     "method": "GET",
#     "params": None
# },
# # 05
# {
#     "url": "http://50.28.76.71:7845/businessstats/graph/list/single/business_impressions_mobile_maps/108/interval/180/",
#     "method": "GET",
#     "params": None
# },

# # ===Geo Grid Urls


# {
#     "url": "http://50.28.76.71:7845/geo/grid/urls/396962",
#     "method": "GET",
#     "params": None
            
# },

# {
#     "url": "http://50.28.76.71:7845/geo/grid/urls/get/16045/",
#     "method": "GET",
#     "params": None
            
# },

# {
#     "url": "http://50.28.76.71:7845/geo/grid/urls/get/67075",
#     "method": "GET",
#     "params": None
            
# },

# {
#     "url": "http://50.28.76.71:7845/geo/grid/urls/get/list/67075/?jan",
#     "method": "GET",
#     "params": None
# },

# {
#         "url": "http://50.28.76.71:7845/geo/grid/urls/create/",
#         "method": "POST",
#         "params":
#         {
#             "keyword_analysis_id": 69644,
#             "geo_grid_url": "https://dev.brandsignals.io/media/bpm_stored_data/gif_grid_image/16045/2023-04-20/69644/grids/mexican restaurants.png",
#             "agency_id": 9,
#             "month_wise": "2023-04-23"
#         }
# },

# {
#         "url": "http://50.28.76.71:7845/geo/grid/urls/create/multiple_1/",
#         "method": "POST",
#         "params":
#         [
#                 {
#                 "keyword_analysis_id": 69644,
#                 "geo_grid_url": "https://dev.brandsignals.io/media/bpm_stored_data/gif_grid_image/16045/2023-04-20/69644/grids/mexican restaurants.png",
#                 "agency_id": 9,
#                 "month_wise": "2023-04-23"
#                 }
#         ]
# },

# {
#         "url": "http://50.28.76.71:7845/geo/grid/urls/create/multiple/",
#         "method": "POST",
#         "params":
#         [
#                 {
#                 "keyword_analysis_id": 69644,
#                 "geo_grid_url": "https://dev.brandsignals.io/media/bpm_stored_data/gif_grid_image/16045/2023-04-20/69644/grids/mexican restaurants.png",
#                 "agency_id": 9,
#                 "month_wise": "2023-04-23"
#                 }
#         ]
# },

# {
#     "url": "http://50.28.76.71:7845/geo/grid/urls/list/all/",
#     "method": "GET",
#     "params": None
# },


# # ===Geo Gifs Urls
# {
#     "url": "http://50.28.76.71:7845/geo/gifs/urls/13160",
#     "method": "GET",
#     "params": None
# },
# {
#     "url": "http://50.28.76.71:7845/geo/gifs/urls/get/69644",
#     "method": "GET",
#     "params": None
# },
# {
#         "url": "http://50.28.76.71:7845/geo/gifs/urls/create/",
#         "method": "POST",
#         "params":
#         {
#                 "keyword_analysis_id": 69644,
#                 "geo_gifs_url": "https://dev.brandsignals.io/media/bpm_stored_data/gif_grid_image/16045/2023-04-20/69644/grids/mexican restaurants.png",
#                 "agency_id": 9
#         }
# },
# {
#         "url": "http://50.28.76.71:7845/geo/gifs/urls/create/multiple/",
#         "method": "POST",
#         "params":
#         [
#             {
#                 "keyword_analysis_id": 69644,
#                 "geo_gifs_url": "https://dev.brandsignals.io/media/bpm_stored_data/gif_grid_image/16045/2023-04-20/69644/grids/mexican restaurants.png",
#                 "agency_id": 9
#             }
#         ]
# },
# {
#     "url": "http://50.28.76.71:7845/geo/gifs/urls/list/all/",
#     "method": "GET",
#     "params": None
# },
    
    
#     # ===Keyword Data

# {
#     "url": "http://50.28.76.71:7845/keywords/1696",
#     "method": "GET",
#     "params": None
# },

# {
#     "url": "http://50.28.76.71:7845/keywords/byname/florist",
#     "method": "GET",
#     "params": None
# },

# {
#         "url": "http://50.28.76.71:7845/keywords/create/",
#         "method": "POST",
#         "params":
#         {
#             "keyword_name": "sQA_223"
#         }
# },


# {
#     "url": "http://50.28.76.71:7845/keywords/list/by/22108",
#     "method": "GET",
#     "params": None
# },

# {
#     "url": "http://50.28.76.71:7845/keywords/get/list/by/QA23",
#     "method": "GET",
#     "params": None
# },


# # ===Reporting Page APIs

# {
#     "url": "http://50.28.76.71:7845/reporting/apis/get/383",
#     "method": "GET",
#     "params": None
# },

# {
#     "url": "http://50.28.76.71:7845/reporting/apis/get/business/data/383?month_wise&days&field",
#     "method": "GET",
#     "params": None
# },

# # =====Queries Reporting====

# {
#     "url": "http://50.28.76.71:7845/queries/2",
#     "method": "GET",
#     "params": None
# },

# {
#     "url": "http://50.28.76.71:7845/queries/by/267473",
#     "method": "GET",
#     "params": None
# },

# {
#         "url": "http://50.28.76.71:7845/queries/create/",
#         "method": "POST",
#         "params":
#         {
#             "business_id": 267473,
#             "query": "string",
#             "day_wise": "2022-08-03",
#             "searches": 0,
#             "percentage_searches": 0
#         }
# },

# {
#     "url": "http://50.28.76.71:7845/queries/list/all/",
#     "method": "GET",
#     "params": None
# },

# {
#     "url": "http://50.28.76.71:7845/queries/list/by/7/business/267473/",
#     "method": "GET",
#     "params": None
# },


# ===Keyword Analysis

# {
#     "url": "http://50.28.76.71:7845/keyword/analysis/15227/",
#     "method": "GET",
#     "params": None
# },

# {
#     "url": "http://50.28.76.71:7845/keyword/analysis/list/12676",
#     "method": "GET",
#     "params": None
# },

# {
#     "url": "http://50.28.76.71:7845/keyword/analysis/list/suggested/201440",
#     "method": "GET",
#     "params": None
# },

# {
#     "url": "http://50.28.76.71:7845/keyword/analysis/list/0/semrush/0/suggested/201440/",
#     "method": "GET",
#     "params": None
# },

# {
#     "url": "http://50.28.76.71:7845/keyword/analysis/list/1/selected/383/?is_selected=1",
#     "method": "GET",
#     "params": None
# },

# {
#     "url": "http://50.28.76.71:7845/keyword/analysis/list/all/selected/67865/?is_selected=1",
#     "method": "GET",
#     "params": None
# },

# {
#     "url": "http://50.28.76.71:7845/keyword/analysis/list/0/selected/383/?is_selected=0",
#     "method": "GET",
#     "params": None
# },

# {
#         "url": "http://50.28.76.71:7845/keyword/analysis/create/",
#         "method": "POST",
#         "params":
#         {
#             "campaign_id": 12676,
#             "keyword_id": 886,
#             "search_volume": 0,
#             "count_per_click": 0,
#             "is_suggested": 1,
#             "is_selected": 1,
#             "is_semrush": 1,
#             "is_added": 2,
#             "category_score": 0,
#             "website_score": 0,
#             "proximity_score": 0,
#             "map_rank": 0,
#             "keyword_analysis_status": 5,
#             "geo_grid_sub_score": 0,
#             "category_sub_score": 0,
#             "on_page_sub_score": 0,
#             "overall_score": 0
#         }
# },


# {
#         "url": "http://50.28.76.71:7845/keyword/analysis/update/is/selected/37397",
#         "method": "PUT",
#         "params":
            
#                 {

#                     "is_selected": 0

#                 }
            
# },

# {
#         "url": "http://50.28.76.71:7845/keyword/analysis/update/all/67865",
#         "method": "PUT",
#         "params":
            
#                 {
#                     "search_volume": 600
#                 }
            
# },

# {
#         "url": "http://50.28.76.71:7845/keyword/analysis/update/status/67865",
#         "method": "PUT",
#         "params":
            
#                 {

#                     "keyword_analysis_status": 5
#                 }
            
# },

# {
#         "url": "http://50.28.76.71:7845/keyword/analysis/statuses/",
#         "method": "PUT",
#         "params":
#             [
#                 {
#                     "id": 67865,
#                     "status": 5
#                 }
#             ]
# },

# {
#         "url": "http://50.28.76.71:7845/keyword/analysis/update/overallscore/67865",
#         "method": "PUT",
#         "params":
            
#                 {
#                     "overall_score": 12
#                 }
            
# },

# {
#         "url": "http://50.28.76.71:7845/keyword/analysis/update/semrushapi/67865",
#         "method": "PUT",
#         "params":
            
#             {
#                 "search_volume": 2213,
#                 "count_per_click": 2324
#             }
# },

# {
#     "url": "http://50.28.76.71:7845/keyword/analysis/list/all/",
#     "method": "GET",
#     "params": None
# },

# {
#     "url": "http://50.28.76.71:7845/keyword/analysis/list/67865",
#     "method": "GET",
#     "params": None
# },

# {
#     "url": "http://50.28.76.71:7845/keyword/analysis/list/all/semrush/suggested/201440",
#     "method": "GET",
#     "params": None
# },

# {
#     "url": "http://50.28.76.71:7845/keyword/analysis/task/67865",
#     "method": "GET",
#     "params": None
# },


# ---------Business--------
#01
# {
#      "url": "http://50.28.76.71:7845/business/copy/latlng",
#      "method": "POST",
#      "params": 
    
#         {
#             "business_id": 317
#         }   
# },
#02 Not Wokring in my User
# {
#     "url": "http://50.28.76.71:7845/business/get/{longitude}/id/{latitude}/",
#     "method": "GET",
#     "params": 
#         {
#             "longitude": -75.1294514,
#             "latitude": 40.0965572
#         }
# },
# #03
# {
#     "url": "http://50.28.76.71:7845/business/108/",
#     "method": "GET",
#     "params": None
# },
# #04 Not Wokring in my User
# {
#     "url": "http://50.28.76.71:7845/business/get/business/lat_lng/267473/",
#     "method": "GET",
#     "params": None
# },
# #05
# {
#     "url": "http://50.28.76.71:7845/business/101",
#     "method": "GET",
#     "params": None
# },
# #06
# {
#     "url": "http://50.28.76.71:7845/business/business/by/7167097690727217027/",
#     "method": "GET",
#     "params": None
# },
# #07
# {
#     "url": "http://50.28.76.71:7845/business/byplace/ChIJa4-I2DxehYAROdaqekFBFh8/",
#     "method": "GET",
#     "params": None
# },
#08 Not Working
# {
#      "url": "http://50.28.76.71:7845/business/create/",
#      "method": "POST",
#      "params": 
    
#         {
#             "business_name": "string",
#             "business_website": "string",
#             "business_image": "string",
#             "business_gmb_cid": "string",
#             "business_category_id": 0,
#             "business_address": "string",
#             "country_id": 0,
#             "states_id": 0,
#             "states": "string",
#             "city": "string",
#             "zip_code": "string",
#             "longitude": 0,
#             "latitude": 0,
#             "place_id": "string",
#             "sub_categories": "string",
#             "is_updated": 0,
#             "is_google_authorized": 0,
#             "account_id": "string",
#             "location_id": "string",
#             "gmb_api_user_id": 0
#         }
    
# },
# #09
# {
#     "url": "http://50.28.76.71:7845/business/update/201",
#     "method": "PUT",
#     "params":
        
#             {
#             "business_name": "string",
#             "business_website": "string",
#             "business_image": "string",
#             "business_category_id": 0,
#             "business_categories": "string",
#             "business_address": "string",
#             "country_id": 0,
#             "states_id": 0,
#             "states": "string",
#             "country": "string",
#             "city": "string",
#             "zip_code": "string",
#             "longitude": 0,
#             "latitude": 0,
#             "place_id": "string",
#             "sub_categories": "string",
#             "is_updated": 1
#             }
        
# },
# #10
# {
#     "url": "http://50.28.76.71:7845/business/update/is/updated/108",
#     "method": "PUT",
#     "params":
        
#             {
#             "is_updated": 1
#             }
        
# },
# #11
# {
#     "url": "http://50.28.76.71:7845/business/update/is/google/auth/108",
#     "method": "PUT",
#     "params":
        
#             {
#             "is_google_authorized": 1
#             }
        
# },
#12
# {
#     "url": "http://50.28.76.71:7845/business/update/google/fields/108",
#     "method": "PUT",
#     "params":
        
#             {
#             "is_google_authorized": 1,
#             "account_id": "string",
#             "location_id": "string",
#             "gmb_api_user_id": 56
#             }
        
# },
#13 Not Working
# {
#     "url": "http://50.28.76.71:7845/business/get/business/update/by/{cid}/?cid=",
#     "method": "GET",
#     "params":
#         {
#             "cid": 10528117706918676785
#         }

# },
#14 Not Working
# {
#     "url": "http://50.28.76.71:7845/business/list/businesses/?gmb_cid &place_id=",
#     "method": "GET",
#     "params":
#         {
#             "gmb_cid ": 3154498074408377883,
#             "place_id ": "ChIJ04sMDPnLj4ARXYmTqWeWRfY"
#         }

# },
#15
# {
#     "url": "http://50.28.76.71:7845/business/list/businesses/is/auth/",
#     "method": "GET",
#     "params": None
# },
# #16
# {
#     "url": "http://50.28.76.71:7845/business/list/businesses/is/auth/?gmb_api_user_id =56",
#     "method": "GET",
#     "params":
#         {
#             "gmb_api_user_id": 56
#         }
# },
# #17
# {
#     "url": "http://50.28.76.71:7845/business/weekly/update/business/lat/lng/",
#     "method": "GET",
#     "params": None
# },
# #18
# {
#     "url": "http://50.28.76.71:7845/business/check/campaigns/aganist/agency/9",
#     "method": "GET",
#     "params": None
# },
#19 Not Working
# {
#     "url": "http://50.28.76.71:7845/business/get/data/of/gmb/api/user/into/json/",
#     "method": "GET",
#     "params": None
# },
#20 Not Working
# {
#     "url": "http://50.28.76.71:7845/business/get/gmb/api/user/json/file/",
#     "method": "GET",
#     "params": None
# },
#21 Not Working
# {
#      "url": "http://50.28.76.71:7845/business/get/data/of/gmb/api/user/into/database/",
#      "method": "POST",
#      "params": 
#         {
#             "gmb_api_user_id": 56
#         }
# },
#22 Not Working
# {
#      "url": "http://50.28.76.71:7845/business/gmb_listing/all/users/",
#      "method": "POST",
#      "params": None
# },
#23
# {
#      "url": "http://50.28.76.71:7845/business/authorize/",
#      "method": "POST",
#      "params": 
#         {
#             "business_id": 108,
#             "gmb_api_user_id": 0,
#             "user_email": "string",
#             "campaing_id": 0,
#             "login_user_id": 0,
#             "user_name": "string"
#         }
# },
# #24
# {
#     "url": "http://50.28.76.71:7845/business/authorize/pull/stats/",
#     "method": "GET",
#     "params": None
# },

# ===Keyword Values

# {
#     "url": "http://50.28.76.71:7845/keywords/values/47311",
#     "method": "GET",
#     "params": None
# },

# {
#     "url": "http://50.28.76.71:7845/keywords/values/by/analysis/69644",
#     "method": "GET",
#     "params": None
# },

# {
#         "url": "http://50.28.76.71:7845/keywords/values/create/",
#         "method": "POST",
#         "params":
#         {
#             "keyword_analysis_id": 69644,
#             "organic_results_link": "string",
#             "top_primary_categories": "string",
#             "has_map": 1,
#             "top_sub_categories": "string",
#             "page_score": 0,
#             "keyword_in_url": 1,
#             "keyword_in_page_title": 1,
#             "keyword_in_h1": 1,
#             "keyword_in_page_description": 1,
#             "keyword_in_page_body": 1,
#             "keyword_in_image_alt": 1,
#             "keyword_in_body_content_score": 1,
#             "geo_grid_keyword_id": "string",
#             "grids_ranks": "string"
#         }
# },

# {
#         "url": "http://50.28.76.71:7845/keywords/values/update/serpapi/47312",
#         "method": "PUT",
#         "params":
            
#                 {
#                 "organic_results_link": "string",
#                 "top_primary_categories": "string",
#                 "has_map": 1
#                 }
            
# },

# {
#         "url": "http://50.28.76.71:7845/keywords/values/update/seoability/47312",
#         "method": "PUT",
#         "params":
            
#                 {
#                 "page_score": 0,
#                 "keyword_in_url": 1,
#                 "keyword_in_page_title": 1,
#                 "keyword_in_h1": 1,
#                 "keyword_in_page_description": 1,
#                 "keyword_in_page_body": 1,
#                 "keyword_in_image_alt": 1,
#                 "keyword_in_body_content_score": 1
#                 }
            
# },

# {
#         "url": "http://50.28.76.71:7845/keywords/values/update/localviking/47312",
#         "method": "PUT",
#         "params":
            
#                 {
#                 "geo_grid_keyword_id": "string",
#                 "grids_ranks": "string"
#                 }
            
# },

# {
#         "url": "http://50.28.76.71:7845/keywords/values/update/all/47312",
#         "method": "PUT",
#         "params":
            
#                 {
#                 "organic_results_link": "string",
#                 "top_primary_categories": "string",
#                 "has_map": 1,
#                 "page_score": 0,
#                 "keyword_in_url": 1,
#                 "keyword_in_page_title": 1,
#                 "keyword_in_h1": 1,
#                 "keyword_in_page_description": 1,
#                 "keyword_in_page_body": 1,
#                 "keyword_in_image_alt": 1,
#                 "keyword_in_body_content_score": 1,
#                 "geo_grid_keyword_id": "string",
#                 "grids_ranks": "string"
#                 }
            
# },

# {
#         "url": "http://50.28.76.71:7845/keywords/values/update/geogrid/id/by/47312",
#         "method": "PUT",
#         "params":
            
#                 {
#                 "geo_grid_keyword_id": "string"
#                 }
            
# },

# {
#     "url": "http://50.28.76.71:7845/keywords/values/list/values/",
#     "method": "GET",
#     "params": None
# },

]

# =========================

second_api_list = [
     {
        "url": "http://50.28.76.71:7845",
        "method": "GET",
        "params": None
    },
     

]


# ======================================

first_auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0YWRtaW4iLCJzY29wZXMiOltdLCJpZCI6MSwiZXhwIjoxNjkzODk2MjI5fQ.QWZ44YhfvxW-0Z8gZlBRHFqwL49rsEeb1IY9IAYuPPY"
second_auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0YWRtaW4iLCJzY29wZXMiOltdLCJpZCI6MSwiZXhwIjoxNjkzMDQ4OTUwfQ.RktyNABxrI0mkSCsj6zwnx1zinxsanAtSN4ek1bRRF0"

# ======================================

# Add a dictionary to store custom error messages for specific response codes
custom_error_messages = {
    500: 'Internal Server Error',
    501: 'Not Implemented',
    502: 'Bad Gateway',
    503: 'Service Unavailable',
    504: 'Gateway Timeout',
    505: 'HTTP Version Not Supported',
    506: 'Variant Also Negotiates',
    507: 'Insufficient Storage',
    508: 'Loop Detected',
    510: 'Not Extended',
    511: 'Network Authentication Required',
    400: 'Bad Request',
    401: 'Unauthorized',
    402: 'Payment Required',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    406: 'Not Acceptable',
    407: 'Proxy Authentication Required',
    408: 'Request Timeout',
    409: 'Conflict',
    410: 'Gone',
    411: 'Length Required',
    412: 'Precondition Failed',
    413: 'Payload Too Large',
    414: 'URI Too Long',
    415: 'Unsupported Media Type',
    416: 'Range Not Satisfiable',
    418: 'iam',
    421: 'Misdirected Request',
    422: 'Unprocessable Entity',
    423: 'Locked',
    424: 'Failed Dependency',
    426: 'Upgrade Required',
    428: 'Precondition Required',
    431: 'Request Header Fields Too Large',
    451: 'Unavailable For Legal Reasons',
    429: 'Too Many Requests',
}
# ================================================

# Combine both API lists
# api_list = first_api_list + second_api_list
# auth_tokens = [first_auth_token, second_auth_token]

# Combine both API lists
api_list = first_api_list + second_api_list
auth_tokens = [first_auth_token] * len(first_api_list) + [second_auth_token] * len(second_api_list)  # Adjust auth_tokens list

# Initialize the response codes dictionary
response_codes_dict = {}

# ================================================

# Function to hit the APIs and save results for 6 hits in a CSV file
def hit_apis_and_save_results(api_list, auth_tokens, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['API', 'Method', 'Hit#', 'Response Code', 'Success', 'Response Time', 'Response Data'])

        response_codes_dict = {}

        # Iterate over each API in the list
        for api_index, api in enumerate(api_list):
            url = api['url']
            method = api['method']
            params = api['params']

            auth_token = auth_tokens[api_index // 6]  # Access the correct auth_token

            headers = {
                'Authorization': f'Bearer {auth_token}',
                'Content-Type': 'application/json'
            }

            # Perform 6 hits for each API
            for hit in range(1, 7):
                start_time = time.time()  # Record the start time
                response = None

                try:
                    # Make the API request
                    if method == 'GET':
                        response = requests.get(url, headers=headers, params=params)
                    elif method == 'POST':
                        response = requests.post(url, json=params, headers=headers)
                    elif method == 'PUT':
                        response = requests.put(url, json=params, headers=headers)
                    elif method == 'PATCH':
                        response = requests.patch(url, json=params, headers=headers)
                    elif method == 'DELETE':
                        response = requests.delete(url, headers=headers)

                    # Get the response code and calculate the response time
                    response_code = response.status_code if response is not None else None
                    response_time = time.time() - start_time if response is not None else 'N/A'
                    
                    # Check if the response is 429 and save it to the 429 CSV
                    if response_code == 429:
                        with open('csv_429_API.csv', 'a', newline='') as csv_file:
                            writer_429 = csv.writer(csv_file)
                            writer_429.writerow([url, method, response_code, f'HIT#{hit}'])

                    # Check if the response is successful or not
                    if response is not None:
                        if 200 <= response_code < 300:
                            success = 'Success'
                            try:
                                # response_data = response.json()
                                response_data = custom_error_messages.get(response_code, 'No Data') if response_code is not None else 'No Response'
                            except ValueError:
                                response_data = custom_error_messages.get(response_code, 'No Data') if response_code is not None else 'No Response'
                                # response_data = response.text
                        else:
                            success = 'Fail'
                            response_data = custom_error_messages.get(response_code, 'No Data')
                            if url not in response_codes_dict:
                                response_codes_dict[url] = {}
                            response_codes_dict[url][hit] = response_code
                    else:
                        success = 'Fail'
                        response_data = custom_error_messages.get(response_code, 'No Data') if response_code is not None else 'No Response'
                        # response_data = 'No Response'

                    # Print data for the hit in the terminal
                    print(f"{url},{method},HIT#{hit},{response_code},{success},{response_time:.2f},{response_data}")

                    # Write the results to the CSV file for the hit
                    writer.writerow([url, method, f"HIT#{hit}", response_code, success, response_time, response_data])

                    # Wait for 1 second before the next hit
                    time.sleep(0.5)

                except Exception as e:
                    # Handle exceptions
                    response_code = response.status_code if response is not None else None
                    response_time = 'N/A'
                    success = 'Fail'
                    response_data = custom_error_messages.get(response_code, 'No Data') if response_code is not None else 'No Response'
                    error_message = str(e)

                    # Print data for the failed hit in the terminal
                    print(f"{url},{method},HIT#{hit},{response_code},{success},{response_time},{response_data},{error_message}")

                    # Write the results to the CSV file for the failed hit
                    writer.writerow([url, method, f"HIT#{hit}", response_code, success, response_time, response_data])

                    # Wait for 1 second before the next hit
                    time.sleep(0.5)

            # Print empty lines to create space between hits for each API
            for _ in range(1):
                print()
                writer.writerow([])

        # Print empty lines to create space between API lists
        for _ in range(4):
            print()
            writer.writerow([])

    # Write the 429 API list to a new CSV file
with open('csv_429_API.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['API', 'Method', 'Response Code', 'Hit#'])

    for url, hit_dict in response_codes_dict.items():
        for hit, response_code in hit_dict.items():
            writer.writerow([url, api_list[url]["method"], response_code, f'HIT#{hit}'])

        # Print empty lines to create space between hits for each API
            for _ in range(1):
                print()
                writer.writerow([])
                writer.writerow([])

# Call the function to hit the APIs and save the results
hit_apis_and_save_results(api_list, auth_tokens, 'api_results.csv')