# -*- coding: utf-8 -*-

import TyfeAPI
from TyfeAPI.lib.curve.ttypes import *
from multiprocessing import Pool,Process
from googletrans import Translator
from random import randint
from login import *
from bs4 import BeautifulSoup
import time,random,sys,json,codecs,threading,glob,re,datetime,urllib.request,urllib.error,urllib.parse,pickle,requests,base64,antolib,subprocess,unicodedata,GACSender,os

print("""

\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m██▀▀▀▀▀▀▀▀███████████████▀▀▀▀█████████████
██▄▄▄  ▄▄▄██████████████  ▄▄▄█████████████
█████  █████▄  ██   ██       ████▀    ▀███
█████  ██████  ▀█  █████  ██████  ▀▀▀▀  ██
█████  ███████    ▄█████  ██████  ▄▄▄▄▄▄██
█████  ████████   ██████  ██████▄  ▀▀▀▀ ██
█████▄▄████████  ███████▄▄████████▄▄▄▄▄███
█████████████   ██████████████████████████
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\033[0m

""")

mainftoken = ""
mainstoken = ""

tyfeftoken = ""
tyfestoken = ""

add1ftoken = ""
add1stoken = ""

add2ftoken = ""
add2stoken = ""

add3ftoken = ""
add3stoken = ""

cl = TyfeAPI.LINE()
if mainftoken == "":
    mainftoken = LINE(appName=0,logNum=0).authToken
if mainstoken == "":
    mainstoken = LINE(appName=1,logNum=0).authToken
cl.nxtQRLogin(ftoken=mainftoken,stoken=mainstoken)
cl.loginResult(ftoken=mainftoken,stoken=mainstoken)

kk = TyfeAPI.LINE()

aa = TyfeAPI.LINE()
ab = TyfeAPI.LINE()
ac = TyfeAPI.LINE()

TyfeLogged = False
TyfeHelperLogged = False

start_runtime = datetime.datetime.now()

with open('tval.pkl', 'rb') as f:
    seeall,tadmin,banned,kickLockList,autoLikeSetting,save1,wait,botProtect,save2,dublist,blockInvite,jfkeyword,join_delay,join_time,joinDetail,preventBlockURL,tyfeFollow,autoDeny,mentmedat = pickle.load(f,encoding='latin1')

anto = antolib.Anto("Noxturnix","MMMLemQ3BTEnz2dpb9dN2pbUmDJ8ZUIN7KELeC5t","Tyfe_Global")

def connectedCB():
    anto.sub("bcastTo")
    anto.sub("bcastMsg")

bcastTo = None

def dataCB(channel, msg):
    global bcastTo
    global TyfeLogged
    global TyfeHelperLogged
    try:
        if channel == "bcastTo":
            bcastTo = msg.decode("utf-8")
        if channel == "bcastMsg" and TyfeLogged:
            kk.sendText(bcastTo,msg.decode("utf-8"))
            if TyfeHelperLogged:
                aa.sendText(bcastTo,msg.decode("utf-8"))
                ab.sendText(bcastTo,msg.decode("utf-8"))
                ac.sendText(bcastTo,msg.decode("utf-8"))
    except:
        pass

def setup():
    anto.mqtt.onConnected(connectedCB)
    anto.mqtt.onData(dataCB)
    anto.mqtt.connect()

setup()

def antoloop():
    time.sleep(300)

Amid = cl.getProfile().mid

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']

dangerMessage = ["cleanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","makasih :d","!kickall","nuke"]

procLock = 0

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

user1 = Amid
user2 = ""

helper1 = ""
helper2 = ""
helper3 = ""

Rapid1To = ""

def Rapid1Say(mtosay):
    cl.sendText(Rapid1To,mtosay)

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

readAlert = False

captkey = ""

lgncall = ""
def logincall(this,pointer):
    if pointer == 0:
        status = "[1/2]"
    elif pointer == 1:
        status = "[2/2]"
    cl.sendText(lgncall,"Tyfe's login URL "+status+": "+this)

lgnhident = 0

def helperlogincall(this,pointer):
    if pointer == 0:
        status = "[1/2]"
    elif pointer == 1:
        status = "[2/2]"
    if lgnhident == 0:
        nident = "I"
    elif lgnhident == 1:
        nident = "II"
    elif lgnhident == 2:
        nident = "III"
    cl.sendText(lgncall,"Tyfe Helper "+nident+"'s login URL "+status+": "+this)

userhelp = """คำสั่งทั้งหมด (พิมพ์ . ตามด้วยคำสั่ง):

- help
- tyfelogin
- tyfehelperlogin
- tyfejoin
- tyfeqrjoin
- tyfeidjoin [ID กลุ่ม]
- tyfefollow [on/off]
- tyfeleave [ID กลุ่ม]
- tyfelogout
- tyfehelperlogout
- sh [คำสั่ง]
- uptime
- name [ชื่อใหม่]
- nmx [ชื่อใหม่]
- myid
- me
- uid (@)
- gid
- info [@]
- joindetail [on/off]
- getjoined
- whois [ID บัญชี]
- remove [@]
- removeall (ID กลุ่ม)
- bye [@]
- groupinfo
- urlstatus
- toggleurl
- checkmention
- groupname [ชื่อใหม่]
- groupurl
- join [ID กลุ่ม] [URL]
- jfset [ข้อความ Keyword] [ดีเลย์] [จำนวนครั้ง]
- tx [ข้อความ]
- autodeny (จำนวน/off)
- denyall (ข้อความ)
- invitecancel
- gift (ID ธีม)
- save
- copy (@)
- load
- mentionall
- profpic [@]
- homepic [@]
- crash
- autoread [on/off]
- speed
- say [ข้อความ] [จำนวน]

**คำสั่งสำหรับบัญชีนี้เท่านั้น"""

def user1script(op):
    global TyfeLogged
    global kk
    global aa
    global ab
    global ac
    global user2
    global readAlert
    global lgncall
    global save1
    global TyfeHelperLogged
    global helper1
    global helper2
    global helper3
    global start_runtime
    global jfkeyword
    global join_delay
    global join_time
    global userhelp
    global joinDetail
    global tyfeFollow
    global procLock
    global captkey
    global lgnhident
    global tyfeftoken
    global tyfestoken
    global add1ftoken
    global add1stoken
    global add2ftoken
    global add2stoken
    global add3ftoken
    global add3stoken
    global autoDeny
    global mentmedat
    try:
        # if op.type not in [61,60,59,55,40,26,25]:
            # print str(op)
            # print "\n\n"
        if op.type == 13:
            invitor = op.param2
            gotinvite = []
            if "\x1e" in op.param3:
                gotinvite = op.param3.split("\x1e")
            else:
                gotinvite.append(op.param3)
            if invitor in [user2,helper1,helper2,helper3] and user1 in gotinvite:
                cl.acceptGroupInvitation(op.param1)
            else:
                group = cl.getGroup(op.param1)
                if len(group.members) <= autoDeny:
                    procLock += 1
                    cl.acceptGroupInvitation(op.param1)
                    cl.leaveGroup(op.param1)
        if op.type == 14 and TyfeLogged:
            kk.leaveGroup(op.param1)
            if TyfeHelperLogged:
                aa.leaveGroup(op.param1)
                ab.leaveGroup(op.param1)
                ac.leaveGroup(op.param1)
        if op.type == 16:
            if procLock > 0:
                procLock -= 1
            else:
                try:
                    if TyfeLogged:
                        if joinDetail:
                            gname = cl.getGroup(op.param1).name
                            kk.sendText(user1,gname+"\n"+op.param1)
                        if tyfeFollow:
                            x = cl.getGroup(op.param1)
                            if user2 not in [i.mid for i in x.members]:
                                defclose = False
                                if x.preventJoinByTicket == False:
                                    ticket = cl.reissueGroupTicket(op.param1)
                                    kk.acceptGroupInvitationByTicket(op.param1,ticket)
                                    if TyfeHelperLogged:
                                        aa.acceptGroupInvitationByTicket(op.param1,ticket)
                                        ab.acceptGroupInvitationByTicket(op.param1,ticket)
                                        ac.acceptGroupInvitationByTicket(op.param1,ticket)
                                    defclose = False
                                else:
                                    sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                                    if sirilist == []:
                                        x.preventJoinByTicket = False
                                        cl.updateGroup(x)
                                        ticket = cl.reissueGroupTicket(op.param1)
                                        kk.acceptGroupInvitationByTicket(op.param1,ticket)
                                        if TyfeHelperLogged:
                                            aa.acceptGroupInvitationByTicket(op.param1,ticket)
                                            ab.acceptGroupInvitationByTicket(op.param1,ticket)
                                            ac.acceptGroupInvitationByTicket(op.param1,ticket)
                                        defclose = True
                                    else:
                                        cl.inviteIntoGroup(op.param1,[user2])
                                        if TyfeHelperLogged:
                                            cl.inviteIntoGroup(op.param1,[helper1,helper2,helper3])
                                        kk.acceptGroupInvitation(op.param1)
                                        if TyfeHelperLogged:
                                            aa.acceptGroupInvitation(op.param1)
                                            ab.acceptGroupInvitation(op.param1)
                                            ac.acceptGroupInvitation(op.param1)
                                if defclose:
                                    x.preventJoinByTicket = True
                                    cl.updateGroup(x)
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            kk.sendText(op.param1,"Tyfe พร้อมใช้งานแล้ว (｀・ω・´)"+tm)
                except Exception as e:
                    print(e)
        if op.type == 19 and op.param3 == user1:
            procLock = 1
            gotk = cl
            kickname = None
            kickname = kk.getContact(op.param2).displayName
            for i in [aa,ab,ac]:
                if kickname == None:
                    kickname = i.getContact(op.param2).displayName
                    print(kickname)
            if kickname == None:
                kickname = cl.getContact(op.param2).displayName
            if not (any(word in kickname for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or kickname.isdigit()):
                isNotAdmin = False
                if op.param2 not in [user1,user2,helper1,helper2,helper3] and not (op.param1 in tadmin and op.param2 in tadmin[op.param1]):
                    isNotAdmin = True
                if isNotAdmin:
                    tmpl = []
                    if op.param1 in banned:
                        tmpl = banned[op.param1]
                    banned[op.param1] = []
                    if op.param2 not in tmpl:
                        banned[op.param1].append(op.param2)
                    if tmpl != []:
                        for oldtarg in tmpl:
                            banned[op.param1].append(oldtarg)
                x = None
                alive = None
                x = kk.getGroup(op.param1)
                for i in [aa,ab,ac]:
                    if x == None:
                        x = i.getGroup(op.param1)
                if x == None:
                    x = cl.getGroup(op.param1)
                mingr = [i.mid for i in x.members]
                if user2 in mingr:
                    alive = kk
                elif helper1 in mingr:
                    alive = aa
                elif helper2 in mingr:
                    alive = ab
                elif helper3 in mingr:
                    alive = ac
                elif user1 in mingr:
                    alive = cl
                defclose = False
                if x.preventJoinByTicket == False:
                    ticket = alive.reissueGroupTicket(op.param1)
                    gotk.acceptGroupInvitationByTicket(op.param1,ticket)
                    defclose = False
                else:
                    sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                    if sirilist == []:
                        x.preventJoinByTicket = False
                        alive.updateGroup(x)
                        ticket = alive.reissueGroupTicket(op.param1)
                        gotk.acceptGroupInvitationByTicket(op.param1,ticket)
                        defclose = True
                    else:
                        alive.inviteIntoGroup(op.param1,[op.param3])
                        try:
                            gotk.acceptGroupInvitation(op.param1)
                        except:
                            pass
                if defclose:
                    x.preventJoinByTicket = True
                    alive.updateGroup(x)
                if isNotAdmin:
                    setKick(op.param1,op.param2,True)
                now2 = datetime.datetime.now()
                nowT = datetime.datetime.strftime(now2,"%H")
                nowM = datetime.datetime.strftime(now2,"%M")
                nowS = datetime.datetime.strftime(now2,"%S")
                tm = "\n\n"+nowT+":"+nowM+":"+nowS
                kk.sendText(op.param1,"สมาชิกไม่ได้รับอนุญาตให้ลบบัญชีนี้ （´・ω・｀）\nพิมพ์ 「Tyfe:halt」 ในกรณีที่ต้องการนำบอทออกจากกลุ่ม"+tm)
                msg = Message()
                msg.to = op.param1
                msg.from_ = user2
                msg.contentType = 13
                msg.text = None
                msg.contentMetadata = {'mid': op.param2}
                kk.sendMessage(msg)
        if op.type == 55:
            if op.param1 in seeall:
                seeall[op.param1].append(op.param2)
                if readAlert == True and TyfeLogged:
                    reader = cl.getContact(op.param2)
                    if reader.attributes != 32:
                        try:
                            kk.sendText(user1,reader.displayName+"\nจากกลุ่ม "+cl.getGroup(op.param1).name+"\nอ่านแล้ว")
                        except:
                            kk.sendText(user1,reader.displayName+"\nอ่านแล้ว")
        if op.type == 26:
            msg = op.message
            if msg.text == "นับ":
                if msg.toType == 2:
                    for i in range(1,10):
                        cl.sendText(msg.to,str(i))
                        time.sleep(0.25)
                    cl.sendText(msg.to,"0")
            """if msg.text == "6":
                if msg.from_ == "u1706c2841f727da3429bf9ea16346ffd" and msg.toType == 2:
                    if randint(1,3) == 1:
                        time.sleep(0.15)
                        print("ues")
                    else:
                        print("no")
                    cl.sendText(msg.to,random.choice(["โฟล์ค"]))"""
            if wait['alwayRead']:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)
                    if TyfeLogged:
                        kk.sendChatChecked(msg.to,msg.id)
                        if TyfeHelperLogged:
                            aa.sendChatChecked(msg.to,msg.id)
                            ab.sendChatChecked(msg.to,msg.id)
                            ac.sendChatChecked(msg.to,msg.id)
            if msg.contentMetadata != {}:
                try:
                    prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                    tagme = False
                    alluids = []
                    for i in range(len(prov)):
                        alluids.append(prov[i]["M"])
                        if prov[i]["M"] == user1:
                            tagme = True
                    alluids = list(set(alluids))
                    if tagme:
                        if len(alluids) <= 4:
                            if msg.to not in mentmedat:
                                mentmedat[msg.to] = []
                            tagfrom = msg.from_
                            tagtime = nowS = datetime.datetime.strftime(datetime.datetime.now(),"%d/%m/%y %H:%M:%S")
                            tagid = msg.id
                            mentmedat[msg.to].append(
                                {
                                    "tfrom" : tagfrom,
                                    "ttime" : tagtime,
                                    "tid" : tagid
                                }
                            )
                        msg.contentType = 7
                        msg.text = ''
                        msg.contentMetadata = {
                                                  'STKPKGID': '608',
                                                  'STKTXT': '[]',
                                                  'STKVER': '16',
                                                  'STKID':'5507'
                                              }
                        cl.sendMessage(msg)
                except:
                    pass
            if msg.text in ["55","555","555+","5555"]:
                if msg.toType != 0:
                    pass
                    cl.sendText(msg.to,"ขำไรวะ")




        if op.type == 25:
            msg = op.message
            try:
                if ".say " in msg.text.lower():
                    spl = re.split(".say ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        mts = spl[1]
                        mtsl = mts.split()
                        mtsTimeArg = len(mtsl) - 1
                        mtsTime = mtsl[mtsTimeArg]
                        del mtsl[mtsTimeArg]
                        mtosay = " ".join(mtsl)
                        global Rapid1To
                        Rapid1To = msg.to
                        RapidTime = mtsTime
                        rmtosay = []
                        for count in range(0,int(RapidTime)):
                            rmtosay.insert(count,mtosay)
                        p = Pool(20)
                        p.map(Rapid1Say,rmtosay)
                        p.close()
                elif msg.text.lower() == ".me":
                    msg.contentType = 13
                    msg.text = None
                    msg.contentMetadata = {'mid': user1}
                    cl.sendMessage(msg)
                elif msg.text.lower() == ".gift":
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': '',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '1'}
                    msg.text = None
                    cl.sendMessage(msg)
                elif ".gift " in msg.text.lower():
                    red = re.compile(re.escape('.gift '),re.IGNORECASE)
                    themeid = red.sub('',msg.text)
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': themeid,
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '1'}
                    msg.text = None
                    cl.sendMessage(msg)
                elif msg.text.lower() == ".groupinfo":
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            gCreator = ginfo.creator.displayName
                        except:
                            gCreator = "[[ERROR]]"
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "ปิด"
                        else:
                            u = "เปิด"
                        cl.sendText(msg.to,"ชื่อกลุ่ม: " + str(ginfo.name) + "\n\nผู้สร้าง: " + gCreator + "\nรหัสกลุ่ม (gid): " + msg.to + "\nรูปกลุ่ม:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nสมาชิก: " + str(len(ginfo.members)) + " ท่าน\nค้างเชิญ: " + sinvitee + " ท่าน\nURL: " + u)
                elif msg.text == ".Speed":
                    cl.sendText(msg.to,"กำลังทดสอบ..")
                    start = time.time()
                    for i in range(3000):
                        1+1
                    cl.sendText(msg.to,str(int(round((time.time() - start) * 1000)))+" ms")
                elif msg.text.lower() == ".speed":
                    start = time.time()
                    cl.sendText(msg.to,"กำลังทดสอบ..")
                    cl.sendText(msg.to,str(int(round((time.time() - start) * 1000)))+" ms")
                    # cl.sendText(msg.to,"0.000000000000 วินาที")
                elif msg.text.lower() == ".invitecancel":
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            cl.cancelGroupInvitation(msg.to,[i])
                elif msg.text.lower() == ".gid":
                    if msg.toType == 2:
                        cl.sendText(msg.to,msg.to)
                    else:
                        cl.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น")
                elif msg.text.lower() == ".uid":
                    if msg.toType == 0:
                        cl.sendText(msg.to,msg.to)
                elif ".uid " in msg.text.lower():
                    if msg.toType == 2:
                        red = re.compile(re.escape('.uid '),re.IGNORECASE)
                        namel = red.sub('',msg.text)
                        namel = namel.lstrip()
                        namel = namel.replace(" @","$spliter$")
                        namel = namel.replace("@","")
                        namel = namel.rstrip()
                        namel = namel.split("$spliter$")
                        gmem = cl.getGroup(msg.to).members
                        for targ in gmem:
                            if targ.displayName in namel:
                                cl.sendText(msg.to,targ.displayName+": "+targ.mid)
                elif msg.text.lower() == ".myid":
                    cl.sendText(msg.to,user1)
                elif msg.text.lower().startswith(".mentionall"):
                    data = msg.text[len(".mentionall"):].strip()
                    if data == "":
                        group = cl.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != user1]
                        cb = ""
                        cb2 = ""
                        count = 1
                        strt = len(str(count)) + 2
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            akh = akh + len(str(count)) + 2 + 5
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 50:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    cl.sendMessage(msg)
                                except:
                                    cl.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            cl.sendMessage(msg)
                        except:
                            cl.sendText(msg.to,"[[NO MENTION]]")
                    elif data[0] == "<":
                        mentargs = int(data[1:].strip())
                        group = cl.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != user1]
                        cb = ""
                        cb2 = ""
                        count = 1
                        strt = len(str(count)) + 2
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            if count > mentargs:
                                break
                            akh = akh + len(str(count)) + 2 + 5
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 50:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    cl.sendMessage(msg)
                                except:
                                    cl.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            cl.sendMessage(msg)
                        except:
                            cl.sendText(msg.to,"[[NO MENTION]]")
                    elif data[0] == ">":
                        mentargs = int(data[1:].strip())
                        group = cl.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != user1]
                        cb = ""
                        cb2 = ""
                        count = 1
                        if mentargs >= 0:
                            strt = len(str(mentargs)) + 2
                        else:
                            strt = len(str(count)) + 2
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            if count < mentargs:
                                count += 1
                                continue
                            akh = akh + len(str(count)) + 2 + 5
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 50:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    cl.sendMessage(msg)
                                except:
                                    cl.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            cl.sendMessage(msg)
                        except:
                            cl.sendText(msg.to,"[[NO MENTION]]")
                    elif data[0] == "=":
                        mentargs = int(data[1:].strip())
                        group = cl.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != user1]
                        cb = ""
                        cb2 = ""
                        count = 1
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            if count != mentargs:
                                count += 1
                                continue
                            akh = akh + len(str(count)) + 2 + 5
                            strt = len(str(count)) + 2
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 50:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    cl.sendMessage(msg)
                                except:
                                    cl.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            cl.sendMessage(msg)
                        except:
                            cl.sendText(msg.to,"[[NO MENTION]]")
                elif msg.text.lower() == ".autoread on":
                    wait['alwayRead'] = True
                    cl.sendText(msg.to,"เปิดโหมดอ่านอัตโนมัติแล้ว")
                elif msg.text.lower() == ".autoread off":
                    wait['alwayRead'] = False
                    cl.sendText(msg.to,"ปิดโหมดอ่านอัตโนมัติแล้ว")
                elif msg.text.lower() == ".tyfelogin":
                    if not TyfeLogged:
                        lgncall = msg.to
                        if tyfeftoken == "":
                            tyfeftoken = LINE(appName=0,logNum=1,callback=logincall).authToken
                        if tyfestoken == "":
                            tyfestoken = LINE(appName=1,logNum=1,callback=logincall).authToken
                        kk.nxtQRLogin(ftoken=tyfeftoken,stoken=tyfestoken,callback=logincall)
                        kk.loginResult(ftoken=tyfeftoken,stoken=tyfestoken)
                        tyfeftoken = tyfestoken = ""
                        user2 = kk.getProfile().mid
                        for i in banned:
                            try:
                                banned[i].remove(user2)
                            except:
                                pass
                        for i in tadmin:
                            try:
                                tadmin[i].remove(user2)
                            except:
                                pass
                        TyfeLogged = True
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(user1,"ล็อกอินสำเร็จ Tyfe พร้อมใช้งานแล้ว (｀・ω・´)"+tm)
                    else:
                        cl.sendText(msg.to,"Tyfe ได้ทำการล็อกอินไปแล้ว")
                elif msg.text.lower() == ".tyfelogout":
                    if TyfeLogged:
                        lgtname = "[ERROR]"
                        try:
                            lgtname = kk.getProfile().displayName
                        except:
                            pass
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        try:
                            kk.sendText(user1,"กำลังล็อกเอ้าท์ (｀・ω・´)"+tm)
                        except:
                            pass
                        user2 = ""
                        kk = None
                        kk = TyfeAPI.LINE()
                        TyfeLogged = False
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"[%H:%M:%S] ")
                        print(nowT+lgtname+" logged out ( Close connection )\n")
                        if TyfeHelperLogged:
                            lgtname = "[ERROR]"
                            try:
                                lgtname = aa.getProfile().displayName
                            except:
                                pass
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            try:
                                aa.sendText(user1,"กำลังล็อกเอ้าท์ (｀・ω・´)"+tm)
                            except:
                                pass
                            helper1 = ""
                            aa = None
                            aa = TyfeAPI.LINE()
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"[%H:%M:%S] ")
                            print(nowT+lgtname+" logged out ( Close connection )\n")
                            lgtname = "[ERROR]"
                            try:
                                lgtname = ab.getProfile().displayName
                            except:
                                pass
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            try:
                                ab.sendText(user1,"กำลังล็อกเอ้าท์ (｀・ω・´)"+tm)
                            except:
                                pass
                            helper2 = ""
                            ab = None
                            ab = TyfeAPI.LINE()
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"[%H:%M:%S] ")
                            print(nowT+lgtname+" logged out ( Close connection )\n")
                            lgtname = "[ERROR]"
                            try:
                                lgtname = ac.getProfile().displayName
                            except:
                                pass
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            try:
                                ac.sendText(user1,"กำลังล็อกเอ้าท์ (｀・ω・´)"+tm)
                            except:
                                pass
                            helper3 = ""
                            ac = None
                            ac = TyfeAPI.LINE()
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"[%H:%M:%S] ")
                            print(nowT+lgtname+" logged out ( Close connection )\n")
                            TyfeHelperLogged = False
                    else:
                        cl.sendText(msg.to,"Tyfe ยังไม่ได้ล็อกอิน")
                elif msg.text.lower() == ".":
                    gs = []
                    try:
                        gs = cl.getGroup(msg.to).members
                    except:
                        try:
                            gs = cl.getRoom(msg.to).contacts
                        except:
                            pass
                    tlist = ""
                    for i in gs:
                        tlist = tlist+i.displayName+" "+i.mid+"\n\n"
                    if TyfeLogged:
                        try:
                            kk.sendText(user1,tlist)
                        except:
                            kk.new_post(tlist)
                    else:
                        cl.sendText(msg.to,"Tyfe ยังไม่ได้ล็อกอิน")
                elif msg.text.lower() in [".tyfejoin","มาหำ"]:
                    if TyfeLogged:
                        x = cl.getGroup(msg.to)
                        if user2 not in [i.mid for i in x.members]:
                            defclose = False
                            if x.preventJoinByTicket == False:
                                ticket = cl.reissueGroupTicket(msg.to)
                                kk.acceptGroupInvitationByTicket(msg.to,ticket)
                                if TyfeHelperLogged:
                                    aa.acceptGroupInvitationByTicket(msg.to,ticket)
                                    ab.acceptGroupInvitationByTicket(msg.to,ticket)
                                    ac.acceptGroupInvitationByTicket(msg.to,ticket)
                                defclose = False
                            else:
                                sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                                if sirilist == []:
                                    x.preventJoinByTicket = False
                                    cl.updateGroup(x)
                                    ticket = cl.reissueGroupTicket(msg.to)
                                    kk.acceptGroupInvitationByTicket(msg.to,ticket)
                                    if TyfeHelperLogged:
                                        aa.acceptGroupInvitationByTicket(msg.to,ticket)
                                        ab.acceptGroupInvitationByTicket(msg.to,ticket)
                                        ac.acceptGroupInvitationByTicket(msg.to,ticket)
                                    defclose = True
                                else:
                                    cl.inviteIntoGroup(msg.to,[user2])
                            if defclose:
                                x.preventJoinByTicket = True
                                cl.updateGroup(x)
                        else:
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            kk.sendText(msg.to,"Tyfe อยู่ในกลุ่มอยู่แล้ว (｀・ω・´)"+tm)
                    else:
                        cl.sendText(msg.to,"Tyfe ยังไม่ได้ล็อกอิน")
                elif msg.text.lower() == ".crash":
                    msg.contentType = 13
                    msg.text = None
                    msg.contentMetadata = {'mid': msg.to+"',"}
                    cl.sendMessage(msg)
                elif msg.text.lower() == ".save":
                    me = cl.getProfile()
                    save1["displayName"] = me.displayName
                    save1["statusMessage"] = me.statusMessage
                    save1["pictureStatus"] = me.pictureStatus
                    save1["Saved"] = True
                    cl.sendText(msg.to,"บันทึกสถานะบัญชีเรียบร้อยแล้ว")
                elif msg.text.lower() == ".load":
                    if save1["Saved"]:
                        me = cl.getProfile()
                        me.displayName = save1["displayName"]
                        me.statusMessage = save1["statusMessage"]
                        me.pictureStatus = save1["pictureStatus"]
                        cl.updateDisplayPicture(me.pictureStatus)
                        cl.updateProfile(me)
                        wait["selfStatus"] = True
                        cl.sendText(msg.to,"โหลดสถานะบัญชีเรียบร้อยแล้ว")
                    else:
                        cl.sendText(msg.to,"ก่อนหน้านี้ยังไม่ได้มีการบันทึกสถานะบัญชี")
                elif msg.text.lower() == ".copy":
                    if msg.toType == 0:
                        wait["selfStatus"] = False
                        targ = cl.getContact(msg.to)
                        me = cl.getProfile()
                        me.displayName = targ.displayName
                        me.statusMessage = targ.statusMessage
                        me.pictureStatus = targ.pictureStatus
                        cl.updateDisplayPicture(me.pictureStatus)
                        cl.updateProfile(me)
                        cl.sendText(msg.to,"สำเร็จแล้ว")
                    else:
                        cl.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในแชทส่วนตัวเท่านั้น")
                elif ".copy " in msg.text.lower():
                    if msg.toType == 2:
                        red = re.compile(re.escape('.copy '),re.IGNORECASE)
                        tname = red.sub('',msg.text)
                        tname = tname.lstrip()
                        tname = tname.replace(" @","$spliter$")
                        tname = tname.rstrip()
                        tname = tname.split("$spliter$")
                        tname = tname[0]
                        tname = tname[1:]
                        clist = {
                            "Founded":False,
                            "displayName":"",
                            "statusMessage":"",
                            "pictureStatus":""
                        }
                        mems = cl.getGroup(msg.to).members
                        for targ in mems:
                            if targ.displayName == tname:
                                clist["displayName"] = targ.displayName
                                clist["statusMessage"] = targ.statusMessage
                                clist["pictureStatus"] = targ.pictureStatus
                                clist["Founded"] = True
                        if clist["Founded"]:
                            wait["selfStatus"] = False
                            me = cl.getProfile()
                            me.displayName = clist["displayName"]
                            me.statusMessage = clist["statusMessage"]
                            me.pictureStatus = clist["pictureStatus"]
                            cl.updateDisplayPicture(me.pictureStatus)
                            cl.updateProfile(me)
                            cl.sendText(msg.to,"สำเร็จแล้ว")
                        else:
                            cl.sendText(msg.to,"ไม่พบรายชื่อ")
                elif ".profpic " in msg.text.lower():
                    if msg.toType == 2:
                        red = re.compile(re.escape('.profpic '),re.IGNORECASE)
                        namel = red.sub('',msg.text)
                        namel = namel.lstrip()
                        namel = namel.replace(" @","$spliter$")
                        namel = namel[1:]
                        namel = namel.rstrip()
                        namel = namel.split("$spliter$")
                        gmem = cl.getGroup(msg.to).members
                        for targ in gmem:
                            if targ.displayName in namel:
                                if targ.displayName != '':
                                    cl.sendText(msg.to,targ.displayName)
                                try:
                                    cl.sendImageWithUrl(msg.to,"http://dl.profile.line.naver.jp/"+targ.pictureStatus)
                                except:
                                    pass
                elif ".homepic " in msg.text.lower():
                    if msg.toType == 2:
                        red = re.compile(re.escape('.homepic '),re.IGNORECASE)
                        namel = red.sub('',msg.text)
                        namel = namel.lstrip()
                        namel = namel.replace(" @","$spliter$")
                        namel = namel[1:]
                        namel = namel.rstrip()
                        namel = namel.split("$spliter$")
                        gmem = cl.getGroup(msg.to).members
                        for targ in gmem:
                            if targ.displayName in namel:
                                if targ.displayName != '':
                                    cl.sendText(msg.to,targ.displayName)
                                try:
                                    cl.sendImageWithUrl(msg.to,cl.channel.getCover(targ.mid))
                                except:
                                    pass
                elif ".groupname " in msg.text.lower():
                    if msg.toType == 2:
                        spl = re.split(".groupname ",msg.text,flags=re.IGNORECASE)
                        if spl[0] == "":
                            gp = cl.getGroup(msg.to)
                            gp.name = spl[1]
                            cl.updateGroup(gp)
                elif msg.text.lower() == ".tyfeqrjoin":
                    if TyfeLogged:
                        x = cl.getGroup(msg.to)
                        if user2 not in [i.mid for i in x.members]:
                            if x.preventJoinByTicket == False:
                                ticket = cl.reissueGroupTicket(msg.to)
                                kk.acceptGroupInvitationByTicket(msg.to,ticket)
                                if TyfeHelperLogged:
                                    aa.acceptGroupInvitationByTicket(msg.to,ticket)
                                    ab.acceptGroupInvitationByTicket(msg.to,ticket)
                                    ac.acceptGroupInvitationByTicket(msg.to,ticket)
                            else:
                                x.preventJoinByTicket = False
                                cl.updateGroup(x)
                                ticket = cl.reissueGroupTicket(msg.to)
                                kk.acceptGroupInvitationByTicket(msg.to,ticket)
                                if TyfeHelperLogged:
                                    aa.acceptGroupInvitationByTicket(msg.to,ticket)
                                    ab.acceptGroupInvitationByTicket(msg.to,ticket)
                                    ac.acceptGroupInvitationByTicket(msg.to,ticket)
                                x.preventJoinByTicket = True
                                cl.updateGroup(x)
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            kk.sendText(msg.to,"Tyfe พร้อมใช้งานแล้ว (｀・ω・´)"+tm)
                        else:
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            kk.sendText(msg.to,"Tyfe อยู่ในกลุ่มอยู่แล้ว (｀・ω・´)"+tm)
                    else:
                        cl.sendText(msg.to,"Tyfe ยังไม่ได้ล็อกอิน")
                elif ".whois " in msg.text.lower():
                    spl = re.split(".whois ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        msg.contentType = 13
                        msg.text = None
                        msg.contentMetadata = {"mid":spl[1]}
                        cl.sendMessage(msg)
                elif ".remove " in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            cl.kickoutFromGroup(msg.to,[prov[i]["M"]])
                elif ".bye " in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        allmid = []
                        for i in range(len(prov)):
                            cl.kickoutFromGroup(msg.to,[prov[i]["M"]])
                            allmid.append(prov[i]["M"])
                        cl.findAndAddContactsByMids(allmid)
                        cl.inviteIntoGroup(msg.to,allmid)
                        cl.cancelGroupInvitation(msg.to,allmid)
                elif ".denyall" in msg.text.lower():
                    spl = re.split(".denyall",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        spl[1] = spl[1].strip()
                        ag = cl.getGroupIdsInvited()
                        txt = "กำลังยกเลิกค้างเชิญจำนวน "+str(len(ag))+" กลุ่ม"
                        if spl[1] != "":
                            txt = txt + " ด้วยข้อความ \""+spl[1]+"\""
                        txt = txt + "\nกรุณารอสักครู่.."
                        cl.sendText(msg.to,txt)
                        procLock = len(ag)
                        for gr in ag:
                            try:
                                cl.acceptGroupInvitation(gr)
                                if spl[1] != "":
                                    cl.sendText(gr,spl[1])
                                cl.leaveGroup(gr)
                            except:
                                pass
                        cl.sendText(msg.to,"สำเร็จแล้ว")
                elif ".tx " in msg.text.lower():
                    spl = re.split(".tx ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        cl.kedapkedip(msg.to,spl[1])
                elif ".name " in msg.text.lower():
                    spl = re.split(".name ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = cl.getProfile()
                        prof.displayName = spl[1]
                        cl.updateProfile(prof)
                        cl.sendText(msg.to,"สำเร็จแล้ว")
                elif ".nmx " in msg.text.lower():
                    spl = re.split(".nmx ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = cl.getProfile()
                        prof.displayName = cl.nmxstring(spl[1])
                        cl.updateProfile(prof)
                        cl.sendText(msg.to,"สำเร็จแล้ว")
                elif ".join " in msg.text.lower():
                    spl = re.split(".join ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            gid = spl[1].split(" ")[0]
                            ticket = spl[1].split(" ")[1].replace("line://ti/g/","") if "line://ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1].replace("http://line.me/R/ti/g/","") if "http://line.me/R/ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1]
                            cl.acceptGroupInvitationByTicket(gid,ticket)
                        except Exception as e:
                            cl.sendText(msg.to,str(e))
                elif msg.text.lower() == ".tyfehelperlogin":
                    if TyfeLogged:
                        if not TyfeHelperLogged:
                            lgncall = msg.to
                            lgnhident = 0
                            if add1ftoken == "":
                                add1ftoken = LINE(appName=0,logNum=2,callback=helperlogincall).authToken
                            if add1stoken == "":
                                add1stoken = LINE(appName=1,logNum=2,callback=helperlogincall).authToken
                            aa.nxtQRLogin(ftoken=add1ftoken,stoken=add1stoken,callback=helperlogincall)
                            aa.loginResult(ftoken=add1ftoken,stoken=add1stoken)
                            add1ftoken = add1stoken = ""
                            helper1 = aa.getProfile().mid
                            lgnhident = 1
                            if add2ftoken == "":
                                add2ftoken = LINE(appName=0,logNum=3,callback=helperlogincall).authToken
                            if add2stoken == "":
                                add2stoken = LINE(appName=1,logNum=3,callback=helperlogincall).authToken
                            ab.nxtQRLogin(ftoken=add2ftoken,stoken=add2stoken,callback=helperlogincall)
                            ab.loginResult(ftoken=add2ftoken,stoken=add2stoken)
                            add2ftoken = add2stoken = ""
                            helper2 = ab.getProfile().mid
                            lgnhident = 2
                            if add3ftoken == "":
                                add3ftoken = LINE(appName=0,logNum=4,callback=helperlogincall).authToken
                            if add3stoken == "":
                                add3stoken = LINE(appName=1,logNum=4,callback=helperlogincall).authToken
                            ac.nxtQRLogin(ftoken=add3ftoken,stoken=add3stoken,callback=helperlogincall)
                            ac.loginResult(ftoken=add3ftoken,stoken=add3stoken)
                            add3ftoken = add3stoken = ""
                            helper3 = ac.getProfile().mid
                            for i in banned:
                                try:
                                    banned[i].remove(helper1)
                                except:
                                    pass
                            for i in tadmin:
                                try:
                                    tadmin[i].remove(helper1)
                                except:
                                    pass
                            for i in banned:
                                try:
                                    banned[i].remove(helper2)
                                except:
                                    pass
                            for i in tadmin:
                                try:
                                    tadmin[i].remove(helper2)
                                except:
                                    pass
                            for i in banned:
                                try:
                                    banned[i].remove(helper3)
                                except:
                                    pass
                            for i in tadmin:
                                try:
                                    tadmin[i].remove(helper3)
                                except:
                                    pass
                            TyfeHelperLogged = True
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            aa.sendText(user1,"ล็อกอินสำเร็จ Tyfe Helper พร้อมใช้งานแล้ว (｀・ω・´)"+tm)
                            ab.sendText(user1,"ล็อกอินสำเร็จ Tyfe Helper พร้อมใช้งานแล้ว (｀・ω・´)"+tm)
                            ac.sendText(user1,"ล็อกอินสำเร็จ Tyfe Helper พร้อมใช้งานแล้ว (｀・ω・´)"+tm)
                        else:
                            cl.sendText(msg.to,"Tyfe Helper ได้ทำการล็อกอินไปแล้ว")
                    else:
                        cl.sendText(msg.to,"Tyfe ยังไม่ได้ล็อกอิน")
                elif msg.text.lower() == ".tyfehelperlogout":
                    if TyfeHelperLogged:
                        lgtname = "[ERROR]"
                        try:
                            lgtname = aa.getProfile().displayName
                        except:
                            pass
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        try:
                            aa.sendText(user1,"กำลังล็อกเอ้าท์ (｀・ω・´)"+tm)
                        except:
                            pass
                        helper1 = ""
                        aa = None
                        aa = TyfeAPI.LINE()
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"[%H:%M:%S] ")
                        print(nowT+lgtname+" logged out ( Close connection )\n")
                        lgtname = "[ERROR]"
                        try:
                            lgtname = ab.getProfile().displayName
                        except:
                            pass
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        try:
                            ab.sendText(user1,"กำลังล็อกเอ้าท์ (｀・ω・´)"+tm)
                        except:
                            pass
                        helper2 = ""
                        ab = None
                        ab = TyfeAPI.LINE()
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"[%H:%M:%S] ")
                        print(nowT+lgtname+" logged out ( Close connection )\n")
                        lgtname = "[ERROR]"
                        try:
                            lgtname = ac.getProfile().displayName
                        except:
                            pass
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        try:
                            ac.sendText(user1,"กำลังล็อกเอ้าท์ (｀・ω・´)"+tm)
                        except:
                            pass
                        helper3 = ""
                        ac = None
                        ac = TyfeAPI.LINE()
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"[%H:%M:%S] ")
                        print(nowT+lgtname+" logged out ( Close connection )\n")
                        TyfeHelperLogged = False
                    else:
                        cl.sendText(msg.to,"Tyfe Helper ยังไม่ได้ล็อกอิน")
                elif msg.text.lower() == ".tyfelogged":
                    if TyfeLogged:
                        msg.contentType = 13
                        msg.text = None
                        msg.contentMetadata = {'mid': user2}
                        cl.sendMessage(msg)
                        if TyfeHelperLogged:
                            time.sleep(0.1)
                            msg.contentMetadata = {'mid': helper1}
                            cl.sendMessage(msg)
                            time.sleep(0.1)
                            msg.contentMetadata = {'mid': helper2}
                            cl.sendMessage(msg)
                            time.sleep(0.1)
                            msg.contentMetadata = {'mid': helper3}
                            cl.sendMessage(msg)
                    else:
                        cl.sendText(msg.to,"Tyfe ยังไม่ได้ล็อกอิน")
                elif msg.text.lower() == ".groupurl":
                    if msg.toType == 2:
                        cl.sendText(msg.to,"http://line.me/R/ti/g/"+str(cl.reissueGroupTicket(msg.to)))
                    else:
                        cl.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น")
                elif ".groupurl " in msg.text.lower():
                    spl = re.split(".groupurl ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            cl.sendText(msg.to,"http://line.me/R/ti/g/"+str(cl.reissueGroupTicket(spl[1])))
                        except Exception as e:
                            cl.sendText(msg.to,"พบข้อผิดพลาด (เหตุผล \""+e.reason+"\")")
                elif msg.text.lower() == ".uptime":
                    cl.sendText(msg.to,(str(datetime.datetime.now() - start_runtime)[:-7].split(" days, ")[0]+" วัน "+str(datetime.datetime.now() - start_runtime)[:-7].split(" days, ")[1].split(":")[0]+" ชั่วโมง " if "days" in str(datetime.datetime.now() - start_runtime) else str(datetime.datetime.now() - start_runtime)[:-7].split(" day, ")[0]+" วัน "+str(datetime.datetime.now() - start_runtime)[:-7].split(" day, ")[1].split(":")[0]+" ชั่วโมง " if "day" in str(datetime.datetime.now() - start_runtime) else str(datetime.datetime.now() - start_runtime)[:-7].split(":")[0]+" ชั่วโมง ")+str(datetime.datetime.now() - start_runtime)[:-7].split(":")[1]+" นาที "+str(datetime.datetime.now() - start_runtime)[:-7].split(":")[2]+" วินาที")
                elif ".sh " in msg.text.lower():
                    spl = re.split(".sh ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            cl.sendText(msg.to,subprocess.getoutput(spl[1]))
                        except:
                            pass
                elif ".jfset " in msg.text.lower():
                    spl = re.split(".jfset ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            del spl[0]
                            tparam = spl[0].split(" ")
                            join_delay = float(tparam[len(tparam)-2])
                            del tparam[len(tparam)-2]
                            join_time = int(tparam[len(tparam)-1])
                            del tparam[len(tparam)-1]
                            jfkeyword = " ".join(tparam)
                            cl.sendText(msg.to,"ตั้งค่าสำเร็จแล้ว")
                        except:
                            cl.sendText(msg.to,"พบข้อผิดพลาด")
                elif msg.text.lower() == ".urlstatus":
                    if msg.toType == 2:
                        x = cl.getGroup(msg.to)
                        if x.preventJoinByTicket:
                            cl.sendText(msg.to,"URL ปิดอยู่")
                        else:
                            cl.sendText(msg.to,"URL เปิดอยู่")
                    else:
                        cl.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น")
                elif msg.text.lower() == ".toggleurl":
                    if msg.toType == 2:
                        x = cl.getGroup(msg.to)
                        x.preventJoinByTicket = not x.preventJoinByTicket
                        cl.updateGroup(x)
                    else:
                        cl.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น")
                elif ".tyfeidjoin " in msg.text.lower():
                    spl = re.split(".tyfeidjoin ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        if TyfeLogged:
                            gid = spl[1]
                            x = cl.getGroup(gid)
                            if user2 not in [i.mid for i in x.members]:
                                defclose = False
                                if x.preventJoinByTicket == False:
                                    ticket = cl.reissueGroupTicket(gid)
                                    kk.acceptGroupInvitationByTicket(gid,ticket)
                                    if TyfeHelperLogged:
                                        aa.acceptGroupInvitationByTicket(gid,ticket)
                                        ab.acceptGroupInvitationByTicket(gid,ticket)
                                        ac.acceptGroupInvitationByTicket(gid,ticket)
                                    defclose = False
                                else:
                                    sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                                    if sirilist == []:
                                        x.preventJoinByTicket = False
                                        cl.updateGroup(x)
                                        ticket = cl.reissueGroupTicket(gid)
                                        kk.acceptGroupInvitationByTicket(gid,ticket)
                                        if TyfeHelperLogged:
                                            aa.acceptGroupInvitationByTicket(gid,ticket)
                                            ab.acceptGroupInvitationByTicket(gid,ticket)
                                            ac.acceptGroupInvitationByTicket(gid,ticket)
                                        defclose = True
                                    else:
                                        cl.inviteIntoGroup(gid,[user2])
                                if defclose:
                                    x.preventJoinByTicket = True
                                    cl.updateGroup(x)
                            else:
                                cl.sendText(msg.to,"Tyfe อยู่ในกลุ่มอยู่แล้ว")
                        else:
                            cl.sendText(msg.to,"Tyfe ยังไม่ได้ล็อคอิน")
                elif ".tyfeidqrjoin " in msg.text.lower():
                    spl = re.split(".tyfeidqrjoin ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        gid = spl[1]
                        if TyfeLogged:
                            x = cl.getGroup(gid)
                            if user2 not in [i.mid for i in x.members]:
                                if x.preventJoinByTicket == False:
                                    ticket = cl.reissueGroupTicket(gid)
                                    kk.acceptGroupInvitationByTicket(gid,ticket)
                                    if TyfeHelperLogged:
                                        aa.acceptGroupInvitationByTicket(gid,ticket)
                                        ab.acceptGroupInvitationByTicket(gid,ticket)
                                        ac.acceptGroupInvitationByTicket(gid,ticket)
                                else:
                                    x.preventJoinByTicket = False
                                    cl.updateGroup(x)
                                    ticket = cl.reissueGroupTicket(gid)
                                    kk.acceptGroupInvitationByTicket(gid,ticket)
                                    if TyfeHelperLogged:
                                        aa.acceptGroupInvitationByTicket(gid,ticket)
                                        ab.acceptGroupInvitationByTicket(gid,ticket)
                                        ac.acceptGroupInvitationByTicket(gid,ticket)
                                    x.preventJoinByTicket = True
                                    cl.updateGroup(x)
                                now2 = datetime.datetime.now()
                                nowT = datetime.datetime.strftime(now2,"%H")
                                nowM = datetime.datetime.strftime(now2,"%M")
                                nowS = datetime.datetime.strftime(now2,"%S")
                                tm = "\n\n"+nowT+":"+nowM+":"+nowS
                                kk.sendText(gid,"Tyfe พร้อมใช้งานแล้ว (｀・ω・´)"+tm)
                            else:
                                cl.sendText(msg.to,"Tyfe อยู่ในกลุ่มอยู่แล้ว")
                        else:
                            cl.sendText(msg.to,"Tyfe ยังไม่ได้ล็อกอิน")
                elif msg.text.lower() == ".getjoined":
                    cl.sendText(msg.to,"กรุณารอสักครู่ ใจเย็นๆ")
                    all = cl.getGroupIdsJoined()
                    text = ""
                    cnt = 0
                    for i in all:
                        text += cl.getGroup(i).name + "\n" + i + "\n\n"
                        cnt += 1
                        if cnt == 10:
                            cl.sendText(msg.to,text[:-2])
                            text = ""
                            cnt = 0
                    cl.sendText(msg.to,text[:-2])
                    cnt = 0
                elif ".tyfeleave " in msg.text.lower():
                    spl = re.split(".tyfeleave ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        if TyfeLogged:
                            try:
                                kk.leaveGroup(spl[1])
                                if TyfeHelperLogged:
                                    aa.leaveGroup(spl[1])
                                    ab.leaveGroup(spl[1])
                                    ac.leaveGroup(spl[1])
                            except Exception as e:
                                cl.sendText(msg.to,str(e))
                        else:
                            cl.sendText(msg.to,"Tyfe ยังไม่ได้ล็อกอิน")
                elif msg.text.lower() == ".joindetail on":
                    if TyfeLogged:
                        if not joinDetail:
                            joinDetail = True
                            cl.sendText(msg.to,"เปิดแล้ว")
                        else:
                            cl.sendText(msg.to,"เปิดอยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"Tyfe ยังไม่ได้ล็อกอิน")
                elif msg.text.lower() == ".joindetail off":
                    if TyfeLogged:
                        if joinDetail:
                            joinDetail = False
                            cl.sendText(msg.to,"ปิดแล้ว")
                        else:
                            cl.sendText(msg.to,"ปิดอยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"Tyfe ยังไม่ได้ล็อกอิน")
                elif msg.text.lower() == ".help":
                    cl.sendText(msg.to,userhelp)
                elif msg.text.lower() == ".tyfefollow on":
                    if not tyfeFollow:
                        tyfeFollow = True
                        cl.sendText(msg.to,"เปิดแล้ว")
                    else:
                        cl.sendText(msg.to,"เปิดอยู่แล้ว")
                elif msg.text.lower() == ".tyfefollow off":
                    if tyfeFollow:
                        tyfeFollow = False
                        cl.sendText(msg.to,"ปิดแล้ว")
                    else:
                        cl.sendText(msg.to,"ปิดอยู่แล้ว")
                elif msg.text.lower() in [".removeall",".removeall "]:
                    if TyfeLogged:
                        gs = cl.getGroup(msg.to)
                        if not (set([user1,user2,helper1,helper2,helper3]).issubset([i.mid for i in gs.members])):
                            defclose = False
                            if gs.preventJoinByTicket == False:
                                ticket = cl.reissueGroupTicket(msg.to)
                                if user2 not in [i.mid for i in gs.members]:
                                    kk.acceptGroupInvitationByTicket(msg.to,ticket)
                                if TyfeHelperLogged:
                                    if not (set([helper1,helper2,helper3]).issubset([i.mid for i in gs.members])):
                                        aa.acceptGroupInvitationByTicket(msg.to,ticket)
                                        ab.acceptGroupInvitationByTicket(msg.to,ticket)
                                        ac.acceptGroupInvitationByTicket(msg.to,ticket)
                                defclose = False
                            else:
                                sirilist = [i.mid for i in gs.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                                if sirilist == []:
                                    gs.preventJoinByTicket = False
                                    cl.updateGroup(gs)
                                    ticket = cl.reissueGroupTicket(msg.to)
                                    if user2 not in [i.mid for i in gs.members]:
                                        kk.acceptGroupInvitationByTicket(msg.to,ticket)
                                    if TyfeHelperLogged:
                                        if not (set([helper1,helper2,helper3]).issubset([i.mid for i in gs.members])):
                                            aa.acceptGroupInvitationByTicket(msg.to,ticket)
                                            ab.acceptGroupInvitationByTicket(msg.to,ticket)
                                            ac.acceptGroupInvitationByTicket(msg.to,ticket)
                                    defclose = True
                                else:
                                    if user2 not in [i.mid for i in gs.members]:
                                        cl.inviteIntoGroup(msg.to,[user2])
                                    if TyfeHelperLogged:
                                        if not (set([helper1,helper2,helper3]).issubset([i.mid for i in gs.members])):
                                            cl.inviteIntoGroup(msg.to,[helper1,helper2,helper3])
                                    if user2 not in [i.mid for i in gs.members]:
                                        kk.acceptGroupInvitation(msg.to)
                                    if TyfeHelperLogged:
                                        if not (set([helper1,helper2,helper3]).issubset([i.mid for i in gs.members])):
                                            aa.acceptGroupInvitation(msg.to)
                                            ab.acceptGroupInvitation(msg.to)
                                            ac.acceptGroupInvitation(msg.to)
                            if defclose:
                                gs.preventJoinByTicket = True
                                cl.updateGroup(gs)
                        sirilist = [i.mid for i in gs.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                        if sirilist == []:
                            groupParam = msg.to
                            targets = [i.mid for i in gs.members if i.mid not in [user1,user2,helper1,helper2,helper3]]
                            if targets == []:
                                kk.sendText(msg.to,"Not found.")
                            else:
                                try:
                                    p = Pool(len(targets))
                                    p.map(kickBan,targets)
                                    p.close()
                                except:
                                    p.close()
                                    allmid = aa.getGroup(msg.to).members
                                    targets = [i.mid for i in allmid if i.mid not in [user1,user2,helper1,helper2,helper3]]
                                    try:
                                        p = Pool(len(targets))
                                        p.map(h1kickBan,targets)
                                        p.close()
                                    except:
                                        p.close()
                                        allmid = ab.getGroup(msg.to).members
                                        targets = [i.mid for i in allmid if i.mid not in [user1,user2,helper1,helper2,helper3]]
                                        try:
                                            p = Pool(len(targets))
                                            p.map(h2kickBan,targets)
                                            p.close()
                                        except:
                                            p.close()
                                            allmid = ac.getGroup(msg.to).members
                                            targets = [i.mid for i in allmid if i.mid not in [user1,user2,helper1,helper2,helper3]]
                                            try:
                                                p = Pool(len(targets))
                                                p.map(h3kickBan,targets)
                                                p.close()
                                            except:
                                                p.close()
                                try:
                                    gs = ac.getGroup(msg.to)
                                    gMembMids = [contact.mid for contact in gs.invitee]
                                    for i in gMembMids:
                                        ac.cancelGroupInvitation(msg.to,[i])
                                except Exception as e:
                                    p.close()
                                    print(e)
                        else:
                            groupParam = msg.to
                            try:
                                p = Pool(len(sirilist))
                                p.map(kickBan,sirilist)
                                p.close()
                            except:
                                p.close()
                            gs = kk.getGroup(msg.to)
                            targets = [i.mid for i in gs.members if i.mid not in [user1,user2,helper1,helper2,helper3]]
                            if targets == []:
                                kk.sendText(msg.to,"Not found.")
                            else:
                                try:
                                    p = Pool(len(targets))
                                    p.map(kickBan,targets)
                                    p.close()
                                except:
                                    p.close()
                                    allmid = aa.getGroup(msg.to).members
                                    targets = [i.mid for i in allmid if i.mid not in [user1,user2,helper1,helper2,helper3]]
                                    try:
                                        p = Pool(len(targets))
                                        p.map(h1kickBan,targets)
                                        p.close()
                                    except:
                                        p.close()
                                        allmid = ab.getGroup(msg.to).members
                                        targets = [i.mid for i in allmid if i.mid not in [user1,user2,helper1,helper2,helper3]]
                                        try:
                                            p = Pool(len(targets))
                                            p.map(h2kickBan,targets)
                                            p.close()
                                        except:
                                            p.close()
                                            allmid = ac.getGroup(msg.to).members
                                            targets = [i.mid for i in allmid if i.mid not in [user1,user2,helper1,helper2,helper3]]
                                            try:
                                                p = Pool(len(targets))
                                                p.map(h3kickBan,targets)
                                                p.close()
                                            except:
                                                p.close()
                                try:
                                    gs = ac.getGroup(msg.to)
                                    gMembMids = [contact.mid for contact in gs.invitee]
                                    for i in gMembMids:
                                        ac.cancelGroupInvitation(msg.to,[i])
                                except Exception as e:
                                    p.close()
                                    print(e)
                        kk.leaveGroup(msg.to)
                        if TyfeHelperLogged:
                            aa.leaveGroup(msg.to)
                            ab.leaveGroup(msg.to)
                            ac.leaveGroup(msg.to)
                    else:
                        cl.sendText(msg.to,"Tyfe ยังไม่ได้ล็อกอิน")
                elif ".removeall " in msg.text.lower():
                    spl = re.split(".removeall ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        if TyfeLogged:
                            gs = cl.getGroup(spl[1])
                            if not (set([user1,user2,helper1,helper2,helper3]).issubset([i.mid for i in gs.members])):
                                defclose = False
                                if gs.preventJoinByTicket == False:
                                    ticket = cl.reissueGroupTicket(spl[1])
                                    if user2 not in [i.mid for i in gs.members]:
                                        kk.acceptGroupInvitationByTicket(spl[1],ticket)
                                    if TyfeHelperLogged:
                                        if not (set([helper1,helper2,helper3]).issubset([i.mid for i in gs.members])):
                                            aa.acceptGroupInvitationByTicket(spl[1],ticket)
                                            ab.acceptGroupInvitationByTicket(spl[1],ticket)
                                            ac.acceptGroupInvitationByTicket(spl[1],ticket)
                                    defclose = False
                                else:
                                    sirilist = [i.mid for i in gs.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                                    if sirilist == []:
                                        gs.preventJoinByTicket = False
                                        cl.updateGroup(gs)
                                        ticket = cl.reissueGroupTicket(spl[1])
                                        if user2 not in [i.mid for i in gs.members]:
                                            kk.acceptGroupInvitationByTicket(spl[1],ticket)
                                        if TyfeHelperLogged:
                                            if not (set([helper1,helper2,helper3]).issubset([i.mid for i in gs.members])):
                                                aa.acceptGroupInvitationByTicket(spl[1],ticket)
                                                ab.acceptGroupInvitationByTicket(spl[1],ticket)
                                                ac.acceptGroupInvitationByTicket(spl[1],ticket)
                                        defclose = True
                                    else:
                                        if user2 not in [i.mid for i in gs.members]:
                                            cl.inviteIntoGroup(spl[1],[user2])
                                        if TyfeHelperLogged:
                                            if not (set([helper1,helper2,helper3]).issubset([i.mid for i in gs.members])):
                                                cl.inviteIntoGroup(spl[1],[helper1,helper2,helper3])
                                        if user2 not in [i.mid for i in gs.members]:
                                            kk.acceptGroupInvitation(spl[1])
                                        if TyfeHelperLogged:
                                            if not (set([helper1,helper2,helper3]).issubset([i.mid for i in gs.members])):
                                                aa.acceptGroupInvitation(spl[1])
                                                ab.acceptGroupInvitation(spl[1])
                                                ac.acceptGroupInvitation(spl[1])
                                if defclose:
                                    gs.preventJoinByTicket = True
                                    cl.updateGroup(gs)
                            sirilist = [i.mid for i in gs.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                            if sirilist == []:
                                groupParam = spl[1]
                                targets = [i.mid for i in gs.members if i.mid not in [user1,user2,helper1,helper2,helper3]]
                                if targets == []:
                                    kk.sendText(spl[1],"Not found.")
                                else:
                                    try:
                                        p = Pool(len(targets))
                                        p.map(kickBan,targets)
                                        p.close()
                                    except:
                                        p.close()
                                        allmid = aa.getGroup(spl[1]).members
                                        targets = [i.mid for i in allmid if i.mid not in [user1,user2,helper1,helper2,helper3]]
                                        try:
                                            p = Pool(len(targets))
                                            p.map(h1kickBan,targets)
                                            p.close()
                                        except:
                                            p.close()
                                            allmid = ab.getGroup(spl[1]).members
                                            targets = [i.mid for i in allmid if i.mid not in [user1,user2,helper1,helper2,helper3]]
                                            try:
                                                p = Pool(len(targets))
                                                p.map(h2kickBan,targets)
                                                p.close()
                                            except:
                                                p.close()
                                                allmid = ac.getGroup(spl[1]).members
                                                targets = [i.mid for i in allmid if i.mid not in [user1,user2,helper1,helper2,helper3]]
                                                try:
                                                    p = Pool(len(targets))
                                                    p.map(h3kickBan,targets)
                                                    p.close()
                                                except:
                                                    p.close()
                                    try:
                                        gs = ac.getGroup(spl[1])
                                        gMembMids = [contact.mid for contact in gs.invitee]
                                        for i in gMembMids:
                                            ac.cancelGroupInvitation(spl[1],[i])
                                    except Exception as e:
                                        p.close()
                                        print(e)
                            else:
                                groupParam = spl[1]
                                try:
                                    p = Pool(len(sirilist))
                                    p.map(kickBan,sirilist)
                                    p.close()
                                except:
                                    p.close()
                                gs = kk.getGroup(spl[1])
                                targets = [i.mid for i in gs.members if i.mid not in [user1,user2,helper1,helper2,helper3]]
                                if targets == []:
                                    kk.sendText(spl[1],"Not found.")
                                else:
                                    try:
                                        p = Pool(len(targets))
                                        p.map(kickBan,targets)
                                        p.close()
                                    except:
                                        p.close()
                                        allmid = aa.getGroup(spl[1]).members
                                        targets = [i.mid for i in allmid if i.mid not in [user1,user2,helper1,helper2,helper3]]
                                        try:
                                            p = Pool(len(targets))
                                            p.map(h1kickBan,targets)
                                            p.close()
                                        except:
                                            p.close()
                                            allmid = ab.getGroup(spl[1]).members
                                            targets = [i.mid for i in allmid if i.mid not in [user1,user2,helper1,helper2,helper3]]
                                            try:
                                                p = Pool(len(targets))
                                                p.map(h2kickBan,targets)
                                                p.close()
                                            except:
                                                p.close()
                                                allmid = ac.getGroup(spl[1]).members
                                                targets = [i.mid for i in allmid if i.mid not in [user1,user2,helper1,helper2,helper3]]
                                                try:
                                                    p = Pool(len(targets))
                                                    p.map(h3kickBan,targets)
                                                    p.close()
                                                except:
                                                    p.close()
                                    try:
                                        gs = ac.getGroup(spl[1])
                                        gMembMids = [contact.mid for contact in gs.invitee]
                                        for i in gMembMids:
                                            ac.cancelGroupInvitation(spl[1],[i])
                                    except Exception as e:
                                        p.close()
                                        print(e)
                            kk.leaveGroup(spl[1])
                            if TyfeHelperLogged:
                                aa.leaveGroup(spl[1])
                                ab.leaveGroup(spl[1])
                                ac.leaveGroup(spl[1])
                        else:
                            cl.sendText(msg.to,"Tyfe ยังไม่ได้ล็อกอิน")
                elif ".info " in msg.text.lower():
                    spl = re.split(".info ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            uid = prov[i]["M"]
                            userData = cl.getContact(uid)
                            try:
                                cl.sendImageWithUrl(msg.to,"http://dl.profile.line.naver.jp/"+userData.pictureStatus)
                            except:
                                pass
                            cl.sendText(msg.to,"ชื่อที่แสดง: "+userData.displayName)
                            cl.sendText(msg.to,"ข้อความสเตตัส:\n"+userData.statusMessage)
                            cl.sendText(msg.to,"ไอดีบัญชี: "+userData.mid)
                            msg.contentType = 13
                            msg.text = None
                            msg.contentMetadata = {'mid': userData.mid}
                            cl.sendMessage(msg)
                elif msg.text.lower() == ".autodeny off":
                    autoDeny = -1
                    cl.sendText(msg.to,"ตั้งค่าสำเร็จแล้ว")
                elif msg.text.lower().startswith(".autodeny "):
                    try:
                        autoDeny = int(msg.text[len(".autodeny "):])
                        cl.sendText(msg.to,"ตั้งค่าสำเร็จแล้ว")
                    except:
                        cl.sendText(msg.to,"พบข้อผิดพลาด")
                elif msg.text.lower() == ".checkmention":
                    if msg.to in mentmedat and mentmedat[msg.to] != []:
                        text = ""
                        for data in mentmedat[msg.to]:
                            try:
                                conname = cl.getContact(data["tfrom"]).displayName
                            except:
                                conname = "[DELETED]"
                            text += "[%s] %s\nline://nv/chatMsg?chatId=%s&messageId=%s\n\n" % (data["ttime"],conname,msg.to,data["tid"])
                        text = text[:-2]
                        try:
                            cl.sendText(msg.to,text)
                        except Exception as e:
                            cl.sendText(msg.to,str(e))
                        del mentmedat[msg.to]
                    else:
                        cl.sendText(msg.to,"ไม่มีการกล่าวถึงก่อนหน้านี้")
                elif msg.text.lower() == ".resetmention":
                    dkey = mentmedat.pop(msg.to,None)
                    cl.sendText(msg.to,"รีเซ็ตข้อมูลการกล่าวถึงเรียบร้อยแล้ว")
                elif msg.text.lower() == ".resetallmention":
                    mentmedat = {}
                    cl.sendText(msg.to,"รีเซ็ตข้อมูลการกล่าวถึงทั้งหมดแล้ว")
                elif "|!" in msg.text:
                    spl = msg.text.split("|!")
                    if spl[len(spl)-1] == "":
                        cl.sendText(msg.to,"กดที่นี่เพื่อเขย่าข้อความด้านบน:\nline://nv/chatMsg?chatId="+msg.to+"&messageId="+msg.id)
                elif msg.text == jfkeyword:
                    if TyfeLogged:
                        if msg.toType == 2:
                            x = cl.getGroup(msg.to)
                            alr = user2 in [i.mid for i in x.members]
                            defClose = False
                            if x.preventJoinByTicket:
                                x.preventJoinByTicket = False
                                cl.updateGroup(x)
                                defClose = True
                            ticket = cl.reissueGroupTicket(msg.to)
                            for i in range(join_time):
                                kk.leaveGroup(msg.to)
                                if TyfeHelperLogged:
                                    aa.leaveGroup(msg.to)
                                    ab.leaveGroup(msg.to)
                                    ac.leaveGroup(msg.to)
                                kk.acceptGroupInvitationByTicket(msg.to,ticket)
                                time.sleep(join_delay)
                                if TyfeHelperLogged:
                                    aa.acceptGroupInvitationByTicket(msg.to,ticket)
                                    time.sleep(join_delay)
                                    ab.acceptGroupInvitationByTicket(msg.to,ticket)
                                    time.sleep(join_delay)
                                    ac.acceptGroupInvitationByTicket(msg.to,ticket)
                                    time.sleep(join_delay)
                            if not alr:
                                kk.leaveGroup(msg.to)
                                if TyfeHelperLogged:
                                    aa.leaveGroup(msg.to)
                                    ab.leaveGroup(msg.to)
                                    ac.leaveGroup(msg.to)
                            if defClose:
                                x.preventJoinByTicket = True
                                cl.updateGroup(x)
                        else:
                            cl.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น")
                    else:
                        cl.sendText(msg.to,"Tyfe ยังไม่ได้ล็อกอิน")
            except AttributeError:
                pass
            except Exception as e:
                print(e)




    except Exception as e:
        print(e)

Rapid2To = ""

def Rapid2Say(mtosay):
    kk.sendText(Rapid2To,mtosay)

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

class BFGenerator(object):
    """Takes a string and generates a brainfuck code that, when run,
       prints the original string to the brainfuck interpreter standard
       output"""
      
    def text_to_brainfuck(self, data):
        """Converts a string into a BF program. Returns the BF code"""
        glyphs = len(set([c for c in data]))
        number_of_bins = max(max([ord(c) for c in data]) // glyphs,1)
        # Create an array that emulates the BF memory array as if the
        # code we are generating was being executed. Initialize the
        # array by creating as many elements as different glyphs in
        # the original string. Then each "bin" gets an initial value
        # which is determined by the actual message.
        # FIXME: I can see how this can become a problem for languages
        # that don't use a phonetic alphabet, such as Chinese.
        bins = [(i + 1) * number_of_bins for i in range(glyphs)]
        code="+" * number_of_bins + "["
        code+="".join([">"+("+"*(i+1)) for i in range(1,glyphs)])
        code+="<"*(glyphs-1) + "-]"
        code+="+" * number_of_bins
        # For each character in the original message, find the position
        # that holds the value closest to the character's ordinal, then
        # generate the BF code to move the memory pointer to that memory
        # position, get the value of that memory position to be equal
        # to the ordinal of the character and print it (i.e. print the
        # character).
        current_bin=0
        for char in data:
            new_bin=[abs(ord(char)-b)
                     for b in bins].index(min([abs(ord(char)-b)
                                               for b in bins]))
            appending_character=""
            if new_bin-current_bin>0:
                appending_character=">"
            else:
                appending_character="<"
            code+=appending_character * abs(new_bin-current_bin)
            if ord(char)-bins[new_bin]>0:
                appending_character="+"
            else:
                appending_character="-"
            code+=(appending_character * abs( ord(char)-bins[new_bin])) +"."
            current_bin=new_bin
            bins[new_bin]=ord(char)
        return code

def run(src):
    c = [0] * 30000
    p = 0
    loop = []
    rv = []
    ts = list(src)
    l = len(ts)
    i = 0;
    while i < l:
        t = ts[i]
        if t == ">": p += 1
        elif t == "<": p -= 1
        elif t == "+": c[p] += 1
        elif t == "-": c[p] -= 1
        elif t == ".": rv.append(chr(c[p]))
        elif t == ",": pass
        elif t == "[":
            if c[p] == 0:
                while ts[i] != "]": i += 1
                loop.pop()
            else:
                loop.append(i - 1)
        elif t == "]": i = loop[-1]
        i += 1

    return "".join(rv)

lmimic = ""

groupParam = ""

def kickBan(targ):
    kk.kickoutFromGroup(groupParam,[targ])

def h1kickBan(targ):
    aa.kickoutFromGroup(groupParam,[targ])

def h2kickBan(targ):
    ab.kickoutFromGroup(groupParam,[targ])

def h3kickBan(targ):
    ac.kickoutFromGroup(groupParam,[targ])

def setKick(to,targ,trig):
    kdone = "No"
    if targ != user2:
        try:
            kdone= kk.kickoutFromGroup(to,[targ])
        except:
            pass
    if kdone != None:
        if TyfeHelperLogged:
            kmid = [helper1,helper2,helper3]
            kact = [aa,ab,ac]
            for i in range(3):
                if kdone != None:
                    if kmid[i] != targ:
                        try:
                            kdone = kact[i].kickoutFromGroup(to,[targ])
                        except:
                            pass
    if kdone != None:
        if targ != user1:
            try:
                cl.kickoutFromGroup(to,[targ])
            except:
                pass
    if trig:
        x = kk.getGroup(to)
        sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
        if sirilist == []:
            if not x.preventJoinByTicket:
                x.preventJoinByTicket = True
                kk.updateGroup(x)
            if to in preventBlockURL:
                preventBlockURL.remove(to)
    

def sendSMS(pnum,mes,capt,msg):
    now2 = datetime.datetime.now()
    nowT = datetime.datetime.strftime(now2,"%H")
    nowM = datetime.datetime.strftime(now2,"%M")
    nowS = datetime.datetime.strftime(now2,"%S")
    tm = "\n\n"+nowT+":"+nowM+":"+nowS
    if msg.toType != 0:
        kk.sendText(msg.to,"กำลังดำเนินการ กรุณารอสักครู่ (｀・ω・´)"+tm)
    else:
        kk.sendText(msg.from_,"กำลังดำเนินการ กรุณารอสักครู่ (｀・ω・´)"+tm)
    resid = json.loads(requests.get("http://2captcha.com/in.php?key="+capt+"&method=userrecaptcha&googlekey=6LdQAAMTAAAAAPrS4iujKYUrHtNB9dv1HFsC7jpj&pageurl=https://globfone.com/send-text/&json=1").content.decode("ascii"))["request"]
    if resid != "ERROR_WRONG_USER_KEY" and resid != "ERROR_ZERO_BALANCE":
        while True:
            tokenresp = json.loads(requests.get("http://2captcha.com/res.php?key="+capt+"&action=get&id="+resid+"&json=1").content.decode("ascii"))
            time.sleep(5)
            if tokenresp["status"] == 1:
                token = tokenresp["request"]
                payload = {
                    "action":"sendSms",
                    "g-recaptcha-response":token,
                    "number":pnum,
                    "message":mes
                }
                resp = requests.post("https://globfone.com/wp-admin/admin-ajax.php",data=payload)
                if "errorMessage" in json.loads(resp.content.decode("ascii")) and json.loads(resp.content.decode("ascii"))["errorMessage"] == "Day limit is 5 smses":
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"จำนวนการส่ง SMS ต่อวันคือ 5 ข้อความ กรุณาลองใหม่อีกครั้งในภายหลัง (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"จำนวนการส่ง SMS ต่อวันคือ 5 ข้อความ กรุณาลองใหม่อีกครั้งในภายหลัง (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)"+tm)
                break
            else:
                if tokenresp["request"] == "ERROR_CAPTCHA_UNSOLVABLE":
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"ไม่สามารถแก้ปัญหา Captcha กรุณาลองใหม่อีกครั้ง (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"ไม่สามารถแก้ปัญหา Captcha กรุณาลองใหม่อีกครั้ง (｀・ω・´)"+tm)
                    break
    elif resid == "ERROR_WRONG_USER_KEY":
        now2 = datetime.datetime.now()
        nowT = datetime.datetime.strftime(now2,"%H")
        nowM = datetime.datetime.strftime(now2,"%M")
        nowS = datetime.datetime.strftime(now2,"%S")
        tm = "\n\n"+nowT+":"+nowM+":"+nowS
        if msg.toType != 0:
            kk.sendText(msg.to,"Key สำหรับ 2captcha ผิดพลาด (｀・ω・´)"+tm)
        else:
            kk.sendText(msg.from_,"Key สำหรับ 2captcha ผิดพลาด (｀・ω・´)"+tm)
    elif resid == "ERROR_ZERO_BALANCE":
        now2 = datetime.datetime.now()
        nowT = datetime.datetime.strftime(now2,"%H")
        nowM = datetime.datetime.strftime(now2,"%M")
        nowS = datetime.datetime.strftime(now2,"%S")
        tm = "\n\n"+nowT+":"+nowM+":"+nowS
        if msg.toType != 0:
            kk.sendText(msg.to,"ยอดเงินคงเหลือใน 2captcha ไม่เพียงพอสำหรับการดำเนินการ (｀・ω・´)"+tm)
        else:
            kk.sendText(msg.from_,"ยอดเงินคงเหลือใน 2captcha ไม่เพียงพอสำหรับการดำเนินการ (｀・ω・´)"+tm)

waitForContactBan = []
waitForContactUnBan = []
waitForContactAddAdmin = []
waitForContactRemoveAdmin = []

tyfehelp = """คำสั่งควบคุม Tyfe ทั้งหมด:

จัดการแอดมิน:
Tyfe:admin [add/remove] (ADMIN)
Tyfe:admin (ADMIN)
Tyfe:superadmin (ADMIN)

จัดการกลุ่ม:
Tyfe:preventkick [on/off] (ADMIN)
Tyfe:botprotect [on/off] (ADMIN)
Tyfe:blockurl [on/off] (ADMIN)
Tyfe:blockinvitation [on/off] (ADMIN)
Tyfe:ban (ADMIN)
Tyfe:unban (ADMIN)
Tyfe:banlist (ADMIN)
Tyfe:kickban (ADMIN)
Tyfe:unbanall (ADMIN)
Tyfe:remove @ (ADMIN)
Tyfe:bye @ (ADMIN)
Tyfe:set

เช็คคนอ่านแชท:
Tyfe:setreadpoint (ADMIN)
Tyfe:reader (ADMIN)

แปลภาษา:
Tyfe:en-id [ข้อความ]
Tyfe:en-th [ข้อความ]
Tyfe:en-jp [ข้อความ]
Tyfe:id-en [ข้อความ]
Tyfe:id-th [ข้อความ]
Tyfe:id-jp [ข้อความ]
Tyfe:th-en [ข้อความ]
Tyfe:th-id [ข้อความ]
Tyfe:th-jp [ข้อความ]
Tyfe:jp-en [ข้อความ]
Tyfe:jp-id [ข้อความ]
Tyfe:jp-th [ข้อความ]

อื่นๆ:
Tyfe:say [ข้อความ] [จำนวน] (ADMIN)
Tyfe:mentionall (ADMIN)
Tyfe:dub [on/off] (ADMIN)
Tyfe:reinvite (ADMIN)
Tyfe:halt (ADMIN)
Tyfe:uninstall (ADMIN)

Tyfe:google [คีย์เวิร์ด]
Tyfe:freeopenvpn
Tyfe:brainfuck:gen [ข้อความ]
Tyfe:brainfuck:int [รหัส]
Tyfe:ctt [ข้อมูล]
Tyfe:qrcode [ข้อมูล]
Tyfe:talk [ข้อความ]
Tyfe:gac [เบอร์มือถือ]
Tyfe:creator
Tyfe:creatorcheck
Tyfe:version

Tyfe:id (SUPER ADMIN)
Tyfe:post [ข้อความ] (SUPER ADMIN)
Tyfe:denyall [ข้อความ] (SUPER ADMIN)
Tyfe:2captcha:key [Key] (SUPER ADMIN)
Tyfe:sms [เบอร์มือถือ (True)] [ข้อความ] (SUPER ADMIN)
Tyfe:autolike [on/off] (SUPER ADMIN)
Tyfe:autolike:comment [on/off] (SUPER ADMIN)
Tyfe:autolike:comment: [ข้อความ] (SUPER ADMIN)
Tyfe:autolike:type [1-6] (SUPER ADMIN)
Tyfe:mimic @ (SUPER ADMIN)
Tyfe:mimic [on/off] (SUPER ADMIN)
Tyfe:save (SUPER ADMIN)
Tyfe:swap (SUPER ADMIN)
Tyfe:load (SUPER ADMIN)
Tyfe:friendalllogged (SUPER ADMIN)

Tyfe:kickall (SUPER ADMIN)
Helper[1-3]:removesiri (SUPER ADMIN)

Tyfe:forcehalt (CREATOR)"""

tyfeversion = "1.5.7"

def user2script(op):
    global readAlert
    global kickLockList
    global banned
    global tadmin
    global groupParam
    global waitForContactBan
    global waitForContactUnBan
    global autoLikeSetting
    global tyfehelp
    global tyfeversion
    global dublist
    global TyfeHelperLogged
    global preventBlockURL
    global blockInvite
    global procLock
    global captkey
    try:
        #if op.type not in [48,55,25]:
            #print str(op)
            #print "\n\n"
        if op.type == 11:
            if op.param3 == "4":
                if op.param1 not in preventBlockURL:
                    chname = kk.getContact(op.param2).displayName
                    if op.param2 not in [user1,user2,helper1,helper2,helper3] and not (op.param1 in tadmin and op.param2 in tadmin[op.param1]) and not (any(word in chname for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or chname.isdigit()):
                        tmpl = []
                        if op.param1 in banned:
                            tmpl = banned[op.param1]
                        banned[op.param1] = []
                        if op.param2 not in tmpl:
                            banned[op.param1].append(op.param2)
                        if tmpl != []:
                            for oldtarg in tmpl:
                                banned[op.param1].append(oldtarg)
                        setKick(op.param1,op.param2,False)
                        gr = kk.getGroup(op.param1)
                        gr.preventJoinByTicket = not gr.preventJoinByTicket
                        kk.updateGroup(gr)
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(op.param1,"สมาชิกไม่ได้รับอนุญาติให้เปิดหรือปิด URL （´・ω・｀）"+tm)
                        msg = Message()
                        msg.to = op.param1
                        msg.from_ = user2
                        msg.contentType = 13
                        msg.text = None
                        msg.contentMetadata = {'mid': op.param2}
                        kk.sendMessage(msg)
        elif op.type == 13:
            invitor = op.param2
            gotinvite = []
            if "\x1e" in op.param3:
                gotinvite = op.param3.split("\x1e")
            else:
                gotinvite.append(op.param3)
            if (invitor == user1 or op.param1 in tadmin and invitor in tadmin[op.param1]) and user2 in gotinvite:
                kk.acceptGroupInvitation(op.param1)
                x = kk.getGroup(op.param1)
                gmems = [i.mid for i in x.members]
                if not (set([user1,user2,helper1,helper2,helper3]).issubset(gmems)):
                    defclose = False
                    if x.preventJoinByTicket == False:
                        ticket = kk.reissueGroupTicket(op.param1)
                        if user1 not in gmems:
                            cl.acceptGroupInvitationByTicket(op.param1,ticket)
                        if TyfeHelperLogged:
                            if helper1 not in gmems:
                                aa.acceptGroupInvitationByTicket(op.param1,ticket)
                            if helper2 not in gmems:
                                ab.acceptGroupInvitationByTicket(op.param1,ticket)
                            if helper3 not in gmems:
                                ac.acceptGroupInvitationByTicket(op.param1,ticket)
                        defclose = False
                    else:
                        sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                        if sirilist == []:
                            x.preventJoinByTicket = False
                            kk.updateGroup(x)
                            ticket = kk.reissueGroupTicket(op.param1)
                            if user1 not in gmems:
                                cl.acceptGroupInvitationByTicket(op.param1,ticket)
                            if TyfeHelperLogged:
                                if helper1 not in gmems:
                                    aa.acceptGroupInvitationByTicket(op.param1,ticket)
                                if helper2 not in gmems:
                                    ab.acceptGroupInvitationByTicket(op.param1,ticket)
                                if helper3 not in gmems:
                                    ac.acceptGroupInvitationByTicket(op.param1,ticket)
                            defclose = True
                        else:
                            ninv = []
                            nacc = []
                            if user1 not in gmems:
                                ninv.append(user1)
                                nacc.append(cl)
                            if TyfeHelperLogged:
                                if helper1 not in gmems:
                                    ninv.append(helper1)
                                    nacc.append(aa)
                                if helper2 not in gmems:
                                    ninv.append(helper2)
                                    nacc.append(ab)
                                if helper3 not in gmems:
                                    ninv.append(helper3)
                                    nacc.append(ac)
                            kk.inviteIntoGroup(op.param1,ninv)
                            for ie in nacc:
                                ie.acceptGroupInvitation(op.param1)
                    if defclose:
                        x.preventJoinByTicket = True
                        kk.updateGroup(x)
                now2 = datetime.datetime.now()
                nowT = datetime.datetime.strftime(now2,"%H")
                nowM = datetime.datetime.strftime(now2,"%M")
                nowS = datetime.datetime.strftime(now2,"%S")
                tm = "\n\n"+nowT+":"+nowM+":"+nowS
                kk.sendText(op.param1,"Tyfe พร้อมใช้งานแล้ว (｀・ω・´)"+tm)
            elif op.param1 in banned and any(i in gotinvite for i in banned[op.param1]):
                isNotAdmin = False
                if invitor not in [user1,user2,helper1,helper2,helper3] and not (op.param1 in tadmin and invitor in tadmin[op.param1]):
                    isNotAdmin = True
                if isNotAdmin:
                    tmpl = []
                    if op.param1 in banned:
                        tmpl = banned[op.param1]
                    banned[op.param1] = []
                    if op.param2 not in tmpl:
                        banned[op.param1].append(op.param2)
                    if tmpl != []:
                        for oldtarg in tmpl:
                            banned[op.param1].append(oldtarg)
                if isNotAdmin:
                    count = 0
                    for i in gotinvite:
                        if count == 0:
                            kk.cancelGroupInvitation(op.param1,[i])
                            if TyfeHelperLogged:
                                count += 1
                            continue
                        elif count == 1:
                            aa.cancelGroupInvitation(op.param1,[i])
                            count += 1
                            continue
                        elif count == 2:
                            ab.cancelGroupInvitation(op.param1,[i])
                            count += 1
                            continue
                        elif count == 3:
                            ac.cancelGroupInvitation(op.param1,[i])
                            count = 0
                            continue
                else:
                    count = 0
                    for i in banned[op.param1]:
                        if i in gotinvite:
                            if count == 0:
                                kk.cancelGroupInvitation(op.param1,[i])
                                if TyfeHelperLogged:
                                    count += 1
                                continue
                            elif count == 1:
                                aa.cancelGroupInvitation(op.param1,[i])
                                count += 1
                                continue
                            elif count == 2:
                                ab.cancelGroupInvitation(op.param1,[i])
                                count += 1
                                continue
                            elif count == 3:
                                ac.cancelGroupInvitation(op.param1,[i])
                                count = 0
                                continue
                if isNotAdmin:
                    setKick(op.param1,invitor,True)
                now2 = datetime.datetime.now()
                nowT = datetime.datetime.strftime(now2,"%H")
                nowM = datetime.datetime.strftime(now2,"%M")
                nowS = datetime.datetime.strftime(now2,"%S")
                tm = "\n\n"+nowT+":"+nowM+":"+nowS
                kk.sendText(op.param1,"สมาชิกไม่ได้รับอนุญาติให้เชิญสมาชิกที่ถูกแบน （´・ω・｀）"+tm)
            elif op.param1 in blockInvite and invitor not in [user1,helper1,helper2,helper3] and not (op.param1 in tadmin and invitor in tadmin[op.param1]) and not any(i in gotinvite for i in [user1,user2,helper1,helper2,helper3]) and not (op.param1 in tadmin and any(i in gotinvite for i in tadmin[op.param1])):
                count = 0
                for i in gotinvite:
                    if count == 0:
                        kk.cancelGroupInvitation(op.param1,[i])
                        if TyfeHelperLogged:
                            count += 1
                        continue
                    elif count == 1:
                        aa.cancelGroupInvitation(op.param1,[i])
                        count += 1
                        continue
                    elif count == 2:
                        ab.cancelGroupInvitation(op.param1,[i])
                        count += 1
                        continue
                    elif count == 3:
                        ac.cancelGroupInvitation(op.param1,[i])
                        count = 0
                        continue
        if op.type == 17:
            if op.param1 in banned and op.param2 in banned[op.param1]:
                setKick(op.param1,op.param2,True)
                now2 = datetime.datetime.now()
                nowT = datetime.datetime.strftime(now2,"%H")
                nowM = datetime.datetime.strftime(now2,"%M")
                nowS = datetime.datetime.strftime(now2,"%S")
                tm = "\n\n"+nowT+":"+nowM+":"+nowS
                kk.sendText(op.param1,"สมาชิกที่ถูกแบนไม่ได้รับอนุญาตให้เข้าร่วมกลุ่ม （´・ω・｀）"+tm)
            elif op.param1 in dublist and op.param2 not in [user1,helper1,helper2,helper3]:
                joinname = kk.getContact(op.param2).displayName
                now2 = datetime.datetime.now()
                nowT = datetime.datetime.strftime(now2,"%H")
                nowM = datetime.datetime.strftime(now2,"%M")
                nowS = datetime.datetime.strftime(now2,"%S")
                tm = "\n\n"+nowT+":"+nowM+":"+nowS
                tlist = [" มาแล้วครับท่านผู้ชม "]
                kk.sendText(op.param1,joinname+random.choice(tlist)+"(｀・ω・´)"+tm)
        if op.type == 19:
            if op.param3 == user2:
                gotk = kk
                gotkick = op.param3
                kickname = None
                kickname = kk.getContact(op.param2).displayName
                if TyfeHelperLogged:
                    for i in [aa,ab,ac]:
                        if kickname == None:
                            kickname = i.getContact(op.param2).displayName
                if kickname == None:
                    kickname = cl.getContact(op.param2).displayName
                if not (any(word in kickname for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or kickname.isdigit()):
                    isNotAdmin = False
                    if op.param2 not in [user1,user2,helper1,helper2,helper3] and not (op.param1 in tadmin and op.param2 in tadmin[op.param1]):
                        isNotAdmin = True
                    if isNotAdmin:
                        tmpl = []
                        if op.param1 in banned:
                            tmpl = banned[op.param1]
                        banned[op.param1] = []
                        if op.param2 not in tmpl:
                            banned[op.param1].append(op.param2)
                        if tmpl != []:
                            for oldtarg in tmpl:
                                banned[op.param1].append(oldtarg)
                    x = None
                    alive = None
                    x = kk.getGroup(op.param1)
                    if TyfeHelperLogged:
                        for i in [aa,ab,ac]:
                            if x == None:
                                x = i.getGroup(op.param1)
                    if x == None:
                        x = cl.getGroup(op.param1)
                    mingr = [i.mid for i in x.members]
                    if user2 in mingr:
                        alive = kk
                    elif helper1 in mingr:
                        alive = aa
                    elif helper2 in mingr:
                        alive = ab
                    elif helper3 in mingr:
                        alive = ac
                    elif user1 in mingr:
                        alive = cl
                    defclose = False
                    if x.preventJoinByTicket == False:
                        ticket = alive.reissueGroupTicket(op.param1)
                        gotk.acceptGroupInvitationByTicket(op.param1,ticket)
                        defclose = False
                    else:
                        sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                        if sirilist == []:
                            x.preventJoinByTicket = False
                            alive.updateGroup(x)
                            ticket = alive.reissueGroupTicket(op.param1)
                            gotk.acceptGroupInvitationByTicket(op.param1,ticket)
                            defclose = True
                        else:
                            alive.inviteIntoGroup(op.param1,[gotkick])
                            try:
                                gotk.acceptGroupInvitation(op.param1)
                            except:
                                pass
                    if defclose:
                        x.preventJoinByTicket = True
                        alive.updateGroup(x)
                    if isNotAdmin:
                        setKick(op.param1,op.param2,True)
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    kk.sendText(op.param1,"สมาชิกไม่ได้รับอนุญาตให้ลบบัญชีนี้ （´・ω・｀）\nพิมพ์ 「Tyfe:halt」 ในกรณีที่ต้องการนำบอทออกจากกลุ่ม"+tm)
                    msg = Message()
                    msg.to = op.param1
                    msg.from_ = user2
                    msg.contentType = 13
                    msg.text = None
                    msg.contentMetadata = {'mid': op.param2}
                    kk.sendMessage(msg)
            elif op.param1 in tadmin and op.param3 in tadmin[op.param1] and op.param2 not in [user1,user2,helper1,helper2,helper3]:
                gotkick = op.param3
                kickname = None
                kickname = kk.getContact(op.param2).displayName
                if not (any(word in kickname for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or kickname.isdigit()):
                    tmpl = []
                    if op.param1 in banned:
                        tmpl = banned[op.param1]
                    banned[op.param1] = []
                    if op.param2 not in tmpl:
                        banned[op.param1].append(op.param2)
                    if tmpl != []:
                        for oldtarg in tmpl:
                            banned[op.param1].append(oldtarg)
                    setKick(op.param1,op.param2,True)
                    kk.findAndAddContactsByMid(gotkick)
                    if TyfeHelperLogged:
                        for i in [aa,ab,ac]:
                            i.findAndAddContactsByMid(gotkick)
                    kk.inviteIntoGroup(op.param1,[gotkick])
                    if TyfeHelperLogged:
                        for i in [aa,ab,ac]:
                            i.inviteIntoGroup(op.param1,[gotkick])
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    kk.sendText(op.param1,"สมาชิกไม่ได้รับอนุญาตให้ลบบัญชีนี้ （´・ω・｀）"+tm)
                    msg = Message()
                    msg.to = op.param1
                    msg.from_ = user2
                    msg.contentType = 13
                    msg.text = None
                    msg.contentMetadata = {'mid': op.param2}
                    kk.sendMessage(msg)
            else:
                if op.param1 in kickLockList:
                    gotkick = op.param3
                    kickname = kk.getContact(op.param2).displayName
                    if op.param2 not in [user1,user2,helper1,helper2,helper3] and not (any(word in kickname for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or kickname.isdigit()) and kk.getContact(gotkick).attributes != 32 and not (op.param1 in tadmin and op.param2 in tadmin[op.param1]):
                        tmpl = []
                        if op.param1 in banned:
                            tmpl = banned[op.param1]
                        banned[op.param1] = []
                        if op.param2 not in tmpl:
                            banned[op.param1].append(op.param2)
                        if tmpl != []:
                            for oldtarg in tmpl:
                                banned[op.param1].append(oldtarg)
                        setKick(op.param1,op.param2,True)
                        kk.findAndAddContactsByMid(gotkick)
                        if TyfeHelperLogged:
                            for i in [aa,ab,ac]:
                                i.findAndAddContactsByMid(gotkick)
                        kk.inviteIntoGroup(op.param1,[gotkick])
                        if TyfeHelperLogged:
                            for i in [aa,ab,ac]:
                                i.inviteIntoGroup(op.param1,[gotkick])
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(op.param1,"โหมดห้ามลบถูกเปิดอยู่ สมาชิกไม่ได้รับอนุญาติลบให้บัญชีภายในกลุ่ม （´・ω・｀）"+tm)
                        msg = Message()
                        msg.to = op.param1
                        msg.from_ = user2
                        msg.contentType = 13
                        msg.text = None
                        msg.contentMetadata = {'mid': op.param2}
                        kk.sendMessage(msg)
                elif op.param1 in dublist:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    tlist = [" ซัดเต็มข้อเลยครับท่านผู้ชม "," สวนแล้วครับท่านผู้ชม "," ถีบแล้วครับ "]
                    kk.sendText(op.param1,kickname+random.choice(tlist)+"（´・ω・｀）"+tm)
        if op.type == 25:
            msg = op.message
            if msg.text.lower() == "scanning":
                kk.sendText(user1,msg.to)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    if msg.toType == 2:
                        if msg.to in waitForContactBan:
                            contmid = msg.contentMetadata['mid']
                            tmpl = []
                            if msg.to in banned:
                                tmpl = banned[msg.to]
                            banned[msg.to] = []
                            if contmid not in tmpl and contmid not in [user1,user2,helper1,helper2,helper3]:
                                banned[msg.to].append(contmid)
                            if tmpl != []:
                                for oldtarg in tmpl:
                                    banned[msg.to].append(oldtarg)
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            kk.sendText(msg.to,"สำเร็จแล้ว (｀・ω・´)"+tm)
                            waitForContactBan.remove(msg.to)
                        if msg.to in waitForContactUnBan:
                            contmid = msg.contentMetadata['mid']
                            if msg.to in banned:
                                if contmid in banned[msg.to]:
                                    banned[msg.to].remove(contmid)
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            kk.sendText(msg.to,"สำเร็จแล้ว (｀・ω・´)"+tm)
                            waitForContactUnBan.remove(msg.to)
                        if msg.to in waitForContactAddAdmin:
                            contmid = msg.contentMetadata['mid']
                            tmpl = []
                            if msg.to in tadmin:
                                tmpl = tadmin[msg.to]
                            tadmin[msg.to] = []
                            if contmid not in tmpl and contmid not in [user1,user2,helper1,helper2,helper3]:
                                tadmin[msg.to].append(contmid)
                            if tmpl != []:
                                for oldtarg in tmpl:
                                    tadmin[msg.to].append(oldtarg)
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            kk.sendText(msg.to,"สำเร็จแล้ว (｀・ω・´)"+tm)
                            waitForContactAddAdmin.remove(msg.to)
                        if msg.to in waitForContactRemoveAdmin:
                            contmid = msg.contentMetadata['mid']
                            if msg.to in tadmin:
                                if contmid in tadmin[msg.to]:
                                    tadmin[msg.to].remove(contmid)
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            kk.sendText(msg.to,"สำเร็จแล้ว (｀・ω・´)"+tm)
                            waitForContactRemoveAdmin.remove(msg.to)
            elif msg.contentType == 16:
                if autoLikeSetting["doLike"]:
                    link = msg.contentMetadata['postEndUrl']
                    link = link.replace("line://home/post?userMid=","")
                    link = link.split("&postId=")
                    if len(link[0]) == 33:
                        kk.like(link[0],link[1],likeType=autoLikeSetting["type"])
                        if TyfeHelperLogged:
                            aa.like(link[0],link[1],likeType=autoLikeSetting["type"])
                            ab.like(link[0],link[1],likeType=autoLikeSetting["type"])
                            ac.like(link[0],link[1],likeType=autoLikeSetting["type"])
                        if autoLikeSetting["doComment"]:
                            kk.comment(link[0],link[1],autoLikeSetting["comment"])
                            if TyfeHelperLogged:
                                aa.comment(link[0],link[1],autoLikeSetting["comment"])
                                ab.comment(link[0],link[1],autoLikeSetting["comment"])
                                ac.comment(link[0],link[1],autoLikeSetting["comment"])
            elif "tyfe:say " in msg.text.lower():
                spl = re.split("tyfe:say ",msg.text,flags=re.IGNORECASE)
                if spl[0] == "":
                    if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                        red = re.compile(re.escape('tyfe:say '),re.IGNORECASE)
                        mts = red.sub('',msg.text)
                        mtsl = mts.split()
                        mtsTimeArg = len(mtsl) - 1
                        mtsTime = mtsl[mtsTimeArg]
                        del mtsl[mtsTimeArg]
                        mtosay = " ".join(mtsl)
                        global Rapid2To
                        if msg.toType != 0:
                            Rapid2To = msg.to
                        else:
                            Rapid2To = msg.from_
                        RapidTime = mtsTime
                        rmtosay = []
                        for count in range(0,int(RapidTime)):
                            rmtosay.insert(count,mtosay)
                        p = Pool(20)
                        p.map(Rapid2Say,rmtosay)
                        p.close()
                    else:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.toType != 0:
                            kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif "tyfe:post " in msg.text.lower():
                if msg.from_ == user1:
                    red = re.compile(re.escape('tyfe:post '),re.IGNORECASE)
                    ttp = red.sub('',msg.text)
                    kk.new_post(str(ttp))
                    kk.sendText(msg.to,"โพสต์ข้อความแล้ว\nข้อความที่โพสต์: "+str(ttp))
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif any(word in msg.text.lower() for word in ["ขอ open","ขอopen","ขอไฟล์ open","ขอไฟล์open"]):
                if msg.toType != 0:
                    kk.sendText(msg.to,"OpenVPN จากเซิฟ LONELY BAT (กรุงเทพฯ)\n[True เท่านั้น] ราคา 50 ทรู\n\nมีจำนวนจำกัด กดเลย:\nhttp://lonelybat.inth.red/openvpn/")
                else:
                    kk.sendText(msg.from_,"OpenVPN จากเซิฟ LONELY BAT (กรุงเทพฯ)\n[True เท่านั้น] ราคา 50 ทรู\n\nมีจำนวนจำกัด กดเลย:\nhttp://lonelybat.inth.red/openvpn/")
            elif msg.text.lower() == "tyfe:freeopenvpn":
                text_file = open("freeopenvpn.txt", "r")
                openvpnmessage = text_file.read()
                text_file.close()
                if openvpnmessage == "#":
                    if msg.toType == 0:
                        kk.sendText(msg.from_,"ขออภัย\nขณะนี้ LONELY BAT ยังไม่มีไฟล์ OpenVPN แจกฟรี\nกรุณาตรวจสอบอีกครั้งในภายหลัง")
                    else:
                        kk.sendText(msg.to,"ขออภัย\nขณะนี้ LONELY BAT ยังไม่มีไฟล์ OpenVPN แจกฟรี\nกรุณาตรวจสอบอีกครั้งในภายหลัง")
                else:
                    if msg.toType != 0:
                        kk.sendText(msg.to,openvpnmessage)
                    else:
                        kk.sendText(msg.from_,openvpnmessage)
            elif "tyfe:brainfuck:gen " in msg.text.lower():
                red = re.compile(re.escape('tyfe:brainfuck:gen '),re.IGNORECASE)
                bf = red.sub('',msg.text)
                bfg=BFGenerator()
                if msg.toType != 0:
                    kk.sendText(msg.to,bfg.text_to_brainfuck(bf))
                else:
                    kk.sendText(msg.from_,bfg.text_to_brainfuck(bf))
            elif "tyfe:brainfuck:int " in msg.text.lower():
                red = re.compile(re.escape('tyfe:brainfuck:int '),re.IGNORECASE)
                bf = red.sub('',msg.text)
                if msg.toType != 0:
                    kk.sendText(msg.to,run(bf))
                else:
                    kk.sendText(msg.from_,run(bf))
            elif msg.text.lower() == "tyfe:mimic on":
                if msg.from_ == user1:
                    mimic["status"] = True
                    kk.sendText(msg.to,"เริ่มการล้อเลียน")
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:mimic off":
                if msg.from_ == user1:
                    mimic["status"] = False
                    kk.sendText(msg.to,"ยกเลิกการล้อเลียน")
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif "tyfe:mimic " in msg.text.lower():
                if msg.from_ in user1:
                    red = re.compile(re.escape('tyfe:mimic '),re.IGNORECASE)
                    target0 = red.sub('',msg.text)
                    target1 = target0.lstrip()
                    target2 = target1.replace("@","")
                    target3 = target2.rstrip()
                    _name = target3
                    gInfo = cl.getGroup(msg.to)
                    targets = []
                    targets.insert(0,"0")
                    for a in gInfo.members:
                        if _name == a.displayName:
            	            targets[0] = a.mid
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if targets[0] == "0":
                        kk.sendText(msg.to,"ไม่พบรายชื่อ (｀・ω・´)"+tm)
                    else:
                        for target in targets:
                            try:
                                global lmimic
                                if lmimic != "":
                                    del mimic["target"][lmimic]
                                lmimic = target
                                mimic["target"][target] = True
                                kk.sendText(msg.to,"สำเร็จแล้ว (｀・ω・´)"+tm)
                            except Exception as error:
                                print(error)
                                kk.sendText(msg.to,"ข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower().startswith("tyfe:mentionall"):
                if msg.from_ in user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    data = msg.text[len("tyfe:mentionall"):].strip()
                    if data == "":
                        group = kk.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != user2]
                        cb = ""
                        cb2 = ""
                        count = 1
                        strt = len(str(count)) + 2
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            akh = akh + len(str(count)) + 2 + 5
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 50:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    kk.sendMessage(msg)
                                except:
                                    kk.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            kk.sendMessage(msg)
                        except:
                            kk.sendText(msg.to,"[[NO MENTION]]")
                    elif data[0] == "<":
                        mentargs = int(data[1:].strip())
                        group = kk.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != user2]
                        cb = ""
                        cb2 = ""
                        count = 1
                        strt = len(str(count)) + 2
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            if count > mentargs:
                                break
                            akh = akh + len(str(count)) + 2 + 5
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 50:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    kk.sendMessage(msg)
                                except:
                                    kk.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            kk.sendMessage(msg)
                        except:
                            kk.sendText(msg.to,"[[NO MENTION]]")
                    elif data[0] == ">":
                        mentargs = int(data[1:].strip())
                        group = kk.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != user2]
                        cb = ""
                        cb2 = ""
                        count = 1
                        if mentargs >= 0:
                            strt = len(str(mentargs)) + 2
                        else:
                            strt = len(str(count)) + 2
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            if count < mentargs:
                                count += 1
                                continue
                            akh = akh + len(str(count)) + 2 + 5
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 50:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    kk.sendMessage(msg)
                                except:
                                    kk.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            kk.sendMessage(msg)
                        except:
                            kk.sendText(msg.to,"[[NO MENTION]]")
                    elif data[0] == "=":
                        mentargs = int(data[1:].strip())
                        group = kk.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != user2]
                        cb = ""
                        cb2 = ""
                        count = 1
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            if count != mentargs:
                                count += 1
                                continue
                            akh = akh + len(str(count)) + 2 + 5
                            strt = len(str(count)) + 2
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 50:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    kk.sendMessage(msg)
                                except:
                                    kk.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            kk.sendMessage(msg)
                        except:
                            kk.sendText(msg.to,"[[NO MENTION]]")
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:reader":
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    mem = []
                    try:
                        mem = kk.getGroup(msg.to).members
                    except:
                        try:
                            mem = kk.getRoom(msg.to).contacts
                        except:
                            pass
                    if msg.to in seeall:
                        thas = [i.mid for i in mem if i.attributes == 32]
                        if seeall[msg.to] != []:
                            text = "บัญชีที่อ่านข้อความ:\n"
                            got = False
                            for targ in mem:
                                if targ.mid in seeall[msg.to] and targ.mid not in thas and targ.mid != msg.from_:
                                    text = text+"- "+targ.displayName+"\n"
                                    got = True
                            text = text[:-1]
                            if got == True:
                                kk.sendText(msg.to,text)
                            else:
                                kk.sendText(msg.to,"บัญชีที่อ่านข้อความ:\n[[ไม่มี]]")
                        else:
                            kk.sendText(msg.to,"บัญชีที่อ่านข้อความ:\n[[ไม่มี]]")
                    else:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(msg.to,"บัญชีหลักยังไม่ได้ส่งข้อความก่อนหน้านี้ (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:reader:log on":
                if msg.from_ == user1:
                    readAlert = True
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    kk.sendText(msg.to,"เปิดโหมดแจ้งคนอ่าน (Realtime) แล้ว (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:reader:log off":
                if msg.from_ == user1:
                    readAlert = False
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    kk.sendText(msg.to,"ปิดโหมดแจ้งคนอ่าน (Realtime) แล้ว (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:preventkick on":
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    if msg.toType == 2:
                        if msg.to not in kickLockList:
                            kickLockList.append(msg.to)
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            kk.sendText(msg.to,"เปิดโหมดห้ามลบแล้ว (｀・ω・´)"+tm)
                        else:
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            kk.sendText(msg.to,"โหมดห้ามลบถูกเปิดอยู่แล้ว (｀・ω・´)"+tm)
                    else:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:preventkick off":
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    if msg.toType == 2:
                        if msg.to in kickLockList:
                            kickLockList.remove(msg.to)
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            kk.sendText(msg.to,"ปิดโหมดห้ามลบแล้ว (｀・ω・´)"+tm)
                        else:
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            kk.sendText(msg.to,"โหมดห้ามลบถูกปิดอยู่แล้ว (｀・ω・´)"+tm)
                    else:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() in ["tyfe:halt","ไปคุยกับรากมะม่วงเถอะ"]:
                if msg.from_ == user1:
                    if msg.toType != 0:
                        kk.leaveGroup(msg.to)
                        if TyfeHelperLogged:
                            aa.leaveGroup(msg.to)
                            ab.leaveGroup(msg.to)
                            ac.leaveGroup(msg.to)
                elif msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    if msg.toType != 0:
                        cl.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        if TyfeHelperLogged:
                            aa.leaveGroup(msg.to)
                            ab.leaveGroup(msg.to)
                            ac.leaveGroup(msg.to)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:setreadpoint":
                if msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    if msg.toType != 0:
                        cl.sendText(msg.to,"กรุณารอสักครู่")
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(msg.to,"สำเร็จแล้ว (｀・ω・´)"+tm)
                    else:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(msg.from_,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น (｀・ω・´)"+tm)
                elif msg.from_ != user1:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() in ["tyfe:ban","tyfe:ban "]:
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    if msg.toType == 2:
                        if msg.to not in waitForContactBan:
                            waitForContactBan.append(msg.to)
                        if msg.to in waitForContactUnBan:
                            waitForContactUnBan.remove(msg.to)
                        if msg.to in waitForContactAddAdmin:
                            waitForContactAddAdmin.remove(msg.to)
                        if msg.to in waitForContactRemoveAdmin:
                            waitForContactRemoveAdmin.remove(msg.to)
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(msg.to,"ส่งคอนแท็กเพื่อทำการแบน (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() in ["tyfe:unban","tyfe:unban "]:
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    if msg.toType == 2:
                        if msg.to not in waitForContactUnBan:
                            waitForContactUnBan.append(msg.to)
                        if msg.to in waitForContactBan:
                            waitForContactBan.remove(msg.to)
                        if msg.to in waitForContactAddAdmin:
                            waitForContactAddAdmin.remove(msg.to)
                        if msg.to in waitForContactRemoveAdmin:
                            waitForContactRemoveAdmin.remove(msg.to)
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(msg.to,"ส่งคอนแท็กเพื่อทำการปลดแบน (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif "tyfe:ban " in msg.text.lower():
                if msg.from_ in user1:
                    if msg.toType == 2:
                        red = re.compile(re.escape('tyfe:ban '),re.IGNORECASE)
                        namel = red.sub('',msg.text)
                        namel = namel.lstrip()
                        namel = namel.replace(" @","$spliter$")
                        namel = namel.replace("@","")
                        namel = namel.rstrip()
                        namel = namel.split("$spliter$")
                        gmem = cl.getGroup(msg.to).members
                        found = False
                        tmpl = []
                        if msg.to in banned:
                            tmpl = banned[msg.to]
                        banned[msg.to] = []
                        for targ in gmem:
                            if targ.displayName in namel:
                                found = True
                                if targ.mid not in tmpl and targ.mid not in [user1,user2]:
                                    banned[msg.to].append(targ.mid)
                        if tmpl != []:
                            for oldtarg in tmpl:
                                banned[msg.to].append(oldtarg)
                        if found == False:
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            kk.sendText(msg.to,"ไม่พบรายชื่อ (｀・ω・´)"+tm)
                        else:
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            kk.sendText(msg.to,"สำเร็จแล้ว (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif "tyfe:unban " in msg.text.lower():
                if msg.from_ in user1:
                    if msg.toType == 2:
                        red = re.compile(re.escape('tyfe:unban '),re.IGNORECASE)
                        namel = red.sub('',msg.text)
                        namel = namel.lstrip()
                        namel = namel.replace("@","")
                        namel = namel.rstrip()
                        namel = namel.split(" ")
                        gmem = cl.getGroup(msg.to).members
                        found = False
                        if msg.to in banned:
                            for targ in gmem:
                                if targ.displayName in namel:
                                    found = True
                                    if targ.mid in banned[msg.to]:
                                        banned[msg.to].remove(targ.mid)
                        if found == False:
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            kk.sendText(msg.to,"ไม่พบรายชื่อ (｀・ω・´)"+tm)
                        else:
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            kk.sendText(msg.to,"สำเร็จแล้ว (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:unbanall":
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    try:
                        dkey = banned.pop(msg.to)
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(msg.to,"ปลดแบนสมาชิกทั้งหมดสำหรับกลุ่มนี้เรียบร้อยแล้ว (｀・ω・´)"+tm)
                    except:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(msg.to,"ไม่มีสมาชิกถูกแบนสำหรับกลุ่มนี้ (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:banlist":
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    if msg.to in banned and banned[msg.to] != []:
                        for targ in banned[msg.to]:
                            try:
                                msg.contentType = 13
                                msg.text = None
                                msg.contentMetadata = {'mid': targ}
                                kk.sendMessage(msg)
                                time.sleep(0.1)
                            except Exception as e:
                                print(e)
                    else:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(msg.to,"ไม่มีสมาชิกถูกแบนสำหรับกลุ่มนี้ (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:kickban":
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    if msg.to in banned and banned[msg.to] != []:
                        gmem = kk.getGroup(msg.to).members
                        groupParam = msg.to
                        targets = []
                        for targ in gmem:
                            if targ.mid in banned[msg.to]:
                                targets.append(targ.mid)
                        p = Pool(len(targets))
                        try:
                            p.map(kickBan,targets)
                        except:
                            if TyfeHelperLogged:
                                try:
                                    p.map(h1kickBan,targets)
                                except:
                                    try:
                                        p.map(h2kickBan,targets)
                                    except:
                                        try:
                                            p.map(h3kickBan,targets)
                                        except:
                                            pass
                        p.close()
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(msg.to,"สำเร็จแล้ว (｀・ω・´)"+tm)
                    else:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(msg.to,"ไม่มีสมาชิกถูกแบนสำหรับกลุ่มนี้ (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:autolike on":
                if msg.from_ == user1:
                    autoLikeSetting["doLike"] = True
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"เปิดไลค์อัตโนมัติแล้ว (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.to,"เปิดไลค์อัตโนมัติแล้ว (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:autolike off":
                if msg.from_ == user1:
                    autoLikeSetting["doLike"] = False
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    if msg.toType != 0:
                        kk.sendText(msg.to,"ปิดไลค์อัตโนมัติแล้ว (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"ปิดไลค์อัตโนมัติแล้ว (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:autolike:comment on":
                if msg.from_ == user1:
                    autoLikeSetting["doComment"] = True
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"เปิดคอมเม้นต์อัตโนมัติแล้ว (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"เปิดคอมเม้นต์อัตโนมัติแล้ว (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:autolike:comment off":
                if msg.from_ == user1:
                    autoLikeSetting["doComment"] = False
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"ปิดคอมเม้นต์อัตโนมัติแล้ว (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"ปิดคอมเม้นต์อัตโนมัติแล้ว (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif "tyfe:autolike:type " in msg.text.lower():
                if msg.from_ == user1:
                    red = re.compile(re.escape('tyfe:autolike:type '),re.IGNORECASE)
                    ltype = red.sub('',msg.text)
                    ltype = ltype.strip()
                    if ltype == "1":
                        autoLikeSetting["type"] = 1001
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.toType != 0:
                            kk.sendText(msg.to,"ตั้งชนิดของการไลค์แล้ว (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.from_,"ตั้งชนิดของการไลค์แล้ว (｀・ω・´)"+tm)
                    elif ltype == "2":
                        autoLikeSetting["type"] = 1002
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.toType != 0:
                            kk.sendText(msg.to,"ตั้งชนิดของการไลค์แล้ว (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.from_,"ตั้งชนิดของการไลค์แล้ว (｀・ω・´)"+tm)
                    elif ltype == "3":
                        autoLikeSetting["type"] = 1003
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.toType != 0:
                            kk.sendText(msg.to,"ตั้งชนิดของการไลค์แล้ว (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.from_,"ตั้งชนิดของการไลค์แล้ว (｀・ω・´)"+tm)
                    elif ltype == "4":
                        autoLikeSetting["type"] = 1004
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.toType != 0:
                            kk.sendText(msg.to,"ตั้งชนิดของการไลค์แล้ว (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.from_,"ตั้งชนิดของการไลค์แล้ว (｀・ω・´)"+tm)
                    elif ltype == "5":
                        autoLikeSetting["type"] = 1005
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.toType != 0:
                            kk.sendText(msg.to,"ตั้งชนิดของการไลค์แล้ว (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.from_,"ตั้งชนิดของการไลค์แล้ว (｀・ω・´)"+tm)
                    elif ltype == "6":
                        autoLikeSetting["type"] = 1006
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.toType != 0:
                            kk.sendText(msg.to,"ตั้งชนิดของการไลค์แล้ว (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.from_,"ตั้งชนิดของการไลค์แล้ว (｀・ω・´)"+tm)
                    else:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.toType != 0:
                            kk.sendText(msg.to,"ชนิดของการไลค์ไม่ถูกต้อง (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.from_,"ชนิดของการไลค์ไม่ถูกต้อง (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif "tyfe:autolike:comment: " in msg.text.lower():
                if msg.from_ == user1:
                    red = re.compile(re.escape('tyfe:autolike:comment: '),re.IGNORECASE)
                    comment = red.sub('',msg.text)
                    comment = comment.strip()
                    autoLikeSetting["comment"] = comment
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"ตั้งคอมเม้นต์อัตโนมัติแล้ว (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"ตั้งคอมเม้นต์อัตโนมัติแล้ว (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:admin add":
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    if msg.toType == 2:
                        if msg.to not in waitForContactAddAdmin:
                            waitForContactAddAdmin.append(msg.to)
                        if msg.to in waitForContactUnBan:
                            waitForContactUnBan.remove(msg.to)
                        if msg.to in waitForContactBan:
                            waitForContactBan.remove(msg.to)
                        if msg.to in waitForContactRemoveAdmin:
                            waitForContactRemoveAdmin.remove(msg.to)
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(msg.to,"ส่งคอนแท็กเพื่อทำการเพิ่มแอดมิน (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:admin remove":
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    if msg.toType == 2:
                        if msg.to not in waitForContactRemoveAdmin:
                            waitForContactRemoveAdmin.append(msg.to)
                        if msg.to in waitForContactUnBan:
                            waitForContactUnBan.remove(msg.to)
                        if msg.to in waitForContactBan:
                            waitForContactBan.remove(msg.to)
                        if msg.to in waitForContactAddAdmin:
                            waitForContactAddAdmin.remove(msg.to)
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(msg.to,"ส่งคอนแท็กเพื่อทำการปลดแอดมิน (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() in ["tyfe:admin","tyfe:admin "]:
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    if msg.to in tadmin and tadmin[msg.to] != []:
                        for targ in tadmin[msg.to]:
                            try:
                                msg.contentType = 13
                                msg.text = None
                                msg.contentMetadata = {'mid': targ}
                                kk.sendMessage(msg)
                                time.sleep(0.1)
                            except Exception as e:
                                print(e)
                    else:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(msg.to,"ไม่มีแอดมินในกลุ่มนี้ (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:superadmin":
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to] or kk.isCreator(msg.from_):
                    msg.contentType = 13
                    msg.text = None
                    msg.contentMetadata = {'mid': user1}
                    kk.sendMessage(msg)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:id":
                if msg.from_ == user1:
                    if msg.toType != 0:
                        kk.sendText(msg.to,"ไอดีของบัญชีนี้: "+user2)
                    else:
                        kk.sendText(msg.from_,"ไอดีของบัญชีนี้: "+user2)
            elif msg.text.lower() == "tyfe:creator":
                msg.contentType = 13
                msg.text = None
                msg.contentMetadata = {'mid': kk.getCreator()}
                kk.sendMessage(msg)
            elif msg.text.lower() == "tyfe:help":
                if msg.toType != 0:
                    kk.sendText(msg.to,tyfehelp)
                else:
                    kk.sendText(msg.from_,tyfehelp)
            elif msg.text.lower() == "tyfe:forcehalt":
                if msg.from_ == kk.getCreator():
                    if msg.toType == 2:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(msg.to,"รับทราบ (｀・ω・´)"+tm)
                        kk.leaveGroup(msg.to)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:creatorcheck":
                if msg.from_ == kk.getCreator():
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณคือผู้สร้าง Tyfe (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณคือผู้สร้าง Tyfe (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่ใช่ผู้สร้าง Tyfe (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่ใช่ผู้สร้าง Tyfe (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:botprotect on":
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    if msg.toType == 2:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.to not in botProtect:
                            botProtect.append(msg.to)
                            kk.sendText(msg.to,"เปิดระบบป้องกันบอทแล้ว (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.to,"เปิดระบบป้องกันบอทอยู่แล้ว (｀・ω・´)"+tm)
                    else:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.toType != 0:
                            kk.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.from_,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:botprotect off":
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    if msg.toType == 2:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.to in botProtect:
                            botProtect.remove(msg.to)
                            kk.sendText(msg.to,"ปิดระบบป้องกันบอทแล้ว (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.to,"ปิดระบบป้องกันบอทอยู่แล้ว (｀・ω・´)"+tm)
                    else:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.toType != 0:
                            kk.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.from_,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:swap":
                if msg.from_ == user1:
                    u1 = cl.getProfile()
                    u2 = kk.getProfile()
                    u1.displayName, u2.displayName = u2.displayName, u1.displayName
                    u1.statusMessage, u2.statusMessage = u2.statusMessage, u1.statusMessage
                    u1.pictureStatus, u2.pictureStatus = u2.pictureStatus, u1.pictureStatus
                    cl.updateDisplayPicture(u1.pictureStatus)
                    cl.updateProfile(u1)
                    kk.updateDisplayPicture(u2.pictureStatus)
                    kk.updateProfile(u2)
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"สำเร็จแล้ว (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"สำเร็จแล้ว (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:save":
                if msg.from_ == user1:
                    me = kk.getProfile()
                    save2["displayName"] = me.displayName
                    save2["statusMessage"] = me.statusMessage
                    save2["pictureStatus"] = me.pictureStatus
                    save2["Saved"] = True
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"บันทึกสถานะบัญชีเรียบร้อยแล้ว (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"บันทึกสถานะบัญชีเรียบร้อยแล้ว (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:load":
                if msg.from_ == user1:
                    if save2["Saved"]:
                        me = kk.getProfile()
                        me.displayName = save2["displayName"]
                        me.statusMessage = save2["statusMessage"]
                        me.pictureStatus = save2["pictureStatus"]
                        kk.updateDisplayPicture(me.pictureStatus)
                        kk.updateProfile(me)
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.toType != 0:
                            kk.sendText(msg.to,"โหลดสถานะบัญชีเรียบร้อยแล้ว (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.from_,"โหลดสถานะบัญชีเรียบร้อยแล้ว (｀・ω・´)"+tm)
                    else:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.toType != 0:
                            kk.sendText(msg.to,"ก่อนหน้านี้ยังไม่ได้มีการบันทึกสถานะบัญชี (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.from_,"ก่อนหน้านี้ยังไม่ได้มีการบันทึกสถานะบัญชี (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif "tyfe:qrcode " in msg.text.lower():
                data = re.split("tyfe:qrcode ",msg.text,flags=re.IGNORECASE)
                if data[0] == "":
                    if msg.toType != 0:
                        kk.sendImageWithUrl(msg.to,"https://chart.googleapis.com/chart?cht=qr&chs=500x500&chl="+data[1])
                    else:
                        kk.sendImageWithUrl(msg.from_,"https://chart.googleapis.com/chart?cht=qr&chs=500x500&chl="+data[1])
            elif "tyfe:talk " in msg.text.lower():
                data = re.split("tyfe:talk ",msg.text,flags=re.IGNORECASE)
                tl = "th-TH"
                if data[0] == "":
                    if msg.toType != 0:
                        kk.sendAudioWithUrl(msg.to,"http://translate.google.com/translate_tts?ie=UTF-8&total=1&idx=0&textlen=32&client=tw-ob&q="+data[1]+"&tl="+tl)
                    else:
                        kk.sendAudioWithUrl(msg.from_,"http://translate.google.com/translate_tts?ie=UTF-8&total=1&idx=0&textlen=32&client=tw-ob&q="+data[1]+"&tl="+tl)
            elif "tyfe:en-id " in msg.text.lower():
                data = re.split("tyfe:en-id ",msg.text,flags=re.IGNORECASE)
                if data[0] == "":
                    if msg.toType != 0:
                        kk.sendText(msg.to,"[EN - ID] Translation:\n"+Translator().translate(data[1],src="en",dest="id").text)
                    else:
                        kk.sendText(msg.from_,"[EN - ID] Translation:\n"+Translator().translate(data[1],src="en",dest="id").text)
            elif "tyfe:en-th " in msg.text.lower():
                data = re.split("tyfe:en-th ",msg.text,flags=re.IGNORECASE)
                if data[0] == "":
                    if msg.toType != 0:
                        kk.sendText(msg.to,"[EN - TH] Translation:\n"+Translator().translate(data[1],src="en",dest="th").text)
                    else:
                        kk.sendText(msg.from_,"[EN - TH] Translation:\n"+Translator().translate(data[1],src="en",dest="th").text)
            elif "tyfe:en-jp " in msg.text.lower():
                data = re.split("tyfe:en-jp ",msg.text,flags=re.IGNORECASE)
                if data[0] == "":
                    if msg.toType != 0:
                        kk.sendText(msg.to,"[EN - JP] Translation:\n"+Translator().translate(data[1],src="en",dest="ja").text)
                    else:
                        kk.sendText(msg.from_,"[EN - JP] Translation:\n"+Translator().translate(data[1],src="en",dest="ja").text)
            elif "tyfe:id-en " in msg.text.lower():
                data = re.split("tyfe:id-en ",msg.text,flags=re.IGNORECASE)
                if data[0] == "":
                    if msg.toType != 0:
                        kk.sendText(msg.to,"[ID - EN] Translation:\n"+Translator().translate(data[1],src="id",dest="en").text)
                    else:
                        kk.sendText(msg.from_,"[ID - EN] Translation:\n"+Translator().translate(data[1],src="id",dest="en").text)
            elif "tyfe:id-th " in msg.text.lower():
                data = re.split("tyfe:id-th ",msg.text,flags=re.IGNORECASE)
                if data[0] == "":
                    if msg.toType != 0:
                        kk.sendText(msg.to,"[ID - TH] Translation:\n"+Translator().translate(data[1],src="id",dest="th").text)
                    else:
                        kk.sendText(msg.from_,"[ID - TH] Translation:\n"+Translator().translate(data[1],src="id",dest="th").text)
            elif "tyfe:id-jp " in msg.text.lower():
                data = re.split("tyfe:id-jp ",msg.text,flags=re.IGNORECASE)
                if data[0] == "":
                    if msg.toType != 0:
                        kk.sendText(msg.to,"[ID - JP] Translation:\n"+Translator().translate(data[1],src="id",dest="ja").text)
                    else:
                        kk.sendText(msg.from_,"[ID - JP] Translation:\n"+Translator().translate(data[1],src="id",dest="ja").text)
            elif "tyfe:th-en " in msg.text.lower():
                data = re.split("tyfe:th-en ",msg.text,flags=re.IGNORECASE)
                if data[0] == "":
                    if msg.toType != 0:
                        kk.sendText(msg.to,"[TH - EN] Translation:\n"+Translator().translate(data[1],src="th",dest="en").text)
                    else:
                        kk.sendText(msg.from_,"[TH - EN] Translation:\n"+Translator().translate(data[1],src="th",dest="en").text)
            elif "tyfe:th-id " in msg.text.lower():
                data = re.split("tyfe:th-id ",msg.text,flags=re.IGNORECASE)
                if data[0] == "":
                    if msg.toType != 0:
                        kk.sendText(msg.to,"[TH - ID] Translation:\n"+Translator().translate(data[1],src="th",dest="id").text)
                    else:
                        kk.sendText(msg.from_,"[TH - ID] Translation:\n"+Translator().translate(data[1],src="th",dest="id").text)
            elif "tyfe:th-jp " in msg.text.lower():
                data = re.split("tyfe:th-jp ",msg.text,flags=re.IGNORECASE)
                if data[0] == "":
                    if msg.toType != 0:
                        kk.sendText(msg.to,"[TH - JP] Translation:\n"+Translator().translate(data[1],src="th",dest="ja").text)
                    else:
                        kk.sendText(msg.from_,"[TH - JP] Translation:\n"+Translator().translate(data[1],src="th",dest="ja").text)
            elif "tyfe:jp-en " in msg.text.lower():
                data = re.split("tyfe:jp-en ",msg.text,flags=re.IGNORECASE)
                if data[0] == "":
                    if msg.toType != 0:
                        kk.sendText(msg.to,"[JP - EN] Translation:\n"+Translator().translate(data[1],src="ja",dest="en").text)
                    else:
                        kk.sendText(msg.from_,"[JP - EN] Translation:\n"+Translator().translate(data[1],src="ja",dest="en").text)
            elif "tyfe:jp-id " in msg.text.lower():
                data = re.split("tyfe:jp-id ",msg.text,flags=re.IGNORECASE)
                if data[0] == "":
                    if msg.toType != 0:
                        kk.sendText(msg.to,"[JP - ID] Translation:\n"+Translator().translate(data[1],src="ja",dest="id").text)
                    else:
                        kk.sendText(msg.from_,"[JP - ID] Translation:\n"+Translator().translate(data[1],src="ja",dest="id").text)
            elif "tyfe:jp-th " in msg.text.lower():
                data = re.split("tyfe:jp-th ",msg.text,flags=re.IGNORECASE)
                if data[0] == "":
                    if msg.toType != 0:
                        kk.sendText(msg.to,"[JP - TH] Translation:\n"+Translator().translate(data[1],src="ja",dest="th").text)
                    else:
                        kk.sendText(msg.from_,"[JP - TH] Translation:\n"+Translator().translate(data[1],src="ja",dest="th").text)
            elif msg.text.lower() == "tyfe:dub on":
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    if msg.toType == 2:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.to not in dublist:
                            dublist.append(msg.to)
                            kk.sendText(msg.to,"เปิดพากษ์สดแล้ว (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.to,"เปิดพากษ์สดอยู่แล้ว (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:dub off":
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    if msg.toType == 2:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.to in dublist:
                            dublist.remove(msg.to)
                            kk.sendText(msg.to,"ปิดพากษ์สดแล้ว (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.to,"ปิดพากษ์สดอยู่แล้ว (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:uninstall":
                if msg.toType == 2:
                    if msg.from_ == user1:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(msg.to,"กำลังถอนการติดตั้ง (｀・ω・´)"+tm)
                        dkey = banned.pop(msg.to,None)
                        dkey = tadmin.pop(msg.to,None)
                        dkey = seeall.pop(msg.to,None)
                        if msg.to in dublist:
                            dublist.remove(msg.to)
                        if msg.to in kickLockList:
                            kickLockList.remove(msg.to)
                        if msg.to in botProtect:
                            botProtect.remove(msg.to)
                        if msg.to in preventBlockURL:
                            preventBlockURL.remove(msg.to)
                        if msg.to in blockInvite:
                            blockInvite.remove(msg.to)
                        kk.leaveGroup(msg.to)
                        if TyfeHelperLogged:
                            aa.leaveGroup(msg.to)
                            ab.leaveGroup(msg.to)
                            ac.leaveGroup(msg.to)
                    elif msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(msg.to,"กำลังถอนการติดตั้ง (｀・ω・´)"+tm)
                        dkey = banned.pop(msg.to,None)
                        dkey = tadmin.pop(msg.to,None)
                        dkey = seeall.pop(msg.to,None)
                        if msg.to in dublist:
                            dublist.remove(msg.to)
                        if msg.to in kickLockList:
                            kickLockList.remove(msg.to)
                        if msg.to in botProtect:
                            botProtect.remove(msg.to)
                        if msg.to in preventBlockURL:
                            preventBlockURL.remove(msg.to)
                        if msg.to in blockInvite:
                            blockInvite.remove(msg.to)
                        kk.leaveGroup(msg.to)
                        if TyfeHelperLogged:
                            aa.leaveGroup(msg.to)
                            ab.leaveGroup(msg.to)
                            ac.leaveGroup(msg.to)
                        cl.leaveGroup(msg.to)
                    else:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.toType != 0:
                            kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif "tyfe:denyall" in msg.text.lower():
                spl = re.split("tyfe:denyall",msg.text,flags=re.IGNORECASE)
                if spl[0] == "":
                    if msg.from_ == user1:
                        spl[1] = spl[1].strip()
                        ag = kk.getGroupIdsInvited()
                        txt = "กำลังยกเลิกค้างเชิญจำนวน "+str(len(ag))+" กลุ่ม"
                        if spl[1] != "":
                            txt = txt + " ด้วยข้อความ \""+spl[1]+"\""
                        txt = txt + "\nกรุณารอสักครู่.. (｀・ω・´)"
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.toType != 0:
                            kk.sendText(msg.to,txt+tm)
                        else:
                            kk.sendText(msg.from_,txt+tm)
                        for gr in ag:
                            try:
                                kk.acceptGroupInvitation(gr)
                                if spl[1] != "":
                                    kk.sendText(gr,spl[1])
                                kk.leaveGroup(gr)
                            except:
                                pass
                        if TyfeHelperLogged:
                            for i in [aa,ab,ac]:
                                ag = i.getGroupIdsInvited()
                                txt = "กำลังยกเลิกค้างเชิญจำนวน "+str(len(ag))+" กลุ่ม"
                                if spl[1] != "":
                                    txt = txt + " ด้วยข้อความ \""+spl[1]+"\""
                                txt = txt + "\nกรุณารอสักครู่.. (｀・ω・´)"
                                now2 = datetime.datetime.now()
                                nowT = datetime.datetime.strftime(now2,"%H")
                                nowM = datetime.datetime.strftime(now2,"%M")
                                nowS = datetime.datetime.strftime(now2,"%S")
                                tm = "\n\n"+nowT+":"+nowM+":"+nowS
                                if msg.toType != 0:
                                    i.sendText(msg.to,txt+tm)
                                else:
                                    i.sendText(msg.from_,txt+tm)
                                for gr in ag:
                                    try:
                                        i.acceptGroupInvitation(gr)
                                        if spl[1] != "":
                                            i.sendText(gr,spl[1])
                                        i.leaveGroup(gr)
                                    except:
                                        pass
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(msg.to,"สำเร็จแล้ว (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:reinvite":
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    x = kk.getGroup(msg.to)
                    if not (set([user1,user2,helper1,helper2,helper3]).issubset([i.mid for i in x.members])):
                        defclose = False
                        if x.preventJoinByTicket == False:
                            ticket = kk.reissueGroupTicket(msg.to)
                            if user1 not in [i.mid for i in x.members]:
                                cl.acceptGroupInvitationByTicket(msg.to,ticket)
                            if TyfeHelperLogged:
                                if not (set([helper1,helper2,helper3]).issubset([i.mid for i in x.members])):
                                    aa.acceptGroupInvitationByTicket(msg.to,ticket)
                                    ab.acceptGroupInvitationByTicket(msg.to,ticket)
                                    ac.acceptGroupInvitationByTicket(msg.to,ticket)
                            defclose = False
                        else:
                            sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                            if sirilist == []:
                                x.preventJoinByTicket = False
                                kk.updateGroup(x)
                                ticket = kk.reissueGroupTicket(msg.to)
                                if user1 not in [i.mid for i in x.members]:
                                    cl.acceptGroupInvitationByTicket(msg.to,ticket)
                                if TyfeHelperLogged:
                                    if not (set([helper1,helper2,helper3]).issubset([i.mid for i in x.members])):
                                        aa.acceptGroupInvitationByTicket(msg.to,ticket)
                                        ab.acceptGroupInvitationByTicket(msg.to,ticket)
                                        ac.acceptGroupInvitationByTicket(msg.to,ticket)
                                defclose = True
                            else:
                                if user1 not in [i.mid for i in x.members]:
                                    kk.inviteIntoGroup(msg.to,[user1])
                                if TyfeHelperLogged:
                                    if not (set([helper1,helper2,helper3]).issubset([i.mid for i in x.members])):
                                        kk.inviteIntoGroup(msg.to,[helper1,helper2,helper3])
                                if user1 not in [i.mid for i in x.members]:
                                    kk.acceptGroupInvitation(msg.to)
                                if TyfeHelperLogged:
                                    if not (set([helper1,helper2,helper3]).issubset([i.mid for i in x.members])):
                                        aa.acceptGroupInvitation(msg.to)
                                        ab.acceptGroupInvitation(msg.to)
                                        ac.acceptGroupInvitation(msg.to)
                        if defclose:
                            x.preventJoinByTicket = True
                            kk.updateGroup(x)
            elif msg.text.lower() == "helper1:removesiri":
                if msg.from_ == user1:
                    if msg.toType == 2:
                        if TyfeHelperLogged:
                            x = kk.getGroup(msg.to)
                            if helper1 in [i.mid for i in x.members]:
                                sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                                if sirilist != []:
                                    groupParam = msg.to
                                    p = Pool(len(sirilist))
                                    try:
                                        p.map(h1kickBan,sirilist)
                                        p.close()
                                    except:
                                        p.close()
            elif msg.text.lower() == "helper2:removesiri":
                if msg.from_ == user1:
                    if msg.toType == 2:
                        if TyfeHelperLogged:
                            x = kk.getGroup(msg.to)
                            if helper2 in [i.mid for i in x.members]:
                                sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                                if sirilist != []:
                                    groupParam = msg.to
                                    p = Pool(len(sirilist))
                                    try:
                                        p.map(h2kickBan,sirilist)
                                        p.close()
                                    except:
                                        p.close()
            elif msg.text.lower() == "helper3:removesiri":
                if msg.from_ == user1:
                    if msg.toType == 2:
                        if TyfeHelperLogged:
                            x = kk.getGroup(msg.to)
                            if helper3 in [i.mid for i in x.members]:
                                sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                                if sirilist != []:
                                    groupParam = msg.to
                                    p = Pool(len(sirilist))
                                    try:
                                        p.map(h3kickBan,sirilist)
                                        p.close()
                                    except:
                                        p.close()
            elif msg.text.lower() == "tyfe:blockurl on":
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    if msg.toType == 2:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.to in preventBlockURL:
                            preventBlockURL.remove(msg.to)
                            kk.sendText(msg.to,"ล็อก URL แล้ว (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.to,"ล็อก URL อยู่แล้ว (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:blockurl off":
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    if msg.toType == 2:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.to not in preventBlockURL:
                            preventBlockURL.append(msg.to)
                            kk.sendText(msg.to,"ปลดล็อก URL แล้ว (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.to,"ปลดล็อก URL อยู่แล้ว (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:blockinvitation on":
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    if msg.toType == 2:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.to not in blockInvite:
                            blockInvite.append(msg.to)
                            kk.sendText(msg.to,"ล็อกการเชิญแล้ว (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.to,"ล็อกการเชิญอยู่แล้ว (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:blockinvitation off":
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    if msg.toType == 2:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.to in blockInvite:
                            blockInvite.remove(msg.to)
                            kk.sendText(msg.to,"ปลดล็อกการเชิญแล้ว (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.to,"ปลดล็อกการเชิญอยู่แล้ว (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif "tyfe:bye " in msg.text.lower():
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        allmid = []
                        for i in range(len(prov)):
                            setKick(msg.to,prov[i]["M"],False)
                            allmid.append(prov[i]["M"])
                        try:
                            kk.findAndAddContactsByMids(allmid)
                        except:
                            pass
                        if TyfeHelperLogged:
                            for i in [aa,ab,ac]:
                                try:
                                    i.findAndAddContactsByMids(allmid)
                                except:
                                    pass
                        try:
                            kk.inviteIntoGroup(msg.to,allmid)
                        except:
                            pass
                        if TyfeHelperLogged:
                            for i in [aa,ab,ac]:
                                try:
                                    i.inviteIntoGroup(msg.to,allmid)
                                except:
                                    pass
                        try:
                            kk.cancelGroupInvitation(msg.to,allmid)
                        except:
                            pass
                        if TyfeHelperLogged:
                            for i in [aa,ab,ac]:
                                try:
                                    i.cancelGroupInvitation(msg.to,allmid)
                                except:
                                    pass
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:friendalllogged":
                if msg.from_ == user1:
                    if TyfeHelperLogged:
                        clfr = [user2,helper1,helper2,helper3]
                        kkfr = [user1,helper1,helper2,helper3]
                        aafr = [user1,user2,helper2,helper3]
                        abfr = [user1,user2,helper1,helper3]
                        acfr = [user1,user2,helper1,helper2]
                        cl.findAndAddContactsByMids(clfr)
                        kk.findAndAddContactsByMids(kkfr)
                        aa.findAndAddContactsByMids(aafr)
                        ab.findAndAddContactsByMids(abfr)
                        ac.findAndAddContactsByMids(acfr)
                    else:
                        clfr = [user2]
                        kkfr = [user1]
                        cl.findAndAddContactsByMids(clfr)
                        kk.findAndAddContactsByMids(kkfr)
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"สำเร็จแล้ว (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"สำเร็จแล้ว (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif "tyfe:remove " in msg.text.lower():
                if msg.from_ == user1 or msg.to in tadmin and msg.from_ in tadmin[msg.to]:
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            setKick(msg.to,prov[i]["M"],False)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:kickall":
                if msg.from_ == user1:
                    gs = kk.getGroup(msg.to)
                    if not (set([user1,user2,helper1,helper2,helper3]).issubset([i.mid for i in gs.members])):
                        defclose = False
                        if gs.preventJoinByTicket == False:
                            ticket = kk.reissueGroupTicket(msg.to)
                            if user1 not in [i.mid for i in gs.members]:
                                cl.acceptGroupInvitationByTicket(msg.to,ticket)
                            if TyfeHelperLogged:
                                if not (set([helper1,helper2,helper3]).issubset([i.mid for i in gs.members])):
                                    aa.acceptGroupInvitationByTicket(msg.to,ticket)
                                    ab.acceptGroupInvitationByTicket(msg.to,ticket)
                                    ac.acceptGroupInvitationByTicket(msg.to,ticket)
                            defclose = False
                        else:
                            sirilist = [i.mid for i in gs.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                            if sirilist == []:
                                gs.preventJoinByTicket = False
                                kk.updateGroup(gs)
                                ticket = kk.reissueGroupTicket(msg.to)
                                if user1 not in [i.mid for i in gs.members]:
                                    cl.acceptGroupInvitationByTicket(msg.to,ticket)
                                if TyfeHelperLogged:
                                    if not (set([helper1,helper2,helper3]).issubset([i.mid for i in gs.members])):
                                        aa.acceptGroupInvitationByTicket(msg.to,ticket)
                                        ab.acceptGroupInvitationByTicket(msg.to,ticket)
                                        ac.acceptGroupInvitationByTicket(msg.to,ticket)
                                defclose = True
                            else:
                                if user1 not in [i.mid for i in gs.members]:
                                    kk.inviteIntoGroup(msg.to,[user1])
                                if TyfeHelperLogged:
                                    if not (set([helper1,helper2,helper3]).issubset([i.mid for i in gs.members])):
                                        kk.inviteIntoGroup(msg.to,[helper1,helper2,helper3])
                                if user1 not in [i.mid for i in gs.members]:
                                    kk.acceptGroupInvitation(msg.to)
                                if TyfeHelperLogged:
                                    if not (set([helper1,helper2,helper3]).issubset([i.mid for i in gs.members])):
                                        aa.acceptGroupInvitation(msg.to)
                                        ab.acceptGroupInvitation(msg.to)
                                        ac.acceptGroupInvitation(msg.to)
                        if defclose:
                            gs.preventJoinByTicket = True
                            kk.updateGroup(gs)
                    sirilist = [i.mid for i in gs.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                    if sirilist == []:
                        groupParam = msg.to
                        targets = [i.mid for i in gs.members if i.mid not in [user1,user2,helper1,helper2,helper3]]
                        if targets == []:
                            kk.sendText(msg.to,"Not found.")
                        else:
                            try:
                                p = Pool(len(targets))
                                p.map(kickBan,targets)
                                p.close()
                            except:
                                p.close()
                                allmid = aa.getGroup(msg.to).members
                                targets = [i.mid for i in allmid if i.mid not in [user1,user2,helper1,helper2,helper3]]
                                try:
                                    p = Pool(len(targets))
                                    p.map(h1kickBan,targets)
                                    p.close()
                                except:
                                    p.close()
                                    allmid = ab.getGroup(msg.to).members
                                    targets = [i.mid for i in allmid if i.mid not in [user1,user2,helper1,helper2,helper3]]
                                    try:
                                        p = Pool(len(targets))
                                        p.map(h2kickBan,targets)
                                        p.close()
                                    except:
                                        p.close()
                                        allmid = ac.getGroup(msg.to).members
                                        targets = [i.mid for i in allmid if i.mid not in [user1,user2,helper1,helper2,helper3]]
                                        try:
                                            p = Pool(len(targets))
                                            p.map(h3kickBan,targets)
                                            p.close()
                                        except:
                                            p.close()
                            try:
                                gs = ac.getGroup(msg.to)
                                gMembMids = [contact.mid for contact in gs.invitee]
                                for i in gMembMids:
                                    ac.cancelGroupInvitation(msg.to,[i])
                            except Exception as e:
                                p.close()
                                print(e)
                    else:
                        groupParam = msg.to
                        try:
                            p = Pool(len(sirilist))
                            p.map(kickBan,sirilist)
                            p.close()
                        except:
                            p.close()
                        gs = kk.getGroup(msg.to)
                        targets = [i.mid for i in gs.members if i.mid not in [user1,user2,helper1,helper2,helper3]]
                        if targets == []:
                            kk.sendText(msg.to,"Not found.")
                        else:
                            try:
                                p = Pool(len(targets))
                                p.map(kickBan,targets)
                                p.close()
                            except:
                                p.close()
                                allmid = aa.getGroup(msg.to).members
                                targets = [i.mid for i in allmid if i.mid not in [user1,user2,helper1,helper2,helper3]]
                                try:
                                    p = Pool(len(targets))
                                    p.map(h1kickBan,targets)
                                    p.close()
                                except:
                                    p.close()
                                    allmid = ab.getGroup(msg.to).members
                                    targets = [i.mid for i in allmid if i.mid not in [user1,user2,helper1,helper2,helper3]]
                                    try:
                                        p = Pool(len(targets))
                                        p.map(h2kickBan,targets)
                                        p.close()
                                    except:
                                        p.close()
                                        allmid = ac.getGroup(msg.to).members
                                        targets = [i.mid for i in allmid if i.mid not in [user1,user2,helper1,helper2,helper3]]
                                        try:
                                            p = Pool(len(targets))
                                            p.map(h3kickBan,targets)
                                            p.close()
                                        except:
                                            p.close()
                            try:
                                gs = ac.getGroup(msg.to)
                                gMembMids = [contact.mid for contact in gs.invitee]
                                for i in gMembMids:
                                    ac.cancelGroupInvitation(msg.to,[i])
                            except Exception as e:
                                p.close()
                                print(e)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:version":
                if msg.toType != 0:
                    kk.sendText(msg.to,"Tyfe ("+tyfeversion+")")
                else:
                    kk.sendText(msg.from_,"Tyfe ("+tyfeversion+")")
            elif "tyfe:google " in msg.text.lower():
                spl = re.split("tyfe:google ",msg.text,flags=re.IGNORECASE)
                if spl[0] == "":
                    if spl[1] != "":
                        try:
                            if msg.toType != 0:
                                kk.sendText(msg.to,"กำลังรับข้อมูล กรุณารอสักครู่..")
                            else:
                                kk.sendText(msg.from_,"กำลังรับข้อมูล กรุณารอสักครู่..")
                            resp = BeautifulSoup(requests.get("https://www.google.co.th/search",params={"q":spl[1],"gl":"th"}).content,"html.parser")
                            text = "ผลการค้นหาจาก Google:\n\n"
                            for el in resp.findAll("h3",attrs={"class":"r"}):
                                try:
                                    tmp = el.a["class"]
                                    continue
                                except:
                                    pass
                                try:
                                    if el.a["href"].startswith("/search?q="):
                                        continue
                                except:
                                    continue
                                text += el.a.text+"\n"
                                text += str(el.a["href"][7:]).split("&sa=U")[0]+"\n\n"
                            text = text[:-2]
                            if msg.toType != 0:
                                kk.sendText(msg.to,str(text))
                            else:
                                kk.sendText(msg.from_,str(text))
                        except Exception as e:
                            print(e)
            elif msg.text.lower().startswith("tyfe:gac "):
                pnum = re.split("tyfe:gac ",msg.text,flags=re.IGNORECASE)[1]
                pnum = "66"+pnum[1:]
                GACReq = GACSender.send(pnum)
                now2 = datetime.datetime.now()
                nowT = datetime.datetime.strftime(now2,"%H")
                nowM = datetime.datetime.strftime(now2,"%M")
                nowS = datetime.datetime.strftime(now2,"%S")
                tm = "\n\n"+nowT+":"+nowM+":"+nowS
                if GACReq.responseNum == 0:
                    if msg.toType != 0:
                        kk.sendText(msg.to,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)"+tm)
                elif GACReq.responseNum == 1:
                    if msg.toType != 0:
                        kk.sendText(msg.to,"ไม่สามารถส่ง SMS ได้ เนื่องจากมีการส่งข้อความไปยังเบอร์เป้าหมายในเวลาที่ใกล้เคียงกันมากเกินไป (｀・ω・´)\nกรุณารออย่างมาก 30 วินาทีแล้วลองอีกครั้ง"+tm)
                    else:
                        kk.sendText(msg.from_,"ไม่สามารถส่ง SMS ได้ เนื่องจากมีการส่งข้อความไปยังเบอร์เป้าหมายในเวลาที่ใกล้เคียงกันมากเกินไป (｀・ω・´)\nกรุณารออย่างมาก 30 วินาทีแล้วลองอีกครั้ง"+tm)
                else:
                    if msg.toType != 0:
                        kk.sendText(msg.to,"พบข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"พบข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:2captcha:key":
                global captkey
                if msg.from_ == user1:
                    if captkey != "":
                        if msg.toType != 0:
                            kk.sendText(msg.to,captkey)
                        else:
                            kk.sendText(msg.from_,captkey)
                    else:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.toType != 0:
                            kk.sendText(msg.to,"ไม่พบการตั้งค่า (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.from_,"ไม่พบการตั้งค่า (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower().startswith("tyfe:2captcha:key "):
                if msg.from_ == user1:
                    captkey = re.split("tyfe:2captcha:key ",msg.text,flags=re.IGNORECASE)[1]
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"ตั้งค่าสำเร็จแล้ว (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"ตั้งค่าสำเร็จแล้ว (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower().startswith("tyfe:sms "):
                if msg.from_ == user1:
                    if captkey != "":
                        data = msg.text.split(" ",2)
                        phoneNumber = "+66 "+data[1][1:]
                        message = data[2]
                        if isEnglish(message):
                            proc = Process(target=sendSMS,args=(phoneNumber,message,captkey,msg))
                            proc.start()
                        else:
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            if msg.toType != 0:
                                kk.sendText(msg.to,"สามารถส่งข้อความได้เฉพาะภาษาอังกฤษ (｀・ω・´)"+tm)
                            else:
                                kk.sendText(msg.from_,"สามารถส่งข้อความได้เฉพาะภาษาอังกฤษ (｀・ω・´)"+tm)
                    else:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        if msg.toType != 0:
                            kk.sendText(msg.to,"กรุณาตั้งค่า key สำหรับ 2captcha ก่อน (｀・ω・´)"+tm)
                        else:
                            kk.sendText(msg.from_,"กรุณาตั้งค่า key สำหรับ 2captcha ก่อน (｀・ω・´)"+tm)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คุณไม่มีสิทธิ์ใช้คำสั่งนี้ (｀・ω・´)"+tm)
            elif msg.text.lower().startswith("tyfe:ctt "):
                try:
                    text = msg.text.split(" ",1)[1]
                    headers = {
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
                    }
                    data = {
                    "q":text
                    }
                    conv = BeautifulSoup(requests.post("http://lullar-de-2.appspot.com/",headers=headers,data=data).content,"html.parser").find("span",attrs={"style":"font-size:40px"}).text
                    if msg.toType != 0:
                        kk.sendText(msg.to,"Conversion:\n"+conv)
                    else:
                        kk.sendText(msg.from_,"Conversion:\n"+conv)
                except Exception as e:
                    print(e)
            elif msg.text.lower() == "tyfe:set":
                if msg.toType != 0:
                    settingshelp = """เช็คการตั้งค่า:
Tyfe:set:check"""
                    kk.sendText(msg.to,settingshelp)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น (｀・ω・´)"+tm)
            elif msg.text.lower() == "tyfe:set:check":
                if msg.toType != 0:
                    val1 = "Off"
                    val2 = "Off"
                    val3 = "Off"
                    val4 = "Off"
                    if msg.to not in preventBlockURL:
                        val1 = "On"
                    if msg.to in blockInvite:
                        val2 = "On"
                    if msg.to in kickLockList:
                        val3 = "On"
                    if msg.to in botProtect:
                        val4 = "On"
                    settingsmsg = """Block URL: %s
Block invitation: %s
Prevent kick: %s
Bot protect: %s""" % (val1,val2,val3,val4)
                    kk.sendText(msg.to,settingsmsg)
                else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น (｀・ω・´)"+tm)
            elif "tyfe:" in msg.text.lower():
                spl = re.split("tyfe:",msg.text,flags=re.IGNORECASE)
                if spl[0] == "":
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    if msg.toType != 0:
                        kk.sendText(msg.to,"คำสั่งที่ไม่รู้จัก (｀・ω・´)"+tm)
                    else:
                        kk.sendText(msg.from_,"คำสั่งที่ไม่รู้จัก (｀・ω・´)"+tm)
            elif msg.text.lower() in dangerMessage:
                try:
                    if msg.toType == 2 and msg.to in botProtect:
                        tmpl = []
                        if msg.to in banned:
                            tmpl = banned[msg.to]
                        banned[msg.to] = []
                        if msg.from_ not in tmpl and msg.from_ not in [user1,user2,helper1,helper2,helper3]:
                            banned[msg.to].append(msg.from_)
                        if tmpl != []:
                            for oldtarg in tmpl:
                                banned[msg.to].append(oldtarg)
                        setKick(msg.to,msg.from_,True)
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(msg.to,"ตรวจพบคำสั่งของบอทลบกลุ่ม จำเป็นต้องนำออกเพื่อความปลอดภัยของสมาชิก (｀・ω・´)"+tm)
                        msg.contentType = 13
                        msg.text = None
                        msg.contentMetadata = {'mid':msg.from_}
                        kk.sendMessage(msg)
                except:
                    pass
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                if msg.toType == 0:
                    msg.to = msg.from_
                msg.from_ = user2
                try:
                    kk.sendMessage(msg)
                except:
                    pass
                if TyfeHelperLogged:
                    try:
                        msg.from_ = helper1
                        aa.sendMessage(msg)
                    except:
                        pass
                    try:
                        msg.from_ = helper2
                        ab.sendMessage(msg)
                    except:
                        pass
                    try:
                        msg.from_ = helper3
                        ac.sendMessage(msg)
                    except:
                         pass
            if msg.from_ == user1:
                seeall[msg.to] = []
    except AttributeError:
        pass
    except Exception as error:
        print(error)

def helper1script(op):
    global kickLockList
    global banned
    global tadmin
    try:
        if op.type == 19 and op.param3 == helper1:
            gotk = aa
            kickname = None
            kickname = kk.getContact(op.param2).displayName
            for i in [aa,ab,ac]:
                if kickname == None:
                    kickname = i.getContact(op.param2).displayName
            if kickname == None:
                kickname = cl.getContact(op.param2).displayName
            if not (any(word in kickname for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or kickname.isdigit()):
                isNotAdmin = False
                if op.param2 not in [user1,user2,helper1,helper2,helper3] and not (op.param1 in tadmin and op.param2 in tadmin[op.param1]):
                    isNotAdmin = True
                if isNotAdmin:
                    tmpl = []
                    if op.param1 in banned:
                        tmpl = banned[op.param1]
                    banned[op.param1] = []
                    if op.param2 not in tmpl:
                        banned[op.param1].append(op.param2)
                    if tmpl != []:
                        for oldtarg in tmpl:
                            banned[op.param1].append(oldtarg)
                x = None
                alive = None
                x = kk.getGroup(op.param1)
                for i in [aa,ab,ac]:
                    if x == None:
                        x = i.getGroup(op.param1)
                if x == None:
                    x = cl.getGroup(op.param1)
                mingr = [i.mid for i in x.members]
                if user2 in mingr:
                    alive = kk
                elif helper1 in mingr:
                    alive = aa
                elif helper2 in mingr:
                    alive = ab
                elif helper3 in mingr:
                    alive = ac
                elif user1 in mingr:
                    alive = cl
                defclose = False
                if x.preventJoinByTicket == False:
                    ticket = alive.reissueGroupTicket(op.param1)
                    gotk.acceptGroupInvitationByTicket(op.param1,ticket)
                    defclose = False
                else:
                    sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                    if sirilist == []:
                        x.preventJoinByTicket = False
                        alive.updateGroup(x)
                        ticket = alive.reissueGroupTicket(op.param1)
                        gotk.acceptGroupInvitationByTicket(op.param1,ticket)
                        defclose = True
                    else:
                        alive.inviteIntoGroup(op.param1,[op.param3])
                        try:
                            gotk.acceptGroupInvitation(op.param1)
                        except:
                            pass
                if defclose:
                    x.preventJoinByTicket = True
                    alive.updateGroup(x)
                if isNotAdmin:
                    setKick(op.param1,op.param2,True)
                now2 = datetime.datetime.now()
                nowT = datetime.datetime.strftime(now2,"%H")
                nowM = datetime.datetime.strftime(now2,"%M")
                nowS = datetime.datetime.strftime(now2,"%S")
                tm = "\n\n"+nowT+":"+nowM+":"+nowS
                kk.sendText(op.param1,"สมาชิกไม่ได้รับอนุญาตให้ลบบัญชีนี้ （´・ω・｀）\nพิมพ์ 「Tyfe:halt」 ในกรณีที่ต้องการนำบอทออกจากกลุ่ม"+tm)
                msg = Message()
                msg.to = op.param1
                msg.from_ = user2
                msg.contentType = 13
                msg.text = None
                msg.contentMetadata = {'mid': op.param2}
                kk.sendMessage(msg)
    except AttributeError:
        pass
    except Exception as e:
        print(e)

def helper2script(op):
    global kickLockList
    global banned
    global tadmin
    try:
        if op.type == 19 and op.param3 == helper2:
            gotk = ab
            kickname = None
            kickname = kk.getContact(op.param2).displayName
            for i in [aa,ab,ac]:
                if kickname == None:
                    kickname = i.getContact(op.param2).displayName
            if kickname == None:
                kickname = cl.getContact(op.param2).displayName
            if not (any(word in kickname for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or kickname.isdigit()):
                isNotAdmin = False
                if op.param2 not in [user1,user2,helper1,helper2,helper3] and not (op.param1 in tadmin and op.param2 in tadmin[op.param1]):
                    isNotAdmin = True
                if isNotAdmin:
                    tmpl = []
                    if op.param1 in banned:
                        tmpl = banned[op.param1]
                    banned[op.param1] = []
                    if op.param2 not in tmpl:
                        banned[op.param1].append(op.param2)
                    if tmpl != []:
                        for oldtarg in tmpl:
                            banned[op.param1].append(oldtarg)
                x = None
                alive = None
                x = kk.getGroup(op.param1)
                for i in [aa,ab,ac]:
                    if x == None:
                        x = i.getGroup(op.param1)
                if x == None:
                    x = cl.getGroup(op.param1)
                mingr = [i.mid for i in x.members]
                if user2 in mingr:
                    alive = kk
                elif helper1 in mingr:
                    alive = aa
                elif helper2 in mingr:
                    alive = ab
                elif helper3 in mingr:
                    alive = ac
                elif user1 in mingr:
                    alive = cl
                defclose = False
                if x.preventJoinByTicket == False:
                    ticket = alive.reissueGroupTicket(op.param1)
                    gotk.acceptGroupInvitationByTicket(op.param1,ticket)
                    defclose = False
                else:
                    sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                    if sirilist == []:
                        x.preventJoinByTicket = False
                        alive.updateGroup(x)
                        ticket = alive.reissueGroupTicket(op.param1)
                        gotk.acceptGroupInvitationByTicket(op.param1,ticket)
                        defclose = True
                    else:
                        alive.inviteIntoGroup(op.param1,[op.param3])
                        try:
                            gotk.acceptGroupInvitation(op.param1)
                        except:
                            pass
                if defclose:
                    x.preventJoinByTicket = True
                    alive.updateGroup(x)
                if isNotAdmin:
                    setKick(op.param1,op.param2,True)
                now2 = datetime.datetime.now()
                nowT = datetime.datetime.strftime(now2,"%H")
                nowM = datetime.datetime.strftime(now2,"%M")
                nowS = datetime.datetime.strftime(now2,"%S")
                tm = "\n\n"+nowT+":"+nowM+":"+nowS
                kk.sendText(op.param1,"สมาชิกไม่ได้รับอนุญาตให้ลบบัญชีนี้ （´・ω・｀）\nพิมพ์ 「Tyfe:halt」 ในกรณีที่ต้องการนำบอทออกจากกลุ่ม"+tm)
                msg = Message()
                msg.to = op.param1
                msg.from_ = user2
                msg.contentType = 13
                msg.text = None
                msg.contentMetadata = {'mid': op.param2}
                kk.sendMessage(msg)
    except AttributeError:
        pass
    except Exception as e:
        print(e)

def helper3script(op):
    global kickLockList
    global banned
    global tadmin
    try:
        if op.type == 19 and op.param3 == helper3:
            gotk = ac
            kickname = None
            kickname = kk.getContact(op.param2).displayName
            for i in [aa,ab,ac]:
                if kickname == None:
                    kickname = i.getContact(op.param2).displayName
            if kickname == None:
                kickname = cl.getContact(op.param2).displayName
            if not (any(word in kickname for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or kickname.isdigit()):
                isNotAdmin = False
                if op.param2 not in [user1,user2,helper1,helper2,helper3] and not (op.param1 in tadmin and op.param2 in tadmin[op.param1]):
                    isNotAdmin = True
                if isNotAdmin:
                    tmpl = []
                    if op.param1 in banned:
                        tmpl = banned[op.param1]
                    banned[op.param1] = []
                    if op.param2 not in tmpl:
                        banned[op.param1].append(op.param2)
                    if tmpl != []:
                        for oldtarg in tmpl:
                            banned[op.param1].append(oldtarg)
                x = None
                alive = None
                x = kk.getGroup(op.param1)
                for i in [aa,ab,ac]:
                    if x == None:
                        x = i.getGroup(op.param1)
                if x == None:
                    x = cl.getGroup(op.param1)
                mingr = [i.mid for i in x.members]
                if user2 in mingr:
                    alive = kk
                elif helper1 in mingr:
                    alive = aa
                elif helper2 in mingr:
                    alive = ab
                elif helper3 in mingr:
                    alive = ac
                elif user1 in mingr:
                    alive = cl
                defclose = False
                if x.preventJoinByTicket == False:
                    ticket = alive.reissueGroupTicket(op.param1)
                    gotk.acceptGroupInvitationByTicket(op.param1,ticket)
                    defclose = False
                else:
                    sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                    if sirilist == []:
                        x.preventJoinByTicket = False
                        alive.updateGroup(x)
                        ticket = alive.reissueGroupTicket(op.param1)
                        gotk.acceptGroupInvitationByTicket(op.param1,ticket)
                        defclose = True
                    else:
                        alive.inviteIntoGroup(op.param1,[op.param3])
                        try:
                            gotk.acceptGroupInvitation(op.param1)
                        except:
                            pass
                if defclose:
                    x.preventJoinByTicket = True
                    alive.updateGroup(x)
                if isNotAdmin:
                    setKick(op.param1,op.param2,True)
                now2 = datetime.datetime.now()
                nowT = datetime.datetime.strftime(now2,"%H")
                nowM = datetime.datetime.strftime(now2,"%M")
                nowS = datetime.datetime.strftime(now2,"%S")
                tm = "\n\n"+nowT+":"+nowM+":"+nowS
                kk.sendText(op.param1,"สมาชิกไม่ได้รับอนุญาตให้ลบบัญชีนี้ （´・ω・｀）\nพิมพ์ 「Tyfe:halt」 ในกรณีที่ต้องการนำบอทออกจากกลุ่ม"+tm)
                msg = Message()
                msg.to = op.param1
                msg.from_ = user2
                msg.contentType = 13
                msg.text = None
                msg.contentMetadata = {'mid': op.param2}
                kk.sendMessage(msg)
    except AttributeError:
        pass
    except Exception as e:
        print(e)

"""try:
    def autoLike():
        while True:
            if TyfeLogged:
                try:
                    hasil = kk.activity(limit=1)
                    for i in range(0,5):
                        if autoLikeSetting["doLike"]:
                            if hasil['result']['posts'][i]['postInfo']['liked'] == False:
                                kk.like(hasil['result']['posts'][i]['userInfo']['mid'],hasil['result']['posts'][i]['postInfo']['postId'],likeType=autoLikeSetting["type"])
                                if autoLikeSetting["doComment"]:
                                    kk.comment(hasil['result']['posts'][i]['userInfo']['mid'],hasil['result']['posts'][i]['postInfo']['postId'],autoLikeSetting["comment"])
                except:
                    pass
            else:
                time.sleep(0.1)
    thread2 = threading.Thread(target=autoLike)
    thread2.daemon = True
    thread2.start()
except:
    pass"""

def antoLoop():
    anto.loop(antoloop)
thread3 = threading.Thread(target=antoLoop)
thread3.daemon = True
thread3.start()

try:
    def user2run():
        while True:
            try:
                if TyfeLogged == True:
                    try:
                        Ops = kk.fetchOps(kk.Poll.rev, 5)
                    except EOFError:
                        raise Exception("It might be wrong revision\n" + str(kk.Poll.rev))
                    for Op in Ops:
                        if (Op.type != 0 and Op.type != OpType.END_OF_OPERATION):
                            kk.Poll.rev = max(kk.Poll.rev, Op.revision)
                            user2script(Op)
                else:
                    time.sleep(0.1)
            except:
                pass
    threadTOP = threading.Thread(target=user2run)
    threadTOP.daemon = True
    threadTOP.start()
except:
    pass

try:
    def helper1run():
        while True:
            try:
                if TyfeHelperLogged == True:
                    try:
                        Ops = aa.fetchOps(aa.Poll.rev, 5)
                    except EOFError:
                        raise Exception("It might be wrong revision\n" + str(aa.Poll.rev))
                    for Op in Ops:
                        if (Op.type != 0 and Op.type != OpType.END_OF_OPERATION):
                            aa.Poll.rev = max(aa.Poll.rev, Op.revision)
                            helper1script(Op)
                else:
                    time.sleep(0.1)
            except:
                pass
    threadTOPH1 = threading.Thread(target=helper1run)
    threadTOPH1.daemon = True
    threadTOPH1.start()
except:
    pass

try:
    def helper2run():
        while True:
            try:
                if TyfeHelperLogged == True:
                    try:
                        Ops = ab.fetchOps(ab.Poll.rev, 5)
                    except EOFError:
                        raise Exception("It might be wrong revision\n" + str(ab.Poll.rev))
                    for Op in Ops:
                        if (Op.type != 0 and Op.type != OpType.END_OF_OPERATION):
                            ab.Poll.rev = max(ab.Poll.rev, Op.revision)
                            helper2script(Op)
                else:
                    time.sleep(0.1)
            except:
                pass
    threadTOPH2 = threading.Thread(target=helper2run)
    threadTOPH2.daemon = True
    threadTOPH2.start()
except:
    pass

try:
    def helper3run():
        while True:
            try:
                if TyfeHelperLogged == True:
                    try:
                        Ops = ac.fetchOps(ac.Poll.rev, 5)
                    except EOFError:
                        raise Exception("It might be wrong revision\n" + str(ac.Poll.rev))
                    for Op in Ops:
                        if (Op.type != 0 and Op.type != OpType.END_OF_OPERATION):
                            ac.Poll.rev = max(ac.Poll.rev, Op.revision)
                            helper3script(Op)
                else:
                    time.sleep(0.1)
            except:
                pass
    threadTOPH3 = threading.Thread(target=helper3run)
    threadTOPH3.daemon = True
    threadTOPH3.start()
except:
    pass

try:
    def mainop():
        try:
            while True:
                try:
                    Ops = cl.fetchOps(cl.Poll.rev, 5)
                except EOFError:
                    raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))
                for Op in Ops:
                    if (Op.type != 0 and Op.type != OpType.END_OF_OPERATION):
                        cl.Poll.rev = max(cl.Poll.rev, Op.revision)
                        user1script(Op)
        except Exception as e:
            with open('tval.pkl', 'wb') as f:
                pickle.dump([seeall,tadmin,banned,kickLockList,autoLikeSetting,save1,wait,botProtect,save2,dublist,blockInvite,jfkeyword,join_delay,join_time,joinDetail,preventBlockURL,tyfeFollow,autoDeny,mentmedat], f)
            print("[Halt] Variable saved ( ",end="")
            print(e,end="")
            print(" )\n")
            os._exit(1)
    mainopstarter = threading.Thread(target=mainop)
    mainopstarter.daemon = True
    mainopstarter.start()
except:
    pass

try:
    while True:
        time.sleep(300)
except:
    with open('tval.pkl', 'wb') as f:
        pickle.dump([seeall,tadmin,banned,kickLockList,autoLikeSetting,save1,wait,botProtect,save2,dublist,blockInvite,jfkeyword,join_delay,join_time,joinDetail,preventBlockURL,tyfeFollow,autoDeny,mentmedat], f)
    print("[keyboardInterrupt] Variable saved")
