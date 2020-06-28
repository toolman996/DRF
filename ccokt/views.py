# import view as view
from django.http import JsonResponse, request
from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.views import APIView

from ccokt.models import User


# @csrf_protect #禁用和全局的情况下为某个试图添加csrf认证
@csrf_exempt #为某个试图免除csrf认证
def user(request):
    if request.method == 'GET':
        name=request.GET.get('name')
        print(name)
        return HttpResponse('GET 查询')
    elif request.method == 'POST':
        name=request.POST.get('name')
        print(name)
        return HttpResponse('POST 添加')
    elif request.method == 'PUT':
        name=request.GET.get('name')
        print(name)
        return HttpResponse('PUT 修改')
    elif request.method == 'DELETE':
        name=request.GET.get('name')
        print(name)
        return HttpResponse('DELETE 删除')
@method_decorator(csrf_exempt, name="dispatch")  # 让类视图免除csrf认证
class Drf(View):
    def get(self,request,*args,**kwargs):#查询
        # get请求查询单个或者多个操作
        id=kwargs.get('id')#获取drf中的参数
        if id:
            result=User.objects.filter(id=id).values().first()
            print(result)
            if result:
                return JsonResponse({
                    'status':200,
                    'msg':'查询成功',
                    'reslut':result
                })
        else:
            reslut=User.objects.all().values()
            print(reslut)
            if reslut:
                return JsonResponse({
                    'status': 200,
                    'msg': '查询成功',
                    'reslut': list(reslut)
                })
        return JsonResponse({
            'status': 500,
            'msg': '没有查询到你所要的信息',
        })

    def post(self, request, *args, **kwargs):
        #新增单个
        username=request.POST.get('name')
        password=request.POST.get('pwd')
        gender=request.POST.get('gender')
        try:
            User.objects.create(username=username,password=password,gender=gender)
            return JsonResponse({
                'status': 200,
                'msg': '创建成功',
                'reslut': {'username':username,'password':password,'gender':gender}
            })
        except:
            return JsonResponse({
                'status': 500,
                'msg': '创建失败',

            })
        # return HttpResponse('POST 添加1')
    def put(self, request, *args, **kwargs):
        # name = request.GET.get('name')
        print('类')
        return HttpResponse('PUT 修改1')
    def delete(self, request, *args, **kwargs):
        # name = request.GET.get('name')
        print('类')
        return HttpResponse('DELETE 删除1')

class UserApiView(APIView):
        #原生django获取参数
    def get(self, request, *args, **kwargs):  # 查询
        #原生django获取参数
        # print(request._request.GET)
        #drf request对象获取参数
        # print(request.GET)
        #通过query_params获取参数
        id=request.query_params.get('id')
        if id:
            result=User.objects.filter(id=id).values().first()
            print(result)
            if result:
                return JsonResponse({
                    'status':200,
                    'msg':'查询成功',
                    'reslut':result
                })
        else:
            reslut=User.objects.all().values()
            print(reslut)
            if reslut:
                return JsonResponse({
                    'status': 200,
                    'msg': '查询成功',
                    'reslut': list(reslut)
                })
        return JsonResponse({
            'status': 500,
            'msg': '没有查询到你所要的信息',
        })

        # return Response('api版函数视图')

    def post(self, request, *args, **kwargs):  # 查询
        # print(request._request.POST)
        # print(request.POST)
        # print(request.data)
        username = request.POST.get('name')
        password = request.POST.get('pwd')
        gender = request.POST.get('gender')
        try:
            User.objects.create(username=username, password=password, gender=gender)
            return JsonResponse({
                'status': 200,
                'msg': '创建成功',
                'reslut': {'username': username, 'password': password, 'gender': gender}
            })
        except:
            return JsonResponse({
                'status': 500,
                'msg': '创建失败',

            })
        # return Response('post api版函数视图')
        # id=kwargs.get('id')#获取drf中的参数
        # if id:
        #     result=User.objects.filter(id=id).values().first()
        #     print(result)
        #     if result:
        #         return JsonResponse({
        #             'status':200,
        #             'msg':'查询成功',
        #             'reslut':result
        #         })
        # else:
        #     reslut=User.objects.all().values()
        #     print(reslut)
        #     if reslut:
        #         return JsonResponse({
        #             'status': 200,
        #             'msg': '查询成功',
        #             'reslut': list(reslut)
        #         })
        # return JsonResponse({
        #     'status': 500,
        #     'msg': '没有查询到你所要的信息',
        # })












































