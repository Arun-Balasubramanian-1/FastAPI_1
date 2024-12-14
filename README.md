Setting Up Py env for the FastAPI Project
1. Creaate a Directory
  mkdir fastapi

2. Create a virtual env
  python3 -m venv  fastapienv

3. Activate fast api env
  source fastapienv/bin/activate
  (fastapienv)

4. List dependancies in env
  pip List

5. Deactivate venv
  deactivate

6. Activate env again and install dependancies
  pip install fastapi
  pip install "uvicorn[standard]"

Setup the local interpreter in Pycharm
  Select Existing 
  Path -> CurrentDirectory/fastapienv/bin/python3.13

Start your Fast API application with below command
  uvicorn books:app --reload

  http://127.0.0.1:8000/

