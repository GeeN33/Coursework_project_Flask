from app import app
from flask import render_template, redirect ,request
from models import Employee

@app.route('/', methods=['GET', 'POST'])
def index():
    employees = Employee.select()
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        Employee(name=name, email=email, phone=phone).save()

    return redirect('/')

@app.route('/update/<id>', methods=['GET', 'POST'])
def update_employee(id):
    if request.method == 'POST':
        id = id
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        Employee(id=id, name=name, email=email, phone=phone).save()
    return redirect('/')

@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete_employee(id):
    if request.method == 'GET':
        employee = Employee.get(Employee.id == id)
        employee .delete_instance()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)