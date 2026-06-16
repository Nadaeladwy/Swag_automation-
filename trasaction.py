
from login_tests import login
from mission import add_mission
def trasaction(test_name, username, password, expected , url):
    
    page = login(test_name, username, password, expected , url)
    add_mission(page)
    




trasaction("test" , "108" , "123456" ,"sec","https://dynamic.novahrs.com/")