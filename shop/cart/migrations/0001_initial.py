# Generated by Django 3.0.6 on 2020-06-05 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def load_cart_status(apps, schema_editor):
    CartState = apps.get_model("cart", "CartState")
    cart_status_new = CartState(id=0, name='New')
    cart_status_new.save()
    cart_status_processing = CartState(id=1, name='Processing')
    cart_status_processing.save()
    cart_status_sent = CartState(id=2, name='Sent')
    cart_status_sent.save()
    cart_status_delivered = CartState(id=3, name='Delivered')
    cart_status_delivered.save()
    cart_status_rejected = CartState(id=4, name='Rejected')
    cart_status_rejected.save()
    cart_status_completed = CartState(id=5, name='Completed')
    cart_status_completed.save()


def delete_cart_status(apps, schema_editor):
    CartState = apps.get_model("cart", "CartState")
    CartState.objects.all().delete()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0005_auto_20200605_0848'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=5)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cartId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cart.Cart')),
                ('goodsId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goods.Goods')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='docStateId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cart.CartState'),
        ),
        migrations.AddField(
            model_name='cart',
            name='employeeUserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employeeUserId', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cart',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='userId', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RunPython(load_cart_status, delete_cart_status)
    ]
