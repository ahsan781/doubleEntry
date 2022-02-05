# Generated by Django 4.0.1 on 2022-01-29 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='accountant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('accountant_name', models.CharField(max_length=200)),
                ('computer', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('fax', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
                ('website', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('access_level', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Accountant_frims',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip4', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Adjustment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ad_date', models.DateField()),
                ('reasons', models.CharField(max_length=200)),
                ('reconciled_flag', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
                ('sales_tax_ammount', models.CharField(max_length=200)),
                ('elec_download_file_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Adjustmenttypes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Discription', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Bank_name', models.CharField(max_length=200)),
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
                ('last_sync_date', models.DateField()),
                ('url_address', models.CharField(max_length=200)),
                ('url_login_id', models.CharField(max_length=200)),
                ('url_login_pwd', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Bankaccount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('account_no', models.CharField(max_length=200)),
                ('current_balance', models.CharField(max_length=200)),
                ('open_date', models.DateField()),
                ('close_date', models.DateField()),
                ('last_statement_date', models.DateField()),
                ('highest_check_no', models.CharField(max_length=200)),
                ('last_statement_ending_balance', models.CharField(max_length=200)),
                ('start_check', models.CharField(max_length=200)),
                ('accouny_discription', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
                ('cash_amount', models.CharField(max_length=200)),
                ('bank_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.bank')),
                ('bankaccount_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.invoiceable_item')),
            ],
        ),
        migrations.CreateModel(
            name='bankaccounttypes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Discription', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='card',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('card_trans_type', models.CharField(max_length=200)),
                ('card_bank_acct', models.CharField(max_length=200)),
                ('card_owner', models.CharField(max_length=200)),
                ('card_number', models.CharField(max_length=200)),
                ('card_number_last_4', models.CharField(max_length=200)),
                ('card_type', models.DateField()),
                ('card_exp_month', models.CharField(max_length=200)),
                ('card_exp_year', models.CharField(max_length=200)),
                ('name_on_card', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
                ('card_desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='category_group_type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Discription', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='check',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('check_no', models.CharField(max_length=200)),
                ('check_cut_date', models.DateField()),
                ('status', models.CharField(max_length=200)),
                ('status_change_date', models.DateField()),
                ('type_of_check', models.CharField(max_length=200)),
                ('possesd_by', models.CharField(max_length=200)),
                ('reconciled_flag', models.CharField(max_length=200)),
                ('check_printed_date', models.CharField(max_length=200)),
                ('check_memo', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
                ('vendor_name_text', models.CharField(max_length=200)),
                ('factor_for_vendor_id', models.CharField(max_length=200)),
                ('elec_download_file_id', models.CharField(max_length=200)),
                ('Add_Ck_total', models.CharField(max_length=200)),
                ('Ads_ref', models.CharField(max_length=200)),
                ('bankaccount_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.bankaccount')),
                ('vendor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.vendors')),
            ],
        ),
        migrations.CreateModel(
            name='check_type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('discription', models.CharField(max_length=200)),
                ('custome_field', models.CharField(max_length=200)),
                ('vertocal_nudge', models.CharField(max_length=200)),
                ('horizental_nudge', models.CharField(max_length=200)),
                ('line_spacing_nudge', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='client_type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('discription', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='invoice_type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('discription', models.CharField(max_length=200)),
                ('custome_field', models.CharField(max_length=200)),
                ('vertocal_nudge', models.CharField(max_length=200)),
                ('horizental_nudge', models.CharField(max_length=200)),
                ('line_spacing_nudge', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('report_name', models.CharField(max_length=200)),
                ('external_path', models.CharField(max_length=200)),
                ('launch_with_program', models.CharField(max_length=200)),
                ('preformatted', models.CharField(max_length=200)),
                ('report_type', models.CharField(max_length=200)),
                ('report_desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Table_id',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
                ('max_id', models.CharField(max_length=200)),
                ('last_sync_date', models.CharField(max_length=200)),
                ('Table_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='table_ID_client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('discription', models.CharField(max_length=200)),
                ('Max_id', models.CharField(max_length=200)),
                ('connecttable', models.CharField(max_length=200)),
                ('comment', models.CharField(max_length=200)),
                ('last_sync_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='trial_Balance_item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('table_code', models.CharField(max_length=200)),
                ('table_name', models.CharField(max_length=200)),
                ('category_discription', models.CharField(max_length=200)),
                ('batch_no', models.CharField(max_length=200)),
                ('item_date', models.DateField()),
                ('debit_amount', models.FloatField()),
                ('credit_amount', models.FloatField()),
                ('debit_adjustment', models.CharField(max_length=200)),
                ('credit_adjustment', models.CharField(max_length=200)),
                ('Add_ref', models.CharField(max_length=200)),
                ('Add_bill_d', models.CharField(max_length=200)),
                ('last_sync_date', models.DateTimeField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
                ('table_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.table_id')),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_recived', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('payment_type', models.CharField(max_length=200)),
                ('payment_method', models.CharField(max_length=200)),
                ('check_number', models.CharField(max_length=200)),
                ('nsf_flag', models.CharField(max_length=200)),
                ('memo', models.CharField(max_length=200)),
                ('credit_payment_id', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
                ('card_id', models.CharField(max_length=200)),
                ('card_auth_code', models.CharField(max_length=200)),
                ('merch_old', models.CharField(max_length=200)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='invoice_payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('invoice_item_paid', models.CharField(max_length=200)),
                ('sales_tax_amt_paid', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
                ('freight_amt_paid', models.CharField(max_length=200)),
                ('invoice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.invoices')),
                ('payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.payment')),
            ],
        ),
        migrations.CreateModel(
            name='invoice_item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('discription', models.CharField(max_length=200)),
                ('unit_price', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('tax_amount', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=200)),
                ('product_code', models.CharField(max_length=200)),
                ('texable_flag', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
                ('credit_payment', models.CharField(max_length=200)),
                ('display_order', models.CharField(max_length=200)),
                ('discount_id', models.CharField(max_length=200)),
                ('trans_date', models.CharField(max_length=200)),
                ('line_item_cost', models.CharField(max_length=200)),
                ('maekup_amt', models.CharField(max_length=200)),
                ('work_order_id', models.CharField(max_length=200)),
                ('Add_ref', models.CharField(max_length=200)),
                ('invoice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.invoices')),
                ('invoiceable_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.invoiceable_item')),
            ],
        ),
        migrations.CreateModel(
            name='clients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=200)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip4', models.CharField(max_length=200)),
                ('contact_number_1', models.CharField(max_length=200)),
                ('contact_number_2', models.CharField(max_length=200)),
                ('computer', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('fax', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('fed_tax_id', models.CharField(max_length=200)),
                ('state_tax_id', models.CharField(max_length=200)),
                ('state_unemployment_id', models.CharField(max_length=200)),
                ('current_year_end_date', models.DateField()),
                ('folder_name', models.CharField(max_length=200)),
                ('last_backup_date', models.DateField()),
                ('last_taxable_loaded', models.DateField()),
                ('sut_precent', models.FloatField()),
                ('program_location', models.CharField(max_length=200)),
                ('fut_percent', models.FloatField()),
                ('remote', models.CharField(max_length=200)),
                ('year_end_only', models.CharField(max_length=200)),
                ('report_group', models.CharField(max_length=200)),
                ('logo', models.CharField(max_length=200)),
                ('accounting_type', models.CharField(max_length=200)),
                ('email_inv_attachment_files_default', models.CharField(max_length=200)),
                ('email_inv_body_default', models.CharField(max_length=200)),
                ('email_inv_rem_subject_default', models.CharField(max_length=200)),
                ('email_inv_rem_body_default', models.CharField(max_length=200)),
                ('email_inv_rem_active_flag', models.CharField(max_length=200)),
                ('last_sync_date_for_client', models.DateField()),
                ('email_inv_rem_days_past_due', models.CharField(max_length=200)),
                ('email_inv_rem_create_on_startup_flag', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
                ('accountant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.accountant')),
                ('checktype_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.check_type')),
                ('clienttype_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.client_type')),
                ('invoicetype_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.invoice_type')),
            ],
        ),
        migrations.CreateModel(
            name='checkcategories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount_paid', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
                ('Bill_desc', models.CharField(max_length=200)),
                ('vendor_1099_flag', models.CharField(max_length=200)),
                ('checkcat_memo', models.CharField(max_length=200)),
                ('credit_payment_id', models.CharField(max_length=200)),
                ('Invoiceable_flag', models.CharField(max_length=200)),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.bills')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
                ('check_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.check')),
                ('invoice_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.invoice_item')),
            ],
        ),
        migrations.CreateModel(
            name='category_group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ategory_group_name', models.CharField(max_length=200)),
                ('act_no_range_start', models.CharField(max_length=200)),
                ('act_no_range_end', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
                ('Add_ref', models.CharField(max_length=200)),
                ('category_group_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category_group_type')),
            ],
        ),
        migrations.CreateModel(
            name='Adjustment_item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('adjustment_amount', models.CharField(max_length=200)),
                ('last_sync_date', models.DateField()),
                ('invoiceable_flag', models.CharField(max_length=200)),
                ('adjustment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.adjustment')),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.bills')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.customer')),
                ('invoice_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.invoice_item')),
            ],
        ),
        migrations.AddField(
            model_name='adjustment',
            name='adjustmenttypes_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.adjustmenttypes'),
        ),
        migrations.AddField(
            model_name='adjustment',
            name='bankaccount_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.bankaccounttypes'),
        ),
        migrations.AddField(
            model_name='adjustment',
            name='vendors_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.vendors'),
        ),
        migrations.AddField(
            model_name='accountant',
            name='accountant_frim_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.accountant_frims'),
        ),
    ]
