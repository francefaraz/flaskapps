def create_room(db,req):
    print(req)
    data={"username":req['username'],"password":req['password']}
    res=db.insert_one(data)


    print("done inserting of data ",res)
    res="inserted"
    return res
