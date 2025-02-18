# T-POO-700-RUN-1

## _How to build TimeManager project_

**TimeManagerAPP**

1 - Go to directory

    cd timeManagerAPP/

2 - Run docker compose

    docker-compose up --build


> localhost:8080/ for the front-end
> localhost:4000/ for the back-end

**Création de Compte**

1. Create a General Manager or Manager Account
    * Launch postman
        >Enter the url : http://localhost:4000//api/auth/register
        * In body, enter the use's email address and password as follows:
        > { “email” : “his_mail@mail.com”, “password”: “Password with 8 caracter”, “password_confirmation”: “Confirmation password” } 
        
            After launching the post request, we copy the returned token.
    * Still on postman, enter the url: http://localhost:4000//api/users
      * In body, fill in the user information as follows: 
      > {“username”:“his_name”,“email”:“his_mail@mail.com”, “role”: “his_role”}}
    
            /!\ It is necessary to write precisely in the role field “manager” for the Manager and “directeur” for the General Manager.
        * In authorization, we select as type “Bearer Token” and we paste in the token field that appears the token we copied when we execute the post request in register. So we launch the request and create our Manager or General Manager.

2. Create an employee account
   * The employee creates an account directly on the application