# ChiDogs #

## Backend ##

My goal was to create a backend to safely allow users to traverse ChiDogs. Implementing various security measures to ensure a safe and enjoyable experience. Django allows for a lot of built in security. Some additional middleware was added to beef up protection. This was achieved by requiring CSRF Tokens, CORS headers, and Cookie handling.

### Security ###

Password Encrypted: PBKDF2 

CSRF Protection: CSRF-View-Middleware

Cookie Handler: JS-Cookie

CORS Control: Django-CORS-Headers-Middleware

## Technology Used ##

#### Back End: Python | Django | JS-Cookie ####

#### Database: PostgreSQL ####

#### Front End: React.js | Semantic UI React ####