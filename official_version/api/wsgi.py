from tuelinh_real_estate.wsgi import application

def handler(event, context):
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': ''
        }

    return {
        'statusCode': '200',
        'body': application(event, context),
        'headers': {
            'Content-Type': 'text/html',
            'Access-Control-Allow-Origin': '*',
        }
    }
