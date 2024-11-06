import pymongo
import os
from fastapi import APIRouter

client = pymongo.MongoClient(os.getenv("MONGO_URI"))

users = client['user']
user = users['user']
workDetails = users['workDetails']

shop = client['shop']
info = shop['info']
env = shop['env']

ohc = client['ohc']['ohc']

opd = client['opd']['opd']

ipd = client['ipd']['ipd']

medicines = client['medicine']['medicine']

pathology = client['pathology']['pathology']

router = APIRouter()


@router.get("/user_analytics/{userid}")
def user_infomation_analytics(userid: str, starting_date: str, ending_date: str):
    user_data = user.find_one({"userid": userid})
    work_data = workDetails.find({"userid": userid})
    ohc_data = ohc.find({"userid": userid})
    opd_data = opd.find({"userid": userid})
    ipd_data = ipd.find({"userid": userid})
    medicines_data = medicines.find({"userid": userid})
    pathology_data = pathology.find({"userid": userid})

    userinfo = {}
    if user_data:
        userinfo = user_data
        userinfo.pop("_id")

    wordDetails = []
    for data in work_data:
        data.pop("_id")
        wordDetails.append(data)

    ohcInfo = []
    for data in ohc_data:
        data.pop("_id")
        ohcInfo.append(data)

    opdInfo = []
    for data in opd_data:
        data.pop("_id")
        opdInfo.append(data)

    ipdInfo = []
    for data in ipd_data:
        data.pop("_id")
        ipdInfo.append(data)

    medicinesInfo = []
    for data in medicines_data:
        data.pop("_id")
        medicinesInfo.append(data)

    pathologyInfo = []
    for data in pathology_data:
        data.pop("_id")
        pathologyInfo.append(data)

    if (len(wordDetails) > 0):
        shopid = wordDetails[0]["shopid"]
        shopInfo = info.find_one({"shopid": shopid})
        envInfo = env.find({"shopid": shopid})
        shop = {}
        if shopInfo:
            shopInfo.pop("_id")
            shop = shopInfo
        envData = []
        for data in envInfo:
            data.pop("_id")
            envData.append(data)
    else:
        shop = {}
        envData = []

    res = {
        "user": userinfo,
        "work": wordDetails,
        "shop": shop,
        "env": envData,
        "userMedical": {
            "ohc": ohcInfo,
            "opd": opdInfo,
            "ipd": ipdInfo,
            "medicines": medicinesInfo,
            "pathology": pathologyInfo
        }
    }

    return {"data": res}
