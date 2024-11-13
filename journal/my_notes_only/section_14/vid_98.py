
####   SMTP CONFIGURATION

### SO INORDER FOR US TO GO AHEAD AND SEND EMAILS TO AND FROM OUR DJANGO APPLICATION, WHAT WE ARE GOING TO DO IS WE ARE GOING TO HAVE TO 
### CONFIGURE OUR SMTP CONFIGURATION, WHICH PERTAINS TO BASICALLY OUR EMAIL AND SETTINGS CONFIGURATION

### WE WILL GO ONTO SETTINGS.PY FILE 

################  SETTINGS.PY

## GO TO THE BOTTOM AND ADD THE FOLLOWING CONFIGURATION

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  ## THIS IS DJANGO'S CORE MAIL BACKEND FOR SMTP, SO THIS WILL ALLOW US TO SEND EMAILS
                                                               ## WITH DJANGO

EMAIL_HOST = 'smtp.gmail.com'  # this is the email host, so we are going to use gmail smtp service. so all emails should be sent from and to a 
                               # GMAIL address

EMAIL_PORT = '587'  ## INTERMS OF EMAIL PORT, THE DEFAULT SMPT SERVER OF GMAIL USES PORT 587

EMAIL_USE_TLS = 'True'  ## HERE WE WANT TO ALSO ENSURE THAT WE HAVE TLS SUPPORT IN PLACE

## THE ABOVE 4 VALUES, WE NEED TO EXACTLY PASS IN LIKE THIS IN SETTINGS.PY, AS THERE ARE DEFAULT VALUES


##  -----------------------

## NOW FOR BELOW, LETS SAY WE WANT TO SEND PASSWORDS RESET MAILS OR WE WANT TO SEND WELCOME EMAILS, WE NEED TO HAVE A FROM EMAIL ADDRESS OR A 
## HOST EMAIL ADDRESS, SO THE EMAIL_HOST_USER AND DEFAULT_FROM_EMAIL PERTAIN TO THAT DEFAULT EMAIL, SO THE HOST EMAIL ADDRESS IS FROM WHERE ALL
## THE EMAILS ARE GOING TO BE COMING FROM. 

EMAIL_HOST_USER = 'ahmeddarmehran1@gmail.com'

EMAIL_HOST_PASSWORD = 'xtrcxdentxopgbsj'  ## FIRST OF ALL AS WE CREATE A NEW GMAIL ADDRESS, WE HAVE TO SET THIS PASSWORD CALLED THE APP PASSWORD,
                                      ## IN OUR SECURTIY SETTINGS OF GMAIL, WE NED TO CREATE AN APP PASSWORD, REFER TO PDF FROM THIS LECTURE'S
                                      ## RESOURCE, TO HOW YOU CAN GENERATE AN APP PASSWORD, WHILE CREATING A NEW GMAIL ACCOUNT

                       ## the above password is create from app pasword on my ahmeddarmehran1@gmail.com account

DEFAULT_FROM_EMAIL = 'ahmeddarmehran1@gmail.com' ##FUNCTIONS SAME AS EMAIL_HOST_USER, THIS IS OPTIONAL FIELD, BUT ITS BETER TO INCLUDE THIS AS WELL

## 'ahmeddarmehran1@gmail.com' IS THE DEFAULT EMAIL ADDRESS THAT DJANGO WILL USE TO SEND EMAILS LIKE WELCOME EMAILS, RESET PASSSWORDS TO USERS. DETAILS IN BELOW LINES

### DETAILS OF LAST 3 LINES



# EMAIL_HOST_USER: This setting represents the username or email address of the email account that Django will use to send emails. When Django sends an email (for example, when sending password reset emails or email verification emails),
# it authenticates with an SMTP server using the credentials provided by EMAIL_HOST_USER and EMAIL_HOST_PASSWORD.

# EMAIL_HOST_PASSWORD: This setting represents the password of the email account specified by EMAIL_HOST_USER. It's the password that Django will use to authenticate with the SMTP server when sending emails.

# DEFAULT_FROM_EMAIL: This setting represents the default sender email address used for outgoing emails. When Django sends emails, it needs to specify a "From" email address. DEFAULT_FROM_EMAIL
#  sets the default "From" email address for all outgoing emails sent by Django.

# Here's how you can set up these settings in your Django project's settings file (settings.py), along with an example:


# # Email account credentials
# EMAIL_HOST_USER = 'your-email@example.com'  # Your email address
# EMAIL_HOST_PASSWORD = 'your-email-password'  # Your email password

# # Default sender email address
# DEFAULT_FROM_EMAIL = 'your-email@example.com'  # Your email address
# In this example:

# EMAIL_HOST, EMAIL_PORT, and EMAIL_USE_TLS specify the SMTP server details for sending emails. You need to replace 'smtp.example.com', 587, and True with the appropriate
# values provided by your email service provider.
# EMAIL_HOST_USER and EMAIL_HOST_PASSWORD specify the email account credentials that Django will use to authenticate with the SMTP server.
# DEFAULT_FROM_EMAIL specifies the default sender email address for outgoing emails. You can replace 'your-email@example.com' with your actual email address.
# Make sure to replace 'smtp.example.com', 'your-email@example.com', and 'your-email-password' with your actual SMTP server address, email address, and password, respectively.

# Once you've set up these email settings, Django will use the specified email account to send emails, and the default sender email address will be used for outgoing emails.

# so the emails that we put in EMAIL_HOST_USER AND  DEFAULT_FROM_EMAIL IS ACTUALLY USED BY DJANGO TO SEND MAILS LIKE WELCOME MAILS, PASSWORD RESET MAIL TO DIFFERENT USER MAILS
# When you configure EMAIL_HOST_USER and DEFAULT_FROM_EMAIL in Django settings, Django will use these email addresses to send various types of emails, such as welcome emails,
# password reset emails, and any other emails your Django application may need to send to users.
# Overall, EMAIL_HOST_USER and DEFAULT_FROM_EMAIL are used by Django to determine the sender email address for outgoing emails sent by your Django application.
    

#### SO HOW DOES IT KNOW WHICH EMAIL ADDRESS TO SEND THE WELCOME MAIL OR PASSWORD RESET MAIL TO?

# Django knows which email address to send the welcome email or password reset email to based on the context in which these emails are triggered.

# Welcome Emails: When a new user registers on your website, they typically provide their email address as part of the registration process. Django retrieves this email address
# from the registration form or user input and uses it as the recipient email address when sending the welcome email. The welcome email is then sent to the email address provided by the user during registration.

# Password Reset Emails: When a user requests a password reset, they typically provide their email address (or username) through a password reset form. Django retrieves this email address from the password
# reset form or user input and uses it as the recipient email address when sending the password reset email. The password reset email is then sent to the email address provided by the user during the password reset request.

## NOW AS WE HAVE CONFIGURE OUR MAIL AND ALO GENERATED THE PASSWORD, With these settings configured, Django will use the specified Gmail account (ahmeddarmehran1@gmail.com) to send emails from your Django application. 
## When Django sends emails, it will authenticate with Gmail's SMTP server using the provided email address and password (EMAIL_HOST_USER and EMAIL_HOST_PASSWORD). The emails will appear to come from the specified
##  sender email address (DEFAULT_FROM_EMAIL).


##########  NOTE AS FOR THIS WE ARE USING THE GMAIL SMTP SERVERS(EMAIL_HOST = 'smtp.gmail.com), ALL THE USERS THAT WIL SIGN UP TOUR MEDIA BLOG WEBSITE EDENTHOUGHT, THET NEED TO EXPLICITY HAVE A GMAIL ACCOUNT
##########  AND NOTHING ELSE



