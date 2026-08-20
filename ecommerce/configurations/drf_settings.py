SPECTACULAR_SETTINGS = {
    'TITLE' : 'Ecommerce Backend API' ,
    'DESCRIPTION' : """
REST API for an e-commerce backend built using Django REST Framework.

Features include:
- User Authentication (JWT)
- Product Management
- Payment Method Management
- Order Management
- Dummy Payment Gateway Orchestration
- Asynchronous Order Processing using Celery
""" ,
    'VERSION' : '1.0.0' ,
    'SERVE_INCLUDE_SCHEMA' : False ,
    'SWAGGER_UI_SETTINGS' : {
        'persistAuthorization' : True , 
    } ,
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS' : 'products.paginations.CustomPagination',
    'PAGE_SIZE' : 4,
    'DEFAULT_PERMISSION_CLASSES' : (
        'rest_framework.permissions.AllowAny',
        ),
    'DEFAULT_AUTHENTICATION_CLASSES' : (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),
    'DEFAULT_SCHEMA_CLASS' : 'drf_spectacular.openapi.AutoSchema' ,
}