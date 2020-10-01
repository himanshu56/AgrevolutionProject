from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import UserModel, ProductVariantModel, OrderModel
# Create your views here.
from django.views import View
import uuid


class SingUpCustomer(View):
    def get(self,request):
        return render(request,"login-signup-customer.html")

    def post(self,request):

        req=request.POST.get('REQ',None)
        if req=='Login':
            mobile = request.POST.get('mobile', None)
            otp = request.POST.get('otp', None)
            if otp=='123456':
                try:
                    usermodel=UserModel.objects.get(mobile=mobile)
                    login(request, usermodel.user)
                    # if usermodel.role=='SAlES':
                    #     return redirect('salesDash/')
                    return redirect('custDash/')
                except Exception as ex:
                    print(ex)
                    return render(request, "login-signup-customer.html", {'error': str(ex)})

        mobile=request.POST.get('mobile',None)
        email=request.POST.get('email',None)
        password=request.POST.get('pass',None)

        try:
            user=User.objects.create(username=mobile,password=password,email=email)
            UserModel.objects.create(user=user,mobile=mobile,role='cust',active=True)
            login(request, user)

            return redirect('custDash/')
        except Exception as ex:
            print(ex)
            return render(request,"login-signup-customer.html",{'error':str(ex)})
        return



class dash1(LoginRequiredMixin,View):
    login_url = '/cust/'

    def get(self,request):
        pro=list()
        productvar=ProductVariantModel.objects.filter(active=True)
        for products in productvar:
            pro.append({'name':products.product.name,'variantname':products.VariantModel.name,'vvalue':products.VariantValue
                           ,'vquantity':products.quantity,'vprice':products.price,
                        'vid':products.id})

        return render(request,'CustomerDashboard.html',{'products':pro})

    def post(self,request):
        vid=request.POST.get('vid',None)
        quant=int(request.POST.get('quant',None))

        productvar = ProductVariantModel.objects.filter(id=vid)[0]
        productvar.quantity=productvar.quantity-quant
        order=OrderModel.objects.create(usermodel=UserModel.objects.get(user=request.user),
                                  price=productvar.price,
                                  product=productvar.product,
                                    quantity_left=productvar.quantity,
                                  variant=productvar.VariantModel,
                                active=False,
                                  )
        productvar.save()
        return redirect('/cust/orderpalced/?id='+str(order.id))

class OrderDetails(LoginRequiredMixin,View):
    login_url = '/cust/'

    def get(self,request):
        orderid=request.GET.get('id')
        past=list()
        ordrrss=OrderModel.objects.filter(usermodel=UserModel.objects.get(active=True,user=request.user))
        for order in ordrrss:
            past.append({
                'id':order.id,
                'price':order.price,
                'product':order.product,
                'vari':order.variant.name,


            })
        return render(request,'CustomerOrder.html',{'order_number':orderid,'past':past})

class admin_sales_login(View):
    def get(self,request):
        return render(request,'sales-admin-login.html')

    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                if UserModel.objects.get(user=user).role=='sales':
                    return redirect('/salesdash/')
                elif UserModel.objects.get(user=user).role=='admin':
                    return redirect('/admindash')
            except Exception as ex:
                print(ex)
                logout(request)
                return render(request, 'sales-admin-login.html', {'error': 'Login Error '+str(ex)})


        else:
            return render(request, 'sales-admin-login.html',{'error':'Login Error'})


class salesdash(LoginRequiredMixin,View):
    login_url = '/cust/adminlogin/'

    def get(self,request):
        if UserModel.objects.get(user=request.user).role=='sales':
            orders=OrderModel.objects.all()
            ordrr=list()
            for i in orders:
                ordrr.append({
                    'orderid':i.id,
                    'product':i.product.name,
                    'variant':i.variant.name,
                    'status':i.status

                })
            return render(request,'sales-dashboard.html',{'orders':ordrr})
        return redirect('adminlogin')

    def post(self,request):
        if UserModel.objects.get(user=request.user).role=='sales':

            vid=request.POST.get('vid')
            status=request.POST.get('status')
            order=OrderModel.objects.get(id=int(vid))
            order.status=status
            order.save()
            return redirect('salesdash')
        return redirect('adminlogin')
class logoute(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        return  redirect('/cust/')