def NULL_not_found(object: any) -> int:
    mychecks = {None,float("Nan"),0,'',False}
    print(type(object))
    if object in mychecks:
        return 0
    return 1