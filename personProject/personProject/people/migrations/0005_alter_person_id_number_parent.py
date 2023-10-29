from django.db import migrations, models
from django.core.validators import MaxValueValidator

def change_field_type(apps, schema_editor):
    YourModel = apps.get_model('people', 'parent')

    for obj in YourModel.objects.all():
        obj.base_salary = int(obj.base_salary)
        obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_alter_person_id_number_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='base_salary',
            field=models.IntegerField(validators=[MaxValueValidator(999999)], null=False),  
        ),
        migrations.RunPython(change_field_type), 
    ]