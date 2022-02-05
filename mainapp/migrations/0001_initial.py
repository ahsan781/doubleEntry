# Generated by Django 4.0.1 on 2022-01-20 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ID_string', models.CharField(max_length=200)),
                ('comment', models.CharField(max_length=200)),
                ('payroll_deduction_flag', models.CharField(max_length=200)),
                ('discription', models.CharField(max_length=200)),
                ('external_account_no', models.CharField(max_length=200)),
                ('default_category', models.CharField(max_length=200)),
                ('visible_to_client', models.CharField(max_length=200)),
                ('system_category', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
                ('fx_ex', models.CharField(max_length=200)),
                ('st_ex', models.CharField(max_length=200)),
                ('fut_ex', models.CharField(max_length=200)),
                ('sut_ex', models.CharField(max_length=200)),
                ('fica_ex', models.CharField(max_length=200)),
                ('sub_account_of', models.CharField(max_length=200)),
                ('med_ex', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='categoryTypes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Discription', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('costmer_no', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip4', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('contact_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('fax', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('texable_flag', models.CharField(max_length=200)),
                ('sales_tax_code', models.DateField()),
                ('sales_tax_rate', models.CharField(max_length=200)),
                ('tex_exempt_id', models.CharField(max_length=200)),
                ('customer_field_1', models.CharField(max_length=200)),
                ('customer_field_2', models.CharField(max_length=200)),
                ('customer_field_3', models.CharField(max_length=200)),
                ('customer_field_4', models.CharField(max_length=200)),
                ('customer_field_5', models.CharField(max_length=200)),
                ('inactive_flag', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
                ('ship_same_as_bill', models.CharField(max_length=200)),
                ('ship_to', models.CharField(max_length=200)),
                ('ship_address1', models.CharField(max_length=200)),
                ('ship_address2', models.CharField(max_length=200)),
                ('ship_city', models.CharField(max_length=200)),
                ('ship_state', models.CharField(max_length=200)),
                ('ship_zip4', models.CharField(max_length=200)),
                ('ship_country', models.CharField(max_length=200)),
                ('default_items', models.CharField(max_length=200)),
                ('log_file', models.CharField(max_length=200)),
                ('email_inv_flag', models.CharField(max_length=200)),
                ('email_inv_cc_flag', models.CharField(max_length=200)),
                ('email_inv_cc_address', models.CharField(max_length=200)),
                ('email_inv_subject', models.CharField(max_length=200)),
                ('emai_inv_body', models.CharField(max_length=200)),
                ('email_inv_add_attachment', models.CharField(max_length=200)),
                ('email_inv_billing_pref', models.CharField(max_length=200)),
                ('email_inv_billing_email', models.CharField(max_length=200)),
                ('email_inv_file_name_formate', models.CharField(max_length=200)),
                ('nameless', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('image1_file', models.CharField(max_length=200)),
                ('default_discount_id', models.CharField(max_length=200)),
                ('email_inv_rem_cc_address', models.CharField(max_length=200)),
                ('email_inv_rem_subject', models.CharField(max_length=200)),
                ('email_inv_rem_cc_body', models.CharField(max_length=200)),
                ('email_inv_rem_active_flag', models.CharField(max_length=200)),
                ('email_inv_rem_days_past_due', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='VendorsType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Discription', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=200)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip4', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('contact_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('fax', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('vendor_1099_flag', models.CharField(max_length=200)),
                ('default_memo', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
                ('tex_id', models.CharField(max_length=200)),
                ('factor_vendor_id', models.CharField(max_length=200)),
                ('inactive_flag', models.CharField(max_length=200)),
                ('customer_field_1', models.CharField(max_length=200)),
                ('customer_field_2', models.CharField(max_length=200)),
                ('customer_field_3', models.CharField(max_length=200)),
                ('customer_field_4', models.CharField(max_length=200)),
                ('customer_field_5', models.CharField(max_length=200)),
                ('check_print_name', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('image_1_file', models.CharField(max_length=200)),
                ('url_address', models.CharField(max_length=200)),
                ('url_login_id', models.CharField(max_length=200)),
                ('url_login_pwd', models.CharField(max_length=200)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
                ('vendorType_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.vendorstype')),
            ],
        ),
        migrations.CreateModel(
            name='invoices',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('invoice_no', models.CharField(max_length=200)),
                ('invoice_date', models.DateField()),
                ('invoive_type', models.CharField(max_length=200)),
                ('term', models.CharField(max_length=200)),
                ('phoneNumber', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('date_printed', models.DateField()),
                ('invoice_memo', models.CharField(max_length=200)),
                ('paid_in_full_flag', models.CharField(max_length=200)),
                ('job_id', models.CharField(max_length=200)),
                ('custome_field', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
                ('footer_message', models.CharField(max_length=200)),
                ('due_date', models.DateField()),
                ('ship_to', models.CharField(max_length=200)),
                ('ship_address1', models.CharField(max_length=200)),
                ('ship_address2', models.CharField(max_length=200)),
                ('ship_city', models.CharField(max_length=200)),
                ('ship_state', models.CharField(max_length=200)),
                ('ship_zip4', models.CharField(max_length=200)),
                ('ship_country', models.CharField(max_length=200)),
                ('ship_traking_no', models.CharField(max_length=200)),
                ('estimate', models.CharField(max_length=200)),
                ('freight_cost', models.CharField(max_length=200)),
                ('prt_opt_bill_fwd', models.CharField(max_length=200)),
                ('prt_opt_aging', models.CharField(max_length=200)),
                ('prt_opt_payment', models.CharField(max_length=200)),
                ('elec_inv_file_name', models.CharField(max_length=200)),
                ('elec_inv_date_sent', models.CharField(max_length=200)),
                ('elec_inv_recipients', models.CharField(max_length=200)),
                ('sales_tax_id', models.CharField(max_length=200)),
                ('freight_paid_by_comp', models.CharField(max_length=200)),
                ('pay_now_merch_old', models.CharField(max_length=200)),
                ('reminder_count', models.CharField(max_length=200)),
                ('ref_number', models.CharField(max_length=200)),
                ('Add_total', models.CharField(max_length=200)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Invoiceable_item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('discription', models.CharField(max_length=200)),
                ('product_date', models.CharField(max_length=200)),
                ('unit_price', models.DateField()),
                ('texable_flag', models.CharField(max_length=200)),
                ('po_only', models.CharField(max_length=200)),
                ('inventory_id', models.CharField(max_length=200)),
                ('untill_cost', models.CharField(max_length=200)),
                ('expense_account', models.CharField(max_length=200)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='invoice_items',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('discription', models.CharField(max_length=200)),
                ('unit_price', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('tax_ammount', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=200)),
                ('product_code', models.CharField(max_length=200)),
                ('texable_flag', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
                ('credit_payment_id', models.CharField(max_length=200)),
                ('display_order', models.CharField(max_length=200)),
                ('discount_id', models.CharField(max_length=200)),
                ('trans_date', models.DateField()),
                ('line_item_cost', models.CharField(max_length=200)),
                ('markUp_amt', models.CharField(max_length=200)),
                ('work_order_id', models.CharField(max_length=200)),
                ('Add_ref', models.CharField(max_length=200)),
                ('invoicable_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.invoiceable_item')),
                ('invoice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.invoices')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='vendor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.vendors'),
        ),
        migrations.AddField(
            model_name='category',
            name='categoryType_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.categorytypes'),
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('recurring_bills_id', models.CharField(max_length=200)),
                ('invoice_no', models.CharField(max_length=200)),
                ('invoice_date', models.DateField()),
                ('due_date', models.DateField()),
                ('discount_amount', models.CharField(max_length=200)),
                ('discount_date', models.DateField()),
                ('bill_memo', models.CharField(max_length=200)),
                ('paid_in_full_flag', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
                ('Add_Ref', models.CharField(max_length=200)),
                ('Add_Total', models.CharField(max_length=200)),
                ('check_no', models.CharField(max_length=200)),
                ('vendor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.vendors')),
            ],
        ),
        migrations.CreateModel(
            name='Bill_Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.CharField(max_length=200)),
                ('memo', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
                ('job_id', models.CharField(max_length=200)),
                ('vendor_credit_id', models.CharField(max_length=200)),
                ('Invoiceable_flag', models.CharField(max_length=200)),
                ('invoice_item_id', models.CharField(max_length=200)),
                ('Add_ref', models.CharField(max_length=200)),
                ('check_no', models.CharField(max_length=200)),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.bills')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
            ],
        ),
    ]