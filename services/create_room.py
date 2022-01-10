def create_room(db, req):
    print(req)
    # data = {
    #     "roomId": req['roomId'],
    #     "roomPassword": req['roomPassword'],
    #     "roomName": req['roomName'],
    #     # "ytUrl": req.get('ytUrl',"hello"),
    #     "map": req['map'],
    #     "mode": req['mode'],
    #     "matchtime": req['matchtime']
    # }

    data = {
            "roomId": req['room_id'],
            "roomPassword": req['room_password'],
            "roomName": req['room_name'],
            "ytUrl": req.get('ytUrl', "https://youtu.be/qq3pVACFVho"),
            "map": req['map'],
            "mode": req.get('mode', "fullmap"),
            "matchtime": req['match_time']
            }
    # if req['roomId'].isdigit() and req['roomz']:
    #

    res = db.insert_one(data)
    res="inserted successfully"
    return res


#
