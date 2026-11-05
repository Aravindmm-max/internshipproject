from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from .models import EmployeeModel
from .forms import (
    EmployeeForm,
    LoginForm,
    RegisterForm,
    ChangePasswordForm
)


# =========================
# Dashboard
# =========================
@login_required
def index(request):

    employees = EmployeeModel.objects.all()

    return render(request, 'dashboard.html', {
        'employees': employees
    })


# =========================
# Register
# =========================
def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')

    else:

        form = RegisterForm()

    return render(request, 'register.html', {
        'form': form
    })


# =========================
# Login
# =========================
def user_login(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":

        form = LoginForm(data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            next_url = request.GET.get('next')

            if next_url:
                return redirect(next_url)

            return redirect('dashboard')

    else:

        form = LoginForm()

    return render(request, 'login.html', {
        'form': form
    })


# =========================
# Logout
# =========================
@login_required
def user_logout(request):

    logout(request)

    return redirect('login')


# =========================
# Add Employee
# =========================
@login_required
def add_employee(request):

    if request.method == "POST":

        form = EmployeeForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            return redirect('dashboard')

    else:

        form = EmployeeForm()

    return render(request, 'add_employee.html', {
        'form': form
    })


# =========================
# Employee Details
# =========================
@login_required
def single_employee(request, id):

    employee = get_object_or_404(EmployeeModel, id=id)

    return render(request, 'single_employee.html', {
        'employee': employee
    })


# =========================
# Update Employee
# =========================
@login_required
def update_employee(request, id):

    employee = get_object_or_404(EmployeeModel, id=id)

    if request.method == "POST":

        form = EmployeeForm(
            request.POST,
            request.FILES,
            instance=employee
        )

        if form.is_valid():

            form.save()

            return redirect('dashboard')

    else:

        form = EmployeeForm(instance=employee)

    return render(request, 'update_employee.html', {
        'form': form
    })


# =========================
# Delete Employee
# =========================
@login_required
def delete_employee(request, id):

    employee = get_object_or_404(EmployeeModel, id=id)

    employee.delete()

    return redirect('dashboard')


# =========================
# Change Password
# =========================
@login_required
def change_password(request):

    if request.method == "POST":

        form = ChangePasswordForm(
            request.user,
            request.POST
        )

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(request, user)

            return redirect('dashboard')

    else:

        form = ChangePasswordForm(request.user)

    return render(request, 'change_pass.html', {
        'form': form
    })