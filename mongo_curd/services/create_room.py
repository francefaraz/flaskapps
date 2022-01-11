import json
def create_room(db, req):
    print(req)
    # data = {
    #     "roomId": req['roomId'],
    #     "roomPassword": req['roomPassword'],
    #     "roomName": req['roomName'],
    #     # "ytUrl": req.get('ytUrl',"https://youtu.be/qq3pVACFVho"),
    #     "map": req['map'],
    #     "mode": req['mode'],
    #     "matchtime": req['matchtime']
    # }

    data = {
            "roomId": req['roomId'],
            "roomPassword": req['roomPassword'],
            "roomName": req['roomName'],
            "ytUrl": req.get('ytUrl', "https://youtu.be/qq3pVACFVho"),
            "map": req['map'],
            "mode": req.get('mode', "fullmap"),
            "matchtime": req['matchtime']
            }
    # if req['roomId'].isdigit() and req['roomz']:
    #

    res = db.insert_one(data)
    res="inserted successfully"
    return res


#



def display(db):
    res=db.find({})
    x=[]
    # print("res is ",res)
    for i in res:
        # print("data is ",i['_id'])
        x.append(i)
    #     print(i)
        
    print(res.collection)
    # res=list(res)
    print("start suresh",type(x))
    # print(dir(res))
    # print(str(x))
    # x=str(x)
 
    return {
        'value':'1',
        'x':x
    }

