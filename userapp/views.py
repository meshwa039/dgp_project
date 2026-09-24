from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import datetime
import mysql.connector
from django.core.files.storage import FileSystemStorage
import json
from django.http import JsonResponse



def getdb():
    mydb = mysql.connector.connect(host="localhost",user="root", passwd="",database="digital_db") 
    return mydb

# Create your views here.
def uindex(request):
    try:
        self = "select * from feedback_tb where f_status = 'Active' order by f_id desc" 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(self)
        f_data = mycursor.fetchall()

        return render(request,'uindex.html',{'f_data': f_data})
       

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 

def usignup(request):
    try:
        msg = ""
        if request.POST:
            u_name = request.POST.get("u_name")
            u_contact = request.POST.get("u_contact")
            u_aadharnumber = request.POST.get("u_aadharnumber")
           
            u_img = request.FILES["u_img"]
            img = FileSystemStorage()
            u_img = img.save(u_img.name,u_img)

            u_idprf = request.FILES["u_idproof"]
            img1 = FileSystemStorage()
            u_idproof = img1.save(u_idprf.name,u_idprf)

            u_password = request.POST.get("u_password")
            
            u_status = "Active"

            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            #insert query
            sel = "select * from user_tb where `u_contact` = '"+str(u_contact)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(sel)
            udata = mycursor.fetchall()

            if len(udata) > 0:
           
                msg = "Sorry This Contact Number Is Already Exists...!"
                

                alldata = {
                    'msg':msg,
                  
                }
                return render(request,'usignup.html',alldata)
            else:
                ins = "INSERT INTO `user_tb`(`u_name`, `u_image`, `u_idproof`, `u_contact`, `u_aadharnumber`, `u_password`, `u_status`, `u_cdate`, `u_udate`) VALUES ('"+str(u_name)+"','"+str(u_img)+"','"+str(u_idproof)+"','"+str(u_contact)+"','"+str(u_aadharnumber)+"','"+str(u_password)+"','"+str(u_status)+"','"+cdate+"','"+cdate+"')"
                print(ins)#query exe - run
                mydb = getdb()
                mycursor = mydb.cursor()
                mycursor.execute(ins)
                mydb.commit()
                return redirect("usignin")

        else:
          

            alldata = {
                'msg':msg,
               
            }
            
            return render(request,'usignup.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def usignin(request):
    try:
        msg = ""
        if request.POST:
            u_username = request.POST.get("u_contact")
            u_password = request.POST.get("u_password")
           
            #insert query
            sel = "select * from user_tb where `u_contact` = '"+str(u_username)+"' and u_password = '"+str(u_password)+"' and u_status = 'Active'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(sel)
            udata = mycursor.fetchall()

            if len(udata) > 0:
                request.session["uname"] = u_username
                request.session["uimg"] = udata[0][2]
                request.session["userid"] = udata[0][0]
                request.session["utime"] = str(udata[0][9])
        
                return redirect("/")           
            else:
                
                msg = " Invalid Username or Password.!" 
                

                alldata = {
                    'msg':msg
                }

                return render(request,'usignin.html',{'msg':msg})
        else:
           
            alldata = {
                'msg':msg
            }
            return render(request,'usignin.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def usignout(request):
    try:
    
            #variable decleration
            username = request.session["userid"]
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            #insert query

            ins = "UPDATE `user_tb` set `u_udate` = '"+cdate+"' where u_id = '"+str(username)+"'"

            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()

            request.session["uname"] = None
            request.session["uimg"] = None
            request.session["userid"] = None
            request.session["utime"] = None
            
            return redirect("usignin")
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def uprofile(request):
    try:
        if request.POST:
           #variable decleration
           u_edt = request.session["userid"]
           u_name = request.POST.get("u_name")
           
           if request.POST.get("u_img") !="":
               u_image = request.FILES["u_img"]
               img = FileSystemStorage()
               old_img = img.save(u_image.name,u_image)

           else:
               old_img = request.POST.get("old_img")

           
           if request.POST.get("u_idproof") !="":
               u_idproof = request.FILES["u_idproof"]
               img1 = FileSystemStorage()
               old_img1 = img1.save(u_idproof.name,u_idproof)

           else:
               old_img1 = request.POST.get("old_img1")

          
           u_aadharnumber = request.POST.get("u_aadharnumber")
           u_password = request.POST.get("u_password")
           cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           
           #insert query
           ins = "UPDATE user_tb set `u_name` = '"+str(u_name)+"', `u_image` = '"+str(old_img)+"', `u_idproof` = '"+str(old_img1)+"', `u_aadharnumber` = '"+str(u_aadharnumber)+"', `u_password` = '"+str(u_password)+"', `u_udate` = '"+cdate+"' where u_id = '"+str(u_edt)+"'"
           #query exe - run
           mydb = getdb()
           mycursor = mydb.cursor()
           mycursor.execute(ins)
           mydb.commit()
           return redirect("uindex")

        else:
            
            u_edt = request.session["userid"]
            selcat = "select * from user_tb where u_id = '"+str(u_edt)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            u_data = mycursor.fetchall() 
            return render(request,'uprofile.html',{'u_data': u_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned') 

def uforgotpassword(request):
    try:
        msg = ""
        if request.POST:
            u_username = request.POST.get("u_username")
           
            #insert query
            sel = "select * from user_tb where `u_contact` = '"+str(u_username)+"' and u_status = 'Active'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(sel)
            udata = mycursor.fetchall()

            if len(udata) > 0:

                
                alldata = {
                    'msg':msg,
                    'udata':udata
                }

                return render(request,'uforgotpassword.html',alldata)
                
            else:
              

                msg = " Sorry This Contact Number Is Not Registered...!" 
                

                alldata = {
                   
                    'msg':msg
                }

                return render(request,'uforgotpassword.html',alldata)
        else:
  
            alldata = {
             
                'msg':msg
            }
            return render(request,'uforgotpassword.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def uabout(request):
    try:
        
        return render(request,'uabout.html',{})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 

def ucontact(request):
    try:
        if request.POST:
            f_name = request.POST.get("f_name")
            f_contact = request.POST.get("f_contact")
            f_message = request.POST.get("f_message")
            f_status="Deactive"
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ins = "INSERT INTO feedback_tb(f_name, f_contact, f_message, f_status, f_cdate, f_udate) VALUES ('"+str(f_name)+"','"+str(f_contact)+"','"+str(f_message)+"','"+str(f_status)+"','"+cdate+"','"+cdate+"')"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("ucontact")
        else:
            return render(request,'ucontact.html',{})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 

def uservice(request):
    try:
        selcat = "select * from category_tb where cat_status = 'Active' order by cat_id asc" 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(selcat)
        cat_data = mycursor.fetchall()

        return render(request,'uservice.html',{'cat_data': cat_data})
        

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 

def uterms(request):
    try:
        
        return render(request,'uterms.html',{})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 

def ubirth(request):
    try:
       
        if request.POST:
            city_dname = request.POST.get("city_dname")
            city_tname = request.POST.get("city_tname")
            city_vname = request.POST.get("city_vname")
            uid =request.session["userid"]
            b_name = request.POST.get("b_name")
            b_gender = request.POST.get("b_gender")
            b_dob = request.POST.get("b_dob")
            b_place = request.POST.get("b_place")
            b_mother = request.POST.get("b_mother")
            b_father = request.POST.get("b_father")
            b_address = request.POST.get("b_address")
            b_peraddress = request.POST.get("b_peraddress")
            b_relation_name	 = request.POST.get("b_relation_name")
            b_time	 = request.POST.get("b_time")
            b_regdate = request.POST.get("b_regdate")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            eid = "0"
            g_status = "Deactive"
            e_status = "Deactive"

            b_idproof = request.FILES["b_idproof"]
            img = FileSystemStorage()
            b_idproof = img.save(b_idproof.name,b_idproof)

            b_hospitalletter = request.FILES["b_hospitalletter"]
            img1 = FileSystemStorage()
            b_hospitalletter = img1.save(b_hospitalletter.name,b_hospitalletter)

            ins = "INSERT INTO `birth_tb`(`u_id`,`city_dname`, `city_tname`, `city_vname`, `b_name`, `b_gender`, `b_dob`, `b_place`, `b_mother`, `b_father`, `b_address`,`b_peraddress`, `b_relation_name`, `b_time`, `b_regdate`, `e_id`, `g_status`, `e_status`, `b_cdate`, `b_udate`,`b_idproof`,`b_hospitalletter`) VALUES ('"+str(uid)+"','"+str(city_dname)+"','"+str(city_tname)+"','"+str(city_vname)+"','"+str(b_name)+"','"+str(b_gender)+"','"+str(b_dob)+"','"+str(b_place)+"','"+str(b_mother)+"','"+str(b_father)+"','"+str(b_address)+"','"+str(b_peraddress)+"','"+str(b_relation_name	)+"','"+str(b_time)+"','"+str(b_regdate)+"','"+str(eid)+"','"+str(g_status)+"','"+str(e_status)+"','"+cdate+"','"+cdate+"','"+str(b_idproof)+"','"+str(b_hospitalletter)+"')"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("ubirthview")

        

        else:
             selv = "SELECT DISTINCT v_dname FROM village_tb WHERE v_status = 'Active'" 
             # connection create object
             mydb = getdb()
             mycursor = mydb.cursor()
             #query execute
             mycursor.execute(selv)
             d_data = mycursor.fetchall()

             today = datetime.datetime.now().strftime("%Y-%m-%d")

             alldata = {
                 'd_data' : d_data,
                 'today' : today,
             }

             return render(request,'ubirth.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def udeath(request):
    try:
       
        if request.POST:
            e_id = "0"
            uid =request.session["userid"]
            city_dname = request.POST.get("city_dname")
            city_tname = request.POST.get("city_tname")
            city_vname = request.POST.get("city_vname")
            dth_name = request.POST.get("dth_name")
            dth_gender = request.POST.get("dth_gender")
            dth_time = request.POST.get("dth_time")
            dth_place = request.POST.get("dth_place")
            dth_mother = request.POST.get("dth_mother")
            dth_father = request.POST.get("dth_father")
            dth_nominy = request.POST.get("dth_nominy")
            dth_type = request.POST.get("dth_type")
            dth_Address	 = request.POST.get("dth_Address")
            dth_Peraddress	 = request.POST.get("dth_Peraddress")
            dth_Deathdate = request.POST.get("dth_Deathdate")
            dth_Relationname = request.POST.get("dth_Relationname")
            dth_Regdate = request.POST.get("dth_Regdate")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            g_status = "Deactive"
            e_status = "Deactive"

            dth_idproof = request.FILES["dth_idproof"]
            img = FileSystemStorage()
            dth_idproof = img.save(dth_idproof.name,dth_idproof)

            dth_hospitalletter = request.FILES["dth_hospitalletter"]
            img1 = FileSystemStorage()
            dth_hospitalletter = img1.save(dth_hospitalletter.name,dth_hospitalletter)
            

            ins = "INSERT INTO `death_tb`(`e_id`,`u_id`,`city_dname`, `city_tname`, `city_vname`, `dth_name`, `dth_gender`, `dth_time`, `dth_place`, `dth_mother`, `dth_father`, `dth_nominy`, `dth_type`, `dth_Address`, `dth_Peraddress`, `dth_Deathdate`, `dth_Relationname`, `dth_Regdate`, `g_status`, `e_status`, `dth_cdate`, `dth_udate`,`dth_idproof`,`dth_hospitalletter`) VALUES ('"+str(e_id)+"','"+str(uid)+"','"+str(city_dname)+"','"+str(city_tname)+"','"+str(city_vname)+"','"+str(dth_name)+"','"+str(dth_gender)+"','"+str(dth_time)+"','"+str(dth_place)+"','"+str(dth_mother)+"','"+str(dth_father)+"','"+str(dth_nominy)+"','"+str(dth_type)+"','"+str(dth_Address)+"','"+str(dth_Peraddress)+"','"+str(dth_Deathdate)+"','"+str(dth_Relationname)+"','"+str(dth_Regdate)+"','"+str(g_status)+"','"+str(e_status)+"','"+cdate+"','"+cdate+"','"+str(dth_idproof)+"','"+str(dth_hospitalletter)+"')"
            print(ins)
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("udeathview")
           

        else:
             selv = "SELECT DISTINCT v_dname FROM village_tb WHERE v_status = 'Active'" 
             # connection create object
             mydb = getdb()
             mycursor = mydb.cursor()
             #query execute
             mycursor.execute(selv)
             d_data = mycursor.fetchall()

             today = datetime.datetime.now().strftime("%Y-%m-%d")

             alldata = {
                 'd_data' : d_data,
                 'today' : today,
             }

   
             return render(request,'udeath.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def ucaste(request):
    try:
       
        if request.POST:
            
            uid = request.session["userid"]
            city_dname = request.POST.get("city_dname")
            city_tname = request.POST.get("city_tname")
            city_vname = request.POST.get("city_vname")
            c_name = request.POST.get("c_name")
            c_gender = request.POST.get("c_gender")
            c_year = request.POST.get("c_year")
            c_address = request.POST.get("c_address")
            c_peraddress = request.POST.get("c_peraddress")
            c_father = request.POST.get("c_father")
            c_regdate = request.POST.get("c_regdate")
            c_blood_relation = request.POST.get("c_blood_relation")
            c_religion	 = request.POST.get("c_religion")
            c_cast_type	 = request.POST.get("c_cast_type")
            c_applyfor = request.POST.get("c_applyfor")
            c_dob = request.POST.get("c_dob")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            e_id = "0"

            g_status = "Deactive"
            e_status = "Deactive"
            c_status = "Reject"

            c_idproof = request.FILES["c_idproof"]
            img = FileSystemStorage()
            c_idproof = img.save(c_idproof.name,c_idproof)
            
            #ins = "INSERT INTO `cast_tb`(`u_id`, `city_dname`, `city_tname`, `city_vname`, `c_name`, `c_gender`, `c_year`, `c_address`, `c_peraddress`, `c_father`, `c_regdate`, `c_blood_relation`, `c_religion`, `c_cast_type`, `c_applyfor`, `c_cdate`, `c_udate`,`e_id`, `e_status`, `g_status`, `c_status`, `c_dob`) VALUES ('"+uid+"','"+str(city_dname)+"','"+str(city_tname)+"','"+str(city_vname)+"','"+str(c_name)+"','"+str(c_gender)+"','"+str(c_year)+"','"+str(c_address)+"','"+str(c_peraddress)+"','"+str(c_father)+"','"+str(c_regdate)+"','"+str(c_blood_relation)+"','"+str(c_religion)+"','"+str(c_cast_type)+"','"+str(c_applyfor)+"','"+cdate+"','"+cdate+"','"+str(e_id)+"','"+str(e_status)+"','"+str(g_status)+"','"+str(c_status)+"','"+str(c_dob)+"')"
            ins = "INSERT INTO `cast_tb`(`u_id`, `city_dname`, `city_tname`, `city_vname`, `c_name`, `c_gender`, `c_year`,`c_address`, `c_peraddress`, `c_father`, `c_regdate`, `c_blood_relation`,`c_religion`, `c_cast_type`, `c_applyfor`, `c_cdate`, `c_udate`, `e_id`, `e_status`, `g_status`, `c_status`, `c_dob`, `c_idproof`) VALUES ('"+str(uid)+"','"+str(city_dname)+"','"+str(city_tname)+"','"+str(city_vname)+"','"+str(c_name)+"','"+str(c_gender)+"','"+str(c_year)+"','"+str(c_address)+"','"+str(c_peraddress)+"','"+str(c_father)+"','"+str(c_regdate)+"','"+str(c_blood_relation)+"','"+str(c_religion)+"','"+str(c_cast_type)+"','"+str(c_applyfor)+"','"+cdate+"','"+cdate+"','"+str(e_id)+"','"+str(e_status)+"','"+str(g_status)+"','"+str(c_status)+"','"+str(c_dob)+"','"+str(c_idproof)+"')"
            #print(ins)
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("ucasteview")

            
        
        else:
             selv = "SELECT DISTINCT v_dname FROM village_tb WHERE v_status = 'Active'" 
             # connection create object
             mydb = getdb()
             mycursor = mydb.cursor()
             #query execute
             mycursor.execute(selv)
             d_data = mycursor.fetchall()

             today = datetime.datetime.now().strftime("%Y-%m-%d")

             alldata = {
                 'today' : today,
                 'd_data' : d_data,
             }
   
             return render(request,'ucaste.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def ubirthview(request):
    try:
        if request.GET.get("b_del") !=None:
            b_del = request.GET.get("b_del")
            bdel = "delete from birth_tb where b_id='"+str(b_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(bdel)
            mydb.commit()
            return redirect("ubirthview")   
        else:
            uid = request.session["userid"]
            self = "select * from birth_tb where u_id  = '"+str(uid)+"' order by b_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(self)
            b_data = mycursor.fetchall()

            return render(request,'ubirthview.html',{'b_data':b_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 

def udeathview(request):
    try:
        if request.GET.get("dth_del") !=None:
            dth_del = request.GET.get("dth_del")
            dthdel = "delete from death_tb where dth_id='"+str(dth_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(dthdel)
            mydb.commit()
            return redirect("udeathview")   
        else:
            uid = request.session["userid"]
            self = "select * from death_tb where u_id  = '"+str(uid)+"' order by dth_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(self)
            dth_data = mycursor.fetchall()

            return render(request,'udeathview.html',{'dth_data':dth_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 

def ucasteview(request):
    try:
        if request.GET.get("c_del") !=None:
            c_del = request.GET.get("c_del")
            cdel = "delete from cast_tb where c_id='"+str(c_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cdel)
            mydb.commit()
            return redirect("ucasteview")   
        else:
            uid = request.session["userid"]
            self = "select * from cast_tb where u_id  = '"+str(uid)+"' order by c_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(self)
            c_data = mycursor.fetchall()

            return render(request,'ucasteview.html',{'c_data':c_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 

def utaxview(request):
    try:
        uid = request.session["userid"]
        self = "select * from tax_tb where u_id  = '"+str(uid)+"' order by tx_id desc" 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(self)
        tx_data = mycursor.fetchall()

        return render(request,'utaxview.html',{'tx_data':tx_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 


def uincomeview(request):
    try:
        if request.GET.get("i_del") !=None:
            i_del = request.GET.get("i_del")
            idel = "delete from income_tb where i_id='"+str(i_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(idel)
            mydb.commit()
            return redirect("uincomeview")   
        else:
            uid = request.session["userid"]
            self = "select * from income_tb where u_id  = '"+str(uid)+"' order by i_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(self)
            i_data = mycursor.fetchall()

            return render(request,'uincomeview.html',{'i_data':i_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 

def uincome(request):
    try:
       
        if request.POST:
            e_id = "0"
            uid =request.session["userid"]
            city_dname = request.POST.get("city_dname")
            city_tname = request.POST.get("city_tname")
            city_vname = request.POST.get("city_vname")
            i_name = request.POST.get("i_name")
            i_gender = request.POST.get("i_gender")
            i_address = request.POST.get("i_address")
            i_peraddress = request.POST.get("i_peraddress")
            i_amount = request.POST.get("i_amount")
            i_year = request.POST.get("i_year")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            i_status = "Reject"
            g_status = "Deactive"
            e_status = "Deactive"

            i_pancard = request.FILES["i_pancard"]
            img = FileSystemStorage()
            i_pancard = img.save(i_pancard.name,i_pancard)

            ins = "INSERT INTO `income_tb`(`e_id`,`u_id`,`city_dname`, `city_tname`, `city_vname`, `i_name`, `i_gender`, `i_address`, `i_peraddress`, `i_amount`, `i_year`,`i_status`,`g_status`,`e_status`, `i_cdate`, `i_udate`,`i_pancard`) VALUES ('"+str(e_id)+"','"+str(uid)+"','"+str(city_dname)+"','"+str(city_tname)+"','"+str(city_vname)+"','"+str(i_name)+"','"+str(i_gender)+"','"+str(i_address)+"','"+str(i_peraddress)+"','"+str(i_amount)+"','"+str(i_year)+"','"+str(i_status)+"','"+str(g_status)+"','"+str(e_status)+"','"+cdate+"','"+cdate+"','"+str(i_pancard)+"')"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("uincomeview")

           

        else:
             selv = "SELECT DISTINCT v_dname FROM village_tb WHERE v_status = 'Active'" 
             # connection create object
             mydb = getdb()
             mycursor = mydb.cursor()
             #query execute
             mycursor.execute(selv)
             d_data = mycursor.fetchall()
   
             return render(request,'uincome.html',{'d_data' : d_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def get_taluka(request, district_name):
    query = "SELECT DISTINCT v_tname FROM village_tb WHERE v_status = 'Active' AND v_dname = %s"
    mydb = getdb()
    mycursor = mydb.cursor()
    mycursor.execute(query, (district_name,))
    taluka_data = mycursor.fetchall()
    mycursor.close()
    mydb.close()

    data = [{'name': row[0]} for row in taluka_data]
    return JsonResponse(data, safe=False)

def get_village(request, taluka_name):
    query = "SELECT DISTINCT v_vname FROM village_tb WHERE v_status = 'Active' AND v_tname = %s"
    mydb = getdb()
    mycursor = mydb.cursor()
    mycursor.execute(query, (taluka_name,))
    village_data = mycursor.fetchall()
    mycursor.close()
    mydb.close()

    data = [{'name': row[0]} for row in village_data]
    return JsonResponse(data, safe=False)

def ubirthedit(request):
    try:

        if request.POST:
           #variable decleration
            b_edt = request.GET.get("b_edt")
            city_dname = request.POST.get("city_dname")
            city_tname = request.POST.get("city_tname")
            city_vname = request.POST.get("city_vname")
            b_name = request.POST.get("b_name")
            b_gender = request.POST.get("b_gender")
            b_dob = request.POST.get("b_dob")
            b_place = request.POST.get("b_place")
            b_mother = request.POST.get("b_mother")
            b_father = request.POST.get("b_father")
            b_address = request.POST.get("b_address")
            b_peraddress = request.POST.get("b_peraddress")
            b_relation_name	 = request.POST.get("b_relation_name")
            b_time	 = request.POST.get("b_time")
            b_regdate = request.POST.get("b_regdate")
            
            g_status = "Deactive"
            e_status = "Deactive"

            if request.POST.get("b_idproof") !="":
               b_idproof = request.FILES["b_idproof"]
               img = FileSystemStorage()
               old_img = img.save(b_idproof.name,b_idproof)

            else:
               old_img = request.POST.get("old_img")

            if request.POST.get("b_hospitalletter") !="":
               b_hospitalletter = request.FILES["b_hospitalletter"]
               img = FileSystemStorage()
               old_img1 = img.save(b_hospitalletter.name,b_hospitalletter)

            else:
               old_img1 = request.POST.get("old_img")
            

            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                      
           #insert query
            ins = "UPDATE birth_tb set `city_dname` = '"+str(city_dname)+"',`b_hospitalletter` = '"+str(old_img1)+"', `b_idproof` = '"+str(old_img)+"',`city_tname` = '"+str(city_tname)+"', `city_vname` = '"+str(city_vname)+"', `b_name` = '"+str(b_name)+"', `b_gender` = '"+str(b_gender)+"', `b_dob` = '"+str(b_dob)+"', `b_place` = '"+str(b_place)+"', `b_mother` = '"+str(b_mother)+"', `b_father` = '"+str(b_father)+"', `b_address` = '"+str(b_address)+"', `b_peraddress` = '"+str(b_peraddress)+"', `b_relation_name` = '"+str(b_relation_name)+"', `b_time` = '"+str(b_time)+"', `b_regdate` = '"+str(b_regdate)+"', `g_status` = '"+str(g_status)+"', `e_status` = '"+str(e_status)+"', `b_udate` = '"+cdate+"' where b_id = '"+str(b_edt)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("ubirthview")

        else:
            
            b_edt = request.GET.get("b_edt")
            
            selcat = "select * from birth_tb where b_id = '"+str(b_edt)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            b_data = mycursor.fetchall()

            selv = "SELECT DISTINCT v_dname FROM village_tb WHERE v_status = 'Active'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selv)
            d_data = mycursor.fetchall()

            today = datetime.datetime.now().strftime("%Y-%m-%d")


            alldata = {
                'b_data': b_data,
                'd_data' : d_data,
                'today' : today,


            } 
            return render(request,'ubirthedit.html',alldata)

    except NameError:
        print("internal error")
    except:
        print('Error returned')  

def udeathedit(request):
    try:
       
        if request.POST:
            dth_edt = request.GET.get("dth_edt")
            city_dname = request.POST.get("city_dname")
            city_tname = request.POST.get("city_tname")
            city_vname = request.POST.get("city_vname")
            dth_name = request.POST.get("dth_name")
            dth_gender = request.POST.get("dth_gender")
            dth_time = request.POST.get("dth_time")
            dth_place = request.POST.get("dth_place")
            dth_mother = request.POST.get("dth_mother")
            dth_father = request.POST.get("dth_father")
            dth_nominy = request.POST.get("dth_nominy")
            dth_type = request.POST.get("dth_type")
            dth_Address	 = request.POST.get("dth_Address")
            dth_Peraddress	 = request.POST.get("dth_Peraddress")
            dth_Deathdate = request.POST.get("dth_Deathdate")
            dth_Relationname = request.POST.get("dth_Relationname")
            dth_Regdate = request.POST.get("dth_Regdate")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            g_status = "Deactive"
            e_status = "Deactive"

            if request.POST.get("dth_idproof") !="":
               dth_idproof = request.FILES["dth_idproof"]
               img = FileSystemStorage()
               old_img = img.save(dth_idproof.name,dth_idproof)

            else:
               old_img = request.POST.get("old_img")


            if request.POST.get("dth_hospitalletter") !="":
               dth_hospitalletter = request.FILES["dth_hospitalletter"]
               img = FileSystemStorage()
               old_img1 = img.save(dth_hospitalletter.name,dth_hospitalletter)

            else:
               old_img1 = request.POST.get("old_img")
            

            ins = "UPDATE death_tb set `city_dname` = '"+str(city_dname)+"',`dth_idproof` = '"+str(old_img)+"', `dth_hospitalletter` = '"+str(old_img1)+"', `city_tname` = '"+str(city_tname)+"', `city_vname` = '"+str(city_vname)+"', `dth_name` = '"+str(dth_name)+"', `dth_gender` = '"+str(dth_gender)+"', `dth_time` = '"+str(dth_time)+"', `dth_place` = '"+str(dth_place)+"', `dth_mother` = '"+str(dth_mother)+"', `dth_father` = '"+str(dth_father)+"', `dth_nominy` = '"+str(dth_nominy)+"', `dth_type` = '"+str(dth_type)+"', `dth_Address` = '"+str(dth_Address)+"', `dth_Peraddress` = '"+str(dth_Peraddress)+"', `dth_Deathdate` = '"+str(dth_Deathdate)+"', `dth_Relationname` = '"+str(dth_Relationname)+"', `dth_Regdate` = '"+str(dth_Regdate)+"', `g_status` = '"+str(g_status)+"', `e_status` = '"+str(e_status)+"', `dth_udate` = '"+cdate+"' where dth_id = '"+str(dth_edt)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("udeathview")
           

        else:
            dth_edt = request.GET.get("dth_edt")
            
            selcat = "select * from death_tb where dth_id = '"+str(dth_edt)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            dth_data = mycursor.fetchall()

            selv = "SELECT DISTINCT v_dname FROM village_tb WHERE v_status = 'Active'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selv)
            d_data = mycursor.fetchall()

            today = datetime.datetime.now().strftime("%Y-%m-%d")

            alldata = {
                'dth_data': dth_data,
                'd_data' : d_data,
                'today' : today,

            } 
            return render(request,'udeathedit.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def ucasteedit(request):
    try:
       
        if request.POST:
            #variable decleration
            c_edt = request.GET.get("c_edt")
            city_dname = request.POST.get("city_dname")
            city_tname = request.POST.get("city_tname")
            city_vname = request.POST.get("city_vname")
            c_name = request.POST.get("c_name")
            c_gender = request.POST.get("c_gender")
            c_year = request.POST.get("c_year")
            c_address = request.POST.get("c_address")
            c_peraddress = request.POST.get("c_peraddress")
            c_father = request.POST.get("c_father")
            c_regdate = request.POST.get("c_regdate")
            c_blood_relation = request.POST.get("c_blood_relation")
            c_religion	 = request.POST.get("c_religion")
            c_cast_type	 = request.POST.get("c_cast_type")
            c_applyfor = request.POST.get("c_applyfor")
            c_dob = request.POST.get("c_dob")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            g_status = "Deactive"
            e_status = "Deactive"
            c_status = "Reject"

            if request.POST.get("c_idproof") !="":
               c_idproof = request.FILES["c_idproof"]
               img = FileSystemStorage()
               old_img = img.save(c_idproof.name,c_idproof)

            else:
               old_img = request.POST.get("old_img")
            
            
            ins = "UPDATE cast_tb set `city_dname` = '"+str(city_dname)+"', `c_idproof` = '"+str(old_img)+"' , `city_tname` = '"+str(city_tname)+"', `city_vname` = '"+str(city_vname)+"', `c_name` = '"+str(c_name)+"', `c_gender` = '"+str(c_gender)+"', `c_year` = '"+str(c_year)+"', `c_address` = '"+str(c_address)+"', `c_peraddress` = '"+str(c_peraddress)+"', `c_father` = '"+str(c_father)+"', `c_regdate` = '"+str(c_regdate)+"', `c_blood_relation` = '"+str(c_blood_relation)+"', `c_religion` = '"+str(c_religion)+"', `c_cast_type` = '"+str(c_cast_type)+"', `c_applyfor` = '"+str(c_applyfor)+"', `c_dob` = '"+str(c_dob)+"', `g_status` = '"+str(g_status)+"', `e_status` = '"+str(e_status)+"', `c_status` = '"+str(c_status)+"', `c_udate` = '"+cdate+"' where c_id = '"+str(c_edt)+"'"
            
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("ucasteview")

            
        
        else:
            c_edt = request.GET.get("c_edt")
            
            selcat = "select * from cast_tb where c_id = '"+str(c_edt)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            c_data = mycursor.fetchall()

            selv = "SELECT DISTINCT v_dname FROM village_tb WHERE v_status = 'Active'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selv)
            d_data = mycursor.fetchall()

            today = datetime.datetime.now().strftime("%Y-%m-%d")

            alldata = {
                'c_data': c_data,
                'd_data' : d_data,
                'today' : today, 

            } 
            return render(request,'ucasteedit.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def uincomeedit(request):
    try:
       
        if request.POST:
            i_edt = request.GET.get("i_edt")
            city_dname = request.POST.get("city_dname")
            city_tname = request.POST.get("city_tname")
            city_vname = request.POST.get("city_vname")
            i_name = request.POST.get("i_name")
            i_gender = request.POST.get("i_gender")
            i_address = request.POST.get("i_address")
            i_peraddress = request.POST.get("i_peraddress")
            i_amount = request.POST.get("i_amount")
            i_year = request.POST.get("i_year")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            i_status = "Reject"
            g_status = "Deactive"
            e_status = "Deactive"
            
            if request.POST.get("i_pancard") !="":
               i_pancard = request.FILES["i_pancard"]
               img = FileSystemStorage()
               old_img = img.save(i_pancard.name,i_pancard)

            else:
               old_img = request.POST.get("old_img")

            ins = "UPDATE income_tb set `city_dname` = '"+str(city_dname)+"' , `i_pancard` = '"+str(old_img)+"', `city_tname` = '"+str(city_tname)+"', `city_vname` = '"+str(city_vname)+"', `i_name` = '"+str(i_name)+"', `i_gender` = '"+str(i_gender)+"', `i_address` = '"+str(i_address)+"', `i_peraddress` = '"+str(i_peraddress)+"', `i_amount` = '"+str(i_amount)+"', `i_year` = '"+str(i_year)+"', `i_status` = '"+str(i_status)+"', `g_status` = '"+str(g_status)+"', `e_status` = '"+str(e_status)+"', `i_udate` = '"+cdate+"' where i_id = '"+str(i_edt)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("uincomeview")

           

        else:
            i_edt = request.GET.get("i_edt")
            
            selcat = "select * from income_tb where i_id = '"+str(i_edt)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            i_data = mycursor.fetchall()

            selv = "SELECT DISTINCT v_dname FROM village_tb WHERE v_status = 'Active'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selv)
            d_data = mycursor.fetchall()

            alldata = {
                'i_data': i_data,
                'd_data' : d_data,

            } 
            return render(request,'uincomeedit.html',alldata)

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def ubirthcertificate(request):
    try:
            
        b_id = request.GET.get("b_id")
    
        uid = request.session["userid"]
        selbirth = "select * from birth_tb,user_tb,employee_tb where birth_tb.u_id = user_tb.u_id and employee_tb.e_id=birth_tb.e_id and birth_tb.u_id  = '"+str(uid)+"' and birth_tb.b_id = '"+str(b_id)+"' and birth_tb.g_status='Active' and birth_tb.e_status='Active'" 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(selbirth)
        b_data = mycursor.fetchall()

        return render(request,'ubirthcertificate.html',{'b_data' : b_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned') 

def check_password(request):
    try:
       
        if request.method == "POST":
            data = json.loads(request.body)  
            entered_password = data.get('password')             
            userid = request.session.get("userid")

            if not userid:
                return JsonResponse({'success': False, 'message': 'User not logged in'})

            # Your database query
            sel = "SELECT * FROM user_tb WHERE u_id = %s"
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(sel, [userid])  
            udata = mycursor.fetchall()

            if len(udata) > 0:
                CORRECT_PASSWORD = udata[0][6]
                if entered_password == CORRECT_PASSWORD:
                    return JsonResponse({'success': True})
                else:
                    return JsonResponse({'success': False, 'message': 'Incorrect password'})
            else:
                return JsonResponse({'success': False, 'message': 'User not found'})

        return JsonResponse({'success': False, 'message': 'Invalid request method'})

    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({'success': False, 'message': 'An error occurred during password verification'})

def udeathcertificate(request):
    try:
            
        dth_id = request.GET.get("b_id")
    
        uid = request.session["userid"]
        selbirth = "select * from death_tb,user_tb,employee_tb where death_tb.u_id = user_tb.u_id and employee_tb.e_id=death_tb.e_id and death_tb.u_id  = '"+str(uid)+"' and death_tb.dth_id = '"+str(dth_id)+"' " 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(selbirth)
        dth_data = mycursor.fetchall()

        return render(request,'udeathcertificate.html',{'dth_data' : dth_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def ucastecertificate(request):
    try:
            
        c_id = request.GET.get("b_id")
    
        uid = request.session["userid"]
        selbirth = "select * from cast_tb,user_tb,employee_tb where cast_tb.u_id = user_tb.u_id and employee_tb.e_id=cast_tb.e_id and cast_tb.u_id  = '"+str(uid)+"' and cast_tb.c_id = '"+str(c_id)+"' and cast_tb.g_status='Active' and cast_tb.e_status='Active'" 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(selbirth)
        c_data = mycursor.fetchall()

        
        return render(request,'ucastecertificate.html',{'c_data' : c_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def uincomecertificate(request):
    try:
            
        i_id = request.GET.get("b_id")
    
        uid = request.session["userid"]
        selbirth = "select * from income_tb,user_tb,employee_tb where income_tb.u_id = user_tb.u_id and employee_tb.e_id=income_tb.e_id and income_tb.u_id  = '"+str(uid)+"' and income_tb.i_id = '"+str(i_id)+"' and income_tb.g_status='Active' and income_tb.e_status='Active'" 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(selbirth)
        i_data = mycursor.fetchall()

        return render(request,'uincomecertificate.html',{'i_data' : i_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')


def utaxcertificate(request):
    try:
            
        tx_id = request.GET.get("b_id")
    
        uid = request.session["userid"]
        selbirth = "select * from tax_tb,user_tb,employee_tb where tax_tb.u_id = user_tb.u_id and employee_tb.e_id=tax_tb.e_id and tax_tb.u_id  = '"+str(uid)+"' and tax_tb.tx_id = '"+str(tx_id)+"' and tax_tb.g_status='Active' and tax_tb.e_status='Active'" 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(selbirth)
        tx_data = mycursor.fetchall()

        return render(request,'utaxcertificate.html',{'tx_data' : tx_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

