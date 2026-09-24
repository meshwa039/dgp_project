from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import datetime
import mysql.connector
from django.core.files.storage import FileSystemStorage


def getdb():
    mydb = mysql.connector.connect(host="localhost",user="root", passwd="",database="digital_db") 
    return mydb

# Create your views here.
def index(request):
    try:
        dcount = "select count(dth_id) from death_tb,user_tb where death_tb.u_id=user_tb.u_id order by dth_id desc" 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(dcount)
        dth_data = mycursor.fetchall()


        bcount = "select count(b_id) from birth_tb,user_tb where birth_tb.u_id=user_tb.u_id order by b_id desc" 
            # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(bcount)
        b_data = mycursor.fetchall()


        icount = "select count(i_id) from income_tb,user_tb where income_tb.u_id=user_tb.u_id  order by i_id desc" 
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(icount)
        i_data = mycursor.fetchall()


        tcount = "select count(tx_id) from tax_tb,user_tb,employee_tb where tax_tb.u_id=user_tb.u_id and tax_tb.e_id=employee_tb.e_id order by tx_id desc"  
        # connection create object
        mydb = getdb()
        mycursor = mydb.cursor()
        #query execute
        mycursor.execute(tcount)
        tx_data = mycursor.fetchall()


        ccount = "select count(c_id) from cast_tb,user_tb where cast_tb.u_id=user_tb.u_id order by c_id desc" 
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

        return render(request,'index.html',alldata)



    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 


def category(request):
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
            return redirect("category")
        elif request.GET.get("cat_del") !=None:
            cat_del = request.GET.get("cat_del")
            cdel = "delete from category_tb where cat_id='"+str(cat_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cdel)
            mydb.commit()
            return redirect("category")
        else:   
            selcat = "select * from category_tb order by cat_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            cat_data = mycursor.fetchall()

            return render(request,'category.html',{'cat_data': cat_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 

def categoryedit(request):
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
           return redirect("category")

        else:
            
            cat_edt = request.GET.get("cat_edt")
            selcat = "select * from category_tb where cat_id = '"+str(cat_edt)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            cat_data = mycursor.fetchall() 
            return render(request,'categoryedit.html',{'cat_data': cat_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')  


def feedback(request):
    try:
        if request.GET.get("f_del") !=None:
            f_del = request.GET.get("f_del")
            cdel = "delete from feedback_tb where f_id='"+str(f_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cdel)
            mydb.commit()
            return redirect("feedback")


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
            return redirect("feedback")

        else:
            selcat = "select * from feedback_tb order by f_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            f_data = mycursor.fetchall()

            return render(request,'feedback.html',{'f_data': f_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 


def user(request):
    try:
        if request.GET.get("user_del") !=None:
            u_del = request.GET.get("user_del")
            cdel = "delete from user_tb where u_id='"+str(u_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cdel)
            mydb.commit()
            return redirect("user")
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
            return redirect("user")

        
        else:
            selcat = "select * from user_tb order by u_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            u_data = mycursor.fetchall()

            return render(request,'user.html',{'u_data': u_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 


def birth(request):
    try:
        if request.GET.get("birth_del") !=None:
            birth_del = request.GET.get("birth_del")
            cdel = "delete from birth_tb where b_id='"+str(birth_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cdel)
            mydb.commit()
            return redirect("birth")
        elif request.GET.get("b_id") !=None:
            birth_id = request.GET.get("b_id")
            birth_status = request.GET.get("birth_status")
            if birth_status=="Active":
                birth_status="Deactive"
            else:
                birth_status="Active"
            #query exe - run
            updatef="update birth_tb set g_status='"+str(birth_status)+"' where b_id='"+str(birth_id)+"'" 
            
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(updatef)
            mydb.commit()
            return redirect("birth")
        else:
            selcat = "select * from birth_tb,user_tb where birth_tb.u_id=user_tb.u_id order by b_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            b_data = mycursor.fetchall()

            return render(request,'birth.html',{'b_data': b_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 


def birthdetails(request):
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
            return redirect("birth")
            
        else:
            birth_id = request.GET.get("birth_id")
            
            selcat = "select * from birth_tb,user_tb where birth_tb.u_id=user_tb.u_id  and b_id = '"+str(birth_id)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            b_data = mycursor.fetchall()

            selemp = "select * from employee_tb where e_status = 'Active'" 
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

            return render(request,'birthdetails.html',alldata)

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 


def death(request):
    try:
        if request.GET.get("death_del") !=None:
            death_del = request.GET.get("death_del")
            cdel = "delete from death_tb where dth_id='"+str(death_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cdel)
            mydb.commit()
            return redirect("death")
        elif request.GET.get("dth_id") !=None:
            death_id = request.GET.get("dth_id")
            death_status = request.GET.get("death_status")
            if death_status=="Active":
                death_status="Deactive"
            else:
                death_status="Active"
            #query exe - run
            updatef="update death_tb set g_status='"+str(death_status)+"' where dth_id='"+str(death_id)+"'" 
            
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(updatef)
            mydb.commit()
            return redirect("death")
        else:
            selcat = "select * from death_tb,user_tb where death_tb.u_id=user_tb.u_id order by dth_id desc"  
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            dth_data = mycursor.fetchall()

            return render(request,'death.html',{'dth_data': dth_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 


def deathdetails(request):
    try:
        if request.POST:
            death_id = request.GET.get("death_id")
            e_id = request.POST.get("dth_employee")
            dth_Remarkdetail = request.POST.get("remark_detail")
            g_status = request.POST.get("a_status")
            e_status = request.POST.get("e_status")

            
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ins = "UPDATE death_tb set `e_id` = '"+str(e_id)+"', `dth_Remarkdetail` = '"+str(dth_Remarkdetail)+"', `g_status` = '"+str(g_status)+"', `e_status` = '"+str(e_status)+"', `dth_udate` = '"+cdate+"' where dth_id = '"+str(death_id)+"'"
            #print(ins)#query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("death")
            
        else:
            death_id = request.GET.get("death_id")
            
            selcat = "select * from death_tb,user_tb where death_tb.u_id=user_tb.u_id and dth_id = '"+str(death_id)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            dth_data = mycursor.fetchall()

            selemp = "select * from employee_tb where e_status = 'Active'" 
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

            return render(request,'deathdetails.html',alldata)

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 



def tax(request):
    try:
        if request.GET.get("tax_del") !=None:
            tax_del = request.GET.get("tax_del")
            cdel = "delete from tax_tb where tx_id='"+str(tax_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cdel)
            mydb.commit()
            return redirect("tax")
        elif request.GET.get("tx_id") !=None:
            tax_id = request.GET.get("tx_id")
            tax_status = request.GET.get("tax_status")
            if tax_status=="Active":
                tax_status="Deactive"
            else:
                tax_status="Active"
            #query exe - run
            updatef="update tax_tb set g_status='"+str(tax_status)+"' where tx_id='"+str(tax_id)+"'" 
            
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(updatef)
            mydb.commit()
            return redirect("tax")
        else:
            selcat = "select * from tax_tb,user_tb,employee_tb where employee_tb.e_id = tax_tb.e_id and tax_tb.u_id=user_tb.u_id order by tx_id desc"  
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            tx_data = mycursor.fetchall()

            return render(request,'tax.html',{'tx_data': tx_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned")


def taxdetails(request):
    try:
        if request.POST:
            tax_id = request.GET.get("tax_id")
            e_id = request.POST.get("tx_employee")
            tx_Remarkdetail = request.POST.get("remark_detail")
            g_status = request.POST.get("a_status")
            e_status = request.POST.get("e_status")
            
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ins = "UPDATE tax_tb set `e_id` = '"+str(e_id)+"', `tx_Remarkdetail` = '"+str(tx_Remarkdetail)+"', `g_status` = '"+str(g_status)+"', `e_status` = '"+str(e_status)+"', `tx_udate` = '"+cdate+"' where tx_id = '"+str(tax_id)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("tax")
            
        else:
            tax_id = request.GET.get("tax_id")
            
            selcat = "select * from tax_tb,user_tb where tax_tb.u_id=user_tb.u_id and tx_id = '"+str(tax_id)+"'"
             
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            tx_data = mycursor.fetchall()
            
            selemp = "select * from employee_tb where e_status = 'Active'"  
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

            
        return render(request,'taxdetails.html',alldata)

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 
 

def cast(request):
    try:
        if request.GET.get("c_del") !=None:
            c_del = request.GET.get("c_del")
            cdel = "delete from cast_tb where c_id='"+str(c_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cdel)
            mydb.commit()
            return redirect("cast")
        
        elif request.GET.get("c_id") !=None:
            cast_id = request.GET.get("c_id")
            cast_status = request.GET.get("cast_status")
            if cast_status=="Active":
                cast_status="Deactive"
            else:
                cast_status="Active"
            #query exe - run
            updatef="update cast_tb set g_status='"+str(cast_status)+"' where c_id='"+str(cast_id)+"'" 
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(updatef)
            mydb.commit()
            return redirect("cast")
        else:
            selcat = "select * from cast_tb,user_tb where cast_tb.u_id=user_tb.u_id order by c_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            c_data = mycursor.fetchall()

            return render(request,'cast.html',{'c_data': c_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned")


def castdetails(request):
    try:  
        if request.POST:
            cast_id = request.GET.get("cast_id")
            e_id = request.POST.get("c_employee")
            c_remarkdetail = request.POST.get("remark_detail")
            g_status = request.POST.get("a_status")
            e_status = request.POST.get("e_status")
            
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ins = "UPDATE cast_tb set `e_id` = '"+str(e_id)+"', `c_remarkdetail` = '"+str(c_remarkdetail)+"', `g_status` = '"+str(g_status)+"', `e_status` = '"+str(e_status)+"', `c_udate` = '"+cdate+"' where c_id = '"+str(cast_id)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("cast")
            
        else:
            cast_id = request.GET.get("cast_id")
            
            selcat = "select * from cast_tb,user_tb where cast_tb.u_id=user_tb.u_id and c_id = '"+str(cast_id)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            c_data = mycursor.fetchall()

            selemp = "select * from employee_tb where e_status = 'Active'" 
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



        return render(request,'castdetails.html',alldata)

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 



def income(request):
    try:
        if request.GET.get("i_del") !=None:
            i_del = request.GET.get("i_del") 
            cdel = "delete from income_tb where i_id='"+str(i_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cdel)
            mydb.commit()
            return redirect("income")
        elif request.GET.get("i_id")!=None:
            income_id = request.GET.get("i_id")
            income_status=request.GET.get("income_status")
            if income_status=="Active":
                income_status="Deactive"
            else:
                income_status="Active"
            #query exe - run
            update="update income_tb set g_status= '"+str(income_status)+"' where i_id='"+str(income_id)+"'" 
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(update)
            mydb.commit()
            return redirect("income")
        else:
            selcat = "select * from income_tb,user_tb where income_tb.u_id=user_tb.u_id order by i_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            i_data = mycursor.fetchall()

            return render(request,'income.html',{'i_data': i_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned")


def incomedetails(request):
    try:
        if request.POST:
            income_id = request.GET.get("income_id")
            e_id = request.POST.get("b_employee")
            i_remarkdetail = request.POST.get("remark_detail")
            g_status = request.POST.get("a_status")
            e_status = request.POST.get("e_status")
            
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ins = "UPDATE income_tb set `e_id` = '"+str(e_id)+"', `i_remarkdetail` = '"+str(i_remarkdetail)+"', `g_status` = '"+str(g_status)+"', `e_status` = '"+str(e_status)+"', `i_udate` = '"+cdate+"' where i_id = '"+str(income_id)+"'"
            #print(ins)#query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("income")
            
        else:
            income_id = request.GET.get("income_id")
            
            selcat = "select * from income_tb,user_tb where income_tb.u_id=user_tb.u_id and i_id = '"+str(income_id)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            i_data = mycursor.fetchall()

            selemp = "select * from employee_tb where e_status = 'Active'" 
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


        return render(request,'incomedetails.html',alldata)

    except NameError:
        print("Internal Error")
    except:
        print("Error returned") 



def employee(request):
    try:
        if request.POST:
            e_name = request.POST.get("e_name")
            
            e_img = request.FILES["e_image"]
            img = FileSystemStorage()
            e_image = img.save(e_img.name,e_img)
            e_contact = request.POST.get("e_contact")
            e_post = request.POST.get("e_post")
            e_email = request.POST.get("e_email")
            e_password = request.POST.get("e_password")
            e_status = request.POST.get("e_status")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ins = "INSERT INTO employee_tb(e_name, e_image, e_contact, e_post, e_email, e_password, e_status, e_cdate, e_udate) VALUES ('"+str(e_name)+"','"+str(e_image)+"','"+str(e_contact)+"','"+str(e_post)+"','"+str(e_email)+"','"+str(e_password)+"','"+str(e_status)+"','"+cdate+"','"+cdate+"')"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("employee")
        
        elif request.GET.get("e_del") !=None:
            e_del = request.GET.get("e_del")
            cdel = "delete from employee_tb where e_id='"+str(e_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cdel)
            mydb.commit()
            return redirect("employee")
        
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
            return redirect("employee")
        else:
            selcat = "select * from employee_tb order by e_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            e_data = mycursor.fetchall()

            return render(request,'employee.html',{'e_data': e_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned")


def employeeedit(request):
    try:
        if request.POST:
           #variable decleration
           e_edt = request.GET.get("e_edt")
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
           return redirect("employee")

        else:
            
            e_edt = request.GET.get("e_edt")
            selcat = "select * from employee_tb where e_id = '"+str(e_edt)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            e_data = mycursor.fetchall() 
            return render(request,'employeeedit.html',{'e_data': e_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')  



def village(request):
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
            return redirect("village")
        elif request.GET.get("v_del") !=None:
            v_del = request.GET.get("v_del")
            cdel = "delete from village_tb where v_id='"+str(v_del)+"'"
            #query exe - run
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(cdel)
            mydb.commit()
            return redirect("village")
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
            return redirect("village")

        else:
            selcat = "select * from village_tb order by v_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            v_data = mycursor.fetchall()

            return render(request,'village.html',{'v_data': v_data})

    except NameError:
        print("Internal Error")
    except:
        print("Error returned")

def villageedit(request):
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
           return redirect("village")

        else:
            
            v_edt = request.GET.get("v_edt")
            selcat = "select * from village_tb where v_id = '"+str(v_edt)+"'" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(selcat)
            v_data = mycursor.fetchall() 
            return render(request,'villageedit.html',{'v_data': v_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')  




def login(request):
    try:
        msg = ""
        if request.POST:
           #variable decleration
           a_username = request.POST.get("a_username")
           a_password = request.POST.get("a_password")
           
           #insert query
           sel = "select * from admin_tb where `a_username` = '"+str(a_username)+"' and a_password = '"+str(a_password)+"'"
           #query exe - run
           mydb = getdb()
           mycursor = mydb.cursor()
           mycursor.execute(sel)
           udata = mycursor.fetchall()

           if len(udata) > 0:
               request.session["name"] = a_username
               request.session["img"] = udata[0][3]
               request.session["time"] = str(udata[0][4])
        
               return redirect("index")           
           else:
               msg = " Invalid Username or Password.!" 
               return render(request,'login.html',{'msg':msg})          
        else:
            return render(request,'login.html',{'msg':msg})
   
    except NameError:
        print("internal error")
    except:
        print('Error returned')


def logout(request):
    try:
        
        #variable decleration
        username = request.session["name"]
        cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #insert query

        ins = "UPDATE `admin_tb` set `a_lastseen` = '"+cdate+"' where a_username = '"+str(username)+"'"
        print(ins)   
        #query exe - run
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(ins)
        mydb.commit()

        request.session["name"] = None
        request.session["img"] = None
        request.session["time"] = None

        return redirect("login")


    except NameError:
        print("internal error")
    except:
        print('Error returned')


def feedbackreport(request):
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
            return render(request,'feedbackreport.html',{'f_data': f_data})
        else:
            return render(request,'feedbackreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')



def userreport(request):
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
            return render(request,'userreport.html',{'u_data': u_data})
        else:
            return render(request,'userreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')


def employeereport(request):
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
            return render(request,'employeereport.html',{'e_data': e_data})
        else:
            return render(request,'employeereport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')



def birthreport(request):
    try:
        if request.POST:
            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")            

            seluser = "select * from birth_tb,user_tb where birth_tb.u_id=user_tb.u_id and DATE(birth_tb.b_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' order by b_id desc" 
            print(seluser)
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(seluser)
            b_data = mycursor.fetchall()
            return render(request,'birthreport.html',{'b_data': b_data})
        else:
            return render(request,'birthreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')




def castreport(request):
    try:
        if request.POST:
            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")            

            seluser = "select * from cast_tb,user_tb,employee_tb where cast_tb.u_id=user_tb.u_id and cast_tb.e_id=employee_tb.e_id and DATE(cast_tb.c_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' order by c_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(seluser)
            c_data = mycursor.fetchall()
            return render(request,'castreport.html',{'c_data': c_data})
        else:
            return render(request,'castreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')


def deathreport(request):
    try:
        if request.POST:
            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")            

            seluser = "select * from death_tb,user_tb,employee_tb where death_tb.u_id=user_tb.u_id and death_tb.e_id=employee_tb.e_id and DATE(death_tb.dth_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' order by dth_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(seluser)
            dth_data = mycursor.fetchall()
            return render(request,'deathreport.html',{'dth_data': dth_data})
        else:
            return render(request,'deathreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')


def incomereport(request):
    try:
        if request.POST:
            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")            

            seluser = "select * from income_tb,user_tb,employee_tb where income_tb.u_id=user_tb.u_id and income_tb.e_id=employee_tb.e_id and DATE(income_tb.i_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' order by i_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(seluser)
            i_data = mycursor.fetchall()
            return render(request,'incomereport.html',{'i_data': i_data})
        else:
            return render(request,'incomereport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def taxreport(request):
    try:
        if request.POST:
            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")            

            seluser = "select * from tax_tb,user_tb,employee_tb where tax_tb.u_id=user_tb.u_id and tax_tb.e_id=employee_tb.e_id and DATE(tax_tb.tx_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' order by tx_id desc" 
            # connection create object
            mydb = getdb()
            mycursor = mydb.cursor()
            #query execute
            mycursor.execute(seluser)
            tx_data = mycursor.fetchall()
            return render(request,'taxreport.html',{'tx_data': tx_data})
        else:
            return render(request,'taxreport.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')


