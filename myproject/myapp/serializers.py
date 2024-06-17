from rest_framework import serializers # type: ignore
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model=Employee
		fields=('post_id','id','name','email','body')
