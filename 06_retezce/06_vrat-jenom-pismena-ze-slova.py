def extract_username(username):
    extracted = ''
    for znak in username:
        # if znak >= '0' and znak <= '9'
        if znak in '0123456789':
            continue
        extracted += znak            
    return extracted

print(extract_username('Jsdf35sdf44'))
