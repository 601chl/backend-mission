# Generated by Django 4.0 on 2022-01-15 12:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='카테고리')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MallsItem',
            fields=[
                ('num', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('price', models.PositiveIntegerField(verbose_name='권장판매가')),
                ('sale_price', models.PositiveIntegerField(verbose_name='실제판매가')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='삭제여부')),
                ('delete_date', models.DateTimeField(blank=True, null=True, verbose_name='삭제날짜')),
                ('is_hidden', models.BooleanField(default=False, verbose_name='노출여부')),
                ('is_sold_out', models.BooleanField(default=False, verbose_name='품절여부')),
                ('kind', models.CharField(blank=True, max_length=1, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('img_url', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='갱신날짜')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.category')),
            ],
        ),
        migrations.CreateModel(
            name='MallsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='마켓이름')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='갱신날짜')),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('url', models.CharField(max_length=200)),
                ('img_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ProductReal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='갱신날짜')),
                ('option_1_type', models.CharField(default='SIZE', max_length=10, verbose_name='옵션1 타입')),
                ('option_1_name', models.CharField(max_length=50, verbose_name='옵션1 이름(내부용)')),
                ('option_1_display_name', models.CharField(max_length=50, verbose_name='옵션1 이름(고객용)')),
                ('option_2_type', models.CharField(default='COLOR', max_length=10, verbose_name='옵션2 타입')),
                ('option_2_name', models.CharField(max_length=50, verbose_name='옵션2 이름(내부용)')),
                ('option_2_display_name', models.CharField(max_length=50, verbose_name='옵션2 이름(고객용)')),
                ('option_3_type', models.CharField(blank=True, default='', max_length=10, verbose_name='옵션3 타입')),
                ('option_3_name', models.CharField(blank=True, default='', max_length=50, verbose_name='옵션3 이름(내부용)')),
                ('option_3_display_name', models.CharField(blank=True, default='', max_length=50, verbose_name='옵션3 이름(고객용)')),
                ('is_sold_out', models.BooleanField(default=False, verbose_name='품절여부')),
                ('is_hidden', models.BooleanField(default=False, verbose_name='노출여부')),
                ('add_price', models.IntegerField(default=0, verbose_name='추가가격')),
                ('stock_quantity', models.PositiveIntegerField(default=0, verbose_name='재고개수')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_reals', to='base.mallsitem')),
            ],
        ),
        migrations.CreateModel(
            name='MallsQuestion',
            fields=[
                ('q_num', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('reply', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.user')),
            ],
        ),
        migrations.AddField(
            model_name='mallsitem',
            name='id',
            field=models.ForeignKey(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, to='base.mallslist'),
        ),
        migrations.AddField(
            model_name='mallsitem',
            name='like_item',
            field=models.ManyToManyField(related_name='like_items', to='base.MallsList'),
        ),
        migrations.CreateModel(
            name='MallsAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='갱신날짜')),
                ('answer', models.TextField()),
                ('q_num', models.ForeignKey(db_column='q_num', on_delete=django.db.models.deletion.DO_NOTHING, to='base.mallsquestion')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
    ]
