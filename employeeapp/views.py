from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import datetime
import mysql.connector
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse


def getdb():
    mydb = mysql.connector.connect(host="localhost",user="root", passwd="",database="digital_db") 
    return mydb

# Create your views here.
def eindex(request):
    try:
        eid = request.session["eid"] 
        dcount = "select count(dth_id) from death_tb,user_tb,employee_tb where death_tb.u_id=user_tb.u_id and death_tb.e_id=employee_tb.e_id and death_tb.g_status = 'Active' and death_tb.e_id ='"+str(eid)+"' " 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(dcount)
        dth_data = mycursor.fetchall()


        bcount = "select count(b_id) from birth_tb,user_tb,employee_tb where birth_tb.u_id=user_tb.u_id and birth_tb.e_id=employee_tb.e_id and birth_tb.g_status = 'Active' and  birth_tb.e_id ='"+str(eid)+"' " 
            # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(bcount)
        b_data = mycursor.fetchall()


        icount = "select count(i_id) from income_tb,user_tb,employee_tb where income_tb.u_id=user_tb.u_id and income_tb.e_id=employee_tb.e_id and income_tb.g_status = 'Active' and  income_tb.e_id ='"+str(eid)+"' " 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(icount)
        i_data = mycursor.fetchall()


        tcount = "select count(tx_id) from tax_tb,user_tb,employee_tb where tax_tb.u_id=user_tb.u_id and tax_tb.e_id=employee_tb.e_id and  tax_tb.e_id ='"+str(eid)+"' "  
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(tcount)
        tx_data = mycursor.fetchall()


        ccount = "select count(c_id) from cast_tb,user_tb,employee_tb where cast_tb.u_id=user_tb.u_id and cast_tb.e_id=employee_tb.e_id and cast_tb.g_status = 'Active' and  cast_tb.e_id ='"+str(eid)+"' " 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(ccount)
        c_data = mycursor.fetchall()


        vcount = "select count(v_id) from village_tb order by v_id desc" 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(vcount)
        v_data = mycursor.fetchall()


        cacount = "select count(cat_id) from category_tb order by cat_id desc" 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(cacount)
        cat_data = mycursor.fetchall()


        ecount = "select count(e_id) from employee_tb order by e_id desc" 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(ecount)
        e_data = mycursor.fetchall()


        ucount = "select count(u_id) from user_tb order by u_id desc" 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(ucount)
        u_data = mycursor.fetchall()


        fcount = "select count(f_id) from feedback_tb order by f_id desc" 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(fcount)
        f_data = mycursor.fetchall()

        alldata = {
            'dcount':dth_data,
            'bcount':b_data,
            'icount':i_data,
            'tcount':tx_data,
            'ccount':c_data,
            'vcount':v_data,
            'cacount':cat_data,
            'ecount':e_data,
            'ucount':u_data,
            'fcount':f_data,
        }

        return render(request,'eindex.html',alldata)



    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 


def ecategory(request):
    try:
        if request.POST:
            cat_name = request.POST.get("cat_name")
            cat_status = request.POST.get("cat_status")
            cat_img = request.FILES["cat_image"]
            img = FileSystemStorage()
            cat_image = img.save(cat_img.name,cat_img)
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ins = "INSERT INTO category_tb(cat_name, cat_image, cat_status, cat_cdate, cat_udate) VALUES ('"+str(cat_name)+"','"+str(cat_image)+"','"+str(cat_status)+"','"+cdate+"','"+cdate+"')"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("ecategory")
        elif request.GET.get("cat_del") !=None:
            cat_del = request.GET.get("cat_del")
            cdel = "delete from category_tb where cat_id='"+str(cat_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cdel)
            mydb.commit()
            return redirect("ecategory")
        else:   
            selcat = "select * from category_tb order by cat_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            cat_data = mycursor.fetchall()

            return render(request,'ecategory.html',{'cat_data': cat_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 

def ecategoryedit(request):
    try:
        if request.POST:
           #variable decleration
           cat_edt = request.GET.get("cat_edt")
           cat_name = request.POST.get("cat_name")
           
           if request.POST.get("cat_image") !="":
               cat_img = request.FILES["cat_image"]
               img = FileSystemStorage()
               old_img = img.save(cat_img.name,cat_img)

           else:
               old_img = request.POST.get("old_img")

           cat_status = request.POST.get("cat_status")
           cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           
           #insert query
           ins = "UPDATE category_tb set `cat_name` = '"+str(cat_name)+"', `cat_image` = '"+str(old_img)+"', `cat_status` = '"+str(cat_status)+"', `cat_udate` = '"+cdate+"' where cat_id = '"+str(cat_edt)+"'"
           #query exe - run
           mydb = getdb()
           mycursor = mydb.cursor()
           mycursor.execute(ins)
           mydb.commit()
           return redirect("ecategory")

        else:
            
            cat_edt = request.GET.get("cat_edt")
            selcat = "select * from category_tb where cat_id = '"+str(cat_edt)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            cat_data = mycursor.fetchall() 
            return render(request,'ecategoryedit.html',{'cat_data': cat_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')  


def efeedback(request):
    try:
        if request.GET.get("f_del") !=None:
            f_del = request.GET.get("f_del")
            cdel = "delete from feedback_tb where f_id='"+str(f_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cdel)
            mydb.commit()
            return redirect("efeedback")


        elif request.GET.get("feed_id") !=None:
            feed_id = request.GET.get("feed_id")
            feed_status=request.GET.get("feed_status")
            if feed_status=="Active":
                feed_status="Deactive"
            else:
                feed_status="Active"
            #query exe - run
            updatef="update feedback_tb set f_status='"+str(feed_status)+"' where f_id='"+str(feed_id)+"'" 
            
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(updatef)
            mydb.commit()
            return redirect("efeedback")

        else:
            selcat = "select * from feedback_tb order by f_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            f_data = mycursor.fetchall()

            return render(request,'efeedback.html',{'f_data': f_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 

def euser(request):
    try:
        if request.GET.get("user_del") !=None:
            u_del = request.GET.get("user_del")
            cdel = "delete from user_tb where u_id='"+str(u_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cdel)
            mydb.commit()
            return redirect("euser")
        elif request.GET.get("us_id") !=None:
            user_id = request.GET.get("us_id")
            user_status=request.GET.get("us_status")
            if user_status=="Active":
                user_status="Deactive"
            else:
                user_status="Active"
            #query exe - run
            updatef="update user_tb set u_status='"+str(user_status)+"' where u_id='"+str(user_id)+"'" 
            
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(updatef)
            mydb.commit()
            return redirect("euser")

        
        else:
            selcat = "select * from user_tb order by u_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            u_data = mycursor.fetchall()

            return render(request,'euser.html',{'u_data': u_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 

def ebirth(request):
    try:
        if request.GET.get("birth_del") !=None:
            birth_del = request.GET.get("birth_del")
            cdel = "delete from birth_tb where b_id='"+str(birth_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cdel)
            mydb.commit()
            return redirect("ebirth")
        elif request.GET.get("b_id") !=None:
            birth_id = request.GET.get("b_id")
            birth_status = request.GET.get("birth_status")
            if birth_status=="Active":
                birth_status="Deactive"
            else:
                birth_status="Active"
            #query exe - run
            updatef="update birth_tb set e_status='"+str(birth_status)+"' where b_id='"+str(birth_id)+"'" 
            
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(updatef)
            mydb.commit()
            return redirect("ebirth")
        else:
            eid = request.session["eid"] 
            selcat = "select * from birth_tb,user_tb where birth_tb.u_id=user_tb.u_id and birth_tb.g_status = 'Active' and birth_tb.e_id ='"+str(eid)+"' order by b_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            b_data = mycursor.fetchall()

            return render(request,'ebirth.html',{'b_data': b_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 

def ebirthdetails(request):
    try:
        if request.POST:
            birth_id = request.GET.get("birth_id")
            e_id = request.POST.get("b_employee")
            b_remarkdetail = request.POST.get("remark_detail")
            g_status = request.POST.get("a_status")
            e_status = request.POST.get("e_status")
            
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ins = "UPDATE birth_tb set `e_id` = '"+str(e_id)+"', `b_remarkdetail` = '"+str(b_remarkdetail)+"', `g_status` = '"+str(g_status)+"', `e_status` = '"+str(e_status)+"', `b_udate` = '"+cdate+"' where b_id = '"+str(birth_id)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("ebirth")
            
        else:
            birth_id = request.GET.get("birth_id")
            
            selcat = "select * from birth_tb,user_tb where birth_tb.u_id=user_tb.u_id  and b_id = '"+str(birth_id)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            b_data = mycursor.fetchall()

            selemp = "select * from employee_tb" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selemp)
            emp_data = mycursor.fetchall()

            alldata  = {
                'b_data' : b_data,
                'emp_data' : emp_data
            }

            return render(request,'ebirthdetails.html',alldata)

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 

def edeath(request):
    try:
        if request.GET.get("death_del") !=None:
            death_del = request.GET.get("death_del")
            cdel = "delete from death_tb where dth_id='"+str(death_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cdel)
            mydb.commit()
            return redirect("edeath")
        elif request.GET.get("dth_id") !=None:
            death_id = request.GET.get("dth_id")
            death_status = request.GET.get("death_status")
            if death_status=="Active":
                death_status="Deactive"
            else:
                death_status="Active"
            #query exe - run
            updatef="update death_tb set e_status='"+str(death_status)+"' where dth_id='"+str(death_id)+"'" 
            
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(updatef)
            mydb.commit()
            return redirect("edeath")
        else:
            eid = request.session["eid"] 
            selcat = "select * from death_tb,user_tb where death_tb.u_id=user_tb.u_id and death_tb.g_status = 'Active' and  death_tb.e_id ='"+str(eid)+"' order by dth_id desc"  
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            dth_data = mycursor.fetchall()

            return render(request,'edeath.html',{'dth_data': dth_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 

def edeathdetails(request):
    try:
        if request.POST:
            death_id = request.GET.get("death_id")
            e_id = request.POST.get("dth_employee")
            dth_Remarkdetail = request.POST.get("remark_detail")
            g_status = request.POST.get("a_status")
            e_status = request.POST.get("e_status")
            
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            if g_status == 'Active' and e_status == 'Active':
                dth_issuedate = datetime.datetime.now().strftime("%Y-%m-%d")
                ins = "UPDATE death_tb set `e_id` = '"+str(e_id)+"', `dth_Remarkdetail` = '"+str(dth_Remarkdetail)+"', `g_status` = '"+str(g_status)+"', `e_status` = '"+str(e_status)+"', `dth_udate` = '"+cdate+"', `dth_issuedate` = '"+dth_issuedate+"' where dth_id = '"+str(death_id)+"'"
            else:
                ins = "UPDATE death_tb set `e_id` = '"+str(e_id)+"', `dth_Remarkdetail` = '"+str(dth_Remarkdetail)+"', `g_status` = '"+str(g_status)+"', `e_status` = '"+str(e_status)+"', `dth_udate` = '"+cdate+"' where dth_id = '"+str(death_id)+"'"

            #print(ins)#query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("edeath")
            
        else:
            death_id = request.GET.get("death_id")
            
            selcat = "select * from death_tb,user_tb where death_tb.u_id=user_tb.u_id and dth_id = '"+str(death_id)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            dth_data = mycursor.fetchall()

            selemp = "select * from employee_tb" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selemp)
            emp_data = mycursor.fetchall()

            alldata  = {
                'dth_data' : dth_data,
                'emp_data' : emp_data
            }

            return render(request,'edeathdetails.html',alldata)

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 

def etax(request):
    try:
        if request.POST:
            eid = request.session["eid"] 
            u_id = request.POST.get("u_id")
            city_dname = request.POST.get("city_dname")
            city_tname = request.POST.get("city_tname")
            city_vname = request.POST.get("city_vname")
            tx_name = request.POST.get("tx_name")
            tx_gender = request.POST.get("tx_gender")
            tx_address = request.POST.get("tx_address")
            tx_peraddress = request.POST.get("tx_peraddress")
            tx_home = request.POST.get("tx_home")
            tx_sqrt = request.POST.get("tx_sqrt")
            tx_amount = request.POST.get("tx_amount")
            tx_year = request.POST.get("tx_year")
            tx_outstanding = request.POST.get("tx_outstanding")

            
            tx_total = request.POST.get("tx_total")
            tx_issue = request.POST.get("tx_issue")
            tx_status = request.POST.get("tx_status")
            e_status = request.POST.get("e_status")
            g_status = "Deactive"
            tx_remarkdetail = request.POST.get("tx_remarkdetail")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            ins = "INSERT INTO tax_tb (e_id,u_id,city_dname,city_tname,city_vname,tx_name,tx_gender,tx_address,tx_peraddress,tx_home,tx_sqrt,tx_amount,tx_year,tx_outstanding,tx_total,tx_issue,tx_status,e_status,g_status,tx_remarkdetail,tx_cdate,tx_udate) VALUES ('"+str(eid)+"','"+str(u_id)+"','"+str(city_dname)+"','"+str(city_tname)+"','"+str(city_vname)+"','"+str(tx_name)+"','"+str(tx_gender)+"','"+str(tx_address)+"','"+str(tx_peraddress)+"','"+str(tx_home)+"','"+str(tx_sqrt)+"','"+str(tx_amount)+"','"+str(tx_year)+"','"+str(tx_outstanding)+"','"+str(tx_total)+"','"+str(tx_issue)+"','"+str(tx_status)+"','"+str(e_status)+"','"+str(g_status)+"','"+str(tx_remarkdetail)+"','"+cdate+"','"+cdate+"')"
            
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("etax")

        elif request.GET.get("tax_del") !=None:
            tax_del = request.GET.get("tax_del")
            cdel = "delete from tax_tb where tx_id='"+str(tax_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cdel)
            mydb.commit()
            return redirect("etax")

        elif request.GET.get("tx_id") !=None:
            tax_id = request.GET.get("tx_id")
            tax_status = request.GET.get("tax_status")
            if tax_status=="Active":
                tax_status="Deactive"
            else:
                tax_status="Active"
            #query exe - run
            updatef="update tax_tb set e_status='"+str(tax_status)+"' where tx_id='"+str(tax_id)+"'" 
            
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(updatef)
            mydb.commit()
            return redirect("etax")
        else:
            eid = request.session["eid"] 
            selcat = "select * from tax_tb,user_tb,employee_tb where employee_tb.e_id = tax_tb.e_id and tax_tb.u_id=user_tb.u_id and  tax_tb.e_id ='"+str(eid)+"' order by tx_id desc"  
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            tx_data = mycursor.fetchall()

            seluser = "select * from user_tb where u_status = 'Active'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(seluser)
            u_data = mycursor.fetchall()

            selv = "SELECT DISTINCT v_dname FROM village_tb WHERE v_status = 'Active'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selv)
            d_data = mycursor.fetchall()

            # selt = "select * from village_tb where v_status = 'Active' GROUP BY v_tname" 
            # # connection create object
            # mydb = getdb()
            # mycursor = mydb.cursor()
            # #query execute
            # mycursor.execute(selt)
            # t_data = mycursor.fetchall()

            # selv = "select * from village_tb where v_status = 'Active' GROUP BY v_vname" 
            # # connection create object
            # mydb = getdb()
            # mycursor = mydb.cursor()
            # #query execute
            # mycursor.execute(selv)
            # v_data = mycursor.fetchall()

            alldata = {
                'tx_data': tx_data,
                'u_data' : u_data,
                'd_data' : d_data,
                # 't_data': t_data,
                # 'v_data' : v_data

            }

            return render(request,'etax.html',alldata)

    except NameError:
        print("Internal Error")
    except:
        print("Error returned")

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

def etaxedit(request):
    try:

        if request.POST:
           #variable decleration
            tx_edt = request.GET.get("tx_edt")
            u_id = request.POST.get("u_id")
            city_dname = request.POST.get("city_dname")
            city_tname = request.POST.get("city_tname")
            city_vname = request.POST.get("city_vname")
            tx_name = request.POST.get("tx_name")
            tx_gender = request.POST.get("tx_gender")
            tx_address = request.POST.get("tx_address")
            tx_peraddress = request.POST.get("tx_peraddress")
            tx_home = request.POST.get("tx_home")
            tx_sqrt = request.POST.get("tx_sqrt")
            tx_amount = request.POST.get("tx_amount")
            tx_year = request.POST.get("tx_year")
            tx_outstanding = request.POST.get("tx_outstanding")
            tx_total = request.POST.get("tx_total")
            tx_issue = request.POST.get("tx_issue")
            tx_status = request.POST.get("tx_status")
            e_status = request.POST.get("e_status")
            
            tx_remarkdetail = request.POST.get("tx_remarkdetail")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                      
           #insert query
            ins = "UPDATE tax_tb set `u_id` = '"+str(u_id)+"', `city_dname` = '"+str(city_dname)+"', `city_tname` = '"+str(city_tname)+"', `city_vname` = '"+str(city_vname)+"', `tx_name` = '"+str(tx_name)+"', `tx_gender` = '"+str(tx_gender)+"', `tx_address` = '"+str(tx_address)+"', `tx_peraddress` = '"+str(tx_peraddress)+"', `tx_home` = '"+str(tx_home)+"', `tx_sqrt` = '"+str(tx_sqrt)+"', `tx_amount` = '"+str(tx_amount)+"', `tx_year` = '"+str(tx_year)+"', `tx_outstanding` = '"+str(tx_outstanding)+"', `tx_total` = '"+str(tx_total)+"', `tx_issue` = '"+str(tx_issue)+"', `tx_status` = '"+str(tx_status)+"', `e_status` = '"+str(e_status)+"', `tx_remarkdetail` = '"+str(tx_remarkdetail)+"', `tx_udate` = '"+cdate+"' where tx_id = '"+str(tx_edt)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("etax")

        else:
            
            tx_edt = request.GET.get("tx_edt")
            selcat = "select * from tax_tb where tx_id = '"+str(tx_edt)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            tx_data = mycursor.fetchall()

            seluser = "select * from user_tb where u_status = 'Active'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(seluser)
            u_data = mycursor.fetchall()

            selv = "SELECT DISTINCT v_dname FROM village_tb WHERE v_status = 'Active'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selv)
            d_data = mycursor.fetchall()

            alldata = {
                'tx_data': tx_data,
                'u_data' : u_data,
                'd_data' : d_data,


            } 
            return render(request,'etaxedit.html',alldata)

    except NameError:
        print("internal error")
    except:
        print('Error returned')  

def etaxdetails(request):
    try:
        if request.POST:
            tax_id = request.GET.get("tax_id")
            e_id = request.POST.get("tx_employee")
            tx_Remarkdetail = request.POST.get("remark_detail")
            g_status = request.POST.get("a_status")
            e_status = request.POST.get("e_status")
            i_status = request.POST.get("i_status")
            
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ins = "UPDATE tax_tb set `e_id` = '"+str(e_id)+"', `tx_Remarkdetail` = '"+str(tx_Remarkdetail)+"', `g_status` = '"+str(g_status)+"', `e_status` = '"+str(e_status)+"', `tx_udate` = '"+cdate+"', i_status = '"+str(i_status)+"' where tx_id = '"+str(tax_id)+"'"
            
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("etax")
            
        else:
            tax_id = request.GET.get("tax_id")
            
            selcat = "select * from tax_tb,user_tb where tax_tb.u_id=user_tb.u_id and tx_id = '"+str(tax_id)+"'"
             
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            tx_data = mycursor.fetchall()
            
            selemp = "select * from employee_tb" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selemp)
            emp_data = mycursor.fetchall()

            alldata  = {
                'tx_data' : tx_data,
                'emp_data' : emp_data
            }

            
        return render(request,'etaxdetails.html',alldata)

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 
 
def ecast(request):
    try:
        if request.GET.get("c_del") !=None:
            c_del = request.GET.get("c_del")
            cdel = "delete from cast_tb where c_id='"+str(c_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cdel)
            mydb.commit()
            return redirect("ecast")
        
        elif request.GET.get("c_id") !=None:
            cast_id = request.GET.get("c_id")
            cast_status = request.GET.get("cast_status")
            if cast_status=="Active":
                cast_status="Deactive"
            else:
                cast_status="Active"
            #query exe - run
            updatef="update cast_tb set e_status='"+str(cast_status)+"' where c_id='"+str(cast_id)+"'" 
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(updatef)
            mydb.commit()
            return redirect("ecast")
        else:
            eid = request.session["eid"] 
            selcat = "select * from cast_tb,user_tb where cast_tb.u_id=user_tb.u_id and cast_tb.g_status = 'Active' and  cast_tb.e_id ='"+str(eid)+"' order by c_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            c_data = mycursor.fetchall()

            return render(request,'ecast.html',{'c_data': c_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned")

def ecastdetails(request):
    try:  
        if request.POST:
            cast_id = request.GET.get("cast_id")
            e_id = request.POST.get("c_employee")
            c_remarkdetail = request.POST.get("remark_detail")
            g_status = request.POST.get("a_status")
            e_status = request.POST.get("e_status")
            c_status = request.POST.get("c_status")
            
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            if g_status == 'Active' and e_status == 'Active':
                c_issuedate = datetime.datetime.now().strftime("%Y-%m-%d")
                ins = "UPDATE cast_tb set `e_id` = '"+str(e_id)+"', `c_remarkdetail` = '"+str(c_remarkdetail)+"', `g_status` = '"+str(g_status)+"', `e_status` = '"+str(e_status)+"', `c_udate` = '"+cdate+"', c_status = '"+str(c_status)+"', `c_issuedate` = '"+c_issuedate+"' where c_id = '"+str(cast_id)+"'"
            else:    
                ins = "UPDATE cast_tb set `e_id` = '"+str(e_id)+"', `c_remarkdetail` = '"+str(c_remarkdetail)+"', `g_status` = '"+str(g_status)+"', `e_status` = '"+str(e_status)+"', `c_udate` = '"+cdate+"', c_status = '"+str(c_status)+"' where c_id = '"+str(cast_id)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("ecast")
            
        else:
            cast_id = request.GET.get("cast_id")
            
            selcat = "select * from cast_tb,user_tb where cast_tb.u_id=user_tb.u_id and c_id = '"+str(cast_id)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            c_data = mycursor.fetchall()

            selemp = "select * from employee_tb" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selemp)
            emp_data = mycursor.fetchall()

            alldata  = {
                'c_data' : c_data,
                'emp_data' : emp_data
            }



        return render(request,'ecastdetails.html',alldata)

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 

def eincome(request):
    try:
        if request.GET.get("i_del") !=None:
            i_del = request.GET.get("i_del") 
            cdel = "delete from income_tb where i_id='"+str(i_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cdel)
            mydb.commit()
            return redirect("eincome")
        elif request.GET.get("i_id")!=None:
            income_id = request.GET.get("i_id")
            income_status=request.GET.get("income_status")
            if income_status=="Active":
                income_status="Deactive"
            else:
                income_status="Active"
            #query exe - run
            update="update income_tb set e_status= '"+str(income_status)+"' where i_id='"+str(income_id)+"'" 
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(update)
            mydb.commit()
            return redirect("eincome")
        else:
            eid = request.session["eid"] 
            selcat = "select * from income_tb,user_tb where income_tb.u_id=user_tb.u_id and income_tb.g_status = 'Active' and  income_tb.e_id ='"+str(eid)+"' order by i_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            i_data = mycursor.fetchall()

            return render(request,'eincome.html',{'i_data': i_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned")

def eincomedetails(request):
    try:
        if request.POST:
            income_id = request.GET.get("income_id")
            e_id = request.POST.get("b_employee")
            i_remarkdetail = request.POST.get("remark_detail")
            g_status = request.POST.get("a_status")
            e_status = request.POST.get("e_status")
            i_status = request.POST.get("i_status")
            
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if g_status == 'Active' and e_status == 'Active':
                i_issuedate = datetime.datetime.now().strftime("%Y-%m-%d")
                ins = "UPDATE income_tb set `e_id` = '"+str(e_id)+"', `i_remarkdetail` = '"+str(i_remarkdetail)+"', `g_status` = '"+str(g_status)+"', `e_status` = '"+str(e_status)+"', `i_udate` = '"+cdate+"', i_status = '"+str(i_status)+"', `i_issuedate` = '"+i_issuedate+"' where i_id = '"+str(income_id)+"'"
            else:
                ins = "UPDATE income_tb set `e_id` = '"+str(e_id)+"', `i_remarkdetail` = '"+str(i_remarkdetail)+"', `g_status` = '"+str(g_status)+"', `e_status` = '"+str(e_status)+"', `i_udate` = '"+cdate+"', i_status = '"+str(i_status)+"' where i_id = '"+str(income_id)+"'"
            #print(ins)#query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("eincome")
            
        else:
            income_id = request.GET.get("income_id")
            
            selcat = "select * from income_tb,user_tb where income_tb.u_id=user_tb.u_id and i_id = '"+str(income_id)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            i_data = mycursor.fetchall()

            selemp = "select * from employee_tb" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selemp)
            emp_data = mycursor.fetchall()

            alldata  = {
                'i_data' : i_data,
                'emp_data' : emp_data
            }


        return render(request,'eincomedetails.html',alldata)

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 

def eemployee(request):
    try:
        if request.GET.get("e_del") !=None:
            e_del = request.GET.get("e_del")
            cdel = "delete from employee_tb where e_id='"+str(e_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cdel)
            mydb.commit()
            return redirect("eemployee")
        
        elif request.GET.get("e_id") !=None:
            employee_id= request.GET.get("e_id")
            employee_status=request.GET.get("employee_status")
            if employee_status=="Active":
                employee_status="Deactive"
            else:
                employee_status="Active"
            #query exe - run
            updatef="update employee_tb set e_status= '"+str(employee_status)+"' where e_id='"+str(employee_id)+"'" 
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(updatef)
            mydb.commit()
            return redirect("eemployee")
        else:
            selcat = "select * from employee_tb order by e_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            e_data = mycursor.fetchall()

            return render(request,'eemployee.html',{'e_data': e_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned")

def evillage(request):
    try:
        if request.POST:
            v_dname = request.POST.get("v_dname")
            v_tname = request.POST.get("v_tname")
            v_vname = request.POST.get("v_vname")
            v_status = request.POST.get("v_status")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ins = "INSERT INTO village_tb(v_dname, v_tname,v_vname, v_status, v_cdate, v_udate) VALUES ('"+str(v_dname)+"','"+str(v_tname)+"','"+str(v_vname)+"','"+str(v_status)+"','"+cdate+"','"+cdate+"')"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("evillage")
        elif request.GET.get("v_del") !=None:
            v_del = request.GET.get("v_del")
            cdel = "delete from village_tb where v_id='"+str(v_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cdel)
            mydb.commit()
            return redirect("evillage")
        elif request.GET.get("v_id") !=None:
            village_id= request.GET.get("v_id")
            village_status=request.GET.get("village_status")
            if village_status=="Active":
                village_status="Deactive"
            else:
                village_status="Active"
            #query exe - run
            updatef="update village_tb set v_status= '"+str(village_status)+"' where v_id='"+str(village_id)+"'" 
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(updatef)
            mydb.commit()
            return redirect("evillage")

        else:
            selcat = "select * from village_tb order by v_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            v_data = mycursor.fetchall()

            return render(request,'evillage.html',{'v_data': v_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned")

def evillageedit(request):
    try:
        if request.POST:
           #variable decleration
           v_edt = request.GET.get("v_edt")
           v_dname = request.POST.get("v_dname")
           v_tname = request.POST.get("v_tname")
           v_vname = request.POST.get("v_vname")

           v_status = request.POST.get("v_status")
           cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           
           #insert query
           ins = "UPDATE `village_tb` set `v_dname` = '"+str(v_dname)+"',`v_tname` = '"+str(v_tname)+"',`v_vname` = '"+str(v_vname)+"', `v_status` = '"+str(v_status)+"', `v_udate` = '"+cdate+"' where v_id = '"+str(v_edt)+"'"
           #query exe - run
           mydb = getdb()
           mycursor = mydb.cursor()
           mycursor.execute(ins)
           mydb.commit()
           return redirect("evillage")

        else:
            
            v_edt = request.GET.get("v_edt")
            selcat = "select * from village_tb where v_id = '"+str(v_edt)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            v_data = mycursor.fetchall() 
            return render(request,'evillageedit.html',{'v_data': v_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')  

def elogin(request):
    try:
        msg = ""
        if request.POST:
           #variable decleration
           e_contact = request.POST.get("e_contact")
           e_password = request.POST.get("e_password")
           
           #insert query
           sel = "select * from employee_tb where `e_contact` = '"+str(e_contact)+"' and e_password = '"+str(e_password)+"'"
           #query exe - run
           mydb = getdb()
           mycursor = mydb.cursor()
           mycursor.execute(sel)
           udata = mycursor.fetchall()

           if len(udata) > 0:
               request.session["econtact"] = e_contact
               request.session["eimg"] = udata[0][2]
               request.session["eid"] = udata[0][0]
               request.session["ename"] = udata[0][1]
               request.session["etime"] = str(udata[0][8])
        
               return redirect("eindex")           
           else:
               msg = " Invalid Username or Password.!" 
               return render(request,'elogin.html',{'msg':msg})          
        else:
            return render(request,'elogin.html',{'msg':msg})
   
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def elogout(request):
    try:
        
        #variable decleration
        username = request.session["ename"]
        cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #insert query

        ins = "UPDATE `employee_tb` set `e_udate` = '"+cdate+"' where e_name = '"+str(username)+"'"
        print(ins)   
        #query exe - run
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(ins)
        mydb.commit()

        request.session["ename"] = None
        request.session["econtact"] = None
        request.session["eimg"] = None
        request.session["etime"] = None
        request.session["eid"] = None

        return redirect("elogin")


    except NameError:
        print("internal error")
    except:
        print('Error returned')

def efeedbackreport(request):
    try:
        if request.POST:
            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")            
            f_status = request.POST.get("f_status")

            seluser = "select * from feedback_tb WHERE DATE(feedback_tb.f_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' order by f_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(seluser)
            f_data = mycursor.fetchall()
            return render(request,'efeedbackreport.html',{'f_data': f_data})
        else:
            return render(request,'efeedbackreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def euserreport(request):
    try:
        if request.POST:
            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")            
            u_status = request.POST.get("u_status")

            seluser = "select * from user_tb WHERE DATE(user_tb.u_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' order by u_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(seluser)
            u_data = mycursor.fetchall()
            return render(request,'euserreport.html',{'u_data': u_data})
        else:
            return render(request,'euserreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def eemployeereport(request):
    try:
        if request.POST:
            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")            
            e_status = request.POST.get("e_status")

            seluser = "select * from employee_tb WHERE DATE(employee_tb.e_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' order by e_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(seluser)
            e_data = mycursor.fetchall()
            return render(request,'eemployeereport.html',{'e_data': e_data})
        else:
            return render(request,'eemployeereport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def ebirthreport(request):
    try:
        if request.POST:
            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")
            eid = request.session["eid"]             

            seluser = "select * from birth_tb,user_tb where birth_tb.u_id=user_tb.u_id and DATE(birth_tb.b_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' and birth_tb.e_id = '"+str(eid)+"' order by b_id desc" 
           
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(seluser)
            b_data = mycursor.fetchall()
            return render(request,'ebirthreport.html',{'b_data': b_data})
        else:
            return render(request,'ebirthreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def ecastreport(request):
    try:
        if request.POST:
            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")
            eid = request.session["eid"]              

            seluser = "select * from cast_tb,user_tb,employee_tb where cast_tb.u_id=user_tb.u_id and cast_tb.e_id=employee_tb.e_id and DATE(cast_tb.c_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' and cast_tb.e_id = '"+str(eid)+"' order by c_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(seluser)
            c_data = mycursor.fetchall()
            return render(request,'ecastreport.html',{'c_data': c_data})
        else:
            return render(request,'ecastreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def edeathreport(request):
    try:
        if request.POST:
            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date") 
            eid = request.session["eid"]            

            seluser = "select * from death_tb,user_tb,employee_tb where death_tb.u_id=user_tb.u_id and death_tb.e_id=employee_tb.e_id and DATE(death_tb.dth_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' and death_tb.e_id = '"+str(eid)+"' order by dth_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(seluser)
            dth_data = mycursor.fetchall()
            return render(request,'edeathreport.html',{'dth_data': dth_data})
        else:
            return render(request,'edeathreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def eincomereport(request):
    try:
        if request.POST:
            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date") 
            eid = request.session["eid"]            

            seluser = "select * from income_tb,user_tb,employee_tb where income_tb.u_id=user_tb.u_id and income_tb.e_id=employee_tb.e_id and DATE(income_tb.i_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' and income_tb.e_id = '"+str(eid)+"' order by i_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(seluser)
            i_data = mycursor.fetchall()
            return render(request,'eincomereport.html',{'i_data': i_data})
        else:
            return render(request,'eincomereport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def etaxreport(request):
    try:
        if request.POST:
            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")
            eid = request.session["eid"]            

            seluser = "select * from tax_tb,user_tb,employee_tb where tax_tb.u_id=user_tb.u_id and tax_tb.e_id=employee_tb.e_id and DATE(tax_tb.tx_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' and tax_tb.e_id = '"+str(eid)+"' order by tx_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(seluser)
            tx_data = mycursor.fetchall()
            return render(request,'etaxreport.html',{'tx_data': tx_data})
        else:
            return render(request,'etaxreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def eprofile(request):
    try:
        if request.POST:
           #variable decleration
           e_edt = request.session["eid"]
           e_name = request.POST.get("e_name")
           
           if request.POST.get("e_image") !="":
               e_img = request.FILES["e_image"]
               img = FileSystemStorage()
               old_img = img.save(e_img.name,e_img)

           else:
               old_img = request.POST.get("old_img")

           e_contact = request.POST.get("e_contact")
           e_post = request.POST.get("e_post")
           e_email = request.POST.get("e_email")
           e_password = request.POST.get("e_password")
           e_status = request.POST.get("e_status")
           cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           
           #insert query
           ins = "UPDATE employee_tb set `e_name` = '"+str(e_name)+"', `e_image` = '"+str(old_img)+"', `e_contact` = '"+str(e_contact)+"', `e_post` = '"+str(e_post)+"', `e_email` = '"+str(e_email)+"', `e_password` = '"+str(e_password)+"', `e_status` = '"+str(e_status)+"', `e_udate` = '"+cdate+"' where e_id = '"+str(e_edt)+"'"
           #query exe - run
           mydb = getdb()
           mycursor = mydb.cursor()
           mycursor.execute(ins)
           mydb.commit()
           return redirect("eprofile")

        else:
            
            e_edt = request.session["eid"]
            selcat = "select * from employee_tb where e_id = '"+str(e_edt)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            e_data = mycursor.fetchall() 
            return render(request,'eprofile.html',{'e_data': e_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')  
