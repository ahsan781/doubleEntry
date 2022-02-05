from sre_constants import CATEGORY
from django.db import models

# Create your models here.
class categoryTypes (models.Model):
      id = models.AutoField(primary_key=True)
      Discription = models.CharField(max_length=200)
      def __str__(self):
             return "%s" % (self.id)
class VendorsType(models.Model):
      id = models.AutoField(primary_key=True)
      Discription = models.CharField(max_length=200)
      def __str__(self):
             return "%s" % (self.id)
       
class category (models.Model):
  id = models.AutoField(primary_key=True)
  ID_string = models.CharField(max_length=200)
  categoryType_id = models.ForeignKey(categoryTypes, on_delete=models.CASCADE)
  comment = models.CharField(max_length=200)
  payroll_deduction_flag = models.CharField(max_length=200)
  discription = models.CharField(max_length=200)
  external_account_no = models.CharField(max_length=200)
  default_category = models.CharField(max_length=200)
  visible_to_client = models.CharField(max_length=200)
  system_category = models.CharField(max_length=200)
  last_sync_date = models.DateField()
  fx_ex = models.CharField(max_length=200)
  st_ex = models.CharField(max_length=200)
  fut_ex = models.CharField(max_length=200)
  sut_ex = models.CharField(max_length=200)
  fica_ex = models.CharField(max_length=200)
  sub_account_of = models.CharField(max_length=200)
  med_ex = models.CharField(max_length=200)
  def __str__(self):
             return "%s" % (self.id)


class Vendors(models.Model):
  id = models.AutoField(primary_key=True)
  category_id = models.ForeignKey(category, on_delete=models.CASCADE)
  vendorType_id = models.ForeignKey(VendorsType, on_delete=models.CASCADE)
  company_name = models.CharField(max_length=200)
  address1 = models.CharField(max_length=200)
  address2 = models.CharField(max_length=200)
  city = models.CharField(max_length=200)
  state = models.CharField(max_length=200)
  zip4 = models.CharField(max_length=200)
  country = models.CharField(max_length=200)
  contact_name = models.CharField(max_length=200)
  phone = models.CharField(max_length=200)
  fax = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  vendor_1099_flag = models.CharField(max_length=200)
  default_memo = models.CharField(max_length=200)
  last_sync_date= models.DateField()
  tex_id = models.CharField(max_length=200)
  factor_vendor_id = models.CharField(max_length=200)
  inactive_flag = models.CharField(max_length=200)
  customer_field_1 = models.CharField(max_length=200)
  customer_field_2 = models.CharField(max_length=200)
  customer_field_3 = models.CharField(max_length=200)
  customer_field_4 = models.CharField(max_length=200)
  customer_field_5 = models.CharField(max_length=200)
  check_print_name = models.CharField(max_length=200)
  mobile = models.CharField(max_length=200)
  image_1_file = models.CharField(max_length=200)
  url_address = models.CharField(max_length=200)
  url_login_id = models.CharField(max_length=200)
  url_login_pwd = models.CharField(max_length=200)
  def __str__(self):
             return "%s" % (self.id)

class Bills(models.Model):
  id = models.AutoField(primary_key=True)
  vendor_id = models.ForeignKey(Vendors, on_delete=models.CASCADE)
  recurring_bills_id = models.CharField(max_length=200)
  invoice_no = models.CharField(max_length=200)
  invoice_date = models.DateField()
  due_date = models.DateField()
  discount_amount = models.CharField(max_length=200)
  discount_date = models.DateField()
  bill_memo = models.CharField(max_length=200)
  paid_in_full_flag = models.CharField(max_length=200)
  last_sync_date = models.DateField()
  Add_Ref = models.CharField(max_length=200)
  Add_Total = models.CharField(max_length=200)
  check_no = models.CharField(max_length=200)
  def __str__(self):
             return "%s" % (self.id)


class Bill_Item(models.Model):
  id = models.AutoField(primary_key=True)
  bill_id = models.ForeignKey(Bills , on_delete=models.CASCADE)
  category_id = models.ForeignKey(category, on_delete=models.CASCADE)
  amount = models.CharField(max_length=200)
  memo = models.CharField(max_length=200)
  last_sync_date = models.DateField()
  job_id = models.CharField(max_length=200)
  vendor_credit_id = models.CharField(max_length=200)
  Invoiceable_flag = models.CharField(max_length=200)
  invoice_item_id = models.CharField(max_length=200)
  Add_ref = models.CharField(max_length=200)
  check_no = models.CharField(max_length=200)
  def __str__(self):
             return "%s" % (self.id)

class Invoiceable_item(models.Model):
  id = models.AutoField(primary_key=True)
  account = models.ForeignKey(category, on_delete=models.CASCADE)
  discription = models.CharField(max_length=200)
  product_date = models.CharField(max_length=200)
  unit_price = models.DateField()
  texable_flag = models.CharField(max_length=200)
  last_sync_date = models.DateField
  po_only = models.CharField(max_length=200)
  inventory_id = models.CharField(max_length=200)
  untill_cost = models.CharField(max_length=200)
  expense_account = models.CharField(max_length=200)
  def __str__(self):
             return "%s" % (self.id)

class customer(models.Model):
  id = models.AutoField(primary_key=True)
  vendor_id = models.ForeignKey(Vendors, on_delete=models.CASCADE)
  costmer_no = models.CharField(max_length=200)
  name  = models.CharField(max_length=200)
  address1 = models.CharField(max_length=200)
  address2 = models.CharField(max_length=200)
  city = models.CharField(max_length=200)
  state = models.CharField(max_length=200)
  zip4 = models.CharField(max_length=200)
  country = models.CharField(max_length=200)
  contact_name = models.CharField(max_length=200)
  phone = models.CharField(max_length=200)
  fax = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  contact = models.CharField(max_length=200)
  texable_flag = models.CharField(max_length=200)
  sales_tax_code = models.DateField()
  sales_tax_rate = models.CharField(max_length=200)
  tex_exempt_id = models.CharField(max_length=200)
  customer_field_1 = models.CharField(max_length=200)
  customer_field_2 = models.CharField(max_length=200)
  customer_field_3 = models.CharField(max_length=200)
  customer_field_4 = models.CharField(max_length=200)
  customer_field_5 = models.CharField(max_length=200)
  inactive_flag = models.CharField(max_length=200)
  last_sync_date = models.DateField()
  ship_same_as_bill = models.CharField(max_length=200)
  ship_to= models.CharField(max_length=200)
  ship_address1 = models.CharField(max_length=200)
  ship_address2 = models.CharField(max_length=200)
  ship_city = models.CharField(max_length=200)
  ship_state = models.CharField(max_length=200)
  ship_zip4 = models.CharField(max_length=200)
  ship_country = models.CharField(max_length=200)
  default_items = models.CharField(max_length=200)
  log_file = models.CharField(max_length=200)
  email_inv_flag = models.CharField(max_length=200)
  email_inv_cc_flag = models.CharField(max_length=200)
  email_inv_cc_address = models.CharField(max_length=200)
  email_inv_subject = models.CharField(max_length=200)
  emai_inv_body = models.CharField(max_length=200)
  email_inv_add_attachment = models.CharField(max_length=200)
  email_inv_billing_pref = models.CharField(max_length=200)
  email_inv_billing_email = models.CharField(max_length=200)
  email_inv_file_name_formate = models.CharField(max_length=200)
  nameless = models.CharField(max_length=200)
  mobile = models.CharField(max_length=200)
  image1_file = models.CharField(max_length=200)
  default_discount_id = models.CharField(max_length=200)
  email_inv_rem_cc_address = models.CharField(max_length=200)
  email_inv_rem_subject = models.CharField(max_length=200)
  email_inv_rem_cc_body  = models.CharField(max_length=200)
  email_inv_rem_active_flag = models.CharField(max_length=200)
  email_inv_rem_days_past_due  = models.CharField(max_length=200)
  def __str__(self):
             return "%s" % (self.id)

class invoices(models.Model):
  id = models.AutoField(primary_key=True)
  customer_id = models.ForeignKey(customer, on_delete=models.CASCADE)
  invoice_no = models.CharField(max_length=200)
  invoice_date = models.DateField()
  invoive_type = models.CharField(max_length=200)
  term = models.CharField(max_length=200)
  phoneNumber = models.CharField(max_length=200)
  status = models.CharField(max_length=200)
  footer_message = models.CharField(max_length=200)
  due_date = models.DateField()
  date_printed = models.DateField()
  invoice_memo = models.CharField(max_length=200)
  paid_in_full_flag = models.CharField(max_length=200)
  job_id = models.CharField(max_length=200)
  custome_field = models.CharField(max_length=200)
  last_sync_date = models.DateField()
  footer_message = models.CharField(max_length=200)
  due_date = models.DateField()
  ship_to= models.CharField(max_length=200)
  ship_address1 = models.CharField(max_length=200)
  ship_address2 = models.CharField(max_length=200)
  ship_city = models.CharField(max_length=200)
  ship_state = models.CharField(max_length=200)
  ship_zip4 = models.CharField(max_length=200)
  ship_country = models.CharField(max_length=200)
  ship_traking_no = models.CharField(max_length=200)
  estimate = models.CharField(max_length=200)
  freight_cost = models.CharField(max_length=200)
  prt_opt_bill_fwd = models.CharField(max_length=200)
  prt_opt_aging = models.CharField(max_length=200)
  prt_opt_payment = models.CharField(max_length=200)
  elec_inv_file_name = models.CharField(max_length=200)
  elec_inv_date_sent = models.CharField(max_length=200)
  elec_inv_recipients = models.CharField(max_length=200)
  sales_tax_id = models.CharField(max_length=200)
  freight_paid_by_comp = models.CharField(max_length=200)
  pay_now_merch_old = models.CharField(max_length=200)
  reminder_count = models.CharField(max_length=200)
  ref_number = models.CharField(max_length=200)
  Add_total = models.CharField(max_length=200)
  def __str__(self):
             return "%s" % (self.id)


class invoice_items(models.Model):
  id = models.AutoField(primary_key=True)
  invoice_id = models.ForeignKey(invoices, on_delete=models.CASCADE)
  invoicable_item_id  = models.ForeignKey(Invoiceable_item, on_delete=models.CASCADE)
  discription = models.CharField(max_length=200)
  unit_price = models.CharField(max_length=200)
  amount = models.CharField(max_length=200)
  tax_ammount = models.CharField(max_length=200)
  quantity = models.CharField(max_length=200)
  product_code = models.CharField(max_length=200)
  texable_flag = models.CharField(max_length=200)
  last_sync_date = models.DateField()
  credit_payment_id = models.CharField(max_length=200)
  display_order = models.CharField(max_length=200)
  discount_id = models.CharField(max_length=200)
  trans_date = models.DateField()
  line_item_cost = models.CharField(max_length=200)
  markUp_amt = models.CharField(max_length=200)
  work_order_id = models.CharField(max_length=200)
  Add_ref = models.CharField(max_length=200)
  def __str__(self):
             return "%s" % (self.id)

class Adjustmenttypes(models.Model):
      id = models.AutoField(primary_key=True)
      Discription = models.CharField(max_length=200)
      def __str__(self):
             return "%s" % (self.id)

class Bank(models.Model):
  id = models.AutoField(primary_key=True)
  Bank_name = models.CharField(max_length=200)
  address1 = models.CharField(max_length=200)
  address2 = models.CharField(max_length=200)
  city = models.CharField(max_length=200)
  state = models.CharField(max_length=200)
  zip4 = models.CharField(max_length=200)
  country = models.CharField(max_length=200)
  contact_name = models.CharField(max_length=200)
  phone = models.CharField(max_length=200)
  fax = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  last_sync_date= models.DateField()
  url_address = models.CharField(max_length=200)
  url_login_id = models.CharField(max_length=200)
  url_login_pwd = models.CharField(max_length=200)
  def __str__(self):
             return "%s" % (self.id)

class bankaccounttypes(models.Model):
      id = models.AutoField(primary_key=True)
      Discription = models.CharField(max_length=200)
      def __str__(self):
             return "%s" % (self.id)


class Bankaccount(models.Model):
  id = models.AutoField(primary_key=True)
  bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
  bankaccount_id  = models.ForeignKey(Invoiceable_item, on_delete=models.CASCADE)
  account_no = models.CharField(max_length=200)
  current_balance = models.CharField(max_length=200)
  open_date = models.DateField()
  close_date = models.DateField()
  last_statement_date = models.DateField()
  highest_check_no = models.CharField(max_length=200)
  last_statement_ending_balance = models.CharField(max_length=200)
  start_check = models.CharField(max_length=200)
  accouny_discription = models.CharField(max_length=200)
  last_sync_date = models.DateField()
  cash_amount = models.CharField(max_length=200)
  def __str__(self):
             return "%s" % (self.id)



class Adjustment(models.Model):
  id = models.AutoField(primary_key=True)
  bankaccount_id  = models.ForeignKey(bankaccounttypes, on_delete=models.CASCADE)
  adjustmenttypes_id  = models.ForeignKey(Adjustmenttypes, on_delete=models.CASCADE)
  vendors_id  = models.ForeignKey(Vendors, on_delete=models.CASCADE)
  ad_date = models.DateField()
  reasons = models.CharField(max_length=200)
  reconciled_flag = models.CharField(max_length=200)
  last_sync_date = models.DateField()
  sales_tax_ammount = models.CharField(max_length=200)
  elec_download_file_id = models.CharField(max_length=200)
  def __str__(self):
             return "%s" % (self.id)



class invoice_item(models.Model):
  id = models.AutoField(primary_key=True)
  invoice_id  = models.ForeignKey(invoices, on_delete=models.CASCADE)
  invoiceable_id  = models.ForeignKey(Invoiceable_item, on_delete=models.CASCADE)
  discription = models.CharField(max_length=200)
  unit_price = models.CharField(max_length=200)
  amount = models.CharField(max_length=200)
  tax_amount = models.CharField(max_length=200)
  quantity = models.CharField(max_length=200)
  product_code = models.CharField(max_length=200)
  texable_flag = models.CharField(max_length=200)
  last_sync_date = models.DateField()
  credit_payment = models.CharField(max_length=200)
  display_order = models.CharField(max_length=200)
  discount_id = models.CharField(max_length=200)
  trans_date = models.CharField(max_length=200)
  line_item_cost = models.CharField(max_length=200)
  maekup_amt = models.CharField(max_length=200)
  work_order_id = models.CharField(max_length=200)
  Add_ref = models.CharField(max_length=200)
  def __str__(self):
             return "%s" % (self.id)



class Adjustment_item(models.Model):
  id = models.AutoField(primary_key=True)
  adjustment_id  = models.ForeignKey(Adjustment, on_delete=models.CASCADE)
  category_id  = models.ForeignKey(category, on_delete=models.CASCADE)
  customer_id  = models.ForeignKey(customer, on_delete=models.CASCADE)
  bill_id  = models.ForeignKey(Bills, on_delete=models.CASCADE)
  invoice_item_id  = models.ForeignKey(invoice_item, on_delete=models.CASCADE)
  adjustment_amount = models.CharField(max_length=200)
  last_sync_date = models.DateField()
  invoiceable_flag = models.CharField(max_length=200)
  def __str__(self):
             return "%s" % (self.id)



class category_group_type(models.Model):
      id = models.AutoField(primary_key=True)
      Discription = models.CharField(max_length=200)
      def __str__(self):
             return "%s" % (self.id)

class category_group(models.Model):
  id = models.AutoField(primary_key=True)
  category_group_item = models.ForeignKey(category_group_type, on_delete=models.CASCADE)
  ategory_group_name = models.CharField(max_length=200)
  act_no_range_start = models.CharField(max_length=200)
  act_no_range_end = models.CharField(max_length=200)
  last_sync_date = models.DateField()
  Add_ref = models.CharField(max_length=200)
  def __str__(self):
             return "%s" % (self.id)

class check(models.Model):
  id = models.AutoField(primary_key=True)
  bankaccount_id  = models.ForeignKey(Bankaccount, on_delete=models.CASCADE)
  vendor_id = models.ForeignKey(Vendors, on_delete=models.CASCADE)
  check_no = models.CharField(max_length=200)
  check_cut_date = models.DateField()
  status = models.CharField(max_length=200)
  status_change_date = models.DateField()
  type_of_check = models.CharField(max_length=200)
  possesd_by = models.CharField(max_length=200)
  reconciled_flag = models.CharField(max_length=200)
  check_printed_date = models.CharField(max_length=200)
  check_memo = models.CharField(max_length=200)
  last_sync_date = models.DateField()
  vendor_name_text = models.CharField(max_length=200)
  factor_for_vendor_id = models.CharField(max_length=200)
  elec_download_file_id = models.CharField(max_length=200)
  Add_Ck_total = models.CharField(max_length=200)
  Ads_ref = models.CharField(max_length=200)
  def __str__(self):
             return "%s" % (self.id)



class checkcategories(models.Model):
  id = models.AutoField(primary_key=True)
  check_id  = models.ForeignKey(check, on_delete=models.CASCADE)
  category_id = models.ForeignKey(category, on_delete=models.CASCADE)
  bill_id = models.ForeignKey(Bills, on_delete=models.CASCADE)
  invoice_item_id = models.ForeignKey(invoice_item, on_delete=models.CASCADE)
  amount_paid = models.CharField(max_length=200)
  last_sync_date = models.DateField()
  Bill_desc = models.CharField(max_length=200)
  vendor_1099_flag = models.CharField(max_length=200)
  checkcat_memo  = models.CharField(max_length=200)
  credit_payment_id = models.CharField(max_length=200)
  Invoiceable_flag = models.CharField(max_length=200)
  def __str__(self):
             return "%s" % (self.id)

class card(models.Model):
  id = models.AutoField(primary_key=True)
  card_trans_type = models.CharField(max_length=200)
  card_bank_acct = models.CharField(max_length=200)
  card_owner = models.CharField(max_length=200)
  card_number = models.CharField(max_length=200)
  card_number_last_4 = models.CharField(max_length=200)
  card_type = models.DateField()
  card_exp_month = models.CharField(max_length=200)
  card_exp_year = models.CharField(max_length=200)
  name_on_card  = models.CharField(max_length=200)
  last_sync_date = models.DateField()
  card_desc = models.CharField(max_length=200)
  def __str__(self):
             return "%s" % (self.id)


class payment(models.Model):
  id = models.AutoField(primary_key=True)
  customer_id  = models.ForeignKey(customer, on_delete=models.CASCADE)
  card_id = models.ForeignKey(card, on_delete=models.CASCADE)
  data_recived = models.CharField(max_length=200)
  amount = models.CharField(max_length=200)
  payment_type = models.CharField(max_length=200)
  payment_method = models.CharField(max_length=200)
  check_number = models.CharField(max_length=200)
  nsf_flag  = models.CharField(max_length=200)
  memo = models.CharField(max_length=200)
  credit_payment_id = models.CharField(max_length=200)
  last_sync_date = models.DateField()
  card_id  = models.CharField(max_length=200)
  card_auth_code  = models.CharField(max_length=200)
  merch_old = models.CharField(max_length=200)
  def __str__(self):
             return "%s" % (self.id)


class invoice_payment(models.Model):
  id = models.AutoField(primary_key=True)
  payment_id  = models.ForeignKey(payment, on_delete=models.CASCADE)
  invoice_id = models.ForeignKey(invoices, on_delete=models.CASCADE)
  invoice_item_paid  = models.CharField(max_length=200)
  sales_tax_amt_paid = models.CharField(max_length=200)
  last_sync_date = models.DateField()
  freight_amt_paid = models.CharField(max_length=200)
  def __str__(self):
             return "%s" % (self.id)




class Report(models.Model):
  id = models.AutoField(primary_key=True)
  report_name = models.CharField(max_length=200)
  external_path = models.CharField(max_length=200)
  launch_with_program  = models.CharField(max_length=200)
  preformatted  = models.CharField(max_length=200)
  report_type = models.CharField(max_length=200)
  report_desc = models.CharField(max_length=200)
  def __str__(self):
             return "%s" % (self.id)



class Table_id(models.Model):
  id = models.AutoField(primary_key=True)
  description = models.CharField(max_length=200)
  max_id = models.CharField(max_length=200)
  last_sync_date = models.CharField(max_length=200)
  Table_type = models.CharField(max_length=200)
  def __str__(self):
             return "%s" % (self.id)



class Accountant_frims(models.Model):
  id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=200)
  address1 = models.CharField(max_length=200)
  address2 = models.CharField(max_length=200)
  city = models.CharField(max_length=200)
  state = models.CharField(max_length=200)
  zip4 = models.CharField(max_length=200)
  last_sync_date= models.DateField()
  def __str__(self):
             return "%s" % (self.id)


class accountant(models.Model):
  id = models.AutoField(primary_key=True)
  accountant_frim_id  = models.ForeignKey(Accountant_frims, on_delete=models.CASCADE)
  accountant_name = models.CharField(max_length=200)
  computer  = models.CharField(max_length=200)
  phone = models.CharField(max_length=200)
  fax = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  last_sync_date= models.DateField()
  website = models.CharField(max_length=200)
  password = models.CharField(max_length=200)
  access_level = models.CharField(max_length=200)
  def __str__(self):
             return "%s" % (self.id)


class check_type(models.Model):
  id = models.AutoField(primary_key=True)
  discription = models.CharField(max_length=200)
  custome_field  = models.CharField(max_length=200)
  vertocal_nudge = models.CharField(max_length=200)
  horizental_nudge  = models.CharField(max_length=200)
  line_spacing_nudge = models.CharField(max_length=200)
  last_sync_date= models.DateField()
  def __str__(self):
             return "%s" % (self.id)


class invoice_type(models.Model):
  id = models.AutoField(primary_key=True)
  discription = models.CharField(max_length=200)
  custome_field  = models.CharField(max_length=200)
  vertocal_nudge = models.CharField(max_length=200)
  horizental_nudge  = models.CharField(max_length=200)
  line_spacing_nudge = models.CharField(max_length=200)
  last_sync_date= models.DateField()
  def __str__(self):
             return "%s" % (self.id)

class client_type(models.Model):
  id = models.AutoField(primary_key=True)
  discription = models.CharField(max_length=200)
  last_sync_date= models.DateField()
  def __str__(self):
             return "%s" % (self.id)


class clients(models.Model):
  id = models.AutoField(primary_key=True)
  accountant_id  = models.ForeignKey(accountant, on_delete=models.CASCADE)
  clienttype_id  = models.ForeignKey(client_type, on_delete=models.CASCADE)
  checktype_id  = models.ForeignKey(check_type, on_delete=models.CASCADE)
  invoicetype_id  = models.ForeignKey(invoice_type, on_delete=models.CASCADE)
  company_name = models.CharField(max_length=200)
  address1 = models.CharField(max_length=200)
  address2 = models.CharField(max_length=200)
  city = models.CharField(max_length=200)
  state = models.CharField(max_length=200)
  zip4 = models.CharField(max_length=200)
  contact_number_1  = models.CharField(max_length=200)
  contact_number_2  = models.CharField(max_length=200)
  computer = models.CharField(max_length=200)
  phone = models.CharField(max_length=200)
  fax = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  website = models.CharField(max_length=200)
  fed_tax_id = models.CharField(max_length=200)
  state_tax_id = models.CharField(max_length=200)
  state_unemployment_id  = models.CharField(max_length=200)
  current_year_end_date  = models.DateField()
  folder_name  = models.CharField(max_length=200)
  last_sync_date_for_client = models.DateField()
  last_backup_date = models.DateField()
  last_taxable_loaded = models.DateField()
  sut_precent = models.FloatField()
  program_location = models.CharField(max_length=200)
  fut_percent  = models.FloatField()
  remote = models.CharField(max_length=200)
  year_end_only = models.CharField(max_length=200)
  report_group = models.CharField(max_length=200)
  logo = models.CharField(max_length=200)
  accounting_type = models.CharField(max_length=200)
  email_inv_attachment_files_default = models.CharField(max_length=200)
  email_inv_body_default = models.CharField(max_length=200)
  email_inv_rem_subject_default = models.CharField(max_length=200)
  email_inv_rem_body_default  = models.CharField(max_length=200)
  email_inv_rem_active_flag  = models.CharField(max_length=200)
  last_sync_date_for_client = models.DateField()
  email_inv_rem_days_past_due = models.CharField(max_length=200)
  email_inv_rem_create_on_startup_flag = models.CharField(max_length=200)
  last_sync_date= models.DateField()
  def __str__(self):
             return "%s" % (self.id)



class table_ID_client(models.Model):
  id = models.AutoField(primary_key=True)
  discription = models.CharField(max_length=200)
  Max_id  = models.CharField(max_length=200)
  connecttable = models.CharField(max_length=200)
  comment = models.CharField(max_length=200)
  last_sync_date= models.DateTimeField()
  def __str__(self):
             return "%s" % (self.id)





class trial_Balance_item(models.Model):
  id = models.AutoField(primary_key=True)
  table_id  = models.ForeignKey(Table_id, on_delete=models.CASCADE)
  category_id  = models.ForeignKey(category, on_delete=models.CASCADE)
  table_code = models.CharField(max_length=200)
  table_name  = models.CharField(max_length=200)
  category_discription = models.CharField(max_length=200)
  batch_no = models.CharField(max_length=200)
  item_date = models.DateField()
  debit_amount  = models.FloatField()
  credit_amount = models.FloatField()
  debit_adjustment = models.CharField(max_length=200)
  credit_adjustment = models.CharField(max_length=200)
  Add_ref  = models.CharField(max_length=200)
  Add_bill_d = models.CharField(max_length=200)
  last_sync_date= models.DateTimeField()
  def __str__(self):
             return "%s" % (self.id)


