from rest_framework import serializers
from ...models import Task
from accounts.models import User






class TaskSerializer (serializers.ModelSerializer):
    class Meta:
        model =Task
        fields = ['id','author','title','is_done','content','created_date' ,'updated_date','deadline']

        read_only_fields = ['author']


    def get_abs_url(self,obj):
        request =self.context.get('request')
        return request.build_absolute_uri(obj.pk)








    def to_representation(self, instance):
        request =self.context.get("request")
        rep= super().to_representation(instance)
        rep['state']='list'
        if request.parser_context.get('kwargs').get('pk'):
            rep['state']='single'
        else:
            rep.pop('content',None)
        return rep





    def create(self, validated_data):
    
        validated_data['author'] = self.context.get('request').user
        return super().create(validated_data)
    

