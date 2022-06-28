# DjangoAuth
This is a django application in which we have implemented authentication through which operational user can register, login and manage client users. The application also provides client user to sign up and verify their accounts using email verification. 


Test

Framework - Django
Database - SQLite

Types of User:
\
	1)Operation User
	\
	2)Client User

Features Available for each user:

	User 1: Operation User
	Actions available to user (Already created in the system)
		1. Login
		2. Disable a client

	User 2: Client User
	Actions available to user -
		1. Sign Up ( return an encrypted URL )
		2. Email Verify ( verification link will be sent to user on the registered email)
		3. Login
		4. Logout

	We have used Knox Authentication for this project which provide features like login, logout, signup for our users. 
	Email verification is done using SMTP protocol
	
Process Flow 
	User 1: Operation User:
			An Operation User can login -> disable/enable client user 
	
	User 2: Client User:
			A Client User can sign up to the application -> verify email -> login -> logout

Postman Test Case:
\
	User 1 : Operation User
	\
		Register: 
	    ![image](https://user-images.githubusercontent.com/79376134/175765600-16aada56-6c12-437b-8174-304bb2953434.png)
            	Login: 
	    ![image](https://user-images.githubusercontent.com/79376134/175765614-ddb7359e-a938-468a-9d07-c40c4ff24619.png)
            	Logout: 
	    ![image](https://user-images.githubusercontent.com/79376134/175765632-19c07551-98df-4b9b-be4c-165d06eec81c.png)

\
	User 2 : Client User
	\
  		Signup: 
	    ![image](https://user-images.githubusercontent.com/79376134/175765657-4466eac2-99fa-477c-84e6-b482c642fff0.png)
            	Email Verification: 
	    ![image](https://user-images.githubusercontent.com/79376134/175765786-1c2de6dd-f38d-4aaa-ae34-df5eaa2436f0.png)
	    ![image](https://user-images.githubusercontent.com/79376134/175765902-0c493c03-da40-4fdf-b4b2-137fc4e4ea06.png)
	    	Login:
		![image](https://user-images.githubusercontent.com/79376134/175765566-a836b720-64c9-4a4f-94da-404780b3fc1d.png)
		Logout:
		![image](https://user-images.githubusercontent.com/79376134/175765562-f4baa261-2953-41cf-9629-ab8fb9df2fee.png)

            

