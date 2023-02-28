
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_auto_20200506_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentextra',
            name='fee',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
