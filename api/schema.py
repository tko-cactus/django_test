import graphene
from graphene_django.types import DjangoObjectType
from .models import Employee, Department
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay
from graphql_relay import from_global_id
from graphql_jwt.decorators import login_required

class EmployedNode(DjangoObjectType):
    class Meta:
        model = Employee
        filter_fields = {
            'name': ['exact', 'icontains'],
            'join_year': ['exact', 'icontains'],
            'department_dept_name': ['icontains']
        }
        interfaces = (relay.Node,)

class DeptCreateMutation(relay.ClientIDMutation):
    class Input:
        dept_name = graphene.String(required=True)
    department = graphene.Field(DepartmentNode)

    @login_required
    def mutate_and_get_payload(root, info, **input):
        
        department = Department(
            dept_name=input.get()
        )



class DepartmentNode(DjangoObjectType):
    class Meta:
        model = Department
        filter_fields = {
            'employees': ['exact'],
            'dept_name': ['exact']}
        Interfaces = (relay.Node,)

class Query(graphene.ObjectType):
    employee = graphene.Field(EmployedNode, id=graphene.NonNull(graphene.ID))
    all_employees = DjangoFilterConnectionField(EmployedNode)
    all_departments = DjangoFilterConnectionField(DepartmentNode)

    @login_required
    def resolve_employee(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Employee.objects.get(id=flogin_requiredrom_global_id(id)[1])

    @login_required
    def resolve_all_employees(self, info, **kwargs):
        return Employee.objects.all()
    
    @login_required
    def resolve_all_departments(self, info, **kwargs):
        return Department.objects.all()