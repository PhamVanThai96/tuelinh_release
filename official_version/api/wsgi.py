from tuelinh_real_estate.wsgi import application

# Add MIME type handling
def handler(event, context):
    return application(event, context)
