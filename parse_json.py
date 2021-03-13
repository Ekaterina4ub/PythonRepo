# parse json from variable to get value '5'

JSON = {
  'Country': [{
        'City': [{
            'Village': {
                'Cat': '4',
                'Dog': '5'
            }
        }]
    }]
}

value = JSON['Country'][0]['City'][0]['Village']['Dog']
print(value)
