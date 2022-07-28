# Generated by Django 3.2.14 on 2022-07-28 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0002_loaddata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzaorder',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='pizzaorder',
            name='delivery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pizzas', to='pizza_app.address'),
        ),
        migrations.AlterField(
            model_name='pizzaorder',
            name='kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pizzas', to='pizza_app.pizzamenuitem'),
        ),
        migrations.AlterField(
            model_name='pizzaorder',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pizzas', to='pizza_app.pizzasize'),
        ),
    ]