#coding:utf-8
import copy
from django.http import JsonResponse
from django.apps import apps
from django.db.models.aggregates import Count,Sum
from .models import xueshengshenqing
from util.codes import *
from util.auth import Auth
import util.message as mes

def xueshengshenqing_register(request):
    if request.method in ["POST", "GET"]:
        msg = {'code': normal_code, "msg": mes.normal_code}
        req_dict = request.session.get("req_dict")

        error = xueshengshenqing.createbyreq(xueshengshenqing, xueshengshenqing, req_dict)
        if error != None:
            msg['code'] = crud_error_code
            msg['msg'] = "User already exists!!!"
        return JsonResponse(msg)

def xueshengshenqing_login(request):
    if request.method in ["POST", "GET"]:
        msg = {'code': normal_code, "msg": mes.normal_code}
        req_dict = request.session.get("req_dict")

        datas = xueshengshenqing.getbyparams(xueshengshenqing, xueshengshenqing, req_dict)
        if not datas:
            msg['code'] = password_error_code
            msg['msg'] = mes.password_error_code
            return JsonResponse(msg)
        try:
            __sfsh__= xueshengshenqing.__sfsh__
        except:
            __sfsh__=None

        if  __sfsh__=='yes':
            if datas[0].get('sfsh')=='no':
                msg['code']=other_code
                msg['msg'] = "account locked, contact the admin"
                return JsonResponse(msg)
                
        req_dict['id'] = datas[0].get('id')
        return Auth.authenticate(Auth, xueshengshenqing, req_dict)


def xueshengshenqing_logout(request):
    if request.method in ["POST", "GET"]:
        msg = {
            "msg": "logout success",
            "code": 0
        }

        return JsonResponse(msg)


def xueshengshenqing_resetPass(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code}

        req_dict = request.session.get("req_dict")

        columns=  xueshengshenqing.getallcolumn( xueshengshenqing, xueshengshenqing)

        try:
            __loginUserColumn__= xueshengshenqing.__loginUserColumn__
        except:
            __loginUserColumn__=None
        username=req_dict.get(list(req_dict.keys())[0])
        if __loginUserColumn__:
            username_str=__loginUserColumn__
        else:
            username_str=username
        if 'mima' in columns:
            password_str='mima'
        else:
            password_str='password'

        init_pwd = '123456'

        eval('''xueshengshenqing.objects.filter({}='{}').update({}='{}')'''.format(username_str,username,password_str,init_pwd))
        
        return JsonResponse(msg)



def xueshengshenqing_session(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code,"msg": mes.normal_code, "data": {}}

        req_dict={"id":request.session.get('params').get("id")}
        msg['data']  = xueshengshenqing.getbyparams(xueshengshenqing, xueshengshenqing, req_dict)[0]

        return JsonResponse(msg)


def xueshengshenqing_default(request):

    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code,"msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        req_dict.update({"isdefault":"yes"})
        data=xueshengshenqing.getbyparams(xueshengshenqing, xueshengshenqing, req_dict)
        if len(data)>0:
            msg['data']  = data[0]
        else:
            msg['data']  = {}
        return JsonResponse(msg)

def xueshengshenqing_page(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")

        columns=  xueshengshenqing.getallcolumn( xueshengshenqing, xueshengshenqing)

        tablename = request.session.get("tablename")

        try:
            __authSeparate__=xueshengshenqing.__authSeparate__
        except:
            __authSeparate__=None

        if __authSeparate__=="yes":
            tablename=request.session.get("tablename")
            if tablename!="users" and 'userid' in columns:
                try:
                    req_dict['userid']=request.session.get("params").get("id")
                except:
                    pass

        try:
            __hasMessage__=xueshengshenqing.__hasMessage__
        except:
            __hasMessage__=None
        if  __hasMessage__=="yes":
            tablename=request.session.get("tablename")
            if tablename!="users":
                req_dict["userid"]=request.session.get("params").get("id")

        __isAdmin__ = None

        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__==tablename:

                try:
                    __isAdmin__ = m.__isAdmin__
                except:
                    __isAdmin__ = None
                break

        if  __isAdmin__ == "yes":
            if req_dict.get("userid"):
                del req_dict["userid"]

        else:
            if tablename!="users" and 'xueshengshenqing'[:7]!='discuss'and "userid" in xueshengshenqing.getallcolumn(xueshengshenqing,xueshengshenqing):
                req_dict["userid"] = request.session.get("params").get("id")
        try:
            __authTables__=xueshengshenqing.__authTables__
        except:
            __authTables__=None

        if __authTables__!=None and  __authTables__!={}:
            try:
                del req_dict['userid']
            except:
                pass
            for authColumn,authTable in __authTables__.items():
                if authTable==tablename:
                    params = request.session.get("params")
                    req_dict[authColumn]=params.get(authColumn)
                    break
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  =xueshengshenqing.page(xueshengshenqing, xueshengshenqing, req_dict)

        return JsonResponse(msg)

def xueshengshenqing_autoSort(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")
        if "clicknum"  in xueshengshenqing.getallcolumn(xueshengshenqing,xueshengshenqing):
            req_dict['sort']='clicknum'
        else:
            req_dict['sort']='clicktime'
        req_dict['order']='desc'
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = xueshengshenqing.page(xueshengshenqing,xueshengshenqing, req_dict)

        return JsonResponse(msg)


def xueshengshenqing_list(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")
        columns=  xueshengshenqing.getallcolumn( xueshengshenqing, xueshengshenqing)
        try:
            __foreEndList__=xueshengshenqing.__foreEndList__
        except:
            __foreEndList__=None

        if __foreEndList__=="前要登":
            tablename=request.session.get("tablename")
            if tablename!="users" and 'userid' in columns:
                try:
                    req_dict['userid']=request.session.get("params").get("id")
                except:
                    pass
        #forrEndListAuth
        try:
            __foreEndListAuth__=xueshengshenqing.__foreEndListAuth__
        except:
            __foreEndListAuth__=None


        #authSeparate
        try:
            __authSeparate__=xueshengshenqing.__authSeparate__
        except:
            __authSeparate__=None

        if __foreEndListAuth__ =="yes" and __authSeparate__=="yes":
            tablename=request.session.get("tablename")
            if tablename!="users":
                req_dict['userid']=request.session.get("params",{"id":0}).get("id")

        tablename = request.session.get("tablename")
        if tablename == "users" and req_dict.get("userid") != None:
            del req_dict["userid"]
        else:
            __isAdmin__ = None

            allModels = apps.get_app_config('main').get_models()
            for m in allModels:
                if m.__tablename__==tablename:

                    try:
                        __isAdmin__ = m.__isAdmin__
                    except:
                        __isAdmin__ = None
                    break

            if __isAdmin__ == "yes":
                if req_dict.get("userid"):
                    del req_dict["userid"]
            else:
                if "userid" in columns:
                    try:

                        req_dict['userid']=request.session.get("params").get("id")
                    except:
                            pass
        try:
            __authTables__=xueshengshenqing.__authTables__
        except:
            __authTables__=None

        if __authTables__!=None and  __authTables__!={} and __foreEndListAuth__=="yes":
            try:
                del req_dict['userid']
            except:
                pass
            for authColumn,authTable in __authTables__.items():
                if authTable==tablename:
                    params = request.session.get("params")
                    req_dict[authColumn]=params.get(authColumn)
                    break
        
        if xueshengshenqing.__tablename__[:7]=="discuss":
            try:
                del req_dict['userid']
            except:
                pass
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = xueshengshenqing.page(xueshengshenqing, xueshengshenqing, req_dict)

        return JsonResponse(msg)

def xueshengshenqing_save(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        tablename=request.session.get("tablename")
        __isAdmin__ = None
        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__==tablename:

                try:
                    __isAdmin__ = m.__isAdmin__
                except:
                    __isAdmin__ = None
                break

        columns=  xueshengshenqing.getallcolumn( xueshengshenqing, xueshengshenqing)
        if tablename!='users' and req_dict.get("userid")!=None and 'userid' in columns  and __isAdmin__!='yes':
            params=request.session.get("params")
            req_dict['userid']=params.get('id')


        error= xueshengshenqing.createbyreq(xueshengshenqing,xueshengshenqing, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error

        return JsonResponse(msg)


def xueshengshenqing_add(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")

        columns=  xueshengshenqing.getallcolumn( xueshengshenqing, xueshengshenqing)
        try:
            __authSeparate__=xueshengshenqing.__authSeparate__
        except:
            __authSeparate__=None

        if __authSeparate__=="yes":
            tablename=request.session.get("tablename")
            if tablename!="users" and 'userid' in columns:
                try:
                    req_dict['userid']=request.session.get("params").get("id")
                except:
                    pass

        try:
            __foreEndListAuth__=xueshengshenqing.__foreEndListAuth__
        except:
            __foreEndListAuth__=None

        if __foreEndListAuth__ and __foreEndListAuth__!="no":
            tablename=request.session.get("tablename")
            if tablename!="users":
                req_dict['userid']=request.session.get("params").get("id")

        error= xueshengshenqing.createbyreq(xueshengshenqing,xueshengshenqing, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg)

def xueshengshenqing_thumbsup(request,id_):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        id_=int(id_)
        type_=int(req_dict.get("type",0))
        rets=xueshengshenqing.getbyid(xueshengshenqing,xueshengshenqing,id_)

        update_dict={
        "id":id_,
        }
        if type_==1:
            update_dict["thumbsupnum"]=int(rets[0].get('thumbsupnum'))+1
        elif type_==2:
            update_dict["crazilynum"]=int(rets[0].get('crazilynum'))+1
        error = xueshengshenqing.updatebyparams(xueshengshenqing,xueshengshenqing, update_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg)


def xueshengshenqing_info(request,id_):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}

        data = xueshengshenqing.getbyid(xueshengshenqing,xueshengshenqing, int(id_))
        if len(data)>0:
            msg['data']=data[0]
        try:
            __browseClick__= xueshengshenqing.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__=="yes"  and  "clicknum"  in xueshengshenqing.getallcolumn(xueshengshenqing,xueshengshenqing):
            try:
                clicknum=int(data[0].get("clicknum",0))+1
            except:
                clicknum=0+1
            click_dict={"id":int(id_),"clicknum":clicknum}
            ret=xueshengshenqing.updatebyparams(xueshengshenqing,xueshengshenqing,click_dict)
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return JsonResponse(msg)

def xueshengshenqing_detail(request,id_):

    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}

        data =xueshengshenqing.getbyid(xueshengshenqing,xueshengshenqing, int(id_))
        if len(data)>0:
            msg['data']=data[0]

        try:
            __browseClick__= xueshengshenqing.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__=="yes"   and  "clicknum"  in xueshengshenqing.getallcolumn(xueshengshenqing,xueshengshenqing):
            try:
                clicknum=int(data[0].get("clicknum",0))+1
            except:
                clicknum=0+1
            click_dict={"id":int(id_),"clicknum":clicknum}

            ret=xueshengshenqing.updatebyparams(xueshengshenqing,xueshengshenqing,click_dict)
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = retfo
        return JsonResponse(msg)


def xueshengshenqing_update(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        if req_dict.get("mima") and req_dict.get("password"):
            if "mima" not  in xueshengshenqing.getallcolumn(xueshengshenqing,xueshengshenqing) :
                del req_dict["mima"]
            if  "password" not  in xueshengshenqing.getallcolumn(xueshengshenqing,xueshengshenqing) :
                del req_dict["password"]
        try:
            del req_dict["clicknum"]
        except:
            pass


        error = xueshengshenqing.updatebyparams(xueshengshenqing, xueshengshenqing, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg)


def xueshengshenqing_delete(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")

        error=xueshengshenqing.deletes(xueshengshenqing,
            xueshengshenqing,
             req_dict.get("ids")
        )
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg)


def xueshengshenqing_vote(request,id_):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code}


        data= xueshengshenqing.getbyid(xueshengshenqing, xueshengshenqing, int(id_))
        for i in data:
            votenum=i.get('votenum')
            if votenum!=None:
                params={"id":int(id_),"votenum":votenum+1}
                error=xueshengshenqing.updatebyparams(xueshengshenqing,xueshengshenqing,params)
                if error!=None:
                    msg['code'] = crud_error_code
                    msg['msg'] = error
        return JsonResponse(msg)


