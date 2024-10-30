# from  af09.aut import Token
from af09.help import Output, Ff
import json,time,sys
from af09.send_request import Api
import urllib.parse
ll=Ff.ll
output = Output()  
api = Api()
output.banner()


# ------------------
def parse_query_to_data(query):
    parsed_query = urllib.parse.parse_qs(query)
    hash_value = parsed_query.get('hash', [''])[0]

    data_parts = []

    # Include auth_date first
    auth_date = parsed_query.get('auth_date', [''])[0]
    if auth_date:
        data_parts.append(f"auth_date={auth_date}")

    # Then add query_id
    query_id = parsed_query.get('query_id', [''])[0]
    if query_id:
        data_parts.append(f"query_id={query_id}")

    # Add user data
    user_data = parsed_query.get('user', [''])[0]
    if user_data:
        user_data_json = json.loads(urllib.parse.unquote(user_data))
        user_str = json.dumps(user_data_json, separators=(',', ':'), ensure_ascii=False)  # Pastikan karakter tidak di-escape
        data_parts.append(f"user={user_str}")

    # Join data parts with newline
    data_str = "\n".join(data_parts)

    # Return result as dictionary
    return {
        "hash": hash_value,
        "data": data_str
    }

def get_user(payload):
    # 
    req=api.post(
        # url= 'https://miniapp.bool.network/backend/bool-tg-interface/assignment/list',
        url='https://miniapp.bool.network/backend/bool-tg-interface/user/user/strict',
        data=payload,
        token=""  
    ) 
    return req
#
def get_querys():
    with open('querys.txt', 'r') as file:
    # Membaca semua baris dan menghapus karakter newline di setiap baris
        queries = [line.strip() for line in file.readlines()]
    return queries

def get_data_user(payload):
    req=api.post(
        url='https://miniapp.bool.network/backend/bool-tg-interface/assignment/list',
        data=json.dumps(payload),
        token=""
    )
    return req

def list_tasks(payload):
    # print(json.dumps(data))
    req=api.post(
        url   = 'https://miniapp.bool.network/backend/bool-tg-interface/assignment/list',
        data  = payload,
        token = ""
    )
    return req

def claim_task(payload):

    req=api.post(
        url   = 'https://miniapp.bool.network/backend/bool-tg-interface/assignment/do',
        data  = payload,
        token = ""
    )
    res= req.json()
    return res

def list_stacking(payload):
    
    req=api.post(
        url   = "https://miniapp.bool.network/backend/bool-tg-interface/assignment/daily/list",
        data  = payload,
        token = ""
    )

    return req

def claim_task_daly(payload):

    req=api.post(
        url   = 'https://miniapp.bool.network/backend/bool-tg-interface/assignment/daily/do',
        data  = payload,
        token = ""
    )
    res= req.json()
    return res

def task_assignment_daly(payload):
    req=api.post(
        url   = "https://miniapp.bool.network/backend/bool-tg-interface/assignment/daily/repeat-assignment",
        data  = payload,
        token = ""
    )
    res= req.json()
    return res

def claim_task_assignment_daly(payload):
    req=api.post(
        url   = "https://miniapp.bool.network/backend/bool-tg-interface/assignment/daily/assignment",
        data  = payload,
        token = ""
    )
    # res= req.json()
    return req

def staking_coin(payload):
    req=api.post(
        url   = "https://miniapp.bool.network/backend/bool-tg-interface/stake/do",
        data  = payload,
        token = ""
    )
    res= req.json()
    return res

def staking_address():
    req=api.get2(
        url   = f"https://bot-api.bool.network/bool-tg-interface/user/vote:devices?pageNo=1&pageSize=1&yield=1",
        data  = '',
        token = ""
    )
    data=req.json()['data']['records'][0]
    return data['deviceID'],data['nextStake'],data["currentStake"]

def list_task_2(payload):
    req=api.post(
        url   = "https://bot-api.bool.network/bool-tg-interface/assignment/list",
        data  = payload,
        token = ""
    )
    res= req.json()
    return res
#
def staked_address(address,total_coin):
    req=api.get(
        url   = f"https://miniapp.bool.network/backend/bool-tg-interface/user/user-vote-devices?address={address}&pageNo=1&pageSize=100&yield=1",
        data  = "",
        token = ""
    )
    
    res= req.json()
    total_staked=0
    len_total_coin= len(str(total_coin))
 
    for d in res['data']['records']:
        total_staked+=int(d['currentStake'][:len_total_coin])
    sisa = total_staked-int(len_total_coin)
    
    return sisa
#


# ----------------- 

def main():
    Q=get_querys()
    for i,d in enumerate(Q):
        output.warning(f"####### {i+1}/{len(Q)} ####### ")
        payload=parse_query_to_data(d)
        
        ### DATA USER
        user=get_user(payload=payload).json()['data']
        output.warning(f"User: {user['username']}")
        
        ###  STACKING Daly
        output.warning("##> DAILY :")
        task_daily=list_stacking(payload).json()
        for daily in task_daily['data'] :
            if daily['done']=="false":
                payload['assignmentId']=daily['assignmentId']
                if claim_task_daly(payload).status_code == 200 :
                    output.success(f"{daily['title']} - Success")
        
        ### task_assignment_daly
        output.warning("##> DAILY - ASSIGMENT :")
        task_assigments=task_assignment_daly(payload)
        for assigment in task_assigments['data'] :
            if assigment['done'] == False:
                payload['assignmentId']=assigment['assignmentId']
                claim_assigment=claim_task_assignment_daly(payload)
                if claim_assigment.status_code == 200 :
                    output.success(f"{assigment['title']} - Success")
                
        # ### TASK
        output.warning("##> LIST-TASK  :")
        tasks=list_tasks(payload)
        for task in tasks.json()['data'] :
            if task['completeTime'] != None :
                output.success(f"{task['title']}   -   Success") 
                continue 
            payload['assignmentId']=task['assignmentId']
            claim=claim_task(payload)
            if claim['code']==200 :
                output.success(f"{task['title']}   -   Success") 
            else:
                output.danger(f"{task['title']}    -   Gagal") 
            time.sleep(0.5)
        
        ### STAKING-POIN
        user=get_user(payload=payload).json()['data']
        total_coin=int(round(float(user['rewardValue'])))
        
        s_address,vote,current_staked=staking_address()
        payload['deviceId']=[s_address]
 
        # get staked
        sisa_coin=staked_address(user['evmAddress'],total_coin)
       
        output.warning("### >  STAKING POIN :")
        if sisa_coin < 1:
            return 
 
        if 0 == int(vote):
            payload['amount']=[sisa_coin]
        else:
            payload['amount']=[(int(current_staked)+int(sisa_coin))]
        res_req_staked=staking_coin(payload)  
        # print(res_req_staked)
        output.success(f"Stakeing {payload['amount']}: {res_req_staked['message']}")
        
        
        
       

if __name__ == "__main__":
    while True:
        try:
            main()
            Ff.countdown(3600)
        except KeyboardInterrupt:
            print("Program dihentikan oleh pengguna (Ctrl+C)")
            
            break
        except Exception as e:
            print(f"Error tidak tertangani: {e}")
            Ff.countdown(10)
            continue
