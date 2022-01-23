from django.shortcuts import render,get_object_or_404
from django.core.mail import send_mail
from .models import Gallery,Highlights



def home(request):
    h_images = Highlights.objects.all()
    return render(request, 'index.html',{'images':h_images})

# Seperates the gallery images into a 2d list of rows
def gallery_object_seperator(max_rows_per_page=1):
    g_images = Gallery.objects.all()

    cnt = 1
    rows = []
    row = []
    # Dividing the images into rows of 3 images per row as the maximum and creating a list of those rows
    for image in g_images:
        if cnt < 3:
            row.append(image)
        else:
            row.append(image)
            cnt = 0
            rows.append(row)
            row = []
        cnt += 1

    if row:
        rows.append(row)

    # Seperating the rows into multiple pages to insure faster loading and better optimization
    home_page = rows[:max_rows_per_page]
    divided_rows_list = []
    first = max_rows_per_page
    last = max_rows_per_page + max_rows_per_page
    curr_page = 1
    for i in range(max_rows_per_page, len(rows), max_rows_per_page):
        divided_rows_list.append(rows[first:last])
        first = last
        last += max_rows_per_page
    return home_page,divided_rows_list

def gallery(request):
    home_page, divided_rows_list = gallery_object_seperator(1)
    return render(request, 'gallery.html', {'rows':home_page,'nxt':1,'prev':len(divided_rows_list)})

    # return render(request,'gallery.html',{'rows':rows})

def nxt_pg(request,num):
    home_page, divided_rows_list = gallery_object_seperator(1)
    if num > len(divided_rows_list) or num == 0:
        return gallery(request)
    elif num < 0:
        num = len(divided_rows_list)
    return render(request, 'gallery.html', {'rows': divided_rows_list[num - 1], 'nxt': num + 1, 'prev': num - 1})

def making(request):
    return render(request,'mk1.html',{'nxt':'making1','prev':'making2'})

def making1(request):
    return render(request,'mk2.html',{'nxt':'making2','prev':'making'})

def making2(request):
    return render(request,'mk3.html',{'nxt':'making','prev':'making1'})

def submitted(request):
    name = email = message = None
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            f'Enquiry from {name.upper()}',
            message,
            email,
            ['sanskarhandicrafts@gmail.com']
        )
        return render(request,'index.html',{'images':h_images,'name':name,'email':email,'message':message})
    else:
        return render(request,'index.html')