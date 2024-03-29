def userEntity(item):
    try:
        user_entity = {
        "id":str(item["_id"]),
        "username":item["username"],
        "email":item["email"],
        "hashed_password":item["hashed_password"]            
        }
        return user_entity
    except KeyError as e:

        print(f"KeyError: {e}")
        return None  # Or raise an exception, depending on your requirements


def usersEntity(entity)->list:
    return [userEntity(item) for item in entity]