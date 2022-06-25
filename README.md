# DjangoAuth
This is a django application in which we have implemented authentication through which operational user can register, login and manage client users. The application also provides client user to sign up and verify their accounts using email verification.

Test

Framework - Django
Database - SQLite

Types of User:
	1)Operation User
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
	    ![image](https://user-images.githubusercontent.com/79376134/175648593-1f844cee-7c76-4656-b006-48fc390ed971.png)
            	Login: 
	    ![image](https://user-images.githubusercontent.com/79376134/175648843-3e158b02-31f3-4917-a858-0ee526edae33.png)
            	Logout: 
	    ![image](https://user-images.githubusercontent.com/79376134/175649193-47df6028-79dc-474b-9c45-8c20cd420499.png)
\
	User 2 : Client User
	\
  		Signup: 
	    ![image](https://user-images.githubusercontent.com/79376134/175649327-ff91061d-b387-41d9-9825-afdddb2ae2ca.png)
            	Email Verification: 
	    ![image](https://user-images.githubusercontent.com/79376134/175649511-07af9377-eb18-45f8-9649-3277b315a734.png)
	    	Login:
		![image](https://user-images.githubusercontent.com/79376134/175765566-a836b720-64c9-4a4f-94da-404780b3fc1d.png)
		Logout:
		![image](https://user-images.githubusercontent.com/79376134/175765562-f4baa261-2953-41cf-9629-ab8fb9df2fee.png)

            

