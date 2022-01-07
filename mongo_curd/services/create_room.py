def create_room(db, req):
    print(req)
    data = {
        "roomId": req['roomId'],
        "roomPassword": req['roomPassword'],
        "roomName": req['roomName'],
        "ytUrl": req['ytUrl'],
        "map": req['map'],
        "mode": req['mode'],
        "matchtime": req['matchtime']
    }
    # if req['roomId'].isdigit() and req['roomz']:
    #

    res = db.insert_one(data)
    return res


#
