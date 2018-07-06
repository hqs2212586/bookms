from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
from app01.models import Book

# 添加书籍
def addbook(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        price = request.POST.get("price")
        date = request.POST.get("date")
        publish = request.POST.get("publish")

        # 生成的记录对象
        book_obj = Book.objects.create(title=title, price=price,pub_date=date, publish=publish)
        # return HttpResponse("OK")
        return redirect('/books/')   # 添加书籍后重定向

    return render(request, 'addbook.html')

# 查看书籍
def books(request):
    book_list = Book.objects.all()   # [obj1,obj2....]

    return render(request, "books.html", locals())  # 局部变量直接传入模板，变量名一一对应

# 删除书籍
def delbook(request, id):
    Book.objects.filter(id=id).delete()
    # 删除完成后重定向
    return redirect('/books/')

# 编辑数据
def changebook(request, id):
    # 拿到点击按钮对应条目的对象
    book_obj = Book.objects.filter(id=id).first()

    if request.method=="POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        date = request.POST.get("date")
        publish = request.POST.get("publish")

        Book.objects.filter(id=id).update(title=title, price=price, pub_date=date, publish=publish)

        return redirect("/books/")

    # 返回一个修改页面
    return render(request, 'changebook.html', {"book_obj":book_obj})