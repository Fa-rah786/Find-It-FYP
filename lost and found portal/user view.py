from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from .models import User

def register_user(request):
    if request.method == 'POST':
        role = request.POST.get('role')

        user = User(
            username=request.POST.get('username'),
            password=make_password(request.POST.get('password')),
            role=role
        )

        if role == 'student':
            user.reg_no = request.POST.get('reg_no')

        elif role == 'staff':
            user.employee_id = request.POST.get('employee_id')

        elif role == 'external':
            user.email = request.POST.get('email')

        user.save()

        return JsonResponse({'message': 'User registered successfully'})
    from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from .models import User

def register_user(request):
    if request.method == 'POST':
        role = request.POST.get('role')

        user = User(
            username=request.POST.get('username'),
            password=make_password(request.POST.get('password')),
            role=role
        )

        if role == 'student':
            user.reg_no = request.POST.get('reg_no')

        elif role == 'staff':
            user.employee_id = request.POST.get('employee_id')

        elif role == 'external':
            user.email = request.POST.get('email')

        user.save()

        return JsonResponse({'message': 'User registered successfully'})
    from .models import Relation

def request_relation(request):
    if request.method == 'POST':
        external_user = request.user
        reg_no = request.POST.get('reg_no')

        try:
            student = User.objects.get(reg_no=reg_no, role='student')
        except User.DoesNotExist:
            return JsonResponse({'error': 'Student not found'})

        Relation.objects.create(
            external_user=external_user,
            student=student,
            relation_type=request.POST.get('relation_type')
        )

        return JsonResponse({'message': 'Request sent'})
    def approve_relation(request):
    if request.method == 'POST':
        relation_id = request.POST.get('relation_id')

        relation = Relation.objects.get(id=relation_id)
        relation.status = 'approved'
        relation.save()

        return JsonResponse({'message': 'Relation approved'})