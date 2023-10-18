import requests
def get_repos(username):
    access_token='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'
    url='https://api.github.com/users/username/'
    headers={
        'Authorization':f'tokan{access_token}'
    }
    response=requests.get(url,headers=headers)
    my_data=response.json()
    print(my_data)
    # response=[]
    # for repo_dict in my_data:
    #     response.append(repo_dict['name'])
    # return response

# import requests
# usrename='rohitnaruka'
# access_token='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'
# base_url='https://api.github.com/users/'
# session=requests.session()
# session.auth=(usrename,access_token)
# response=session.get(f"{base_url}/user/respo")
# respo=response.json()
# #print(respo)
# for i in respo:
#     print(i)

