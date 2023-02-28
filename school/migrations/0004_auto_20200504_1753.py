

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20200504_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='present_status',
            field=models.CharField(max_length=10),
        ),
    ]
