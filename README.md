Steps to run the code

1. install all the requirements from requirements.txt
2. change the postgre credentials in local_config.py
3. now run
    > uvicorn main:app --reload
4. go to http://127.0.0.1:8000/docs  in your browser to see all the available api's



Things still to do: 

* image addition in the post
* add update and delete post
* add comment and like