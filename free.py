import requests

urls_list=["https://www.google.com/search?q=shrine+board&oq=&gs_lcrp=EgZjaHJvbWUqCQgBECMYJxjqAjIJCAAQIxgnGOoCMgkIARAjGCcY6gIyCQgCECMYJxjqAjIJCAMQIxgnGOoCMgkIBBAjGCcY6gIyCQgFECMYJxjqAjIJCAYQIxgnGOoCMgkIBxAjGCcY6gLSAQkyMzMzajBqMTWoAgiwAgE&sourceid=chrome&ie=UTF-8",]

for x in urls_list:
    
    try:
        response=requests.get(x)
        if response.status_code ==200:
            print(f"data from {x}")
            print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching {x}: {e}")