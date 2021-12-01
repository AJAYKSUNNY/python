# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Sequelizemeta(models.Model):
    name = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'SequelizeMeta'


class AadhaarDetails(models.Model):
    aadhaar_details_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField(unique=True)
    aadhaar_first_name = models.CharField(max_length=191, blank=True, null=True)
    aadhaar_number = models.CharField(max_length=191, blank=True, null=True)
    encrypted_aadhar_number = models.CharField(max_length=200, blank=True, null=True)
    aadhaar_address = models.TextField(blank=True, null=True)
    aadhaar_city = models.CharField(max_length=191, blank=True, null=True)
    aadhaar_state = models.CharField(max_length=191, blank=True, null=True)
    aadhaar_pin = models.CharField(max_length=191, blank=True, null=True)
    aadhaar_gender = models.CharField(max_length=191, blank=True, null=True)
    aadhaar_dob = models.DateField(blank=True, null=True)
    has_verified = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aadhaar_details'


class AadhaarEsigns(models.Model):
    aadhaar_esigns_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    source_type = models.CharField(max_length=191)
    source_id = models.IntegerField()
    mob_master_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aadhaar_esigns'


class AccountPermissions(models.Model):
    slug = models.CharField(unique=True, max_length=191)
    name = models.CharField(max_length=191)
    description = models.CharField(max_length=191)
    permissions = models.TextField(blank=True, null=True)
    account_permissions_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'account_permissions'


class Accounts(models.Model):
    accounts_id = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=191, blank=True, null=True)
    account_permissions_id = models.IntegerField()
    is_banned = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    api_version = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'


class Activations(models.Model):
    user_id = models.PositiveIntegerField()
    code = models.CharField(max_length=191)
    completed = models.IntegerField()
    completed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activations'


class ActivityFeeds(models.Model):
    activity_feeds_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    source_type = models.CharField(max_length=199)
    source_id = models.IntegerField()
    invoice_type = models.CharField(max_length=50, blank=True, null=True)
    party_name = models.CharField(max_length=199, blank=True, null=True)
    l2_categories_id = models.IntegerField(blank=True, null=True)
    l2_category = models.CharField(max_length=199, blank=True, null=True)
    l3_categories_id = models.IntegerField(blank=True, null=True)
    l3_category = models.CharField(max_length=199, blank=True, null=True)
    ref_no = models.CharField(max_length=199, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    status = models.CharField(max_length=199, blank=True, null=True)
    invoice_types_id = models.IntegerField(blank=True, null=True)
    invoice_statuses_id = models.IntegerField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    activity_date = models.DateTimeField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    contacts_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_feeds'


class AddressProofTypes(models.Model):
    address_proofs_id = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=191)
    name = models.CharField(max_length=191)
    type = models.CharField(max_length=191)
    doc_code = models.CharField(max_length=191, blank=True, null=True)
    doc_id = models.CharField(max_length=191, blank=True, null=True)
    cif_type = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address_proof_types'


class AddressTypes(models.Model):
    address_types_id = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=191)
    name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address_types'


class Addresses(models.Model):
    addresses_id = models.AutoField(primary_key=True)
    users_id = models.PositiveIntegerField()
    accounts_id = models.PositiveIntegerField()
    companies_id = models.IntegerField(blank=True, null=True)
    person_name = models.CharField(max_length=191, blank=True, null=True)
    source = models.CharField(max_length=191, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    address_types_id = models.IntegerField(blank=True, null=True)
    address_line = models.CharField(max_length=191, blank=True, null=True)
    address_line_1 = models.CharField(max_length=300, blank=True, null=True)
    address_line_2 = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=191, blank=True, null=True)
    state = models.CharField(max_length=191, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    address_type = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addresses'


class AddressesTest(models.Model):
    addresses_id = models.AutoField(primary_key=True)
    users_id = models.PositiveIntegerField()
    accounts_id = models.PositiveIntegerField()
    companies_id = models.IntegerField(blank=True, null=True)
    person_name = models.CharField(max_length=191, blank=True, null=True)
    source = models.CharField(max_length=191, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    address_types_id = models.IntegerField(blank=True, null=True)
    address_line = models.CharField(max_length=191, blank=True, null=True)
    city = models.CharField(max_length=191, blank=True, null=True)
    state = models.CharField(max_length=191, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addresses_test'


class AdjustmentStatuses(models.Model):
    adjustment_statuses_id = models.AutoField(primary_key=True)
    adjustment_status = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adjustment_statuses'


class AdminActivities(models.Model):
    admin_activities_id = models.AutoField(primary_key=True)
    modified_users_id = models.TextField(blank=True, null=True)
    users_id = models.TextField()
    activity = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_activities'


class AdminAdditionalDocuments(models.Model):
    admin_additional_documents_id = models.AutoField(primary_key=True)
    files_id = models.IntegerField()
    address_proofs_id = models.IntegerField()
    is_deleted = models.IntegerField()
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    source_type = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    admin_users_id = models.IntegerField()
    is_send_to_bank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'admin_additional_documents'


class AdminButtonList(models.Model):
    admin_button_list_id = models.AutoField(primary_key=True)
    admin_menu_id = models.IntegerField()
    button_name = models.TextField()
    button_id = models.TextField()
    is_disable = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_button_list'


class AdminComments(models.Model):
    admin_comments_id = models.AutoField(primary_key=True)
    mob_master_id = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    admin_users_id = models.IntegerField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    source_type = models.CharField(max_length=200)
    is_seen = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'admin_comments'


class AdminInternalMenu(models.Model):
    admin_internal_menu_id = models.AutoField(primary_key=True)
    admin_menu_id = models.IntegerField()
    display_name = models.CharField(max_length=199)
    url = models.CharField(max_length=199)
    is_disable = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_internal_menu'


class AdminM2PUploadKyc(models.Model):
    admin_m2p_upload_kyc_id = models.AutoField(primary_key=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    id_proof_files_id = models.CharField(max_length=200, blank=True, null=True)
    address_proof_files_id = models.CharField(max_length=200, blank=True, null=True)
    card_details_id = models.CharField(max_length=200, blank=True, null=True)
    admin_users_id = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_m2p_upload_kyc'


class AdminMakerChecker(models.Model):
    admin_maker_checker_id = models.BigAutoField(primary_key=True)
    maker_users_id = models.IntegerField()
    checker_users_id = models.IntegerField(blank=True, null=True)
    maker_initiated_date = models.DateTimeField()
    checker_action_date = models.DateTimeField(blank=True, null=True)
    admin_maker_checker_status_id = models.IntegerField()
    source_table = models.CharField(max_length=191)
    source_id = models.IntegerField()
    platform = models.CharField(max_length=191, blank=True, null=True)
    action_type = models.CharField(max_length=191)
    description = models.CharField(max_length=191)
    request = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_maker_checker'


class AdminMakerCheckerStatuses(models.Model):
    admin_maker_checker_statuses_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=191)
    is_active = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_maker_checker_statuses'


class AdminMenu(models.Model):
    admin_menu_id = models.AutoField(primary_key=True)
    admin_menu_category_id = models.IntegerField()
    display_name = models.CharField(max_length=191)
    url_id = models.CharField(max_length=191)
    icon = models.CharField(max_length=191)
    is_disable = models.IntegerField()
    menu_order = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_menu'


class AdminMenuCategory(models.Model):
    admin_menu_category_id = models.AutoField(primary_key=True)
    admin_menu_category_name = models.CharField(max_length=191)
    order = models.IntegerField()
    is_disable = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_menu_category'


class AdminPanVerification(models.Model):
    admin_pan_verification_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    companies_id = models.IntegerField()
    source_type = models.CharField(max_length=191)
    source_id = models.IntegerField()
    pan_no = models.CharField(max_length=10)
    name_on_pan = models.CharField(max_length=99)
    pan_status = models.CharField(max_length=191)
    pan_duplicate = models.CharField(max_length=191)
    pan_name = models.CharField(max_length=191)
    pan_dob = models.CharField(max_length=191)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_pan_verification'


class AdminPanVerificationKerzaLog(models.Model):
    admin_pan_verification_kerza_log_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    companies_id = models.IntegerField()
    request_id = models.TextField()
    response = models.TextField()
    request = models.CharField(max_length=191)
    merchant_ref_id = models.CharField(max_length=191, blank=True, null=True)
    is_enterprise = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_pan_verification_kerza_log'
        unique_together = (('companies_id', 'merchant_ref_id'),)


class AdminPermissions(models.Model):
    admin_permissions_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    created_by = models.IntegerField()
    permission_type = models.CharField(max_length=99)
    permission = models.TextField()
    button_permission = models.TextField()
    report_permission = models.TextField()
    feature_permission = models.CharField(max_length=400)
    is_disable = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_permissions'


class AdminReasons(models.Model):
    admin_reasons_id = models.AutoField(primary_key=True)
    source_id = models.CharField(max_length=191)
    source_table = models.CharField(max_length=191, blank=True, null=True)
    reason = models.TextField()
    admin_users_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_reasons'


class AdminReconciliationRefunds(models.Model):
    admin_reconciliation_refunds_id = models.BigAutoField(primary_key=True)
    payment_gateway_id = models.IntegerField()
    open_pg_txn_id = models.CharField(max_length=191, blank=True, null=True)
    pg_txn_ref_num = models.CharField(max_length=191, blank=True, null=True)
    transaction_id = models.CharField(max_length=191, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    gateway_tdr = models.FloatField(blank=True, null=True)
    gateway_gst = models.FloatField(blank=True, null=True)
    gateway_total_fee = models.FloatField(blank=True, null=True)
    gateway_net_amount = models.FloatField(blank=True, null=True)
    bank_or_card_name = models.CharField(max_length=191, blank=True, null=True)
    refund_status = models.CharField(max_length=191, blank=True, null=True)
    bank_ref_number = models.CharField(max_length=191, blank=True, null=True)
    card_number = models.CharField(max_length=191, blank=True, null=True)
    card_issuing_bank = models.CharField(max_length=191, blank=True, null=True)
    transaction_type = models.CharField(max_length=191, blank=True, null=True)
    payment_status = models.CharField(max_length=191, blank=True, null=True)
    transaction_date = models.DateTimeField()
    settlement_date = models.DateTimeField()
    customer_email = models.CharField(max_length=191, blank=True, null=True)
    customer_mobile = models.CharField(max_length=191, blank=True, null=True)
    merchant_company_details = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_reconciliation_refunds'


class AdminReconciliations(models.Model):
    admin_reconciliation_id = models.AutoField(primary_key=True)
    file_id = models.CharField(max_length=191, blank=True, null=True)
    source_type = models.CharField(max_length=191, blank=True, null=True)
    admin_users_id = models.IntegerField(blank=True, null=True)
    total_rows = models.IntegerField(blank=True, null=True)
    uploaded_rows = models.IntegerField(blank=True, null=True)
    wrong_format_rows = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_reconciliations'


class AdminReportList(models.Model):
    admin_report_list_id = models.AutoField(primary_key=True)
    report_name = models.TextField()
    report_unique_id = models.TextField()
    is_disable = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_report_list'


class AdminSaltFranchiseeTransactions(models.Model):
    admin_salt_franchisee_transactions_id = models.AutoField(primary_key=True)
    task_id = models.IntegerField()
    order_id = models.CharField(max_length=191)
    relationship = models.CharField(max_length=191)
    team_name = models.CharField(max_length=191)
    task_type = models.CharField(max_length=191)
    notes = models.TextField()
    agent_id = models.IntegerField()
    agent_name = models.CharField(max_length=191)
    distance = models.DecimalField(max_digits=8, decimal_places=2)
    total_time_taken_min = models.DecimalField(max_digits=8, decimal_places=2)
    pickup_from = models.TextField()
    customer_name = models.CharField(max_length=191)
    customer_address = models.TextField()
    customer_phone = models.CharField(max_length=191)
    customer_email = models.CharField(max_length=191)
    start_before = models.DateTimeField()
    complete_before = models.DateTimeField()
    completion_time = models.DateTimeField()
    task_status = models.CharField(max_length=191)
    ref_image = models.CharField(max_length=191)
    rating = models.CharField(max_length=191)
    review = models.CharField(max_length=191)
    latitude = models.CharField(max_length=191)
    longitude = models.CharField(max_length=191)
    tags = models.CharField(max_length=191)
    promo_applied = models.CharField(max_length=191)
    customer_template_id = models.CharField(max_length=191)
    task_details_items = models.CharField(max_length=191)
    task_details_quantity = models.CharField(max_length=191)
    task_details_amount = models.DecimalField(max_digits=8, decimal_places=2)
    sub_total = models.DecimalField(max_digits=8, decimal_places=2)
    item_details_item_name = models.CharField(max_length=191)
    item_details_options = models.CharField(max_length=191)
    item_details_quantity = models.IntegerField()
    item_details_price = models.DecimalField(max_digits=8, decimal_places=2)
    delivery_cost = models.DecimalField(max_digits=8, decimal_places=2)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(max_length=191)
    customer_notes = models.TextField()
    discount_code = models.CharField(max_length=191)
    pricing = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_salt_franchisee_transactions'


class AdminSaltMerchantTransactions(models.Model):
    admin_salt_merchant_transactions_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    order_status = models.CharField(max_length=191)
    order_total = models.DecimalField(max_digits=8, decimal_places=2)
    sub_total = models.DecimalField(max_digits=8, decimal_places=2)
    surge_amount = models.DecimalField(max_digits=8, decimal_places=2)
    tax = models.DecimalField(max_digits=8, decimal_places=2)
    delivery_charge = models.DecimalField(max_digits=8, decimal_places=2)
    tip = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=8, decimal_places=2)
    promo_discount = models.DecimalField(max_digits=8, decimal_places=2)
    remaining_balance = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(max_length=191)
    delivery_mode = models.CharField(max_length=191)
    transaction_id = models.CharField(max_length=191)
    transaction_status = models.CharField(max_length=191)
    promo_code = models.CharField(max_length=191)
    currency_symbol = models.CharField(max_length=191)
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=191)
    customer_email = models.CharField(max_length=191)
    customer_phone_no = models.CharField(max_length=191)
    merchant_id = models.IntegerField()
    store_name = models.CharField(max_length=191)
    delivery_address = models.TextField()
    pickup_address = models.TextField()
    description = models.TextField()
    distance = models.DecimalField(max_digits=8, decimal_places=2)
    order_time = models.DateTimeField()
    pickup_time = models.DateTimeField()
    delivery_time = models.DateTimeField()
    ratings = models.IntegerField()
    reviews = models.TextField()
    merchant_earning = models.DecimalField(max_digits=8, decimal_places=2)
    commission_amount = models.DecimalField(max_digits=8, decimal_places=2)
    commission_payout_status = models.CharField(max_length=191)
    order_preparation_time = models.DecimalField(max_digits=8, decimal_places=2)
    merchant_tag = models.CharField(max_length=191)
    commission_tag = models.CharField(max_length=191)
    city = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_salt_merchant_transactions'


class AdminSaltOrderConsolidated(models.Model):
    admin_salt_order_consolidated_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    order_total = models.DecimalField(max_digits=8, decimal_places=2)
    sub_total = models.DecimalField(max_digits=8, decimal_places=2)
    surge_amount = models.DecimalField(max_digits=8, decimal_places=2)
    tax = models.DecimalField(max_digits=8, decimal_places=2)
    delivery_charge = models.DecimalField(max_digits=8, decimal_places=2)
    tip = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=8, decimal_places=2)
    promo_discount = models.DecimalField(max_digits=8, decimal_places=2)
    remaining_balance = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(max_length=191)
    order_status = models.CharField(max_length=191)
    delivery_mode = models.CharField(max_length=191)
    transaction_id = models.CharField(max_length=191)
    transaction_status = models.CharField(max_length=191)
    customer_id = models.IntegerField()
    merchant_id = models.IntegerField()
    merchant_earning_amount = models.DecimalField(max_digits=8, decimal_places=2)
    commission_amount = models.DecimalField(max_digits=8, decimal_places=2)
    commission_payout_status = models.CharField(max_length=191)
    task_id = models.IntegerField()
    team_name = models.CharField(max_length=191)
    agent_id = models.IntegerField()
    salt_franchisee_details_id = models.IntegerField()
    is_available_in_salt_settlement = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_salt_order_consolidated'


class AdminVerificationDetails(models.Model):
    admin_verification_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    mob_master_id = models.IntegerField()
    companies_id = models.IntegerField()
    is_approved = models.CharField(max_length=191)
    time_of_action = models.DateTimeField(blank=True, null=True)
    kyc_verified = models.IntegerField()
    risk_verified = models.IntegerField()
    kyc_verified_date = models.DateTimeField(blank=True, null=True)
    risk_verified_date = models.DateTimeField(blank=True, null=True)
    onboarding_status_id = models.IntegerField()
    assigned_industry_types_id = models.TextField(blank=True, null=True)
    other_action_by = models.CharField(max_length=200)
    other_action_by_date = models.DateTimeField(blank=True, null=True)
    kyc_on_hold_reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_ekyc_document_verified = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_verification_details'


class Ads(models.Model):
    ads_id = models.AutoField(primary_key=True)
    ad_type = models.CharField(max_length=20, blank=True, null=True)
    ad_position = models.CharField(max_length=20, blank=True, null=True)
    img_url = models.TextField(blank=True, null=True)
    is_img_clickable = models.IntegerField(blank=True, null=True)
    action_label = models.CharField(max_length=40, blank=True, null=True)
    action_url = models.TextField(blank=True, null=True)
    action_url_type = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    user_config = models.TextField(blank=True, null=True)
    ad_clicks = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ads'


class AgingAnalytics(models.Model):
    aging_analytics_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    contacts_id = models.IntegerField(blank=True, null=True)
    customer_name = models.CharField(max_length=200)
    dso_zero_to_thirty_days = models.DecimalField(max_digits=16, decimal_places=2)
    dso_thirty_to_sixty_days = models.DecimalField(max_digits=16, decimal_places=2)
    dso_sixty_to_ninty_days = models.DecimalField(max_digits=16, decimal_places=2)
    dso_ninty_and_more_days = models.DecimalField(max_digits=16, decimal_places=2)
    total_outstanding = models.DecimalField(max_digits=16, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aging_analytics'


class AgingAnalyticsPayables(models.Model):
    aging_analytics_payables_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    contacts_id = models.IntegerField(blank=True, null=True)
    customer_name = models.CharField(max_length=200)
    dpo_zero_to_thirty_days = models.DecimalField(max_digits=16, decimal_places=2)
    dpo_thirty_to_sixty_days = models.DecimalField(max_digits=16, decimal_places=2)
    dpo_sixty_to_ninty_days = models.DecimalField(max_digits=16, decimal_places=2)
    dpo_ninty_and_more_days = models.DecimalField(max_digits=16, decimal_places=2)
    total_outstanding = models.DecimalField(max_digits=16, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aging_analytics_payables'


class ApiCredentials(models.Model):
    api_credentials_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    access_key = models.CharField(max_length=191)
    secret_key = models.TextField()
    is_api_enabled = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_credentials'


class ApiHttpLogs(models.Model):
    api_http_logs_id = models.AutoField(primary_key=True)
    uri = models.CharField(max_length=300, blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    request_header = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    status_code = models.CharField(max_length=191, blank=True, null=True)
    client_ip = models.CharField(max_length=191, blank=True, null=True)
    took_ms = models.CharField(max_length=191, blank=True, null=True)
    request_id = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_http_logs'


class ApiWhitelistIps(models.Model):
    api_credentials_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    ip_address = models.CharField(max_length=191)
    is_blacklisted = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_whitelist_ips'


class ApiriaCompanyDeductions(models.Model):
    apiria_company_deductions_id = models.AutoField(primary_key=True)
    apiria_company_payrolls_id = models.CharField(max_length=200)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tds = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pf_employee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pf_employer = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    esi = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    lwf = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apiria_company_deductions'


class ApiriaCompanyPayrolls(models.Model):
    apiria_company_payrolls_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    month = models.CharField(max_length=30, blank=True, null=True)
    year = models.CharField(max_length=10, blank=True, null=True)
    total_payout = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    salary_payout = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apiria_company_payrolls'


class ApiriaEmployeeCompensations(models.Model):
    apiria_employee_compensations_id = models.AutoField(primary_key=True)
    apiria_employees_id = models.CharField(max_length=200)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    contacts_id = models.IntegerField()
    apiria_employee_identifier = models.CharField(max_length=200, blank=True, null=True)
    ctc_monthly_basic = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ctc_monthly_hra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ctc_monthly_others = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ctc_yearly_basic = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ctc_yearly_hra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ctc_yearly_others = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apiria_employee_compensations'


class ApiriaEmployeeDeductions(models.Model):
    apiria_employee_deductions_id = models.AutoField(primary_key=True)
    apiria_employees_id = models.CharField(max_length=200, blank=True, null=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    contacts_id = models.IntegerField(blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tds = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pf_employee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pf_employer = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    esi = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    lwf = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apiria_employee_deductions'


class ApiriaEmployeePayrolls(models.Model):
    apiria_employee_payrolls_id = models.AutoField(primary_key=True)
    apiria_employees_id = models.CharField(max_length=200, blank=True, null=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField(blank=True, null=True)
    contacts_id = models.IntegerField(blank=True, null=True)
    total_payout = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    salary_payout = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apiria_employee_payrolls'


class ApiriaEmployees(models.Model):
    apiria_employees_id = models.AutoField(primary_key=True)
    apiria_employee_identifier = models.CharField(max_length=200)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    contacts_id = models.IntegerField()
    employee_first_name = models.CharField(max_length=200, blank=True, null=True)
    employee_last_name = models.CharField(max_length=200, blank=True, null=True)
    employee_account_num = models.CharField(max_length=200, blank=True, null=True)
    employee_bank_name = models.CharField(max_length=200, blank=True, null=True)
    employee_bank_ifsc = models.CharField(max_length=40, blank=True, null=True)
    employee_email = models.CharField(max_length=200, blank=True, null=True)
    employee_mobile_num = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apiria_employees'


class ApiriaOrgs(models.Model):
    apiria_orgs_id = models.AutoField(primary_key=True)
    users_id = models.PositiveIntegerField()
    accounts_id = models.PositiveIntegerField()
    companies_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    apiria_response = models.CharField(max_length=255)
    response_status = models.CharField(max_length=100)
    is_enabled = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'apiria_orgs'


class AppSubscriptionPackages(models.Model):
    app_subscription_packages_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=191, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    subscription_modules_ids = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    package_duration = models.CharField(max_length=191, blank=True, null=True)
    app_types_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_subscription_packages'


class AppSubscriptions(models.Model):
    app_subscriptions_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    amount_paid = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    subscription_payment_statuses_id = models.IntegerField(blank=True, null=True)
    payment_token_id = models.CharField(max_length=191, blank=True, null=True)
    payment_id = models.CharField(max_length=191, blank=True, null=True)
    payment_reference_id = models.CharField(max_length=191, blank=True, null=True)
    payment_method = models.CharField(max_length=255, blank=True, null=True)
    app_subscription_packages_id = models.IntegerField(blank=True, null=True)
    app_types_id = models.IntegerField(blank=True, null=True)
    is_subscribed = models.IntegerField()
    is_expired = models.IntegerField()
    subscription_start_date = models.DateTimeField(blank=True, null=True)
    subscription_end_date = models.DateTimeField(blank=True, null=True)
    is_picked = models.IntegerField()
    invoices_id = models.IntegerField(blank=True, null=True)
    invoices_files_id = models.IntegerField(blank=True, null=True)
    invoice_sent_on = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    source_of_registration = models.CharField(max_length=191, blank=True, null=True)
    source_type = models.CharField(max_length=191, blank=True, null=True)
    source_id = models.CharField(max_length=191, blank=True, null=True)
    invoice_sent_statuses_id = models.IntegerField()
    rmid = models.CharField(max_length=191, blank=True, null=True)
    smid = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_subscriptions'


class AppTypes(models.Model):
    app_types_id = models.AutoField(primary_key=True)
    app_type = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_types'


class ArzooDisbursement(models.Model):
    arzoo_disb_id = models.AutoField(primary_key=True)
    lending_id = models.IntegerField()
    nbfc_app_id = models.IntegerField()
    acknowledged = models.IntegerField()
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    mobile = models.CharField(max_length=30, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    arzoo_transaction_id = models.CharField(max_length=200, db_collation='utf8mb4_unicode_ci')
    is_failed = models.IntegerField()
    open_transaction_id = models.CharField(max_length=100, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    open_charge_rate_type = models.CharField(max_length=20, db_collation='utf8mb4_unicode_ci')
    open_charge_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    open_charge = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    repay_interest_rate_type = models.CharField(max_length=20, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    repay_interest_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    repay_interest_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arzoo_disbursement'


class ArzooDisbursementLogs(models.Model):
    arzoo_disbursement_logs_id = models.AutoField(primary_key=True)
    arzoo_disb_id = models.IntegerField()
    lending_id = models.IntegerField()
    nbfc_app_id = models.IntegerField()
    acknowledged = models.IntegerField()
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    mobile = models.CharField(max_length=30, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    arzoo_transaction_id = models.CharField(max_length=200, db_collation='utf8mb4_unicode_ci')
    is_failed = models.IntegerField()
    open_transaction_id = models.CharField(max_length=100, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    open_charge_rate_type = models.CharField(max_length=20, db_collation='utf8mb4_unicode_ci')
    open_charge_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    open_charge = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    repay_interest_rate_type = models.CharField(max_length=20, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    repay_interest_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    repay_interest_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arzoo_disbursement_logs'


class AtomSettlementLogs(models.Model):
    atom_settlement_logs_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    merchant_id = models.CharField(max_length=191, blank=True, null=True)
    merchant_txn_id = models.CharField(max_length=191, blank=True, null=True)
    api_name = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    txn_date = models.CharField(max_length=191, blank=True, null=True)
    atom_txn_id = models.CharField(max_length=191, blank=True, null=True)
    settlement_date = models.CharField(max_length=191, blank=True, null=True)
    request_url = models.CharField(max_length=191, blank=True, null=True)
    request_header = models.CharField(max_length=191, blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    response_code = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atom_settlement_logs'


class AtomSettlements(models.Model):
    atom_settlements_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    pg_transactions_id = models.IntegerField(unique=True, blank=True, null=True)
    merchant_terminal_id = models.CharField(max_length=191, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    merchant_transaction_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    convenience_fee = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    atom_tdr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    atom_gst = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    atom_total_fee = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    atom_net_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    open_tdr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    same_day_settlement_charge = models.DecimalField(max_digits=12, decimal_places=2)
    open_gst = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    open_total_fee = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    open_net_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    pg_txn_ref_num = models.CharField(unique=True, max_length=191, blank=True, null=True)
    open_pg_txn_id = models.CharField(unique=True, max_length=191, blank=True, null=True)
    customer_name = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=100)
    customer_mobile = models.CharField(max_length=30)
    merchant_company_details = models.CharField(max_length=255)
    available_on = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    source_type = models.CharField(max_length=191, blank=True, null=True)
    source_id = models.CharField(max_length=191, blank=True, null=True)
    settlement_source = models.CharField(max_length=191)
    settlement_txn_id = models.CharField(max_length=191, blank=True, null=True)
    settlement_status_id = models.IntegerField(blank=True, null=True)
    settled_by = models.IntegerField(blank=True, null=True)
    settled_to_open_date = models.DateTimeField(blank=True, null=True)
    settled_to_merchant_date = models.DateTimeField(blank=True, null=True)
    settlement_modes_id = models.IntegerField(blank=True, null=True)
    is_held = models.IntegerField(blank=True, null=True)
    hold_by = models.IntegerField(blank=True, null=True)
    hold_reason = models.CharField(max_length=191, blank=True, null=True)
    merchant_name = models.CharField(max_length=191, blank=True, null=True)
    merchant_id = models.CharField(max_length=191, blank=True, null=True)
    atom_txn_id = models.CharField(max_length=191, blank=True, null=True)
    txn_state = models.CharField(max_length=191, blank=True, null=True)
    transaction_date = models.CharField(max_length=191, blank=True, null=True)
    client_code = models.CharField(max_length=191, blank=True, null=True)
    merchant_txn_id = models.CharField(max_length=191, blank=True, null=True)
    product = models.CharField(max_length=191, blank=True, null=True)
    discriminator = models.CharField(max_length=191, blank=True, null=True)
    bank_or_card_name = models.CharField(max_length=191, blank=True, null=True)
    card_type = models.CharField(max_length=191, blank=True, null=True)
    card_num = models.CharField(max_length=191, blank=True, null=True)
    card_issuing_bank = models.CharField(max_length=191, blank=True, null=True)
    bank_ref_num = models.CharField(max_length=191, blank=True, null=True)
    refund_ref_num = models.CharField(max_length=191, blank=True, null=True)
    gross_txn_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    txn_charges = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    service_tax = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    sb_cess = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    krishi_kalyan_cess = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    total_chargeable = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    net_amount_to_be_paid = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    payment_status = models.CharField(max_length=191, blank=True, null=True)
    settlement_date = models.DateTimeField(blank=True, null=True)
    refund_status = models.CharField(max_length=191, blank=True, null=True)
    surcharge = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    recon_status = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_processed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atom_settlements'


class AuditLogs(models.Model):
    log_name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    subject_id = models.IntegerField(blank=True, null=True)
    subject_type = models.CharField(max_length=150, blank=True, null=True)
    causer_id = models.IntegerField(blank=True, null=True)
    causer_type = models.CharField(max_length=150, blank=True, null=True)
    properties = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=10, blank=True, null=True)
    original_latitude = models.CharField(max_length=10, blank=True, null=True)
    longitude = models.CharField(max_length=10, blank=True, null=True)
    original_longitude = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit_logs'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AxisBankAccountLeads(models.Model):
    axis_bank_account_leads_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    app_ref_id = models.CharField(max_length=191, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    axis_bank_validation_token = models.CharField(max_length=400, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    device_id = models.CharField(max_length=15, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    is_aadhaar_verified = models.CharField(max_length=1, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    ekyc_url = models.CharField(max_length=600, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    ekyc_start_time = models.DateTimeField(blank=True, null=True)
    vcip_url = models.CharField(max_length=400, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    resume_vcip_url = models.CharField(max_length=400, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    payment_url = models.CharField(max_length=400, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    customer_consents = models.JSONField(blank=True, null=True)
    terms_and_conditions = models.CharField(max_length=1, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    payment_url_generated_at = models.DateTimeField(blank=True, null=True)
    application_status_id = models.IntegerField(blank=True, null=True)
    vkyc_failure_reason = models.CharField(max_length=191, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    vkyc_url_hit_first_time = models.IntegerField()
    vkyc_url_first_hit_at = models.DateTimeField(blank=True, null=True)
    payment_url_hit_first_time = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'axis_bank_account_leads'


class AxisBankAccounts(models.Model):
    axis_bank_accounts_id = models.BigAutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    customer_id = models.CharField(max_length=191, blank=True, null=True)
    account_number = models.CharField(max_length=191, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'axis_bank_accounts'


class AxisBankAccountsBackup(models.Model):
    axis_bank_accounts_id = models.BigAutoField(primary_key=True)
    companies_id = models.IntegerField(blank=True, null=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    app_ref_id = models.CharField(max_length=191, blank=True, null=True)
    pan = models.CharField(max_length=15, blank=True, null=True)
    customer_id = models.CharField(max_length=191, blank=True, null=True)
    account_number = models.CharField(max_length=191, blank=True, null=True)
    application_status = models.CharField(max_length=2, blank=True, null=True)
    validation_token = models.CharField(max_length=200, blank=True, null=True)
    ekyc_url = models.CharField(max_length=400, blank=True, null=True)
    device_id = models.CharField(max_length=191, blank=True, null=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    aadhaar_verified = models.CharField(max_length=1, blank=True, null=True)
    vcip_url = models.CharField(max_length=191, blank=True, null=True)
    resume_vcip_url = models.CharField(max_length=191, blank=True, null=True)
    vkyc_status = models.CharField(max_length=1, blank=True, null=True)
    vkyc_failure_reason = models.CharField(max_length=100, blank=True, null=True)
    payment_redirect_url = models.CharField(max_length=400, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'axis_bank_accounts_backup'


class AxisBankCityStateMaster(models.Model):
    axis_bank_city_state_master_id = models.BigAutoField(primary_key=True)
    state = models.CharField(max_length=191, blank=True, null=True)
    state_abbr = models.CharField(max_length=191, blank=True, null=True)
    city = models.CharField(max_length=191, blank=True, null=True)
    city_abbr = models.CharField(max_length=191, blank=True, null=True)
    pin = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'axis_bank_city_state_master'


class AxisBankCustomerDetails(models.Model):
    axis_bank_customer_details_id = models.BigAutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    app_ref_id = models.CharField(max_length=191, blank=True, null=True)
    mobile_number = models.CharField(max_length=10, blank=True, null=True)
    device_id = models.CharField(max_length=20, blank=True, null=True)
    pan_number = models.CharField(max_length=10, blank=True, null=True)
    aadhar_subsidy = models.CharField(max_length=191, blank=True, null=True)
    branch = models.CharField(max_length=191, blank=True, null=True)
    branch_id = models.CharField(max_length=191, blank=True, null=True)
    branch_pincode = models.CharField(max_length=10, blank=True, null=True)
    branch_name = models.CharField(max_length=200, blank=True, null=True)
    ifsc_code = models.CharField(max_length=50, blank=True, null=True)
    customer_type = models.CharField(max_length=5)
    tax_details = models.CharField(max_length=191, blank=True, null=True)
    tax_resident = models.CharField(max_length=1, blank=True, null=True)
    product_name = models.CharField(max_length=5)
    email_statement = models.CharField(max_length=1)
    email_id = models.CharField(max_length=191, blank=True, null=True)
    self_declaration = models.CharField(max_length=1, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    customer_name_title = models.CharField(max_length=10, blank=True, null=True)
    customer_name_firstname = models.CharField(max_length=50, blank=True, null=True)
    customer_name_middlename = models.CharField(max_length=50, blank=True, null=True)
    customer_name_lastname = models.CharField(max_length=50, blank=True, null=True)
    address_line_1 = models.CharField(max_length=191, blank=True, null=True)
    address_line_2 = models.CharField(max_length=191, blank=True, null=True)
    address_line_3 = models.CharField(max_length=191, blank=True, null=True)
    landmark = models.CharField(max_length=191, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    city = models.CharField(max_length=191, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    country = models.CharField(max_length=191)
    resident_type = models.CharField(max_length=191, blank=True, null=True)
    comm_address_same_as_perm_address = models.CharField(max_length=1, blank=True, null=True)
    comm_address_line_1 = models.CharField(max_length=191, blank=True, null=True)
    comm_address_line_2 = models.CharField(max_length=191, blank=True, null=True)
    comm_address_line_3 = models.CharField(max_length=191, blank=True, null=True)
    comm_landmark = models.CharField(max_length=191, blank=True, null=True)
    comm_pincode = models.CharField(max_length=6, blank=True, null=True)
    comm_city = models.CharField(max_length=191, blank=True, null=True)
    comm_state = models.CharField(max_length=2, blank=True, null=True)
    comm_country = models.CharField(max_length=191)
    comm_resident_type = models.CharField(max_length=191, blank=True, null=True)
    mother_name_title = models.CharField(max_length=10, blank=True, null=True)
    mother_first_name = models.CharField(max_length=191, blank=True, null=True)
    mother_middle_name = models.CharField(max_length=191, blank=True, null=True)
    mother_last_name = models.CharField(max_length=191, blank=True, null=True)
    father_name_title = models.CharField(max_length=10, blank=True, null=True)
    father_first_name = models.CharField(max_length=191, blank=True, null=True)
    father_middle_name = models.CharField(max_length=191, blank=True, null=True)
    father_last_name = models.CharField(max_length=191, blank=True, null=True)
    mother_maiden_title = models.CharField(max_length=10, blank=True, null=True)
    mother_maiden_first_name = models.CharField(max_length=191, blank=True, null=True)
    mother_maiden_middle_name = models.CharField(max_length=191, blank=True, null=True)
    mother_maiden_last_name = models.CharField(max_length=191, blank=True, null=True)
    country_of_birth = models.CharField(max_length=191, blank=True, null=True)
    city_of_birth_abbr = models.CharField(max_length=10, blank=True, null=True)
    city_of_birth = models.CharField(max_length=191, blank=True, null=True)
    nationality = models.CharField(max_length=191)
    gender = models.CharField(max_length=1, blank=True, null=True)
    occupation_code = models.CharField(max_length=5, blank=True, null=True)
    educational_qualification = models.CharField(max_length=1, blank=True, null=True)
    income_range = models.CharField(max_length=15, blank=True, null=True)
    marital_status = models.CharField(max_length=6, blank=True, null=True)
    name_on_debit_card = models.CharField(max_length=191, blank=True, null=True)
    nominee_name = models.CharField(max_length=191, blank=True, null=True)
    nominee_relation_with_customer = models.CharField(max_length=191, blank=True, null=True)
    guardian_details_flag = models.CharField(max_length=1, blank=True, null=True)
    nominee_date_of_birth = models.CharField(max_length=191, blank=True, null=True)
    guardian_address_same_as_perm_address = models.CharField(max_length=1, blank=True, null=True)
    guardian_address_line_1 = models.CharField(max_length=191, blank=True, null=True)
    guardian_address_line_2 = models.CharField(max_length=191, blank=True, null=True)
    guardian_address_line_3 = models.CharField(max_length=191, blank=True, null=True)
    guardian_landmark = models.CharField(max_length=191, blank=True, null=True)
    guardian_pincode = models.CharField(max_length=6, blank=True, null=True)
    guardian_city = models.CharField(max_length=191, blank=True, null=True)
    guardian_state = models.CharField(max_length=2, blank=True, null=True)
    guardian_country = models.CharField(max_length=191, blank=True, null=True)
    guardian_name = models.CharField(max_length=191, blank=True, null=True)
    guardian_relation_with_nominee = models.CharField(max_length=191, blank=True, null=True)
    nominee_address_same_as_perm_address = models.CharField(max_length=1, blank=True, null=True)
    nominee_address_line_1 = models.CharField(max_length=191, blank=True, null=True)
    nominee_address_line_2 = models.CharField(max_length=191, blank=True, null=True)
    nominee_address_line_3 = models.CharField(max_length=191, blank=True, null=True)
    nominee_landmark = models.CharField(max_length=191, blank=True, null=True)
    nominee_pincode = models.CharField(max_length=6, blank=True, null=True)
    nominee_city = models.CharField(max_length=191, blank=True, null=True)
    nominee_state = models.CharField(max_length=2, blank=True, null=True)
    nominee_country = models.CharField(max_length=191, blank=True, null=True)
    customer_consents = models.JSONField(blank=True, null=True)
    cc_od_check = models.JSONField(blank=True, null=True)
    account_opening_purpose = models.CharField(max_length=191, blank=True, null=True)
    nature_of_business = models.CharField(max_length=191, blank=True, null=True)
    source_of_funds = models.CharField(max_length=191, blank=True, null=True)
    number_of_years_in_business = models.CharField(max_length=3, blank=True, null=True)
    credit_facility_declaration = models.CharField(max_length=5, blank=True, null=True)
    dealing_in_cryptocurrency = models.CharField(max_length=5, blank=True, null=True)
    tax_resident_of_india = models.CharField(max_length=5, blank=True, null=True)
    credit_facility_details = models.JSONField(blank=True, null=True)
    is_final_submit = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'axis_bank_customer_details'


class AxisBankFundTransfers(models.Model):
    axis_bank_fund_transfers_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    request_id = models.CharField(max_length=191, blank=True, null=True)
    erp_uid = models.CharField(max_length=191, blank=True, null=True)
    transaction_type = models.CharField(max_length=191, blank=True, null=True)
    bnfid = models.IntegerField(blank=True, null=True)
    transaction_id = models.CharField(max_length=191, blank=True, null=True)
    transaction_date = models.CharField(max_length=191, blank=True, null=True)
    transaction_req_id = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bank_ref_number = models.IntegerField(blank=True, null=True)
    error_code = models.CharField(max_length=191, blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'axis_bank_fund_transfers'


class AxisBankOnboardingLogs(models.Model):
    axis_bank_onboarding_logs_id = models.BigAutoField(primary_key=True)
    api_called = models.CharField(max_length=191, blank=True, null=True)
    user_input = models.JSONField(blank=True, null=True)
    request_sent = models.JSONField(blank=True, null=True)
    headers_sent = models.JSONField(blank=True, null=True)
    response_received = models.JSONField(blank=True, null=True)
    decrypted_response = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'axis_bank_onboarding_logs'


class AxisBeneficiaryRegistrations(models.Model):
    axis_beneficiary_registrations_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    contacts_id = models.IntegerField(blank=True, null=True)
    request_id = models.CharField(max_length=191, blank=True, null=True)
    erp_uid = models.CharField(max_length=191, blank=True, null=True)
    payee_id = models.IntegerField(blank=True, null=True)
    bene_name = models.CharField(max_length=191, blank=True, null=True)
    bene_account_no = models.CharField(max_length=191, blank=True, null=True)
    ifsc_code = models.CharField(max_length=191, blank=True, null=True)
    bene_nick_name = models.CharField(max_length=191, blank=True, null=True)
    bank_name = models.CharField(max_length=191, blank=True, null=True)
    bene_req_id = models.CharField(max_length=191, blank=True, null=True)
    no_of_req = models.IntegerField(blank=True, null=True)
    bnfid = models.IntegerField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'axis_beneficiary_registrations'


class AxisConnectedAccounts(models.Model):
    axis_connected_accounts_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    request_id = models.CharField(max_length=191, blank=True, null=True)
    erp_uid = models.CharField(max_length=191, blank=True, null=True)
    account_number = models.CharField(max_length=191, blank=True, null=True)
    cid = models.CharField(max_length=191, blank=True, null=True)
    uid = models.CharField(max_length=191, blank=True, null=True)
    bank_connection_statuses_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'axis_connected_accounts'


class BankAccounts(models.Model):
    bank_accounts_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    bank_id = models.CharField(max_length=191, blank=True, null=True)
    bank_account_number = models.CharField(max_length=191, blank=True, null=True)
    bank_ifsc_code = models.CharField(max_length=191, blank=True, null=True)
    bank_branch = models.CharField(max_length=191, blank=True, null=True)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_accounts'


class BankConnectionStatuses(models.Model):
    bank_connection_statuses_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=200)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_connection_statuses'


class BankIfsc(models.Model):
    bank_ifsc_id = models.AutoField(primary_key=True)
    bank = models.CharField(max_length=191, blank=True, null=True)
    ifsc = models.CharField(unique=True, max_length=100, blank=True, null=True)
    micr = models.CharField(max_length=191, blank=True, null=True)
    branch = models.CharField(max_length=191, blank=True, null=True)
    address = models.CharField(max_length=191, blank=True, null=True)
    contact = models.CharField(max_length=191, blank=True, null=True)
    city = models.CharField(max_length=191, blank=True, null=True)
    district = models.CharField(max_length=191, blank=True, null=True)
    state = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_ifsc'


class BankMaintainenceConfigurations(models.Model):
    bank_maintainence_configurations_id = models.AutoField(primary_key=True)
    partner_banks_id = models.IntegerField()
    bank_name = models.CharField(max_length=200)
    maintainence_flag = models.IntegerField()
    message = models.CharField(max_length=350)

    class Meta:
        managed = False
        db_table = 'bank_maintainence_configurations'


class BankMopSettings(models.Model):
    bank_mop_settings_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    mob_stakeholder_details_id = models.IntegerField()
    team_member_details_id = models.IntegerField()
    is_maker = models.IntegerField()
    is_checker = models.IntegerField()
    partner_banks_id = models.IntegerField()
    per_transaction_limit = models.DecimalField(max_digits=14, decimal_places=2)
    per_day_limit = models.DecimalField(max_digits=14, decimal_places=2)
    per_month_limit = models.DecimalField(max_digits=14, decimal_places=2)
    approval_checker_amount = models.DecimalField(max_digits=14, decimal_places=2)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_mop_settings'


class BankTransactionStatuses(models.Model):
    bank_transaction_statuses_id = models.AutoField(primary_key=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    partner_banks_id = models.IntegerField()
    status_code = models.CharField(max_length=350)
    status_message = models.CharField(max_length=191)
    interpreted_message = models.CharField(max_length=350, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_transaction_statuses'


class BankTransactions(models.Model):
    bank_transactions_id = models.AutoField(primary_key=True)
    bank_accounts_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    transaction_ref_no = models.CharField(unique=True, max_length=191, blank=True, null=True)
    transaction_mode = models.CharField(max_length=191, blank=True, null=True)
    transaction_type = models.CharField(max_length=191, blank=True, null=True)
    transaction_status = models.CharField(max_length=191, blank=True, null=True)
    transaction_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    contacts_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_transactions'


class BankingMopCompanySettings(models.Model):
    banking_mop_company_settings_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    open_bank_accounts_id = models.IntegerField(blank=True, null=True)
    transaction_types_id = models.IntegerField()
    per_transaction_limit = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    per_month_limit = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    per_day_limit = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banking_mop_company_settings'


class BankingMopSettings(models.Model):
    banking_mop_settings_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    mob_stakeholder_details_id = models.IntegerField()
    team_member_details_id = models.IntegerField()
    maker_checker_groups_id = models.IntegerField()
    partner_banks_id = models.IntegerField()
    per_transaction_limit = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    per_month_limit = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    per_day_limit = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    approval_checker_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    is_maker = models.IntegerField()
    is_checker = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banking_mop_settings'


class BankingMopUserSettings(models.Model):
    banking_mop_settings_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    mob_stakeholder_details_id = models.IntegerField()
    team_member_details_id = models.IntegerField()
    maker_checker_groups_id = models.IntegerField()
    partner_banks_id = models.IntegerField()
    per_transaction_limit = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    per_month_limit = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    per_day_limit = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    approval_checker_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    is_maker = models.IntegerField()
    is_checker = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_verified = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'banking_mop_user_settings'


class BankingNodalStatementKotak(models.Model):
    banking_nodal_statement_kotak_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    fund_transfer_types_id = models.IntegerField()
    statement_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    ref_no = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    fund_flow_type = models.CharField(max_length=2)
    balance = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    destination_account_number = models.CharField(max_length=191, blank=True, null=True)
    source_account_number = models.CharField(max_length=191, blank=True, null=True)
    synced_at = models.DateTimeField(blank=True, null=True)
    sync_type = models.CharField(max_length=10)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banking_nodal_statement_kotak'


class BankingNodalStatementOpen(models.Model):
    banking_nodal_statement_open_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    fund_transfer_types_id = models.IntegerField()
    statement_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    ref_no = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    fund_flow_type = models.CharField(max_length=2)
    balance = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    destination_account_number = models.CharField(max_length=191, blank=True, null=True)
    source_account_number = models.CharField(max_length=191, blank=True, null=True)
    synced_at = models.DateTimeField(blank=True, null=True)
    sync_type = models.CharField(max_length=10)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banking_nodal_statement_open'


class BankingServices(models.Model):
    banking_services_id = models.AutoField(primary_key=True)
    banking_service_name = models.CharField(max_length=200)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banking_services'


class BeneAccountVerificationSources(models.Model):
    bene_account_verification_sources_id = models.AutoField(primary_key=True)
    verification_method_name = models.CharField(max_length=191)
    partner_banks_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bene_account_verification_sources'


class BillPaymentRequests(models.Model):
    bill_payment_requests_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    invoices_id = models.IntegerField()
    partner_banks_id = models.IntegerField()
    link_types_id = models.IntegerField()
    external_fund_transfers_id = models.IntegerField(blank=True, null=True)
    debit_account_number = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_payment_requests'


class BillingInvoices(models.Model):
    billing_invoices_id = models.AutoField(primary_key=True)
    invoice_no = models.CharField(max_length=191)
    batch_name = models.CharField(max_length=191)
    companies_id = models.IntegerField(blank=True, null=True)
    file_name = models.CharField(max_length=191, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    added_on = models.DateTimeField()
    is_mail_sent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'billing_invoices'


class BobSettlements(models.Model):
    bob_settlements_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    pg_transactions_id = models.CharField(unique=True, max_length=191, blank=True, null=True)
    merchant_terminal_id = models.CharField(max_length=191, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=14, decimal_places=2)
    merchant_transaction_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    convenience_fee = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    bob_tdr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    bob_gst = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    bob_total_fee = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    bob_net_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    open_tdr = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    same_day_settlement_charge = models.DecimalField(max_digits=12, decimal_places=2)
    open_gst = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    open_total_fee = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    open_net_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    pg_txn_ref_num = models.CharField(unique=True, max_length=191, blank=True, null=True)
    open_pg_txn_id = models.CharField(unique=True, max_length=191, blank=True, null=True)
    settlement_source = models.CharField(max_length=191)
    settlement_txn_id = models.CharField(max_length=191, blank=True, null=True)
    settlement_status_id = models.IntegerField()
    settled_by = models.IntegerField(blank=True, null=True)
    settled_to_open_date = models.DateTimeField(blank=True, null=True)
    settled_to_merchant_date = models.DateTimeField(blank=True, null=True)
    settlement_modes_id = models.IntegerField()
    is_held = models.IntegerField(blank=True, null=True)
    hold_by = models.IntegerField(blank=True, null=True)
    hold_reason = models.CharField(max_length=191, blank=True, null=True)
    is_processed = models.IntegerField()
    transaction_date = models.CharField(max_length=191, blank=True, null=True)
    settlement_date = models.CharField(max_length=191, blank=True, null=True)
    transaction_id = models.CharField(max_length=191, blank=True, null=True)
    merchant_aggregator_id = models.CharField(max_length=191, blank=True, null=True)
    mid = models.CharField(max_length=191, blank=True, null=True)
    merchant_legal_name = models.CharField(max_length=191, blank=True, null=True)
    sid = models.CharField(max_length=191, blank=True, null=True)
    store_trading = models.CharField(max_length=191, blank=True, null=True)
    tid = models.CharField(max_length=191, blank=True, null=True)
    batch_number = models.CharField(max_length=191, blank=True, null=True)
    card_number_or_vpa = models.CharField(max_length=191, blank=True, null=True)
    payment_method = models.CharField(max_length=191, blank=True, null=True)
    interchange = models.CharField(max_length=191, blank=True, null=True)
    merchant_category_code = models.CharField(max_length=191, blank=True, null=True)
    mcc_category = models.CharField(max_length=191, blank=True, null=True)
    transaction_type = models.CharField(max_length=191, blank=True, null=True)
    transaction_currency_code = models.CharField(max_length=191, blank=True, null=True)
    transaction_amount = models.CharField(max_length=191, blank=True, null=True)
    additional_amount = models.CharField(max_length=191, blank=True, null=True)
    settlement_currency = models.CharField(max_length=191, blank=True, null=True)
    settlement_amount = models.CharField(max_length=191, blank=True, null=True)
    late_settlement = models.CharField(max_length=191, blank=True, null=True)
    rrf_amount = models.CharField(max_length=191, blank=True, null=True)
    msf_amount = models.CharField(max_length=191, blank=True, null=True)
    gst = models.CharField(max_length=191, blank=True, null=True)
    min_amount = models.CharField(max_length=191, blank=True, null=True)
    max_amount = models.CharField(max_length=191, blank=True, null=True)
    csf_amount = models.CharField(max_length=191, blank=True, null=True)
    csf_tax = models.CharField(max_length=191, blank=True, null=True)
    net_amount = models.CharField(max_length=191, blank=True, null=True)
    approved_or_declined = models.CharField(max_length=191, blank=True, null=True)
    auth_or_approval_code = models.CharField(max_length=191, blank=True, null=True)
    retrieval_ref_num = models.CharField(max_length=191, blank=True, null=True)
    system_trace_audit_num = models.CharField(max_length=191, blank=True, null=True)
    pg_payment_txn_id = models.CharField(max_length=191, blank=True, null=True)
    pg_txn_id = models.CharField(max_length=191, blank=True, null=True)
    merchant_track_id = models.CharField(max_length=191, blank=True, null=True)
    udf = models.TextField(blank=True, null=True)
    payment_date = models.CharField(max_length=191, blank=True, null=True)
    transaction_status = models.CharField(max_length=191, blank=True, null=True)
    arn = models.CharField(max_length=191, blank=True, null=True)
    upi_txn_id = models.CharField(max_length=191, blank=True, null=True)
    source_type = models.CharField(max_length=191, blank=True, null=True)
    source_id = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bob_settlements'


class BookKeeping(models.Model):
    book_keeping_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    contacts_id = models.IntegerField(blank=True, null=True)
    contacts_name = models.CharField(max_length=191, blank=True, null=True)
    expense_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    income_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    open_banking_nodal_statements_id = models.IntegerField(blank=True, null=True)
    categories_id = models.IntegerField(blank=True, null=True)
    category_name = models.CharField(max_length=191, blank=True, null=True)
    ref_no = models.CharField(max_length=250, blank=True, null=True)
    type = models.CharField(max_length=7)
    source_type = models.CharField(max_length=199, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    transaction_types_id = models.IntegerField()
    is_reversal = models.IntegerField()
    transaction_date = models.DateTimeField(blank=True, null=True)
    is_split = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_keeping'


class BotsUps(models.Model):
    bots_ups_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    reset_link = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bots_ups'


class BranchCodeRmMapping(models.Model):
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    branch_code = models.CharField(max_length=191)
    branch_name = models.CharField(max_length=191)
    cluster = models.CharField(max_length=191)
    region = models.CharField(max_length=191)
    zone = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branch_code_rm_mapping'


class BudgetTags(models.Model):
    budget_tags_id = models.AutoField(primary_key=True)
    budgets_id = models.IntegerField()
    tags_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_tags'


class Budgets(models.Model):
    budgets_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    contacts_id = models.IntegerField(blank=True, null=True)
    categories_id = models.IntegerField(blank=True, null=True)
    invoices_id = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budgets'


class BulkTransferCronAssignments(models.Model):
    bulk_transfer_cron_assignments_id = models.AutoField(primary_key=True)
    batch_id = models.CharField(max_length=100)
    users_id = models.IntegerField()
    cron_name = models.CharField(max_length=200, blank=True, null=True)
    is_verified_batch = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    link_types_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bulk_transfer_cron_assignments'


class BusinessAccountTypes(models.Model):
    business_account_types_id = models.AutoField(primary_key=True)
    account_type = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_account_types'


class BusinessPanDetails(models.Model):
    business_pan_details_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    doi = models.CharField(max_length=191, blank=True, null=True)
    pan_number = models.CharField(max_length=191, blank=True, null=True)
    has_verified = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_pan_details'


class BusinessSector(models.Model):
    business_sector_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_sector'


class CampaignDetails(models.Model):
    name = models.CharField(max_length=191)
    description = models.CharField(max_length=191)
    active = models.IntegerField()
    cash_allotted = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cash_used = models.DecimalField(max_digits=8, decimal_places=2)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    campaign_type_id = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaign_details'


class CampaignEvents(models.Model):
    campaign_id = models.PositiveIntegerField(blank=True, null=True)
    event_id = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaign_events'


class CardBalanceHistories(models.Model):
    card_balance_histories_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    card_details_id = models.IntegerField(blank=True, null=True)
    card_number = models.CharField(max_length=200)
    partner_banks_id = models.IntegerField()
    current_balance = models.DecimalField(max_digits=14, decimal_places=2)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    type = models.CharField(max_length=2)
    ref_id = models.CharField(max_length=200, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    is_load_money = models.IntegerField()
    is_transfered = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_withdraw = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_balance_histories'


class CardBalanceHistoriesMappings(models.Model):
    card_balance_histories_mapping_id = models.AutoField(primary_key=True)
    card_balance_histories_ids = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_balance_histories_mappings'


class CardBalances(models.Model):
    card_balances_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    card_details_id = models.IntegerField()
    current_balance = models.DecimalField(max_digits=14, decimal_places=2)
    card_provider_partner_banks_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_balances'


class CardCreditEnhancements(models.Model):
    card_credit_enhancements_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    card_details_id = models.IntegerField()
    is_user_consent_taken = models.IntegerField()
    enhanced_limit = models.DecimalField(max_digits=14, decimal_places=2)
    remarks = models.CharField(max_length=191)
    current_available_limit = models.FloatField()
    credit_assigned = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_credit_enhancements'


class CardDetailRecords(models.Model):
    card_detail_records_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    card_details_id = models.IntegerField()
    team_member_details_id = models.IntegerField()
    old_kit_no = models.CharField(max_length=255)
    old_sbm_federals_id = models.IntegerField()
    new_kit_no = models.CharField(max_length=255)
    new_sbm_federals_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_detail_records'


class CardDetails(models.Model):
    card_details_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    team_member_details_id = models.IntegerField(blank=True, null=True)
    name_on_card = models.CharField(max_length=200, blank=True, null=True)
    masked_card_number = models.CharField(max_length=200, blank=True, null=True)
    card_types_id = models.IntegerField(blank=True, null=True)
    card_provider = models.CharField(max_length=200, blank=True, null=True)
    source_type = models.CharField(max_length=200, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    balance_limit = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    current_balance = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    used_limit = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    card_ref_id = models.CharField(max_length=200)
    open_card_statuses_id = models.IntegerField(blank=True, null=True)
    companies_card_statuses_id = models.IntegerField(blank=True, null=True)
    users_card_statuses_id = models.IntegerField(blank=True, null=True)
    card_activation_statuses_id = models.IntegerField(blank=True, null=True)
    activation_status_message = models.TextField(blank=True, null=True)
    card_activation_date = models.DateTimeField(blank=True, null=True)
    is_kyc_documents_submitted = models.IntegerField()
    is_kyc_document_verified = models.IntegerField()
    card_load_limit = models.DecimalField(max_digits=16, decimal_places=2)
    card_status_last_updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    owner_card = models.IntegerField()
    open_card_type = models.CharField(max_length=191, blank=True, null=True)
    card_load_amount = models.IntegerField(blank=True, null=True)
    set_pin_status = models.IntegerField(blank=True, null=True)
    share_code = models.CharField(max_length=191, blank=True, null=True)
    card_labels_id = models.IntegerField(blank=True, null=True)
    monthly_limit = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    card_category_id = models.IntegerField(blank=True, null=True)
    caf_s3_url = models.CharField(max_length=200, blank=True, null=True)
    source_of_registration = models.CharField(max_length=255, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    activation_period = models.CharField(max_length=16)
    expiration_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_details'


class CardKycDetails(models.Model):
    card_kyc_details_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    card_details_id = models.IntegerField()
    admin_users_id = models.IntegerField(blank=True, null=True)
    address_proof_types_id = models.CharField(max_length=191)
    address_proof_files_id = models.CharField(max_length=200)
    card_kyc_statuses_id = models.IntegerField(blank=True, null=True)
    address_proof_number = models.CharField(max_length=199)
    date_of_birth = models.CharField(max_length=199)
    name = models.CharField(max_length=199)
    individual_pan_details_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_kyc_details'


class CardKycStatuses(models.Model):
    card_kyc_statuses_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_kyc_statuses'


class CardLabels(models.Model):
    card_labels_id = models.AutoField(primary_key=True)
    label_name = models.CharField(max_length=100)
    file_url = models.CharField(max_length=255, blank=True, null=True)
    users_id = models.IntegerField()
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_labels'


class CardLoadMoneyRequests(models.Model):
    card_load_money_requests_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    team_member_details_id = models.IntegerField()
    card_details_id = models.IntegerField()
    approvers_id = models.IntegerField(blank=True, null=True)
    load_amount = models.DecimalField(max_digits=16, decimal_places=2)
    load_request_statuses_id = models.IntegerField()
    transaction_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_load_money_requests'


class CardManualProcessedTransactions(models.Model):
    id = models.BigAutoField(primary_key=True)
    card_transaction_ref_no = models.CharField(max_length=150, blank=True, null=True)
    email_id = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    result = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_manual_processed_transactions'


class CardNumberDetails(models.Model):
    card_number_details_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    card_details_id = models.IntegerField()
    open_card_type = models.CharField(max_length=7, blank=True, null=True)
    kit_no = models.CharField(max_length=1000, blank=True, null=True)
    card_number = models.CharField(max_length=1000, blank=True, null=True)
    expiry = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_number_details'


class CardRequests(models.Model):
    card_requests_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    team_member_details_id = models.IntegerField(blank=True, null=True)
    card_details_id = models.IntegerField()
    masked_card_number = models.CharField(max_length=200, blank=True, null=True)
    balance_limit = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    addresses_id = models.IntegerField(blank=True, null=True)
    shipping_address_line = models.CharField(max_length=300, blank=True, null=True)
    shipping_city = models.CharField(max_length=200, blank=True, null=True)
    shipping_state = models.CharField(max_length=200, blank=True, null=True)
    shipping_pincode = models.CharField(max_length=100, blank=True, null=True)
    is_free = models.IntegerField()
    shipping_statuses_id = models.IntegerField(blank=True, null=True)
    bank_transaction_status_id = models.IntegerField(blank=True, null=True)
    internal_transaction_ref_id = models.CharField(max_length=200, blank=True, null=True)
    open_charges_ref_id = models.CharField(max_length=200)
    purpose = models.TextField(blank=True, null=True)
    partner_banks_id = models.IntegerField(blank=True, null=True)
    link_types_id = models.IntegerField(blank=True, null=True)
    shipped_on = models.DateTimeField(blank=True, null=True)
    shipping_partners_id = models.IntegerField(blank=True, null=True)
    shipping_tracking_id = models.CharField(max_length=200, blank=True, null=True)
    delivered_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    cards_purchase_orders_id = models.IntegerField(blank=True, null=True)
    open_card_type = models.CharField(max_length=191, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_requests'


class CardStatementTransactions(models.Model):
    card_statement_transactions_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    card_details_id = models.IntegerField()
    card_statements_id = models.IntegerField(blank=True, null=True)
    card_balance = models.DecimalField(max_digits=14, decimal_places=2)
    card_limit = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    open_pay_balance = models.DecimalField(max_digits=14, decimal_places=2)
    split_card = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    split_open = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    split = models.TextField()
    transaction_amount = models.DecimalField(max_digits=14, decimal_places=2)
    transaction_type = models.CharField(max_length=2)
    transaction_ref_id = models.CharField(max_length=100)
    transaction_date = models.DateTimeField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    used_limit = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    transaction_description = models.CharField(max_length=191, blank=True, null=True)
    repayment = models.IntegerField()
    fine = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'card_statement_transactions'


class CardStatements(models.Model):
    card_statements_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    card_details_id = models.IntegerField()
    statement_date = models.DateTimeField()
    statement_amount = models.DecimalField(max_digits=14, decimal_places=2)
    due_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    payment_date = models.DateTimeField(blank=True, null=True)
    payment_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    payment_status = models.IntegerField()
    files_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    statement_tax = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    statement_fine = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_statements'


class CardStatuses(models.Model):
    card_statuses_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=100)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_statuses'


class CardTransactionStatuses(models.Model):
    card_transaction_statuses_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=100)
    is_active = models.IntegerField()
    partner_banks_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_transaction_statuses'


class CardTransactions(models.Model):
    card_transactions_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    card_category_id = models.IntegerField(blank=True, null=True)
    card_details_id = models.IntegerField()
    masked_card_number = models.CharField(max_length=100)
    card_transaction_ref_no = models.CharField(max_length=100)
    retrieval_ref_no = models.CharField(max_length=20, blank=True, null=True)
    txn_id = models.CharField(max_length=25, blank=True, null=True)
    card_transaction_date = models.DateTimeField()
    transaction_mode = models.CharField(max_length=2)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    balance = models.DecimalField(max_digits=14, decimal_places=2)
    card_transaction_statuses_id = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    txn_currency = models.CharField(max_length=20, blank=True, null=True)
    merchant_id = models.CharField(max_length=200, blank=True, null=True)
    merchant_name = models.CharField(max_length=200, blank=True, null=True)
    merchant_location = models.CharField(max_length=200, blank=True, null=True)
    txn_origin = models.CharField(max_length=200, blank=True, null=True)
    txn_status = models.CharField(max_length=200, blank=True, null=True)
    source_type_name = models.CharField(max_length=200, blank=True, null=True)
    source_type_transaction_id = models.IntegerField(blank=True, null=True)
    team_member_details_id = models.IntegerField(blank=True, null=True)
    mcc_id = models.PositiveIntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=191, blank=True, null=True)
    terminal_id = models.CharField(max_length=150, blank=True, null=True)
    m2p_txn_currency = models.CharField(max_length=20, db_collation='utf8mb4_bin', blank=True, null=True)
    atm_fees = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_transactions'


class CardTypes(models.Model):
    card_types_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    logo = models.TextField()
    url = models.CharField(max_length=250)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_types'


class CardVirtualUsedLimits(models.Model):
    card_virtual_used_limits_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    team_member_details_id = models.IntegerField(blank=True, null=True)
    card_details_id = models.IntegerField()
    monthly_limit = models.FloatField()
    used_limit = models.FloatField()
    last_updated_used_limit_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card_virtual_used_limits'


class CardsAtmFees(models.Model):
    open_card_type = models.CharField(max_length=10, blank=True, null=True)
    transaction_type = models.CharField(max_length=25, blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cards_atm_fees'


class CardsDownTime(models.Model):
    cards_down_time_id = models.AutoField(primary_key=True)
    card_provider = models.CharField(max_length=200, blank=True, null=True)
    start_time = models.CharField(max_length=10, blank=True, null=True)
    end_time = models.CharField(max_length=10, blank=True, null=True)
    down_time_status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cards_down_time'


class CardsModels(models.Model):
    cards_models_id = models.AutoField(primary_key=True)
    card_model = models.CharField(max_length=20)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cards_models'


class CardsPurchaseOrders(models.Model):
    cards_purchase_orders_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    companies_id = models.IntegerField()
    no_of_cards = models.IntegerField()
    cards_models_id = models.IntegerField()
    card_transactions_status_id = models.IntegerField(blank=True, null=True)
    layer_payment_status_id = models.IntegerField(blank=True, null=True)
    order_purchase_amount = models.FloatField()
    open_charge_ref_id = models.CharField(max_length=80, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    addresses_id = models.IntegerField()
    team_member_details_id = models.IntegerField()
    card_type = models.CharField(max_length=50, blank=True, null=True)
    owner_card = models.IntegerField()
    open_card_type = models.CharField(max_length=191, blank=True, null=True)
    payment_token = models.CharField(max_length=500, blank=True, null=True)
    invoice_url = models.CharField(max_length=500, blank=True, null=True)
    invoice_id = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cards_purchase_orders'


class CareerJobApplications(models.Model):
    career_jobs_id = models.IntegerField()
    name = models.CharField(max_length=191)
    email = models.CharField(max_length=191)
    mobile = models.CharField(max_length=191)
    current_city = models.CharField(max_length=191, blank=True, null=True)
    website = models.CharField(max_length=191, blank=True, null=True)
    resume_files_id = models.IntegerField(blank=True, null=True)
    cover_files_id = models.IntegerField(blank=True, null=True)
    utm_source = models.CharField(max_length=191, blank=True, null=True)
    utm_medium = models.CharField(max_length=191, blank=True, null=True)
    utm_campaign = models.CharField(max_length=191, blank=True, null=True)
    utm_term = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'career_job_applications'


class CareerJobs(models.Model):
    career_jobs_id = models.AutoField(primary_key=True)
    career_verticals_id = models.IntegerField()
    job_role = models.CharField(max_length=191)
    job_description = models.TextField()
    location = models.CharField(max_length=191)
    employment_type = models.CharField(max_length=191)
    experience = models.CharField(max_length=191)
    skills = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'career_jobs'


class CareerVerticals(models.Model):
    career_verticals_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=191)
    slug = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'career_verticals'


class Categories(models.Model):
    categories_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    category_name = models.CharField(max_length=191, blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class CircleCouponCodeMerchantMappings(models.Model):
    circle_coupon_code_merchant_mappings_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    circle_partners_id = models.IntegerField()
    circle_partner_coupon_codes_id = models.IntegerField()
    coupon_codes = models.CharField(max_length=60)
    is_unique = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circle_coupon_code_merchant_mappings'


class CirclePartnerCouponCodes(models.Model):
    circle_partner_coupon_codes_id = models.AutoField(primary_key=True)
    circle_partners_id = models.IntegerField()
    coupon_code = models.CharField(max_length=20)
    is_used = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circle_partner_coupon_codes'


class CirclePartners(models.Model):
    circle_partners_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    priority = models.IntegerField()
    logo = models.CharField(max_length=191)
    partner_desc = models.CharField(max_length=191)
    url = models.CharField(max_length=191)
    redirect_url = models.CharField(max_length=191)
    coupons = models.CharField(max_length=191)
    coupon_desc = models.TextField()
    is_active = models.IntegerField()
    is_unique = models.IntegerField()
    is_redeemable = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circle_partners'


class ClientConfigurations(models.Model):
    client_config_id = models.AutoField(primary_key=True)
    client_type = models.CharField(max_length=20)
    version_code = models.IntegerField()
    force_update_version_code = models.IntegerField()
    app_name = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_configurations'


class ClientPgSettings(models.Model):
    client_pg_settings_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.CharField(max_length=191)
    pg_activation_statuses_id = models.CharField(max_length=244)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_pg_settings'


class CommunicationChannels(models.Model):
    communication_channels_id = models.AutoField(primary_key=True)
    channel_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'communication_channels'


class Companies(models.Model):
    companies_id = models.AutoField(primary_key=True)
    has_icici_connected = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    company_name = models.CharField(max_length=191, blank=True, null=True)
    brand_name = models.CharField(max_length=191, blank=True, null=True)
    companies_va_number = models.CharField(unique=True, max_length=191, blank=True, null=True)
    partner_banks_id = models.CharField(max_length=191, blank=True, null=True)
    fund_transfer_partner_banks_id = models.IntegerField(blank=True, null=True)
    vpa_partner_banks_id = models.IntegerField(blank=True, null=True)
    mob_business_types_id = models.IntegerField(blank=True, null=True)
    company_id = models.CharField(max_length=200, blank=True, null=True)
    company_pan = models.CharField(max_length=50, blank=True, null=True)
    company_cin = models.CharField(max_length=50, blank=True, null=True)
    company_gstin = models.CharField(max_length=50, blank=True, null=True)
    service_tax_number = models.CharField(max_length=191, blank=True, null=True)
    vat_tin_number = models.CharField(max_length=191, blank=True, null=True)
    company_tan = models.CharField(max_length=200, blank=True, null=True)
    company_cst = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=191, blank=True, null=True)
    website_description = models.TextField(blank=True, null=True)
    company_mcc_types_id = models.IntegerField(blank=True, null=True)
    referral = models.CharField(max_length=60, blank=True, null=True)
    onboarding_completed_on = models.DateTimeField(blank=True, null=True)
    openbook_kyc_completed_on = models.DateTimeField(blank=True, null=True)
    seller_types_id = models.IntegerField(blank=True, null=True)
    seller_tagged_on = models.DateTimeField(blank=True, null=True)
    company_phone = models.CharField(max_length=191, blank=True, null=True)
    mob_statuses_id = models.IntegerField()
    onboarding_statuses_id = models.IntegerField(blank=True, null=True)
    is_short_kyc_user = models.IntegerField()
    is_joint_account = models.IntegerField()
    is_offline_merchant = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    api_version = models.CharField(max_length=20, blank=True, null=True)
    business_account_types_id = models.IntegerField()
    companies_va_number_temp = models.CharField(max_length=191, blank=True, null=True)
    partner_banks_id_temp = models.CharField(max_length=191, blank=True, null=True)
    smid = models.IntegerField(blank=True, null=True)
    current_account_applied = models.IntegerField()
    is_ekyc_verified = models.IntegerField()
    is_auto_verified = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'companies'


class CompaniesExternalMappings(models.Model):
    companies_external_mappings_id = models.BigAutoField(primary_key=True)
    companies_id = models.PositiveIntegerField()
    external_source = models.CharField(max_length=191)
    external_identifier = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'companies_external_mappings'


class CompanyCurrentAccountRequirements(models.Model):
    company_current_account_requirements_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField(unique=True)
    debit_card = models.IntegerField(blank=True, null=True)
    cheque_book = models.IntegerField(blank=True, null=True)
    name_on_card = models.CharField(max_length=191, blank=True, null=True)
    branch_pincode = models.CharField(max_length=191, blank=True, null=True)
    branch_code = models.CharField(max_length=191, blank=True, null=True)
    branch_name = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_current_account_requirements'


class CompanyGstDetails(models.Model):
    company_gst_details_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField(blank=True, null=True)
    is_gst_applicable = models.IntegerField(blank=True, null=True)
    gstin = models.CharField(max_length=191, blank=True, null=True)
    legal_name = models.CharField(max_length=191, blank=True, null=True)
    trade_name = models.CharField(max_length=191, blank=True, null=True)
    registration_type = models.CharField(max_length=191, blank=True, null=True)
    assessee_of_other_territory = models.IntegerField(blank=True, null=True)
    gstin_status = models.CharField(max_length=191, blank=True, null=True)
    registration_date = models.DateField(blank=True, null=True)
    return_filing_frequency = models.CharField(max_length=9, blank=True, null=True)
    qrmp_scheme = models.IntegerField(db_column='QRMP_scheme', blank=True, null=True)  # Field name made lowercase.
    opt_for_iff = models.IntegerField(blank=True, null=True)
    tax_rate = models.CharField(max_length=2, blank=True, null=True)
    enable_tax_rate_for_purchase = models.IntegerField(blank=True, null=True)
    eway_bill_applicable = models.IntegerField(blank=True, null=True)
    eway_bill_intrastate_threshold = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    eway_bill_interstate_threshold = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    einvoice_applicable = models.IntegerField(blank=True, null=True)
    einvoice_applicable_date = models.DateField(blank=True, null=True)
    hsn_sac_codes = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_gst_details'


class CompanyMccTypes(models.Model):
    company_mcc_types_id = models.AutoField(primary_key=True)
    industry_name = models.CharField(max_length=191)
    mcc_code = models.IntegerField()
    description = models.TextField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_mcc_types'


class CompanyRiskVerification(models.Model):
    company_risk_verifications_id = models.BigAutoField(primary_key=True)
    companies_id = models.IntegerField(blank=True, null=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    risk_category = models.CharField(max_length=200, blank=True, null=True)
    risk_approval_category = models.CharField(max_length=200, blank=True, null=True)
    risk_checks = models.TextField(blank=True, null=True)
    risk_checks_description = models.CharField(max_length=200, blank=True, null=True)
    risk_verified_by = models.IntegerField(blank=True, null=True)
    risk_verified_date = models.CharField(max_length=200, blank=True, null=True)
    risk_business_categories_id = models.IntegerField(blank=True, null=True)
    risk_industry_categories_id = models.IntegerField(blank=True, null=True)
    risk_industry_sub_categories_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_risk_verification'


class CompanyTaxes(models.Model):
    company_taxes_id = models.AutoField(primary_key=True)
    accounts_id = models.PositiveIntegerField(blank=True, null=True)
    users_id = models.PositiveIntegerField(blank=True, null=True)
    companies_id = models.PositiveIntegerField(blank=True, null=True)
    tax_name = models.CharField(max_length=11, blank=True, null=True)
    tax_desc = models.CharField(max_length=200, blank=True, null=True)
    tax_perc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_taxes'


class ConnectedBankStatements(models.Model):
    connected_bank_statements_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    partner_banks_id = models.IntegerField()
    contacts_id = models.IntegerField(blank=True, null=True)
    is_contact = models.IntegerField(blank=True, null=True)
    categories_id = models.IntegerField(blank=True, null=True)
    category_name = models.CharField(max_length=250, blank=True, null=True)
    open_bank_accounts_id = models.IntegerField(blank=True, null=True)
    withdraw_bank_accounts_id = models.IntegerField(blank=True, null=True)
    link_types_id = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ref_no = models.CharField(max_length=250, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    transaction_types_id = models.IntegerField(blank=True, null=True)
    transaction_mode = models.CharField(max_length=2)
    transaction_date = models.DateTimeField(blank=True, null=True)
    account_number = models.CharField(max_length=250, blank=True, null=True)
    bank_name = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'connected_bank_statements'


class ConnectedBankingLeads(models.Model):
    connected_banking_leads_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    company_name = models.CharField(max_length=200, blank=True, null=True)
    contact_person = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=200, blank=True, null=True)
    alternate_phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    pincode = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=199, blank=True, null=True)
    source_partner_bank_id = models.IntegerField(blank=True, null=True)
    leads_partner_bank_id = models.IntegerField(blank=True, null=True)
    connected_lead_status_id = models.IntegerField(blank=True, null=True)
    admin_users_id = models.IntegerField(blank=True, null=True)
    lead_initiated_date = models.DateTimeField(blank=True, null=True)
    source_table = models.CharField(max_length=100, blank=True, null=True)
    source_table_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    rm_users_id = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'connected_banking_leads'


class ConnectedLeadStatusHistories(models.Model):
    connected_lead_status_histories_id = models.AutoField(primary_key=True)
    connected_banking_leads_id = models.IntegerField()
    connected_lead_status_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'connected_lead_status_histories'


class ConnectedLeadsStatus(models.Model):
    connected_lead_status_id = models.IntegerField()
    lead_status_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'connected_leads_status'


class Contacts(models.Model):
    contacts_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=191)
    type_of_contact = models.CharField(max_length=191, blank=True, null=True)
    contact_type = models.CharField(max_length=8, blank=True, null=True)
    primary_contact = models.CharField(max_length=191, blank=True, null=True)
    beneficiary_account_number = models.CharField(max_length=191, blank=True, null=True)
    ifsc_code = models.CharField(max_length=191, blank=True, null=True)
    default_transaction_types_id = models.IntegerField(blank=True, null=True)
    bank_name = models.CharField(max_length=191, blank=True, null=True)
    branch_name = models.CharField(max_length=191, blank=True, null=True)
    is_bene_active = models.IntegerField()
    email_id = models.CharField(max_length=191, blank=True, null=True)
    email_verification_status = models.CharField(max_length=11)
    countries_id = models.IntegerField()
    country = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    mobile_number = models.CharField(max_length=50, blank=True, null=True)
    contact_person = models.CharField(max_length=200, blank=True, null=True)
    landline_number = models.CharField(max_length=50, blank=True, null=True)
    mobile_number_country_code = models.CharField(max_length=191)
    incoming_categories_id = models.IntegerField(blank=True, null=True)
    outgoing_categories_id = models.IntegerField(blank=True, null=True)
    invoice_payment_terms_id = models.IntegerField(blank=True, null=True)
    bill_payment_terms_id = models.IntegerField(blank=True, null=True)
    dpo = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    dpo_quarter = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    dpo_year = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    dso = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    dso_quarter = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    dso_year = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    billing_address_id = models.IntegerField(blank=True, null=True)
    shipping_address_id = models.IntegerField(blank=True, null=True)
    partner_banks_id = models.CharField(max_length=191, blank=True, null=True)
    contacts_va_number = models.CharField(unique=True, max_length=191, blank=True, null=True)
    currency = models.CharField(max_length=191)
    pan = models.CharField(max_length=191, blank=True, null=True)
    gstin = models.CharField(max_length=191, blank=True, null=True)
    gstin_status = models.IntegerField(blank=True, null=True)
    tds = models.CharField(max_length=191, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    other_details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    categories_id = models.IntegerField(blank=True, null=True)
    vpa = models.CharField(max_length=50, blank=True, null=True)
    display_name = models.CharField(max_length=191)
    email_is_user = models.IntegerField()
    mobile_is_user = models.IntegerField()
    invite_url = models.CharField(max_length=191, blank=True, null=True)
    is_invited = models.IntegerField()
    gst_reg_type = models.CharField(max_length=200, blank=True, null=True)
    nature_of_supply = models.CharField(max_length=200, blank=True, null=True)
    is_ecommerce_operator = models.IntegerField(blank=True, null=True)
    is_transporter = models.IntegerField(blank=True, null=True)
    transporter_id = models.CharField(max_length=191, blank=True, null=True)
    dr_or_cr = models.CharField(max_length=100, blank=True, null=True)
    payment_favouring = models.CharField(max_length=200, blank=True, null=True)
    contacts_va_number_temp = models.CharField(max_length=191, blank=True, null=True)
    partner_banks_id_temp = models.CharField(max_length=191, blank=True, null=True)
    contact_vpa = models.CharField(max_length=191, blank=True, null=True)
    is_enterprise = models.IntegerField()
    contacts_ref_id = models.CharField(max_length=191, blank=True, null=True)
    is_updated = models.IntegerField()
    shipping_name = models.CharField(max_length=191, blank=True, null=True)
    billing_name = models.CharField(max_length=191, blank=True, null=True)
    registration_type = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    credit_limit_outstanding = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    credit_limit_available = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    opening_balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    closing_balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payroll_enabled = models.IntegerField()
    is_igst = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField()
    is_deletable = models.IntegerField()
    url = models.CharField(max_length=191, blank=True, null=True)
    qr_sticker_url = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts'


class ContactsBulkInvitations(models.Model):
    contacts_bulk_invitations_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    contacts_ids = models.TextField()
    is_picked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts_bulk_invitations'


class ContactsPayoutAccounts(models.Model):
    contacts_payout_accounts_id = models.AutoField(primary_key=True)
    contacts_id = models.BigIntegerField()
    payout_account_type = models.CharField(max_length=12)
    vpa = models.CharField(max_length=191)
    bank_account_name = models.CharField(max_length=191)
    bank_account_ifsc = models.CharField(max_length=191)
    bank_account_number = models.CharField(max_length=191)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts_payout_accounts'


class ContactsTds(models.Model):
    contacts_tds_id = models.AutoField(primary_key=True)
    contacts_id = models.IntegerField()
    pan = models.CharField(max_length=15, blank=True, null=True)
    deductee_type = models.CharField(max_length=25, blank=True, null=True)
    tds_category_id = models.IntegerField(blank=True, null=True)
    tds = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_ltr = models.IntegerField(blank=True, null=True)
    ltr_certificate_number = models.CharField(max_length=75, blank=True, null=True)
    ltr_category = models.CharField(max_length=100, blank=True, null=True)
    ltr_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ltr_tds_perc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts_tds'


class Countries(models.Model):
    countries_id = models.AutoField(primary_key=True)
    iso = models.CharField(max_length=2)
    name = models.CharField(max_length=199)
    nice_name = models.CharField(max_length=199)
    iso3 = models.CharField(max_length=3)
    numcode = models.IntegerField()
    phonecode = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class CouponCodeTypes(models.Model):
    coupon_code_types_id = models.AutoField(primary_key=True)
    coupon_code_types = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupon_code_types'


class CouponCodes(models.Model):
    coupon_codes_id = models.AutoField(primary_key=True)
    coupon_code = models.CharField(max_length=191, blank=True, null=True)
    coupon_code_types_id = models.IntegerField(blank=True, null=True)
    is_valid = models.IntegerField(blank=True, null=True)
    validity_start_date = models.CharField(max_length=191, blank=True, null=True)
    validity_end_date = models.CharField(max_length=191, blank=True, null=True)
    discount_type = models.CharField(max_length=5)
    discount_value = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    total_coupons = models.IntegerField(blank=True, null=True)
    used_coupons = models.IntegerField()
    per_user_allowed_limit = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupon_codes'


class CourierPartnerList(models.Model):
    courier_partner_lists_id = models.AutoField(primary_key=True)
    partner_name = models.CharField(max_length=200)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courier_partner_list'


class CreationTypes(models.Model):
    creation_types_id = models.AutoField(primary_key=True)
    creation_type = models.CharField(max_length=80)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'creation_types'


class Currencies(models.Model):
    currencies_id = models.AutoField(primary_key=True)
    countries_id = models.IntegerField()
    currency_name = models.CharField(max_length=199)
    currency_code = models.CharField(max_length=10)
    currency_symbol = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currencies'


class DcbConnectedAccounts(models.Model):
    dcb_connected_accounts_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    unique_id = models.CharField(max_length=200, blank=True, null=True)
    bank_account_number = models.CharField(max_length=200, blank=True, null=True)
    registration_status = models.CharField(max_length=200, blank=True, null=True)
    account_statement = models.CharField(max_length=200, blank=True, null=True)
    account_balance = models.CharField(max_length=200, blank=True, null=True)
    fund_transfer = models.CharField(max_length=200, blank=True, null=True)
    is_callback_successfull = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dcb_connected_accounts'


class DcbConnectedStatements(models.Model):
    dcb_connected_statements_id = models.AutoField(primary_key=True)
    unique_id = models.CharField(max_length=191, blank=True, null=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    request_id = models.IntegerField()
    transaction_particular = models.CharField(max_length=191, blank=True, null=True)
    deposit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    withdrawl = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=191, blank=True, null=True)
    opening_balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    closing_balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    serial_number = models.CharField(max_length=191, blank=True, null=True)
    reference_number = models.CharField(max_length=191, blank=True, null=True)
    transaction_id = models.CharField(max_length=191, blank=True, null=True)
    bank_message = models.CharField(max_length=191, blank=True, null=True)
    api_status = models.CharField(max_length=191, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dcb_connected_statements'


class DcbFundTransfers(models.Model):
    dcb_fund_transfers_id = models.AutoField(primary_key=True)
    bank_transaction_status_id = models.IntegerField(blank=True, null=True)
    external_fund_transfers_id = models.IntegerField(blank=True, null=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    request_id = models.IntegerField()
    debit_account = models.CharField(max_length=191, blank=True, null=True)
    credit_account = models.CharField(max_length=191, blank=True, null=True)
    ifsc_code = models.CharField(max_length=191, blank=True, null=True)
    amount = models.CharField(max_length=191, blank=True, null=True)
    transfer_mode = models.CharField(max_length=191, blank=True, null=True)
    payee_name = models.CharField(max_length=191, blank=True, null=True)
    unique_id = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.CharField(max_length=191, blank=True, null=True)
    reference_number = models.CharField(max_length=191, blank=True, null=True)
    transaction_id = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dcb_fund_transfers'


class DemoRequests(models.Model):
    demo_requests_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    product_url = models.CharField(max_length=255)
    comments = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demo_requests'


class Departments(models.Model):
    departments_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class DigioENachDetails(models.Model):
    digio_e_nach_details_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    users_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField()
    is_contact = models.IntegerField()
    contacts_id = models.IntegerField()
    identifier = models.CharField(max_length=191)
    identifier_type = models.CharField(max_length=191)
    expire_in_days = models.IntegerField()
    enach_type = models.CharField(max_length=191)
    mandate_request_id = models.CharField(max_length=191)
    mandate_creation_date_time = models.CharField(max_length=191)
    sponsor_bank_id = models.CharField(max_length=191)
    sponsor_bank_name = models.CharField(max_length=191)
    destination_bank_id = models.CharField(max_length=191)
    destination_bank_name = models.CharField(max_length=191)
    bank_identifier = models.CharField(max_length=191)
    login_id = models.CharField(max_length=191)
    mandate_sequence = models.CharField(max_length=191)
    customer_account_type = models.CharField(max_length=191)
    management_category = models.CharField(max_length=191)
    service_provider_name = models.CharField(max_length=191)
    service_provider_utility_code = models.CharField(max_length=191)
    customer_account_number = models.CharField(max_length=191)
    instrument_type = models.CharField(max_length=191)
    customer_name = models.CharField(max_length=191)
    customer_ref_number = models.CharField(max_length=191)
    collection_amount = models.DecimalField(max_digits=16, decimal_places=2)
    maximum_amount = models.DecimalField(max_digits=16, decimal_places=2)
    is_recurring = models.CharField(max_length=191)
    frequency = models.CharField(max_length=191)
    first_collection_date = models.DateField()
    final_collection_date = models.DateField()
    source_type = models.CharField(max_length=191)
    source_id = models.IntegerField()
    mandate_id = models.CharField(max_length=191)
    status = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digio_e_nach_details'


class DigioEsignResponses(models.Model):
    digio_esign_responses_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    digio_document_id = models.CharField(max_length=191, blank=True, null=True)
    is_agreement = models.CharField(max_length=191, blank=True, null=True)
    agreement_type = models.CharField(max_length=191, blank=True, null=True)
    agreement_status = models.CharField(max_length=191, blank=True, null=True)
    file_name = models.CharField(max_length=191, blank=True, null=True)
    esign_request_created_at = models.CharField(max_length=191, blank=True, null=True)
    self_signed = models.CharField(max_length=191, blank=True, null=True)
    self_sign_type = models.CharField(max_length=250, blank=True, null=True)
    no_of_pages = models.CharField(max_length=191, blank=True, null=True)
    signing_parties_name = models.CharField(max_length=191, blank=True, null=True)
    signing_parties_status = models.CharField(max_length=191, blank=True, null=True)
    signing_parties_type = models.CharField(max_length=191, blank=True, null=True)
    signing_parties_signature_type = models.CharField(max_length=191, blank=True, null=True)
    signing_parites_identifier = models.CharField(max_length=191, blank=True, null=True)
    signing_parties_reason = models.CharField(max_length=191, blank=True, null=True)
    signing_parties_expire_on = models.CharField(max_length=191, blank=True, null=True)
    sign_request_details_name = models.CharField(max_length=191, blank=True, null=True)
    sign_request_details_requested_on = models.CharField(max_length=191, blank=True, null=True)
    sign_request_details_expire_on = models.CharField(max_length=191, blank=True, null=True)
    sign_request_details_identifier = models.CharField(max_length=191, blank=True, null=True)
    sign_request_details_requester_type = models.CharField(max_length=191, blank=True, null=True)
    channel = models.CharField(max_length=191, blank=True, null=True)
    txn_id = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digio_esign_responses'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DocumentProofFiles(models.Model):
    document_proof_files_id = models.AutoField(primary_key=True)
    files_id = models.IntegerField()
    source_table = models.CharField(max_length=191, blank=True, null=True)
    source_table_id = models.IntegerField(blank=True, null=True)
    mob_master_id = models.IntegerField(blank=True, null=True)
    address_proof_types_id = models.IntegerField(blank=True, null=True)
    document_side = models.CharField(max_length=10, blank=True, null=True)
    business_registration_proof_types_id = models.IntegerField(blank=True, null=True)
    id_proof_number = models.CharField(max_length=200, blank=True, null=True)
    id_proof_expiry_date = models.DateTimeField(blank=True, null=True)
    additional_details = models.TextField(blank=True, null=True)
    address_types_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_document_verified = models.IntegerField()
    admin_users_id = models.IntegerField(blank=True, null=True)
    verified_date = models.DateField(blank=True, null=True)
    share_code = models.CharField(max_length=200, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    company_proof_document_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document_proof_files'


class DocumentProofFilesReuploads(models.Model):
    document_proof_files_reuploads_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    admin_users_id = models.IntegerField(blank=True, null=True)
    address_proof_types_id = models.IntegerField(blank=True, null=True)
    document_name = models.CharField(max_length=100, blank=True, null=True)
    document_side = models.CharField(max_length=10, blank=True, null=True)
    source_table = models.CharField(max_length=100, blank=True, null=True)
    source_table_id = models.IntegerField(blank=True, null=True)
    is_uploaded = models.IntegerField()
    uploaded_on = models.DateTimeField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    old_document_proof_files_id = models.IntegerField(blank=True, null=True)
    new_document_proof_files_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document_proof_files_reuploads'


class DynamicVpaBlacklists(models.Model):
    dynamic_vpa_blacklists_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    vpa = models.CharField(unique=True, max_length=100)
    is_blacklisted = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dynamic_vpa_blacklists'


class EcwidStoresDetails(models.Model):
    ecwid_stores_details_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    store_id = models.CharField(max_length=15)
    channel_id = models.CharField(max_length=255)
    store_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    suspended = models.CharField(max_length=255)
    registered = models.CharField(max_length=255)
    plan_name = models.CharField(max_length=255)
    period_in_months = models.CharField(max_length=255)
    profile_id = models.CharField(max_length=255)
    pay_date_previous = models.CharField(max_length=255)
    pay_date_next = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    request_for_unsubs = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecwid_stores_details'


class EcwidSubscriptionPayments(models.Model):
    ecwid_subscription_payments_id = models.AutoField(primary_key=True)
    ecwid_subscriptions_id = models.PositiveIntegerField(blank=True, null=True)
    accounts_id = models.PositiveIntegerField(blank=True, null=True)
    companies_id = models.PositiveIntegerField(blank=True, null=True)
    users_id = models.PositiveIntegerField(blank=True, null=True)
    store_id = models.PositiveIntegerField(blank=True, null=True)
    subscription_type = models.CharField(max_length=20, blank=True, null=True)
    payment_token = models.CharField(max_length=255, blank=True, null=True)
    payment_ref_num = models.CharField(max_length=255, blank=True, null=True)
    amount = models.CharField(max_length=100, blank=True, null=True)
    billing = models.CharField(max_length=50, blank=True, null=True)
    plan_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecwid_subscription_payments'


class EcwidSubscriptions(models.Model):
    ecwid_subscriptions_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    plan_name = models.CharField(max_length=255)
    subscription_requested_on = models.CharField(max_length=255)
    ecwid_subscription_expiry = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecwid_subscriptions'


class Ecwids(models.Model):
    ecwids_id = models.AutoField(primary_key=True)
    users_id = models.PositiveIntegerField()
    accounts_id = models.PositiveIntegerField()
    companies_id = models.PositiveIntegerField()
    store_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecwids'


class EmailLoggers(models.Model):
    email_loggers_id = models.AutoField(primary_key=True)
    to_email = models.CharField(max_length=191)
    from_email = models.CharField(max_length=191, blank=True, null=True)
    aws_response = models.TextField(blank=True, null=True)
    aws_response_status = models.TextField(blank=True, null=True)
    email_subject = models.TextField()
    message_id = models.CharField(max_length=200)
    is_bounced = models.IntegerField()
    is_complaint = models.IntegerField()
    is_delivered = models.IntegerField()
    description = models.TextField()
    bounce_type = models.TextField(blank=True, null=True)
    bounce_sub_type = models.TextField(blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)
    is_picked = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_loggers'


class EmailTemplates(models.Model):
    email_templates_id = models.AutoField(primary_key=True)
    reference_id = models.PositiveIntegerField()
    email_template = models.TextField(db_collation='utf8mb4_unicode_ci')
    subject = models.TextField(db_collation='utf8mb4_unicode_ci')
    template_name = models.CharField(max_length=191, blank=True, null=True)
    template_code = models.CharField(unique=True, max_length=191, blank=True, null=True)
    platform = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_templates'


class EmailVerificationHistories(models.Model):
    email_verification_histories_id = models.BigAutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=191, blank=True, null=True)
    verification_status = models.CharField(max_length=191, blank=True, null=True)
    never_bounce_status = models.CharField(max_length=199, blank=True, null=True)
    email_verification_statuses_id = models.IntegerField(blank=True, null=True)
    email_verification_providers_id = models.IntegerField(blank=True, null=True)
    attempts = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_verification_histories'


class EmailVerificationProviders(models.Model):
    email_verification_providers_id = models.AutoField(primary_key=True)
    provider_name = models.CharField(max_length=191)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_verification_providers'


class EmailVerificationStatuses(models.Model):
    email_verification_statuses_id = models.AutoField(primary_key=True)
    email_verification_statuses = models.CharField(max_length=191)
    description = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_verification_statuses'


class EmandateStatuses(models.Model):
    emandate_statuses_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emandate_statuses'


class EmployeeBankAccounts(models.Model):
    employee_bank_accounts_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    team_member_details_id = models.IntegerField()
    bank_account_number = models.CharField(max_length=200)
    bank_ifsc_code = models.CharField(max_length=50)
    account_holder_name = models.CharField(max_length=200)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_bank_accounts'


class EmployeeExpenseReports(models.Model):
    employee_expense_reports_id = models.AutoField(primary_key=True)
    reports_id = models.IntegerField()
    employee_expenses_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_expense_reports'


class EmployeeExpenses(models.Model):
    employee_expenses_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    card_details_id = models.IntegerField(blank=True, null=True)
    team_member_details_id = models.IntegerField(blank=True, null=True)
    masked_card_number = models.CharField(max_length=200, blank=True, null=True)
    transaction_ref_no = models.CharField(max_length=200)
    l2_categories_id = models.IntegerField()
    l3_categories_id = models.IntegerField()
    transaction_date = models.DateTimeField()
    merchant_name = models.CharField(max_length=200, blank=True, null=True)
    expense_statuses_id = models.IntegerField()
    transaction_mode = models.CharField(max_length=2)
    transaction_type = models.CharField(max_length=4)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    is_reimbursable = models.IntegerField()
    requests_id = models.IntegerField(blank=True, null=True)
    mcc_id = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_expenses'


class EmployeeReportSettings(models.Model):
    employee_report_settings_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    report_prefix = models.CharField(max_length=150)
    sequence_number_initial_value = models.CharField(max_length=150)
    is_report_sequence_id_updated = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_report_settings'


class EmployeeSequenceIds(models.Model):
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    employee_sequence_id = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_sequence_ids'


class EmployeeSettings(models.Model):
    employee_settings_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    employee_prefix = models.CharField(max_length=100)
    sequence_number_initial_value = models.CharField(max_length=100)
    is_employee_sequence_id_updated = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_settings'


class EnachIciciFileTransactions(models.Model):
    enach_icici_file_transactions_id = models.AutoField(primary_key=True)
    npci_mandate_registrations_id = models.IntegerField()
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    payment_date = models.CharField(max_length=255)
    umrn = models.CharField(max_length=200, blank=True, null=True)
    response_reason_code = models.IntegerField(blank=True, null=True)
    debit_account_no = models.CharField(max_length=255)
    recipient_name = models.CharField(max_length=255)
    ifsc_code = models.CharField(max_length=255)
    beneficiary_account_no = models.CharField(max_length=255)
    bank_transaction_status_code = models.CharField(max_length=255, blank=True, null=True)
    consumer_ref_num = models.CharField(max_length=255, blank=True, null=True)
    utr_no = models.CharField(max_length=255, blank=True, null=True)
    response_date = models.CharField(max_length=255, blank=True, null=True)
    request_file_path = models.TextField(blank=True, null=True)
    response_file_path = models.TextField(blank=True, null=True)
    is_processed = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enach_icici_file_transactions'


class EnachMandateStatuses(models.Model):
    enach_mandate_statuses_id = models.BigAutoField(primary_key=True)
    mandate_ref_num = models.CharField(max_length=255, blank=True, null=True)
    consumer_ref_num = models.CharField(max_length=255, blank=True, null=True)
    accepted = models.IntegerField(blank=True, null=True)
    accpted_reference_no = models.CharField(max_length=255, blank=True, null=True)
    reject_reason_code = models.CharField(max_length=255, blank=True, null=True)
    reject_reason_description = models.CharField(max_length=255, blank=True, null=True)
    umrn = models.CharField(max_length=255, blank=True, null=True)
    rejected_by = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enach_mandate_statuses'


class EnterpriseDynamicVpaGenerations(models.Model):
    enterprise_dynamic_vpa_generations_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    vpa = models.CharField(max_length=100, blank=True, null=True)
    vpa_type = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enterprise_dynamic_vpa_generations'


class EnterpriseMerchantResponseUrls(models.Model):
    enterprise_merchant_response_urls_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    webhook_url = models.TextField()
    redirect_url = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enterprise_merchant_response_urls'


class EnterprisePennydropFloaterUpdations(models.Model):
    enterprise_pennydrop_floater_updations_id = models.BigAutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    invoices_id = models.IntegerField(unique=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enterprise_pennydrop_floater_updations'


class EnterprisePgCheckoutWebhookPushes(models.Model):
    enterprise_pg_checkout_webhook_pushes_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    txn_status = models.CharField(max_length=191, blank=True, null=True)
    txn_status_message = models.CharField(max_length=191, blank=True, null=True)
    pg_merchant_ref_id = models.CharField(max_length=191, blank=True, null=True)
    customer_name = models.CharField(max_length=191, blank=True, null=True)
    customer_mob_num = models.CharField(max_length=191, blank=True, null=True)
    customer_email = models.CharField(max_length=191, blank=True, null=True)
    currency = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    source_type = models.CharField(max_length=191, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    event_source = models.CharField(max_length=191, blank=True, null=True)
    event_types_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enterprise_pg_checkout_webhook_pushes'


class EnterprisePgTransactionStatuses(models.Model):
    enterprise_pg_transaction_statuses_id = models.AutoField(primary_key=True)
    enterprise_pg_transaction_status = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enterprise_pg_transaction_statuses'


class EnterpriseVaPaymentStatementMails(models.Model):
    enterprise_va_payment_statement_mails_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    url = models.TextField(blank=True, null=True)
    email_id = models.CharField(max_length=191)
    email_loggers_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    mail_type = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enterprise_va_payment_statement_mails'


class EnterpriseVaPaymentsWebhookPushes(models.Model):
    enterprise_va_payments_webhook_pushes_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    virtual_accounts_id = models.IntegerField(blank=True, null=True)
    virtual_account_number = models.CharField(max_length=191, blank=True, null=True)
    virtual_account_ifsc_code = models.CharField(max_length=191, blank=True, null=True)
    vpa = models.CharField(max_length=191, blank=True, null=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    primary_contact = models.CharField(max_length=191, blank=True, null=True)
    email_id = models.CharField(max_length=191, blank=True, null=True)
    landline_number = models.CharField(max_length=191, blank=True, null=True)
    mobile_number = models.CharField(max_length=191, blank=True, null=True)
    event_source = models.CharField(max_length=191, blank=True, null=True)
    event_types_id = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    bank_ref_id = models.CharField(max_length=191, blank=True, null=True)
    payment_date = models.CharField(max_length=191, blank=True, null=True)
    payment_mode = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enterprise_va_payments_webhook_pushes'


class EnterpriseWebhookPushes(models.Model):
    enterprise_webhook_pushes_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    hash = models.TextField()
    request = models.TextField()
    response_code = models.CharField(max_length=50)
    response_body = models.TextField()
    webhook_push_attempt = models.IntegerField()
    event_source = models.CharField(max_length=191, blank=True, null=True)
    event_types_id = models.IntegerField(blank=True, null=True)
    source_type = models.CharField(max_length=191, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enterprise_webhook_pushes'


class EquitasConnectedAccountLeads(models.Model):
    equitas_connected_account_lead_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    customer_lead_id = models.CharField(max_length=191)
    entity_lead_id = models.CharField(max_length=191, blank=True, null=True)
    account_lead_id = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equitas_connected_account_leads'


class EquitasConnectedAccounts(models.Model):
    equitas_connected_accounts_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    customer_id = models.CharField(max_length=200, blank=True, null=True)
    bank_account_number = models.CharField(max_length=200, blank=True, null=True)
    bank_connection_statuses_id = models.IntegerField()
    is_user_notified = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equitas_connected_accounts'


class EquitasConnectedBranchLists(models.Model):
    equitas_connected_branch_lists_id = models.AutoField(primary_key=True)
    premises_id = models.CharField(max_length=191)
    branch_id = models.CharField(max_length=191)
    ifsc = models.CharField(max_length=191)
    zone = models.CharField(max_length=191)
    state = models.CharField(max_length=191)
    district = models.CharField(max_length=191)
    rbi_centre = models.CharField(max_length=191)
    branch_type = models.CharField(max_length=191)
    branch_name = models.CharField(max_length=191)
    region = models.CharField(max_length=191)
    cluster = models.CharField(max_length=191)
    pin_code = models.CharField(max_length=191)
    address = models.TextField()
    active = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equitas_connected_branch_lists'


class EquitasConnectedCustomerAccountSummaries(models.Model):
    equitas_connected_customer_account_summaries_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    account_number = models.CharField(max_length=191)
    product = models.CharField(max_length=191)
    account_status = models.IntegerField()
    account_status_description = models.CharField(max_length=191, blank=True, null=True)
    interest_available = models.DecimalField(max_digits=14, decimal_places=2)
    available_balance = models.DecimalField(max_digits=14, decimal_places=2)
    currency = models.CharField(max_length=191, blank=True, null=True)
    average_balance_required = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    account_title = models.CharField(max_length=191, blank=True, null=True)
    email_address = models.CharField(max_length=191, blank=True, null=True)
    customer_company_name = models.CharField(max_length=191)
    mobile_number = models.CharField(max_length=191, blank=True, null=True)
    customer_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equitas_connected_customer_account_summaries'


class EquitasConnectedCustomerAccountsDetails(models.Model):
    equitas_connected_customer_accounts_details_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    customer_id = models.IntegerField()
    account_type = models.CharField(max_length=191)
    account_opening_date = models.CharField(max_length=191)
    account_number = models.CharField(max_length=191)
    customer_relationship = models.CharField(max_length=191)
    account_mobile_no = models.CharField(max_length=191, blank=True, null=True)
    account_email_id = models.CharField(max_length=191, blank=True, null=True)
    depcdnb = models.CharField(db_column='depCdNb', max_length=191, blank=True, null=True)  # Field name made lowercase.
    product_name = models.CharField(max_length=191, blank=True, null=True)
    currency_short_name = models.CharField(max_length=191, blank=True, null=True)
    relation_date = models.DateField(blank=True, null=True)
    value_date = models.CharField(max_length=191, blank=True, null=True)
    external_account_id = models.IntegerField(blank=True, null=True)
    model_code = models.CharField(max_length=191, blank=True, null=True)
    self_deposit_bx_id = models.IntegerField(blank=True, null=True)
    loan_application_number = models.IntegerField(blank=True, null=True)
    current_status = models.IntegerField(blank=True, null=True)
    currency_code = models.IntegerField(blank=True, null=True)
    available_balance = models.CharField(max_length=191)
    orignal_balance = models.CharField(max_length=191)
    reason = models.CharField(max_length=191)
    branch_id = models.CharField(max_length=191)
    branch_name = models.CharField(max_length=191)
    classification = models.CharField(max_length=191)
    current_status_desc = models.CharField(max_length=191)
    transaction_in_month = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equitas_connected_customer_accounts_details'


class EquitasConnectedCustomerDetails(models.Model):
    equitas_connected_customer_details_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    customer_name = models.CharField(max_length=191)
    customer_id = models.IntegerField()
    dob = models.CharField(max_length=191, blank=True, null=True)
    gender = models.CharField(max_length=191, blank=True, null=True)
    mobile_no = models.CharField(max_length=191, blank=True, null=True)
    email_id = models.CharField(max_length=191, blank=True, null=True)
    aadhar_no = models.CharField(max_length=191, blank=True, null=True)
    income_tax_no = models.CharField(max_length=191, blank=True, null=True)
    income_type_desc = models.CharField(max_length=191, blank=True, null=True)
    addres_line1 = models.CharField(max_length=191, blank=True, null=True)
    addres_line2 = models.CharField(max_length=191, blank=True, null=True)
    addres_line3 = models.CharField(max_length=191, blank=True, null=True)
    city = models.CharField(max_length=191, blank=True, null=True)
    country_sub_division = models.CharField(max_length=191, blank=True, null=True)
    country = models.CharField(max_length=191, blank=True, null=True)
    pincode = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equitas_connected_customer_details'


class EquitasConnectedCustomerLeadStatuses(models.Model):
    equitas_connected_customer_lead_statuses_id = models.AutoField(primary_key=True)
    account_lead_id = models.CharField(max_length=191)
    process_name = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    user_id = models.CharField(max_length=191)
    completed_by = models.CharField(max_length=191, blank=True, null=True)
    completed_on = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.CharField(max_length=191, blank=True, null=True)
    sub_id = models.CharField(max_length=191, blank=True, null=True)
    exit_state = models.CharField(max_length=191)
    exit_type = models.CharField(max_length=191)
    user_group = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equitas_connected_customer_lead_statuses'


class EquitasConnectedCustomerLeads(models.Model):
    equitas_connected_customer_lead_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    mob_stakeholder_details_id = models.IntegerField()
    first_name = models.CharField(max_length=191)
    last_name = models.CharField(max_length=191)
    mother_maiden_name = models.CharField(max_length=191, blank=True, null=True)
    phone_number = models.CharField(max_length=191)
    identity_type = models.CharField(db_column='identity_Type', max_length=191, blank=True, null=True)  # Field name made lowercase.
    dob = models.CharField(max_length=191, blank=True, null=True)
    aadhar = models.CharField(max_length=191, blank=True, null=True)
    middle_name = models.CharField(max_length=191, blank=True, null=True)
    pancard = models.CharField(max_length=191, blank=True, null=True)
    title = models.CharField(max_length=191)
    account_type = models.CharField(max_length=191)
    account_number = models.CharField(max_length=191, blank=True, null=True)
    customer_lead_id = models.CharField(max_length=191, blank=True, null=True)
    entity_lead_id = models.CharField(max_length=191, blank=True, null=True)
    is_customer_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equitas_connected_customer_leads'


class EquitasConnectedDocumentMappings(models.Model):
    equitas_connected_document_mapping_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    customer_lead_id = models.IntegerField()
    document_ref_no = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equitas_connected_document_mappings'


class EquitasConnectedEntityLeads(models.Model):
    equitas_connected_entity_lead_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    company_name = models.CharField(max_length=191)
    phone_number = models.CharField(max_length=191)
    date_of_incorporation = models.DateField()
    pancard = models.CharField(max_length=191)
    cin_number = models.CharField(max_length=191, blank=True, null=True)
    cst_number = models.CharField(max_length=191, blank=True, null=True)
    gst_number = models.CharField(max_length=191, blank=True, null=True)
    tan_number = models.CharField(max_length=191, blank=True, null=True)
    account_type = models.CharField(max_length=191)
    account_number = models.CharField(max_length=191, blank=True, null=True)
    entity_lead_id = models.CharField(max_length=191)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equitas_connected_entity_leads'


class EquitasConnectedLeadStatusHistories(models.Model):
    equitas_connected_lead_status_histories_id = models.AutoField(primary_key=True)
    equitas_connected_leads_id = models.IntegerField()
    equitas_connected_lead_statuses_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equitas_connected_lead_status_histories'


class EquitasConnectedLeadStatuses(models.Model):
    equitas_connected_lead_statuses_id = models.AutoField(primary_key=True)
    lead_status_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equitas_connected_lead_statuses'


class EquitasConnectedLeads(models.Model):
    equitas_connected_leads_id = models.AutoField(primary_key=True)
    connected_banking_leads_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    equitas_connected_lead_statuses_id = models.IntegerField(blank=True, null=True)
    is_success = models.IntegerField()
    api_error_message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equitas_connected_leads'


class EquitasConnectedStatements(models.Model):
    equitas_connected_statements_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    balance = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=191, blank=True, null=True)
    account_number = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    opening_balance = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    closing_balance = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    transaction_mode = models.CharField(max_length=191, blank=True, null=True)
    transaction_id = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    api_status = models.CharField(max_length=191, blank=True, null=True)
    date = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equitas_connected_statements'


class EquitasConnectedUploadDocuments(models.Model):
    equitas_connected_upload_documents_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    customer_lead_id = models.IntegerField()
    document_ref_no = models.IntegerField()
    document_name = models.CharField(max_length=191)
    document_type = models.IntegerField()
    category_code = models.IntegerField()
    sub_category_code = models.IntegerField()
    assigned_doc_status = models.IntegerField()
    additional_doc_details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equitas_connected_upload_documents'


class EquitasDocCategoryTypes(models.Model):
    equitas_doc_category_types_id = models.IntegerField()
    doc_category_desc = models.CharField(max_length=100)
    mob_business_types_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equitas_doc_category_types'


class EquitasDocSubcategoryTypes(models.Model):
    equitas_doc_subcategory_types_id = models.IntegerField()
    doc_subcategory_desc = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'equitas_doc_subcategory_types'


class EquitasDocTypes(models.Model):
    equitas_doc_types_id = models.AutoField(primary_key=True)
    doc_list_code = models.IntegerField()
    doc_type_desc = models.CharField(max_length=100)
    equitas_doc_subcategory_types_id = models.IntegerField()
    address_proof_id = models.IntegerField()
    equitas_doc_category_types_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'equitas_doc_types'


class EquitasFundTransfers(models.Model):
    equitas_fund_transfers_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    internal_transaction_ref_id = models.CharField(max_length=191, blank=True, null=True)
    debtor_name = models.CharField(max_length=191, blank=True, null=True)
    debit_account = models.CharField(max_length=191, blank=True, null=True)
    creditor_name = models.CharField(max_length=191, blank=True, null=True)
    credit_account = models.CharField(max_length=191, blank=True, null=True)
    ifsc_code = models.CharField(max_length=191, blank=True, null=True)
    amount = models.CharField(max_length=191, blank=True, null=True)
    transfer_mode = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.CharField(max_length=191, blank=True, null=True)
    bank_transaction_status_id = models.IntegerField(blank=True, null=True)
    external_fund_transfers_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    bank_error_code = models.CharField(max_length=191, blank=True, null=True)
    bank_error_message = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equitas_fund_transfers'


class EquitasNriCustomerDetails(models.Model):
    equitas_nri_customer_details_id = models.AutoField(primary_key=True)
    equitas_nri_savings_account_leads_id = models.IntegerField(blank=True, null=True)
    customer_lead_id = models.IntegerField(blank=True, null=True)
    customer_photo = models.CharField(max_length=160, blank=True, null=True)
    customer_signature = models.CharField(max_length=160, blank=True, null=True)
    passport_front = models.CharField(max_length=160, blank=True, null=True)
    passport_back = models.CharField(max_length=160, blank=True, null=True)
    passport_extra = models.CharField(max_length=160, blank=True, null=True)
    visa_front = models.CharField(max_length=160, blank=True, null=True)
    visa_back = models.CharField(max_length=160, blank=True, null=True)
    utility_bill_original = models.CharField(max_length=160, blank=True, null=True)
    communication_address_proof_types_id = models.CharField(max_length=160, blank=True, null=True)
    communication_address_proof_front = models.CharField(max_length=160, blank=True, null=True)
    communication_address_proof_back = models.CharField(max_length=160, blank=True, null=True)
    pio_proof = models.CharField(max_length=60, blank=True, null=True)
    first_name = models.CharField(max_length=160, blank=True, null=True)
    middle_name = models.CharField(max_length=160, blank=True, null=True)
    last_name = models.CharField(max_length=160, blank=True, null=True)
    mothers_maiden_name = models.CharField(max_length=160, blank=True, null=True)
    fathers_name = models.CharField(max_length=160, blank=True, null=True)
    is_minor = models.CharField(max_length=160, blank=True, null=True)
    mobile_number = models.CharField(max_length=160, blank=True, null=True)
    dob = models.CharField(max_length=160, blank=True, null=True)
    aadhaar_number = models.CharField(max_length=160, blank=True, null=True)
    pan_number = models.CharField(max_length=160, blank=True, null=True)
    title = models.CharField(max_length=160, blank=True, null=True)
    gender = models.CharField(max_length=160, blank=True, null=True)
    passport_number = models.CharField(max_length=160, blank=True, null=True)
    passport_issuing_country = models.CharField(max_length=160, blank=True, null=True)
    passport_date_of_issue = models.CharField(max_length=160, blank=True, null=True)
    passport_place_of_issue = models.CharField(max_length=160, blank=True, null=True)
    visa_type = models.CharField(max_length=160, blank=True, null=True)
    visa_place_of_issue = models.CharField(max_length=160, blank=True, null=True)
    visa_issue_date = models.CharField(max_length=160, blank=True, null=True)
    visa_expiry_date = models.CharField(max_length=160, blank=True, null=True)
    oci_card_number = models.CharField(max_length=160, blank=True, null=True)
    oci_date_of_issue = models.CharField(max_length=160, blank=True, null=True)
    oci_place_of_issue = models.CharField(max_length=160, blank=True, null=True)
    customer_status = models.CharField(max_length=160, blank=True, null=True)
    martial_status = models.CharField(max_length=160, blank=True, null=True)
    spouse_name = models.CharField(max_length=160, blank=True, null=True)
    us_person = models.CharField(max_length=160, blank=True, null=True)
    us_citizen = models.CharField(max_length=160, blank=True, null=True)
    green_card_holder = models.CharField(max_length=160, blank=True, null=True)
    born_in_usa = models.CharField(max_length=160, blank=True, null=True)
    country_of_residence = models.CharField(max_length=160, blank=True, null=True)
    nationality = models.CharField(max_length=160, blank=True, null=True)
    indian_address = models.TextField(blank=True, null=True)
    indian_city = models.CharField(max_length=160, blank=True, null=True)
    indian_state = models.CharField(max_length=160, blank=True, null=True)
    indian_country = models.CharField(max_length=160, blank=True, null=True)
    indian_pin_code = models.CharField(max_length=160, blank=True, null=True)
    indian_mobile_number = models.CharField(max_length=160, blank=True, null=True)
    overseas_address = models.TextField(blank=True, null=True)
    overseas_city = models.CharField(max_length=160, blank=True, null=True)
    overseas_state = models.CharField(max_length=160, blank=True, null=True)
    overseas_country = models.CharField(max_length=160, blank=True, null=True)
    overseas_pin_code = models.CharField(max_length=10, blank=True, null=True)
    overseas_country_code = models.CharField(max_length=10, blank=True, null=True)
    indian_country_code = models.CharField(max_length=10, blank=True, null=True)
    overseas_mobile_number = models.CharField(max_length=160, blank=True, null=True)
    otp_to_be_sent_to = models.CharField(max_length=160, blank=True, null=True)
    email_id = models.CharField(max_length=160, blank=True, null=True)
    purpose_of_account = models.CharField(max_length=160, blank=True, null=True)
    source_of_funds = models.CharField(max_length=160, blank=True, null=True)
    no_of_years_in_foreign_country = models.CharField(max_length=160, blank=True, null=True)
    occupation_type = models.CharField(max_length=160, blank=True, null=True)
    name_of_employer = models.CharField(max_length=160, blank=True, null=True)
    designation = models.CharField(max_length=160, blank=True, null=True)
    self_employed_profession = models.CharField(max_length=160, blank=True, null=True)
    business_since = models.CharField(max_length=160, blank=True, null=True)
    business_date_of_incorporation = models.CharField(max_length=160, blank=True, null=True)
    nature_of_business = models.CharField(max_length=160, blank=True, null=True)
    name_of_company = models.CharField(max_length=160, blank=True, null=True)
    type_of_company = models.CharField(max_length=160, blank=True, null=True)
    name_of_currency = models.CharField(max_length=160, blank=True, null=True)
    annual_family_income = models.CharField(max_length=160, blank=True, null=True)
    held_indian_passport = models.CharField(max_length=160, blank=True, null=True)
    belong_to_indian_teritory = models.CharField(max_length=160, blank=True, null=True)
    citizenship_of_india = models.CharField(max_length=60, blank=True, null=True)
    grand_father_name = models.CharField(max_length=160, blank=True, null=True)
    pio_spouse_name = models.CharField(max_length=160, blank=True, null=True)
    nre_check_book = models.CharField(max_length=10, blank=True, null=True)
    nro_check_book = models.CharField(max_length=10, blank=True, null=True)
    nre_debit_card = models.CharField(max_length=10, blank=True, null=True)
    nro_debit_card = models.CharField(max_length=10, blank=True, null=True)
    pep = models.CharField(max_length=160, blank=True, null=True)
    country_of_tax_residency = models.CharField(max_length=160, blank=True, null=True)
    tax_identification_type = models.CharField(max_length=160, blank=True, null=True)
    pan_application_date = models.CharField(max_length=160, blank=True, null=True)
    pan_acknowledgement_number = models.CharField(max_length=160, blank=True, null=True)
    agricultural_income = models.CharField(max_length=160, blank=True, null=True)
    other_than_agricutural_income = models.CharField(max_length=160, blank=True, null=True)
    passport_date_of_expiry = models.CharField(max_length=160, blank=True, null=True)
    social_security_number = models.CharField(max_length=160, blank=True, null=True)
    wish_to_nominate = models.CharField(max_length=4, blank=True, null=True)
    nomine_name = models.CharField(max_length=160, blank=True, null=True)
    nomine_address = models.TextField(blank=True, null=True)
    nomine_city = models.CharField(max_length=10, blank=True, null=True)
    nomine_pin_code = models.CharField(max_length=10, blank=True, null=True)
    nomine_state = models.CharField(max_length=160, blank=True, null=True)
    nomine_contact_no = models.CharField(max_length=16, blank=True, null=True)
    nomine_dob = models.CharField(max_length=160, blank=True, null=True)
    nomine_relationship = models.CharField(max_length=160, blank=True, null=True)
    correspondence_sent_to = models.CharField(max_length=60, blank=True, null=True)
    type_of_employer = models.CharField(max_length=60, blank=True, null=True)
    sms_alerts_on = models.CharField(max_length=60, blank=True, null=True)
    tin_number = models.CharField(max_length=30, blank=True, null=True)
    received_tin_number = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    guardian_name = models.CharField(max_length=60, blank=True, null=True)
    type_of_guardian = models.CharField(max_length=60, blank=True, null=True)
    guardian_relationship = models.CharField(max_length=20, blank=True, null=True)
    guardian_appointed_date = models.CharField(max_length=20, blank=True, null=True)
    is_nomine_minor = models.CharField(max_length=5, blank=True, null=True)
    nomine_guardian_name = models.CharField(max_length=20, blank=True, null=True)
    nomine_guardian_age = models.CharField(max_length=10, blank=True, null=True)
    nomine_guardian_dob = models.CharField(max_length=20, blank=True, null=True)
    tax_resident_of_other_country = models.CharField(max_length=20, blank=True, null=True)
    applied_for_pan = models.CharField(max_length=20, blank=True, null=True)
    place = models.CharField(max_length=20, blank=True, null=True)
    date = models.CharField(max_length=20, blank=True, null=True)
    original_document_type = models.CharField(max_length=20, blank=True, null=True)
    country_of_birth = models.CharField(max_length=20, blank=True, null=True)
    city_of_birth = models.CharField(max_length=20, blank=True, null=True)
    tax_resident_of_us = models.CharField(max_length=3, blank=True, null=True)
    tin_number_other = models.CharField(max_length=191, blank=True, null=True)
    country_of_tax_residency_other = models.CharField(max_length=191, blank=True, null=True)
    tax_identification_type_other = models.CharField(max_length=191, blank=True, null=True)
    nomine_age = models.IntegerField(blank=True, null=True)
    business_address_proof = models.CharField(max_length=3, blank=True, null=True)
    nomine_country = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equitas_nri_customer_details'


class EquitasNriCustomerDocuments(models.Model):
    equitas_nri_customer_documents_id = models.AutoField(primary_key=True)
    equitas_nri_customer_details_id = models.IntegerField()
    equitas_doc_subcategory_types_id = models.IntegerField()
    equitas_nri_doc_types_id = models.IntegerField()
    document_url = models.CharField(max_length=191)
    document_name = models.CharField(max_length=191)
    document_reference_number = models.IntegerField()
    is_assigned = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equitas_nri_customer_documents'


class EquitasNriLeadStatuses(models.Model):
    equitas_nri_lead_statuses_id = models.AutoField(primary_key=True)
    equitas_nri_lead_status_name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equitas_nri_lead_statuses'


class EquitasNriSavingsAccountLeads(models.Model):
    equitas_nri_savings_account_leads_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=191, blank=True, null=True)
    last_name = models.CharField(max_length=191, blank=True, null=True)
    mothers_maiden_name = models.CharField(max_length=191, blank=True, null=True)
    mobile_number = models.CharField(max_length=191, blank=True, null=True)
    email_id = models.CharField(max_length=160, blank=True, null=True)
    dob = models.CharField(max_length=191, blank=True, null=True)
    middle_name = models.CharField(max_length=191, blank=True, null=True)
    aadhar_number = models.CharField(max_length=191, blank=True, null=True)
    pan_number = models.CharField(max_length=191, blank=True, null=True)
    title = models.CharField(max_length=191, blank=True, null=True)
    account_type = models.CharField(max_length=160, blank=True, null=True)
    mode_of_operation = models.CharField(max_length=160, blank=True, null=True)
    account_variant = models.CharField(max_length=160, blank=True, null=True)
    branch_name = models.CharField(max_length=160, blank=True, null=True)
    branch_code = models.CharField(max_length=160, blank=True, null=True)
    referral_code = models.CharField(max_length=160, blank=True, null=True)
    customer_aof = models.CharField(max_length=160, blank=True, null=True)
    customer_signed_aof = models.CharField(max_length=160, blank=True, null=True)
    customer_lead_id = models.IntegerField(blank=True, null=True)
    account_lead_id = models.IntegerField(blank=True, null=True)
    lead_status_id = models.IntegerField(blank=True, null=True)
    rm_users_id = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.CharField(max_length=191, blank=True, null=True)
    dvu_remarks = models.CharField(max_length=191, blank=True, null=True)
    is_success = models.IntegerField()
    utm_source = models.CharField(max_length=255, blank=True, null=True)
    utm_medium = models.CharField(max_length=255, blank=True, null=True)
    utm_campaign = models.CharField(max_length=255, blank=True, null=True)
    agreed_to_terms_conditions = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equitas_nri_savings_account_leads'


class EquitasSavingsCustomerDetails(models.Model):
    equitas_savings_customer_details_id = models.AutoField(primary_key=True)
    mobile_number = models.CharField(max_length=255, blank=True, null=True)
    pan_card = models.CharField(max_length=255, blank=True, null=True)
    mother_maiden_name = models.CharField(max_length=255, blank=True, null=True)
    fathers_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    city_of_birth = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equitas_savings_customer_details'


class EventDetails(models.Model):
    name = models.CharField(max_length=191)
    description = models.CharField(max_length=191)
    active = models.IntegerField()
    term_and_condition = models.TextField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    cash_allotted = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cash_used = models.DecimalField(max_digits=8, decimal_places=2)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    event_type_id = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    notification_class = models.CharField(max_length=191, blank=True, null=True)
    credit_type_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_details'


class EventTransactions(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    campaign_id = models.PositiveIntegerField(blank=True, null=True)
    event_id = models.PositiveIntegerField(blank=True, null=True)
    users_id = models.PositiveIntegerField(blank=True, null=True)
    accounts_id = models.PositiveIntegerField(blank=True, null=True)
    companies_id = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_transactions'


class EventTypes(models.Model):
    event_types_id = models.AutoField(primary_key=True)
    event_type = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_types'


class ExpenseCategories(models.Model):
    expense_categories_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    category_name = models.CharField(max_length=191, blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expense_categories'


class ExpenseReports(models.Model):
    expense_reports_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    approver_users_id = models.IntegerField()
    report_seq_id = models.CharField(max_length=200)
    report_name = models.CharField(max_length=200)
    total_value = models.DecimalField(max_digits=12, decimal_places=2)
    report_statuses_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expense_reports'


class ExpenseStatuses(models.Model):
    expense_statuses_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=100)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expense_statuses'


class ExpenseTags(models.Model):
    expense_tags_id = models.AutoField(primary_key=True)
    expenses_id = models.IntegerField()
    tags_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expense_tags'


class Expenses(models.Model):
    expenses_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    contacts_id = models.IntegerField()
    categories_id = models.IntegerField(blank=True, null=True)
    invoices_id = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    online_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    offline_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    transaction_id = models.CharField(max_length=191, blank=True, null=True)
    mode_of_payment = models.CharField(max_length=191, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expenses'


class ExternalBankingServiceCalls(models.Model):
    external_banking_service_calls_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    partner_banks_id = models.IntegerField(blank=True, null=True)
    open_bank_accounts_id = models.IntegerField()
    banking_services_id = models.IntegerField(blank=True, null=True)
    last_updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'external_banking_service_calls'


class ExternalFundTransactions(models.Model):
    external_fund_transactions_id = models.AutoField(primary_key=True)
    bank_transaction_details_id = models.IntegerField()
    transaction_types_id = models.IntegerField(blank=True, null=True)
    partner_banks_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField()
    batch_id = models.CharField(max_length=100)
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    bank_transaction_status_id = models.IntegerField()
    external_fund_transfers_id = models.IntegerField()
    internal_transaction_ref_id = models.CharField(max_length=191)
    utr_number = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)
    response_status = models.CharField(max_length=191, blank=True, null=True)
    payment_response_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'external_fund_transactions'


class ExternalFundTransactionsHistory(models.Model):
    external_fund_transaction_histories_id = models.AutoField(primary_key=True)
    external_fund_transactions_id = models.IntegerField()
    bank_transaction_status_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'external_fund_transactions_history'


class ExternalFundTransferTags(models.Model):
    external_fund_transfer_tags_id = models.AutoField(primary_key=True)
    external_fund_transfers_id = models.IntegerField()
    tags_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'external_fund_transfer_tags'


class ExternalFundTransfers(models.Model):
    external_fund_transfers_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    batch_id = models.CharField(max_length=100)
    users_id = models.IntegerField()
    contacts_id = models.IntegerField(blank=True, null=True)
    withdraw_bank_accounts_id = models.IntegerField(blank=True, null=True)
    is_contact = models.IntegerField()
    source_type = models.CharField(max_length=200, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    recepient_name = models.CharField(max_length=191, blank=True, null=True)
    email_id = models.CharField(max_length=191, blank=True, null=True)
    mobile_number = models.CharField(max_length=191, blank=True, null=True)
    partner_banks_id = models.IntegerField(blank=True, null=True)
    link_types_id = models.IntegerField(blank=True, null=True)
    transaction_client_types_id = models.IntegerField(blank=True, null=True)
    open_bank_accounts_id = models.IntegerField(blank=True, null=True)
    debit_account_number = models.CharField(max_length=200, blank=True, null=True)
    beneficiary_account_number = models.CharField(max_length=200, blank=True, null=True)
    beneficiary_ifsc_code = models.CharField(max_length=200, blank=True, null=True)
    client_ip = models.CharField(max_length=45, blank=True, null=True)
    expense_categories_id = models.IntegerField(blank=True, null=True)
    payment_schedules_id = models.IntegerField(blank=True, null=True)
    merchant_ref_id = models.CharField(max_length=250, blank=True, null=True)
    creation_types_id = models.IntegerField(blank=True, null=True)
    l2_categories_id = models.IntegerField(blank=True, null=True)
    l3_categories_id = models.IntegerField(blank=True, null=True)
    repeat_for = models.IntegerField(blank=True, null=True)
    frequencies_id = models.IntegerField(blank=True, null=True)
    payment_count = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    internal_transaction_ref_id = models.CharField(max_length=191)
    bank_transaction_status_id = models.IntegerField()
    api_error_message = models.TextField(blank=True, null=True)
    transaction_types_id = models.IntegerField()
    purpose = models.CharField(max_length=191, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    next_payment_date = models.DateTimeField(blank=True, null=True)
    is_cancelled = models.IntegerField()
    latitude = models.CharField(max_length=191, blank=True, null=True)
    longitude = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    payee_vpa = models.CharField(max_length=191, blank=True, null=True)
    open_payroll_transactions_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'external_fund_transfers'


class ExternalInvoices(models.Model):
    external_invoices_id = models.AutoField(primary_key=True)
    external_webhook_log_id = models.IntegerField()
    invoice_id = models.IntegerField()
    invoice_s3_link = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'external_invoices'


class ExternalPayments(models.Model):
    external_payments_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField(blank=True, null=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    contacts_id = models.IntegerField(blank=True, null=True)
    open_banking_nodal_statements_id = models.IntegerField()
    link_types_id = models.IntegerField(blank=True, null=True)
    partner_banks_id = models.IntegerField(blank=True, null=True)
    transaction_ref_no = models.CharField(max_length=60, blank=True, null=True)
    pg_statuses_id = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    balance_amount_to_be_tagged = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    mode_of_transfer = models.CharField(max_length=200, blank=True, null=True)
    bank_transaction_id = models.CharField(max_length=200, blank=True, null=True)
    source_bank = models.CharField(max_length=200, blank=True, null=True)
    source_bank_account_number = models.CharField(max_length=200, blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'external_payments'


class ExternalPaymentsInvoiceLinks(models.Model):
    external_payments_invoice_links_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    contacts_id = models.IntegerField()
    invoices_id = models.IntegerField()
    external_payments_id = models.IntegerField()
    manual_transactions_id = models.IntegerField()
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'external_payments_invoice_links'


class ExternalServiceDataChanges(models.Model):
    external_service_data_changes_id = models.BigAutoField(primary_key=True)
    source = models.CharField(max_length=191)
    source_id = models.PositiveIntegerField()
    processed = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'external_service_data_changes'


class ExternalSources(models.Model):
    external_sources_id = models.BigAutoField(primary_key=True)
    external_source_name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'external_sources'


class ExternalTransfers(models.Model):
    external_transfers_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField(blank=True, null=True)
    contacts_id = models.IntegerField(blank=True, null=True)
    open_banking_nodal_statements_id = models.IntegerField()
    link_types_id = models.IntegerField()
    partner_banks_id = models.IntegerField(blank=True, null=True)
    ref_no = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    balance_amount_to_be_tagged = models.DecimalField(max_digits=16, decimal_places=2)
    transfer_mode = models.CharField(max_length=250, blank=True, null=True)
    beneficiary_bank = models.CharField(max_length=200, blank=True, null=True)
    beneficiary_bank_account_number = models.CharField(max_length=200, blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'external_transfers'


class ExternalTransfersInvoiceLinks(models.Model):
    external_transfers_invoice_links_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    contacts_id = models.IntegerField()
    invoices_id = models.IntegerField()
    external_transfers_id = models.IntegerField()
    manual_transactions_id = models.IntegerField()
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'external_transfers_invoice_links'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class FaqFiles(models.Model):
    faq_files_id = models.AutoField(primary_key=True)
    faqs_id = models.IntegerField(blank=True, null=True)
    file_url = models.CharField(max_length=191, blank=True, null=True)
    file_extension = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faq_files'


class FaqModules(models.Model):
    faq_modules_id = models.AutoField(primary_key=True)
    module_name = models.CharField(max_length=199)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faq_modules'


class FaqSubModules(models.Model):
    faq_sub_modules_id = models.AutoField(primary_key=True)
    faq_modules_id = models.IntegerField()
    sub_module_name = models.CharField(max_length=199)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faq_sub_modules'


class Faqs(models.Model):
    faqs_id = models.AutoField(primary_key=True)
    keywords = models.CharField(max_length=299)
    faq_modules_id = models.IntegerField()
    faq_sub_modules_id = models.IntegerField(blank=True, null=True)
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    platform = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faqs'


class FeaturePermissionTypes(models.Model):
    feature_permission_types_id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feature_permission_types'


class FeaturePermissions(models.Model):
    feature_permissions_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    feature_permission_types_id = models.IntegerField(blank=True, null=True)
    is_allowed = models.IntegerField(blank=True, null=True)
    admin_users_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feature_permissions'


class FifoTest(models.Model):
    data = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fifo_test'


class Files(models.Model):
    files_id = models.AutoField(primary_key=True)
    url = models.TextField(blank=True, null=True)
    original_file_name = models.CharField(max_length=191, blank=True, null=True)
    mime_type = models.CharField(max_length=250, blank=True, null=True)
    hash = models.CharField(unique=True, max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'files'


class FilesBulk(models.Model):
    files_bulk_id = models.AutoField(primary_key=True)
    users_id = models.PositiveIntegerField()
    accounts_id = models.PositiveIntegerField()
    companies_id = models.IntegerField(blank=True, null=True)
    batch_id = models.CharField(max_length=15)
    files_id = models.IntegerField(unique=True)
    open_bank_accounts_id = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField()
    row_count = models.IntegerField()
    row_count_success = models.IntegerField()
    row_count_failed = models.IntegerField()
    row_count_duplicate = models.IntegerField(blank=True, null=True)
    total_value = models.DecimalField(max_digits=16, decimal_places=2)
    total_value_success = models.DecimalField(max_digits=16, decimal_places=2)
    total_value_failed = models.DecimalField(max_digits=16, decimal_places=2)
    total_value_duplicate = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=191)
    remarks = models.TextField(blank=True, null=True)
    action_type = models.CharField(max_length=20)
    is_processed = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'files_bulk'


class FilesBulkHistories(models.Model):
    files_bulk_histories_id = models.AutoField(primary_key=True)
    files_bulk_id = models.IntegerField()
    batch_id = models.CharField(max_length=15)
    row_count = models.IntegerField()
    row_count_success = models.IntegerField()
    row_count_failed = models.IntegerField()
    total_value = models.DecimalField(max_digits=16, decimal_places=2)
    total_value_success = models.DecimalField(max_digits=16, decimal_places=2)
    total_value_failed = models.DecimalField(max_digits=16, decimal_places=2)
    status = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'files_bulk_histories'


class FlaggedTransactionHistories(models.Model):
    flagged_transaction_histories_id = models.AutoField(primary_key=True)
    source_id = models.IntegerField(blank=True, null=True)
    source_table = models.CharField(max_length=191, blank=True, null=True)
    flagged_transaction_statuses_id = models.IntegerField()
    flagged_date = models.DateTimeField(blank=True, null=True)
    admin_users_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flagged_transaction_histories'


class FlaggedTransactionStatuses(models.Model):
    flagged_transaction_statuses_id = models.IntegerField()
    status_name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flagged_transaction_statuses'


class FlaggedUserAccounts(models.Model):
    flagged_user_accounts_id = models.BigAutoField(primary_key=True)
    flagged_type = models.CharField(max_length=191, blank=True, null=True)
    flagged_value = models.CharField(max_length=191, blank=True, null=True)
    total_count = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=191, blank=True, null=True)
    admin_users_id = models.IntegerField(blank=True, null=True)
    is_flagged = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flagged_user_accounts'


class FosAgencies(models.Model):
    fos_agencies_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fos_agencies'


class FosDigitalKycDetails(models.Model):
    fos_digital_kyc_details_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=191, blank=True, null=True)
    dob = models.CharField(max_length=191, blank=True, null=True)
    gender = models.CharField(max_length=191, blank=True, null=True)
    user_profile_image_id = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=191, blank=True, null=True)
    city = models.CharField(max_length=191, blank=True, null=True)
    state = models.CharField(max_length=191, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    latitude = models.CharField(max_length=191, blank=True, null=True)
    longitude = models.CharField(max_length=191, blank=True, null=True)
    user_document_proof_files_id = models.TextField(blank=True, null=True)
    user_photo_with_kyc_doc_files_id = models.IntegerField(blank=True, null=True)
    mob_business_types_id = models.IntegerField(blank=True, null=True)
    mob_business_document_proof_files_id = models.TextField(blank=True, null=True)
    fos_agent_name = models.CharField(max_length=191, blank=True, null=True)
    fos_agent_id = models.CharField(max_length=191, blank=True, null=True)
    fos_agent_profile_image_id = models.IntegerField(blank=True, null=True)
    refernce_id = models.CharField(max_length=191, blank=True, null=True)
    is_customer_otp_verified = models.IntegerField()
    is_fos_agent_otp_verified = models.IntegerField()
    fos_agent_otp_verified_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fos_digital_kyc_details'


class Frequencies(models.Model):
    frequencies_id = models.AutoField(primary_key=True)
    frequency_name = models.CharField(max_length=191, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frequencies'


class FtCardPgTransactions(models.Model):
    ft_card_pg_transactions_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    amount = models.CharField(max_length=191)
    open_bank_accounts_id = models.CharField(max_length=191)
    open_pg_txn_id = models.CharField(max_length=191)
    payment_gateways_id = models.CharField(max_length=191)
    card_types_id = models.CharField(max_length=191)
    redirect_url = models.CharField(max_length=300)
    pg_txn_status_id = models.CharField(max_length=10)
    pg_txn_time = models.DateTimeField()
    pg_txn_ref_num = models.CharField(max_length=191)
    payment_link_unique_id = models.CharField(max_length=300)
    source_type = models.CharField(max_length=191)
    source_id = models.CharField(max_length=191)
    files_id = models.CharField(max_length=191)
    batch_id = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ft_card_pg_transactions'


class FtCards(models.Model):
    ft_cards_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    card_number = models.TextField(blank=True, null=True)
    masked_card_number = models.CharField(max_length=300, blank=True, null=True)
    expiry_mm = models.TextField(blank=True, null=True)
    expiry_yy = models.TextField(blank=True, null=True)
    name_on_card = models.CharField(max_length=300, blank=True, null=True)
    email_id = models.CharField(max_length=191, blank=True, null=True)
    card_types_id = models.IntegerField()
    transaction_types_id = models.IntegerField()
    partner_banks_id = models.IntegerField()
    mobile = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ft_cards'


class FundTransferBulkIntermediaries(models.Model):
    fund_transfer_bulk_intermediaries_id = models.AutoField(primary_key=True)
    files_bulk_id = models.IntegerField(blank=True, null=True)
    batch_id = models.CharField(max_length=15)
    users_id = models.PositiveIntegerField()
    accounts_id = models.PositiveIntegerField()
    companies_id = models.PositiveIntegerField()
    bank_response = models.TextField()
    partner_banks_id = models.IntegerField(blank=True, null=True)
    transaction_types_id = models.IntegerField(blank=True, null=True)
    contacts_id = models.IntegerField(blank=True, null=True)
    source_type = models.CharField(max_length=200, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    expense_categories_id = models.IntegerField(blank=True, null=True)
    expense_category_name = models.CharField(max_length=200, blank=True, null=True)
    external_fund_transfers_id = models.IntegerField(blank=True, null=True)
    invoices_id = models.IntegerField(blank=True, null=True)
    link_types_id = models.IntegerField(blank=True, null=True)
    debit_account_number = models.CharField(max_length=200, blank=True, null=True)
    recepient_name = models.CharField(max_length=250, blank=True, null=True)
    email_id = models.CharField(max_length=250, blank=True, null=True)
    mobile_number = models.CharField(max_length=30, blank=True, null=True)
    ifsc_code = models.CharField(max_length=20, blank=True, null=True)
    beneficiary_account_number = models.CharField(max_length=40, blank=True, null=True)
    is_complete = models.IntegerField()
    read_status = models.CharField(max_length=10)
    reason = models.TextField(blank=True, null=True)
    purpose = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    is_recurring = models.IntegerField(blank=True, null=True)
    frequencies_id = models.IntegerField(blank=True, null=True)
    repeat_for = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fund_transfer_bulk_intermediaries'


class FundTransferBulkIntermediariesTemps(models.Model):
    fund_transfer_bulk_intermediaries_temps_id = models.AutoField(primary_key=True)
    parent_fund_transfer_bulk_intermediaries_id = models.IntegerField()
    files_bulk_id = models.IntegerField(blank=True, null=True)
    batch_id = models.CharField(max_length=15)
    users_id = models.PositiveIntegerField()
    accounts_id = models.PositiveIntegerField()
    companies_id = models.PositiveIntegerField()
    bank_response = models.TextField()
    partner_banks_id = models.IntegerField(blank=True, null=True)
    transaction_types_id = models.IntegerField(blank=True, null=True)
    contacts_id = models.IntegerField(blank=True, null=True)
    source_type = models.CharField(max_length=200, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    expense_categories_id = models.IntegerField(blank=True, null=True)
    expense_category_name = models.CharField(max_length=200, blank=True, null=True)
    external_fund_transfers_id = models.IntegerField(blank=True, null=True)
    invoices_id = models.IntegerField(blank=True, null=True)
    link_types_id = models.IntegerField(blank=True, null=True)
    debit_account_number = models.CharField(max_length=200, blank=True, null=True)
    recepient_name = models.CharField(max_length=250, blank=True, null=True)
    email_id = models.CharField(max_length=250, blank=True, null=True)
    mobile_number = models.CharField(max_length=30, blank=True, null=True)
    ifsc_code = models.CharField(max_length=20, blank=True, null=True)
    beneficiary_account_number = models.CharField(max_length=40, blank=True, null=True)
    is_complete = models.IntegerField()
    read_status = models.CharField(max_length=10)
    reason = models.TextField(blank=True, null=True)
    purpose = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    is_recurring = models.IntegerField(blank=True, null=True)
    frequencies_id = models.IntegerField(blank=True, null=True)
    repeat_for = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fund_transfer_bulk_intermediaries_temps'


class FundTransferTypes(models.Model):
    fund_transfer_types_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    slug = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fund_transfer_types'


class GlobalPayoutSettings(models.Model):
    global_payout_settings_id = models.AutoField(primary_key=True)
    link_types_id = models.IntegerField()
    is_payout_enabled = models.IntegerField()
    flash_message = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'global_payout_settings'


class GlobalReferralSettings(models.Model):
    global_referral_settings_id = models.AutoField(primary_key=True)
    reward_types_id = models.IntegerField(blank=True, null=True)
    is_global_referral_enabled = models.IntegerField()
    flash_message = models.CharField(max_length=200, blank=True, null=True)
    referral_reward_max_cap = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    referral_daily_reward_max_cap = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    referral_current_daily_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'global_referral_settings'


class GmbAddressStatuses(models.Model):
    gmb_address_statuses_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gmb_address_statuses'


class GmbAddresses(models.Model):
    gmb_addresses_id = models.AutoField(primary_key=True)
    gmb_consents_id = models.PositiveIntegerField(blank=True, null=True)
    accounts_id = models.PositiveIntegerField(blank=True, null=True)
    companies_id = models.PositiveIntegerField(blank=True, null=True)
    users_id = models.PositiveIntegerField(blank=True, null=True)
    gmb_address_statuses_id = models.PositiveIntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    address_line = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    address_proof = models.CharField(max_length=191, blank=True, null=True)
    proof_name = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_residential = models.IntegerField(blank=True, null=True)
    business_description = models.TextField(blank=True, null=True)
    latitude = models.CharField(max_length=181, blank=True, null=True)
    longitude = models.CharField(max_length=181, blank=True, null=True)
    primary_category = models.CharField(max_length=181, blank=True, null=True)
    additional_categories = models.TextField(blank=True, null=True)
    opening_hours = models.TextField(blank=True, null=True)
    gmb_locations_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gmb_addresses'


class GmbConsents(models.Model):
    gmb_consents_id = models.AutoField(primary_key=True)
    users_id = models.PositiveIntegerField(blank=True, null=True)
    accounts_id = models.PositiveIntegerField(blank=True, null=True)
    companies_id = models.PositiveIntegerField(blank=True, null=True)
    access_token = models.TextField(blank=True, null=True)
    refresh_token = models.TextField(blank=True, null=True)
    account_name = models.CharField(max_length=255, blank=True, null=True)
    accounts_response = models.TextField(blank=True, null=True)
    token_expires_at = models.PositiveIntegerField(blank=True, null=True)
    tnc = models.CharField(max_length=50, blank=True, null=True)
    request_edit = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gmb_consents'


class GmbErrorLogs(models.Model):
    gmb_error_logs_id = models.AutoField(primary_key=True)
    accounts_id = models.PositiveIntegerField(blank=True, null=True)
    companies_id = models.PositiveIntegerField(blank=True, null=True)
    users_id = models.PositiveIntegerField(blank=True, null=True)
    error_type_id = models.PositiveIntegerField(blank=True, null=True)
    error_type = models.CharField(max_length=255, blank=True, null=True)
    api = models.CharField(max_length=255, blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gmb_error_logs'


class GmbLocations(models.Model):
    gmb_locations_id = models.AutoField(primary_key=True)
    gmb_consents_id = models.PositiveIntegerField(blank=True, null=True)
    users_id = models.PositiveIntegerField(blank=True, null=True)
    accounts_id = models.PositiveIntegerField(blank=True, null=True)
    companies_id = models.PositiveIntegerField(blank=True, null=True)
    addresses_id = models.PositiveIntegerField(blank=True, null=True)
    request_id = models.CharField(max_length=255, blank=True, null=True)
    location_name = models.CharField(max_length=255, blank=True, null=True)
    primary_category = models.TextField(blank=True, null=True)
    regular_hours = models.TextField(blank=True, null=True)
    lat_lng = models.CharField(max_length=255, blank=True, null=True)
    location_response = models.TextField(blank=True, null=True)
    verify_response = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gmb_locations'


class GmbMedias(models.Model):
    gmb_medias_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    image_name = models.CharField(max_length=255)
    source_url = models.CharField(max_length=255)
    media_formate = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    google_url = models.CharField(max_length=255)
    thumbnail_url = models.CharField(max_length=255)
    create_time = models.CharField(max_length=255)
    dimension_width = models.CharField(max_length=255)
    dimension_height = models.CharField(max_length=255)
    insights = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gmb_medias'


class GspGstReturnFilings(models.Model):
    gsp_gst_return_filing_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    gstin = models.IntegerField()
    is_any_delay = models.CharField(max_length=191)
    is_defaulter = models.CharField(max_length=191)
    filing_frequency = models.CharField(max_length=191)
    financial_year = models.CharField(max_length=191)
    status = models.CharField(max_length=191)
    date_of_filing = models.CharField(max_length=191)
    return_period = models.CharField(max_length=191)
    is_delay = models.CharField(max_length=191)
    valid = models.CharField(max_length=191, blank=True, null=True)
    return_type = models.CharField(max_length=191)
    mode_of_filing = models.CharField(max_length=191)
    app_ref_number = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gsp_gst_return_filings'


class GstAuthenticationAddresses(models.Model):
    gst_authentication_addresses_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    gst_authentication_id = models.IntegerField()
    email = models.CharField(max_length=191, blank=True, null=True)
    address = models.CharField(max_length=191, blank=True, null=True)
    mobile = models.CharField(max_length=191, blank=True, null=True)
    business_nature = models.CharField(max_length=191, blank=True, null=True)
    last_update_address = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gst_authentication_addresses'


class GstAuthenticationLogs(models.Model):
    gst_authentication_logs_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    request = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gst_authentication_logs'


class GstAuthentications(models.Model):
    gst_authentication_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    member_name_by_gsp = models.CharField(max_length=191, blank=True, null=True)
    can_flag = models.CharField(max_length=191, blank=True, null=True)
    primary_bus_contact_info = models.CharField(max_length=191, blank=True, null=True)
    address = models.CharField(max_length=191, blank=True, null=True)
    mobile_no = models.CharField(max_length=191, blank=True, null=True)
    nature_of_business = models.CharField(max_length=191, blank=True, null=True)
    last_update_address = models.CharField(max_length=191, blank=True, null=True)
    trade_name = models.CharField(max_length=191, blank=True, null=True)
    last_updated = models.CharField(max_length=191, blank=True, null=True)
    contacted = models.CharField(max_length=191, blank=True, null=True)
    reg_date_gst = models.CharField(max_length=191, blank=True, null=True)
    state_jurisdiction_code = models.CharField(max_length=191, blank=True, null=True)
    state_jurisdiction = models.CharField(max_length=191, blank=True, null=True)
    central_jurisdiction_code = models.CharField(max_length=191, blank=True, null=True)
    ppr = models.CharField(max_length=191, blank=True, null=True)
    taxpayer_type = models.CharField(max_length=191, blank=True, null=True)
    compliance_rating = models.CharField(max_length=191, blank=True, null=True)
    date_cancellation_reg = models.CharField(max_length=191, blank=True, null=True)
    constitution_business = models.CharField(max_length=191, blank=True, null=True)
    current_status_reg = models.CharField(max_length=191, blank=True, null=True)
    gstin = models.CharField(max_length=191, blank=True, null=True)
    legal_name_business = models.CharField(max_length=191, blank=True, null=True)
    central_jurisdiction = models.CharField(max_length=191, blank=True, null=True)
    nature_business_reg_gst = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gst_authentications'


class GstDataLogs(models.Model):
    gst_data_logs_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField(blank=True, null=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    gstin = models.CharField(max_length=20, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    data_type = models.CharField(max_length=10, blank=True, null=True)
    period = models.DateTimeField(blank=True, null=True)
    action = models.CharField(max_length=10, blank=True, null=True)
    visible_to = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gst_data_logs'


class GstNotices(models.Model):
    gst_notices_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    gstin = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    notice_order_id = models.CharField(max_length=100)
    issued_by = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    date_of_issue = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    application_id = models.IntegerField(blank=True, null=True)
    due_date = models.DateTimeField()
    amount = models.IntegerField()
    is_read = models.CharField(max_length=5)
    document_id = models.IntegerField()
    application_cd = models.CharField(max_length=50, blank=True, null=True)
    application_def_id = models.IntegerField()
    pdf_download_url = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gst_notices'


class GstPayments(models.Model):
    gst_payments_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    recepient_name = models.CharField(max_length=191, blank=True, null=True)
    partner_banks_id = models.IntegerField(blank=True, null=True)
    open_bank_accounts_id = models.IntegerField(blank=True, null=True)
    debit_account_number = models.CharField(max_length=200, blank=True, null=True)
    beneficiary_account_number = models.CharField(max_length=200, blank=True, null=True)
    beneficiary_ifsc_code = models.CharField(max_length=200, blank=True, null=True)
    payment_schedules_id = models.IntegerField()
    link_types_id = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    transaction_types_id = models.IntegerField(blank=True, null=True)
    transaction_client_types_id = models.IntegerField()
    transaction_date = models.DateTimeField(blank=True, null=True)
    internal_transaction_ref_id = models.CharField(max_length=191)
    l2_categories_id = models.IntegerField(blank=True, null=True)
    l3_categories_id = models.IntegerField(blank=True, null=True)
    is_success = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gst_payments'


class GstReturnsHistory(models.Model):
    gst_returns_history_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    gstin = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    return_type = models.CharField(max_length=10)
    financial_year = models.CharField(max_length=10)
    return_period = models.CharField(max_length=10)
    app_ref_number = models.CharField(max_length=50)
    date_of_filing = models.DateTimeField()
    mode_of_filing = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gst_returns_history'


class GstSearchBasisPans(models.Model):
    gst_search_basis_pan_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    email_id = models.CharField(max_length=191, blank=True, null=True)
    application_status = models.CharField(max_length=191, blank=True, null=True)
    moblie_number = models.CharField(max_length=191, blank=True, null=True)
    registration_name = models.CharField(max_length=191, blank=True, null=True)
    gstin_ref_id = models.CharField(max_length=191, blank=True, null=True)
    reg_type = models.CharField(max_length=191, blank=True, null=True)
    auth_status = models.CharField(max_length=191, blank=True, null=True)
    tin_number = models.CharField(max_length=191, blank=True, null=True)
    pan = models.CharField(max_length=191, blank=True, null=True)
    gstin_id = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gst_search_basis_pans'


class GstrFilingLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    companies_id = models.IntegerField(blank=True, null=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    api_name = models.CharField(max_length=200)
    request = models.TextField(blank=True, null=True)
    post_data = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'gstr_filing_log'


class GupshupErrorCodes(models.Model):
    gupshup_error_codes_id = models.AutoField(primary_key=True)
    error_code = models.IntegerField()
    error_description = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gupshup_error_codes'


class GupshupSmsLogs(models.Model):
    gupshup_sms_logs_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    contacts_id = models.IntegerField(blank=True, null=True)
    api_name = models.CharField(max_length=200, blank=True, null=True)
    sms_templates_id = models.IntegerField(blank=True, null=True)
    mobile_number = models.CharField(max_length=100)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    response_status = models.CharField(max_length=100, blank=True, null=True)
    message_id = models.CharField(max_length=100, blank=True, null=True)
    delivery_response = models.TextField(blank=True, null=True)
    delivery_status = models.CharField(max_length=100, blank=True, null=True)
    cause = models.CharField(max_length=100, blank=True, null=True)
    gupshup_error_codes_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    notification_trigger_histories_id = models.IntegerField(blank=True, null=True)
    ack_id = models.CharField(max_length=150, blank=True, null=True)
    retry_limit = models.IntegerField(blank=True, null=True)
    payload = models.TextField(blank=True, null=True)
    cron_retry_limit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gupshup_sms_logs'


class GupshupWhatsappNotifications(models.Model):
    gupshup_whatsapp_notifications_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    api_name = models.CharField(max_length=200, blank=True, null=True)
    whatsapp_templates_id = models.IntegerField(blank=True, null=True)
    mobile_number = models.CharField(max_length=100)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    response_status = models.CharField(max_length=100, blank=True, null=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    msg_id = models.CharField(max_length=100, blank=True, null=True)
    txn_ref_no = models.CharField(max_length=200, blank=True, null=True)
    gupshup_error_codes_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gupshup_whatsapp_notifications'


class GupshupWhatsappWebhookLogs(models.Model):
    gupshup_whatsapp_webhook_logs_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    api_name = models.CharField(max_length=191, blank=True, null=True)
    request = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gupshup_whatsapp_webhook_logs'


class Gurucans(models.Model):
    gurucans_id = models.AutoField(primary_key=True)
    users_id = models.PositiveIntegerField()
    accounts_id = models.PositiveIntegerField()
    companies_id = models.PositiveIntegerField()
    school_name = models.CharField(max_length=250)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gurucans'


class HsnCodes(models.Model):
    hsn_codes_id = models.AutoField(primary_key=True)
    hsn_chapter = models.CharField(max_length=191, blank=True, null=True)
    hsn_description = models.TextField(blank=True, null=True)
    hsn_code = models.CharField(max_length=191, blank=True, null=True)
    hsn_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cess = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    related_import_or_export_code = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hsn_codes'


class HsnDetails(models.Model):
    hsn_details_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=15)
    name = models.TextField()
    comments = models.TextField(blank=True, null=True)
    igst_rate = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hsn_details'


class HubCityProductCounts(models.Model):
    hub_city_product_count_id = models.BigAutoField(primary_key=True)
    city = models.CharField(unique=True, max_length=100)
    products_count = models.BigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hub_city_product_counts'


class HubProductCategories(models.Model):
    hub_product_categories_id = models.AutoField(primary_key=True)
    offering_types_id = models.IntegerField()
    hub_category_name = models.CharField(max_length=191)
    description = models.CharField(max_length=191, blank=True, null=True)
    category_url = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hub_product_categories'


class HubProductEnquiries(models.Model):
    hub_product_enquiries_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    hub_products_id = models.IntegerField()
    hub_seller_profile_id = models.IntegerField()
    buyer_first_name = models.CharField(max_length=191)
    buyer_last_name = models.CharField(max_length=191)
    buyer_email = models.CharField(max_length=191)
    buyer_phone_number = models.CharField(max_length=191)
    buyer_pincode = models.CharField(max_length=191)
    buyer_city = models.CharField(max_length=191)
    order_description = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hub_product_enquiries'


class HubProductSubCategories(models.Model):
    hub_product_sub_categories_id = models.AutoField(primary_key=True)
    hub_product_categories_id = models.IntegerField()
    hub_subcategory_name = models.CharField(max_length=191)
    hub_subcategory_description = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hub_product_sub_categories'


class HubProductTags(models.Model):
    hub_product_tags_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    product_tag_name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hub_product_tags'


class HubProductTagsMappings(models.Model):
    hub_product_tags_mappings_id = models.AutoField(primary_key=True)
    hub_products_id = models.IntegerField()
    hub_product_tags_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hub_product_tags_mappings'


class HubProductVerificationStatuses(models.Model):
    hub_product_verification_status_id = models.AutoField(primary_key=True)
    status_type = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hub_product_verification_statuses'


class HubProducts(models.Model):
    hub_products_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    admin_users_id = models.IntegerField(blank=True, null=True)
    hub_product_categories_id = models.IntegerField()
    hub_product_subcategories_id = models.IntegerField(blank=True, null=True)
    hub_offerings_type_id = models.IntegerField()
    product_title = models.CharField(max_length=191)
    description = models.TextField()
    price = models.FloatField()
    is_product_verified = models.IntegerField()
    is_images_verified = models.IntegerField()
    is_show_price = models.IntegerField(blank=True, null=True)
    list_type = models.CharField(max_length=191)
    product_remark = models.CharField(max_length=191, blank=True, null=True)
    product_url = models.CharField(max_length=191, blank=True, null=True)
    images = models.TextField()
    activated_on = models.DateTimeField()
    hub_product_verification_status_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hub_products'


class HubSellerProfiles(models.Model):
    hub_seller_profiles_id = models.AutoField(primary_key=True)
    users_id = models.PositiveIntegerField()
    accounts_id = models.PositiveIntegerField()
    companies_id = models.PositiveIntegerField()
    first_name = models.CharField(max_length=191, blank=True, null=True)
    last_name = models.CharField(max_length=191, blank=True, null=True)
    company_name = models.CharField(max_length=191, blank=True, null=True)
    email_id = models.CharField(max_length=191, blank=True, null=True)
    mobile_number = models.CharField(max_length=50, blank=True, null=True)
    business_types_id = models.IntegerField(blank=True, null=True)
    launch_year = models.CharField(max_length=100, blank=True, null=True)
    address_line = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=100, blank=True, null=True)
    about_company = models.TextField(blank=True, null=True)
    company_website = models.CharField(max_length=191, blank=True, null=True)
    seller_profile_url = models.CharField(max_length=191, blank=True, null=True)
    is_disabled = models.IntegerField()
    is_deleted = models.IntegerField()
    onboarded_on = models.DateTimeField(blank=True, null=True)
    is_verified_seller = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hub_seller_profiles'


class IciciAccountOpenings(models.Model):
    icici_account_openings_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    business_types_id = models.IntegerField(blank=True, null=True)
    individual_pan_details_id = models.IntegerField(blank=True, null=True)
    mob_business_details_id = models.IntegerField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    stakeholder_details_id = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    message = models.CharField(max_length=191, blank=True, null=True)
    error_code = models.CharField(max_length=191, blank=True, null=True)
    application_no = models.CharField(max_length=191, blank=True, null=True)
    tracker_id = models.CharField(max_length=191, blank=True, null=True)
    lead_status = models.CharField(max_length=191, blank=True, null=True)
    web_url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_account_openings'


class IciciBankingNodalStatements(models.Model):
    icici_banking_nodal_statements_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    source = models.CharField(max_length=191, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    va_number = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ref_no = models.CharField(max_length=191, blank=True, null=True)
    mode = models.CharField(max_length=191, blank=True, null=True)
    transaction_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_banking_nodal_statements'


class IciciCardTransactions(models.Model):
    icici_card_transaction_id = models.BigAutoField(primary_key=True)
    transaction_date = models.DateField()
    mode = models.CharField(max_length=2)
    delivery_channel = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    rrn_number = models.CharField(max_length=200, blank=True, null=True)
    merchant_name = models.CharField(max_length=200, blank=True, null=True)
    merchant_city = models.CharField(max_length=200, blank=True, null=True)
    merchant_state = models.CharField(max_length=200, blank=True, null=True)
    trans_amount = models.FloatField()
    closing_balance = models.FloatField()
    account_number = models.IntegerField(blank=True, null=True)
    dr_card_number = models.IntegerField(blank=True, null=True)
    cr_card_number = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_card_transactions'


class IciciConnectedAccounts(models.Model):
    icici_connected_accounts_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    cid = models.CharField(max_length=200, blank=True, null=True)
    uid = models.CharField(max_length=200, blank=True, null=True)
    alias_id = models.CharField(max_length=191, blank=True, null=True)
    aggr_name = models.CharField(max_length=250, blank=True, null=True)
    aggr_id = models.CharField(max_length=200, blank=True, null=True)
    urn = models.CharField(max_length=200, blank=True, null=True)
    bank_account_number = models.CharField(max_length=200, blank=True, null=True)
    bank_connection_statuses_id = models.IntegerField(blank=True, null=True)
    is_callback_successfull = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_connected_accounts'


class IciciConnectedBankingLeads(models.Model):
    icici_connected_banking_leads_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    company_name = models.CharField(max_length=191, blank=True, null=True)
    contact_person = models.CharField(max_length=191, blank=True, null=True)
    phone_number = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    pincode = models.CharField(max_length=191, blank=True, null=True)
    appoinment_datetime = models.CharField(max_length=191, blank=True, null=True)
    partner_banks_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_connected_banking_leads'


class IciciCurrentAccountOpening(models.Model):
    icici_current_account_opening_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    tracker_id = models.CharField(max_length=191, blank=True, null=True)
    account_type = models.CharField(max_length=191, blank=True, null=True)
    cust_name = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    mobile_number = models.CharField(max_length=191, blank=True, null=True)
    pan_number = models.CharField(max_length=191, blank=True, null=True)
    aadhar = models.CharField(max_length=191, blank=True, null=True)
    gstin = models.CharField(max_length=191, blank=True, null=True)
    iec_code = models.CharField(max_length=191, blank=True, null=True)
    tan_number = models.CharField(max_length=191, blank=True, null=True)
    tin_number = models.CharField(max_length=191, blank=True, null=True)
    vat_number = models.CharField(max_length=191, blank=True, null=True)
    fssai_number = models.CharField(max_length=191, blank=True, null=True)
    cst_number = models.CharField(max_length=191, blank=True, null=True)
    entity_name = models.CharField(max_length=191, blank=True, null=True)
    uam_number = models.CharField(max_length=191, blank=True, null=True)
    prof_tax_number = models.CharField(max_length=191, blank=True, null=True)
    cin_number = models.CharField(max_length=191, blank=True, null=True)
    asbo_number = models.CharField(max_length=191, blank=True, null=True)
    sol_id = models.CharField(max_length=191, blank=True, null=True)
    account_number = models.CharField(max_length=191, blank=True, null=True)
    account_number_status = models.CharField(max_length=191, blank=True, null=True)
    account_status = models.CharField(max_length=191, blank=True, null=True)
    lead_id = models.CharField(max_length=191, blank=True, null=True)
    lead_status = models.CharField(max_length=191, blank=True, null=True)
    is_completed = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_current_account_opening'


class IciciDirectTax281Payments(models.Model):
    icici_direct_tax_281_payments_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    icici_direct_tax_payment_details_id = models.IntegerField(blank=True, null=True)
    bill_id = models.IntegerField(blank=True, null=True)
    journal_entries_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_direct_tax_281_payments'


class IciciDirectTaxPayerDetails(models.Model):
    icici_direct_tax_payer_details_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    corp_user = models.CharField(max_length=191, blank=True, null=True)
    uid = models.CharField(max_length=191, blank=True, null=True)
    api_req_tran_id = models.CharField(max_length=191, blank=True, null=True)
    debit_account = models.CharField(max_length=191, blank=True, null=True)
    debit_bank_code = models.CharField(max_length=191, blank=True, null=True)
    debit_bank_branch_code = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_direct_tax_payer_details'


class IciciDirectTaxPaymentDetails(models.Model):
    icici_direct_tax_payment_details_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    corp_user = models.CharField(max_length=191, blank=True, null=True)
    uid = models.CharField(max_length=50, blank=True, null=True)
    api_req_tran_id = models.CharField(max_length=191, blank=True, null=True)
    major_head = models.CharField(max_length=191, blank=True, null=True)
    pan = models.CharField(max_length=20, blank=True, null=True)
    tan = models.CharField(max_length=30, blank=True, null=True)
    addr_line1 = models.CharField(max_length=191, blank=True, null=True)
    addr_line2 = models.CharField(max_length=191, blank=True, null=True)
    addr_line3 = models.CharField(max_length=191, blank=True, null=True)
    addr_line4 = models.CharField(max_length=191, blank=True, null=True)
    addr_line5 = models.CharField(max_length=191, blank=True, null=True)
    addr_pin = models.CharField(max_length=50, blank=True, null=True)
    addr_state = models.CharField(max_length=50, blank=True, null=True)
    minor_head = models.CharField(max_length=50, blank=True, null=True)
    is_directly_created = models.IntegerField(blank=True, null=True)
    challan_no = models.CharField(max_length=50, blank=True, null=True)
    assess_year = models.CharField(max_length=50, blank=True, null=True)
    nature_payment = models.CharField(max_length=50, blank=True, null=True)
    tds_categories_id = models.IntegerField(blank=True, null=True)
    debit_account = models.CharField(max_length=50, blank=True, null=True)
    debit_bank_code = models.CharField(max_length=50, blank=True, null=True)
    debit_bank_branch_code = models.CharField(max_length=50, blank=True, null=True)
    financial_year = models.CharField(max_length=50, blank=True, null=True)
    income_tax_amt = models.FloatField(blank=True, null=True)
    surcharge_amt = models.FloatField(blank=True, null=True)
    edu_cess_amt = models.FloatField(blank=True, null=True)
    equlztn_levy_amt = models.FloatField(blank=True, null=True)
    interest_amt = models.FloatField(blank=True, null=True)
    other_fee_amt = models.FloatField(blank=True, null=True)
    penalty_amt = models.FloatField(blank=True, null=True)
    penalty_code = models.CharField(max_length=10, blank=True, null=True)
    other_amt = models.FloatField(blank=True, null=True)
    txn_amt = models.FloatField(blank=True, null=True)
    bank_transac_id = models.CharField(max_length=50, blank=True, null=True)
    response_cin = models.CharField(db_column='response_CIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    response_transaction_proc_date = models.CharField(max_length=50, blank=True, null=True)
    response_code = models.CharField(max_length=50, blank=True, null=True)
    response_message = models.CharField(max_length=50, blank=True, null=True)
    response_bank_transaction_id = models.CharField(max_length=50, blank=True, null=True)
    challan_link = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_enterprise = models.IntegerField(blank=True, null=True)
    merchant_ref_id = models.CharField(max_length=191, blank=True, null=True)
    source_type = models.CharField(max_length=200, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_direct_tax_payment_details'


class IciciEcollectStatementHistories(models.Model):
    icici_ecollect_statement_histories_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField(blank=True, null=True)
    customer_code = models.CharField(max_length=191, blank=True, null=True)
    va_number = models.CharField(max_length=191, blank=True, null=True)
    utr = models.CharField(max_length=191, blank=True, null=True)
    customer_ac_number = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    payee_name = models.CharField(max_length=191, blank=True, null=True)
    payee_ac_number = models.CharField(max_length=191, blank=True, null=True)
    payee_bank_ifsc = models.CharField(max_length=191, blank=True, null=True)
    payee_payment_date = models.CharField(max_length=191, blank=True, null=True)
    bank_internal_transaction_number = models.CharField(max_length=191, blank=True, null=True)
    mode = models.CharField(max_length=191, blank=True, null=True)
    success_and_rejected = models.CharField(max_length=191, blank=True, null=True)
    code = models.CharField(max_length=191, blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_ecollect_statement_histories'


class IciciEcollectStatements(models.Model):
    icici_ecollect_statements_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField(blank=True, null=True)
    customer_code = models.CharField(max_length=191, blank=True, null=True)
    va_number = models.CharField(max_length=191, blank=True, null=True)
    utr = models.CharField(max_length=191, blank=True, null=True)
    customer_ac_number = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    payee_name = models.CharField(max_length=191, blank=True, null=True)
    payee_ac_number = models.CharField(max_length=191, blank=True, null=True)
    payee_bank_ifsc = models.CharField(max_length=191, blank=True, null=True)
    payee_payment_date = models.CharField(max_length=191, blank=True, null=True)
    bank_internal_transaction_number = models.CharField(max_length=191, blank=True, null=True)
    mode = models.CharField(max_length=191, blank=True, null=True)
    success_and_rejected = models.CharField(max_length=191, blank=True, null=True)
    code = models.CharField(max_length=191, blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_ecollect_statements'


class IciciFederals(models.Model):
    icici_federal_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_federals'


class IciciFundTransfers(models.Model):
    icici_fund_transfers_id = models.AutoField(primary_key=True)
    cid = models.CharField(max_length=200, blank=True, null=True)
    uid = models.CharField(max_length=200)
    urn = models.CharField(max_length=200, blank=True, null=True)
    account_number = models.CharField(max_length=200, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    is_otp_verification_successful = models.IntegerField(blank=True, null=True)
    bank_transaction_status_id = models.IntegerField(blank=True, null=True)
    balance = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    external_fund_transfers_id = models.IntegerField(blank=True, null=True)
    api_status = models.CharField(max_length=200, blank=True, null=True)
    bank_message = models.TextField(blank=True, null=True)
    req_id = models.CharField(max_length=200, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_fund_transfers'


class IciciInstaOdApplies(models.Model):
    icici_insta_od_applies_id = models.AutoField(primary_key=True)
    icici_insta_od_cib_lops_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    max_offer_amount = models.DecimalField(max_digits=14, decimal_places=2)
    kyc_flag = models.CharField(max_length=191)
    account_no = models.CharField(max_length=191)
    pq_flg = models.CharField(max_length=191)
    adb = models.CharField(max_length=191)
    name = models.CharField(max_length=191)
    email = models.CharField(max_length=191)
    unsecured_exposure = models.CharField(max_length=191)
    spo_flag = models.CharField(max_length=191)
    mobile_no = models.CharField(max_length=191)
    ucc = models.CharField(max_length=191)
    mec_score = models.CharField(max_length=191)
    message = models.CharField(max_length=191)
    url = models.CharField(max_length=191)
    status = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_insta_od_applies'


class IciciInstaOdCibLops(models.Model):
    icici_insta_od_cib_lops_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    cid = models.CharField(max_length=191)
    uid = models.CharField(max_length=191)
    urn = models.CharField(max_length=191)
    account_no = models.CharField(max_length=191)
    dest_prod = models.CharField(max_length=191)
    max_offer_amt = models.DecimalField(max_digits=14, decimal_places=2)
    max_tenure = models.CharField(max_length=191)
    kyc_waiver = models.CharField(max_length=191)
    spo_flag = models.CharField(max_length=191)
    ucc_ucic = models.CharField(max_length=191)
    mec_score = models.CharField(max_length=191)
    adb = models.CharField(max_length=191)
    unsecured_exposure = models.CharField(max_length=191)
    response = models.CharField(max_length=191)
    message = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_insta_od_cib_lops'


class IciciInstaOdGuestLogins(models.Model):
    icici_insta_od_guest_logins_id = models.BigAutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    partner_banks_id = models.IntegerField()
    name = models.CharField(max_length=191)
    email = models.CharField(max_length=191)
    mobile = models.CharField(max_length=191)
    source_flag = models.CharField(max_length=191)
    constitution = models.CharField(max_length=191)
    status = models.IntegerField()
    url = models.TextField()
    account_number = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_insta_od_guest_logins'


class IciciInstaOdOtpLopOffers(models.Model):
    icici_insta_od_otp_lop_offers_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    urn = models.CharField(max_length=191)
    mobile_no = models.CharField(max_length=20)
    is_otp_required = models.CharField(max_length=2)
    product_cd = models.CharField(max_length=191)
    transaction_identifier = models.CharField(unique=True, max_length=191, blank=True, null=True)
    account_no = models.CharField(max_length=191)
    max_offer_amount = models.DecimalField(max_digits=14, decimal_places=2)
    max_tenure = models.CharField(max_length=191)
    processing_fee = models.CharField(max_length=191)
    interest_rate = models.CharField(max_length=191)
    spo_flag = models.CharField(max_length=191)
    dest_prod = models.CharField(max_length=191)
    url = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_insta_od_otp_lop_offers'


class IciciIsurepayStatementHistories(models.Model):
    icici_isurepay_statement_histories_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField(blank=True, null=True)
    mode_of_collection = models.CharField(max_length=191, blank=True, null=True)
    client_code = models.CharField(max_length=191, blank=True, null=True)
    va_number = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    transaction_date = models.CharField(max_length=191, blank=True, null=True)
    i_bank_transaction_id = models.CharField(max_length=191, blank=True, null=True)
    pay_mode = models.CharField(max_length=191, blank=True, null=True)
    i_sure_id = models.CharField(max_length=191, blank=True, null=True)
    micr_code = models.CharField(max_length=191, blank=True, null=True)
    bank_name = models.CharField(max_length=191, blank=True, null=True)
    branch_name = models.CharField(max_length=191, blank=True, null=True)
    instrument_number = models.CharField(max_length=191, blank=True, null=True)
    instrument_date = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    reject_reason = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_isurepay_statement_histories'


class IciciIsurepayStatements(models.Model):
    icici_isurepay_statements_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField(blank=True, null=True)
    client_code = models.CharField(max_length=191, blank=True, null=True)
    va_number = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    transaction_date = models.CharField(max_length=191, blank=True, null=True)
    i_bank_transaction_id = models.CharField(max_length=191, blank=True, null=True)
    pay_mode = models.CharField(max_length=191, blank=True, null=True)
    i_sure_id = models.CharField(max_length=191, blank=True, null=True)
    micr_code = models.CharField(max_length=191, blank=True, null=True)
    bank_name = models.CharField(max_length=191, blank=True, null=True)
    branch_name = models.CharField(max_length=191, blank=True, null=True)
    instrument_number = models.CharField(max_length=191, blank=True, null=True)
    instrument_date = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    reject_reason = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_isurepay_statements'


class IciciNeftTransactionStatusHistories(models.Model):
    icici_neft_transaction_status_histories_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    external_fund_transactions_id = models.IntegerField(blank=True, null=True)
    credit_date = models.CharField(max_length=191, blank=True, null=True)
    utr_number = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    response = models.CharField(max_length=191, blank=True, null=True)
    message = models.CharField(max_length=191, blank=True, null=True)
    errorcode = models.CharField(db_column='ErrorCode', max_length=191, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_neft_transaction_status_histories'


class IciciNeftTransactions(models.Model):
    icici_neft_transactions_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    external_fund_transactions_id = models.IntegerField(blank=True, null=True)
    transaction_types_id = models.IntegerField(blank=True, null=True)
    utr_number = models.IntegerField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_neft_transactions'


class IciciQrCodes(models.Model):
    icici_qr_codes_id = models.AutoField(primary_key=True)
    vpa_series = models.CharField(max_length=191, blank=True, null=True)
    vpa = models.CharField(max_length=191)
    uuid = models.CharField(max_length=191)
    url = models.CharField(max_length=191)
    qr_sticker_url = models.CharField(max_length=191, blank=True, null=True)
    is_printed = models.IntegerField()
    is_linked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    partner_bank_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_qr_codes'


class IciciQrZipfileDetails(models.Model):
    icici_qr_zipfile_details_id = models.AutoField(primary_key=True)
    series_start_value = models.CharField(max_length=191)
    series_end_value = models.CharField(max_length=191)
    type = models.CharField(max_length=191)
    count = models.CharField(max_length=191)
    zip_file_url = models.CharField(max_length=191)
    qr_standee_zip_file_url = models.CharField(max_length=191, blank=True, null=True)
    is_processed = models.IntegerField()
    is_generated = models.IntegerField()
    admin_users_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    partner_bank_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_qr_zipfile_details'


class IciciToKotakInternalTransfers(models.Model):
    icici_to_kotak_internal_transfers_id = models.AutoField(primary_key=True)
    transaction_type = models.CharField(max_length=191, blank=True, null=True)
    transaction_ref_id = models.CharField(max_length=191, blank=True, null=True)
    bene_name = models.CharField(max_length=191, blank=True, null=True)
    bene_code = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    date_of_payment = models.CharField(max_length=191, blank=True, null=True)
    credit_ac_no = models.CharField(max_length=191, blank=True, null=True)
    credit_ac_ifsc = models.CharField(max_length=191, blank=True, null=True)
    debit_ac_no = models.CharField(max_length=191, blank=True, null=True)
    bene_email = models.CharField(max_length=191, blank=True, null=True)
    bene_mobile = models.CharField(max_length=191, blank=True, null=True)
    remitter_ac_no = models.CharField(max_length=191, blank=True, null=True)
    remitter_ac_name = models.CharField(max_length=191, blank=True, null=True)
    narration = models.CharField(max_length=191, blank=True, null=True)
    bank_payment_ref_no = models.CharField(max_length=191, blank=True, null=True)
    processing_remarks = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    rejection_reason = models.CharField(max_length=191, blank=True, null=True)
    customer_ref_number = models.CharField(max_length=191, blank=True, null=True)
    request_file_location = models.CharField(max_length=191, blank=True, null=True)
    response_file_location = models.CharField(max_length=191, blank=True, null=True)
    is_processed = models.IntegerField()
    admin_users_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_to_kotak_internal_transfers'


class IciciUpiCreateMandates(models.Model):
    icici_upi_create_mandates_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    mandate_id = models.CharField(max_length=191, blank=True, null=True)
    contacts_id = models.CharField(max_length=191, blank=True, null=True)
    merchant_name = models.CharField(max_length=191, blank=True, null=True)
    sub_merchant_name = models.CharField(max_length=191, blank=True, null=True)
    payer_va = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    note = models.CharField(max_length=191, blank=True, null=True)
    collect_by_date = models.CharField(max_length=191, blank=True, null=True)
    merchant_tran_id = models.CharField(max_length=191, blank=True, null=True)
    revoke_merchant_tran_id = models.CharField(max_length=191, blank=True, null=True)
    bill_number = models.CharField(max_length=191, blank=True, null=True)
    validity_start_date = models.CharField(max_length=191, blank=True, null=True)
    validity_end_date = models.CharField(max_length=191, blank=True, null=True)
    amount_limit = models.CharField(max_length=191, blank=True, null=True)
    remark = models.CharField(max_length=191, blank=True, null=True)
    request_type = models.CharField(max_length=191, blank=True, null=True)
    frequency = models.CharField(max_length=191, blank=True, null=True)
    debit_day = models.CharField(max_length=191, blank=True, null=True)
    debit_rule = models.CharField(max_length=191, blank=True, null=True)
    revokable = models.CharField(max_length=191, blank=True, null=True)
    blockfund = models.CharField(max_length=191, blank=True, null=True)
    purpose = models.CharField(max_length=191, blank=True, null=True)
    bank_rrn = models.CharField(max_length=191, blank=True, null=True)
    umn = models.TextField(blank=True, null=True)
    mandate_status = models.CharField(max_length=191, blank=True, null=True)
    next_execution_date = models.CharField(max_length=191, blank=True, null=True)
    api_status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    merchant_ref_id = models.CharField(max_length=191, blank=True, null=True)
    is_enterprise = models.IntegerField(blank=True, null=True)
    as_present_notification_success_time = models.CharField(max_length=191, blank=True, null=True)
    as_present_next_debit_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_upi_create_mandates'


class IciciUpiExecuteMandates(models.Model):
    icici_upi_execute_mandates_id = models.BigAutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    mandate_id = models.CharField(max_length=191, blank=True, null=True)
    icici_upi_create_mandates_id = models.IntegerField(blank=True, null=True)
    merchant_tran_id = models.CharField(max_length=191, blank=True, null=True)
    bill_number = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    retry_count = models.IntegerField(blank=True, null=True)
    mandate_seq_no = models.IntegerField(blank=True, null=True)
    purpose = models.CharField(max_length=191, blank=True, null=True)
    umn = models.CharField(max_length=191, blank=True, null=True)
    remark = models.CharField(max_length=191, blank=True, null=True)
    success = models.CharField(max_length=191, blank=True, null=True)
    message = models.CharField(max_length=191, blank=True, null=True)
    bank_rrn = models.CharField(max_length=191, blank=True, null=True)
    transac_ref_id = models.CharField(max_length=191, blank=True, null=True)
    last_executed_on = models.CharField(max_length=191, blank=True, null=True)
    api_status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    mandate_status = models.CharField(max_length=191, blank=True, null=True)
    bank_transaction_statuses_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_upi_execute_mandates'


class IciciUpiLogs(models.Model):
    icici_upi_logs_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    api_name = models.CharField(max_length=200)
    request = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_upi_logs'


class IciciUpiMandateHistories(models.Model):
    icici_upi_mandate_histories_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    icici_upi_create_mandates_id = models.IntegerField(blank=True, null=True)
    mandate_status_id = models.IntegerField(blank=True, null=True)
    activity_date = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_upi_mandate_histories'


class IciciUpiMandateNotifications(models.Model):
    icici_upi_mandate_notifications_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    icici_upi_create_mandates_id = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    execution_date = models.CharField(max_length=191, blank=True, null=True)
    merchant_tran_id = models.CharField(max_length=191, blank=True, null=True)
    mandate_seq_no = models.IntegerField(blank=True, null=True)
    response_code = models.IntegerField(blank=True, null=True)
    success = models.CharField(max_length=191, blank=True, null=True)
    message = models.CharField(max_length=191, blank=True, null=True)
    notification_status = models.CharField(max_length=191, blank=True, null=True)
    bank_rrn = models.CharField(max_length=191, blank=True, null=True)
    api_status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_upi_mandate_notifications'


class IciciUpiMandateStatuses(models.Model):
    icici_upi_mandate_statuses_id = models.AutoField(primary_key=True)
    mandate_status = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_upi_mandate_statuses'


class IciciVirtualAccountNumbers(models.Model):
    icici_virtual_account_numbers_id = models.AutoField(primary_key=True)
    company_va = models.CharField(max_length=191)
    beneficiary_va = models.CharField(max_length=191)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'icici_virtual_account_numbers'


class IciciWalletAccounts(models.Model):
    icici_wallet_accounts_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    contacts_id = models.IntegerField(blank=True, null=True)
    is_contact = models.IntegerField(blank=True, null=True)
    va_number = models.CharField(max_length=191, blank=True, null=True)
    wallet_user_code = models.CharField(db_column='wallet-user-code', max_length=191)  # Field renamed to remove unsuitable characters.
    adhar_card_id = models.CharField(db_column='adhar-card-id', max_length=191, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    adhar_ref_no = models.CharField(db_column='adhar-ref-no', max_length=191, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    user_name = models.CharField(db_column='user-name', max_length=191, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    address_line1 = models.CharField(db_column='address-line1', max_length=191, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    address_line2 = models.CharField(db_column='address-line2', max_length=191, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    address_line3 = models.CharField(db_column='address-line3', max_length=191, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    email_id = models.CharField(db_column='email-id', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    mobile_no = models.CharField(db_column='mobile-no', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    user_bank_name = models.CharField(db_column='user-bank-name', max_length=191, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    user_bank_code = models.CharField(db_column='user-bank-code', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    user_ifsc_code = models.CharField(db_column='user-ifsc-code', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    user_bank_account = models.CharField(db_column='user-bank-account', max_length=191, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    request_date_time = models.CharField(db_column='request-date-time', max_length=191, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    user_dob = models.CharField(db_column='user-dob', max_length=191, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    user_status = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icici_wallet_accounts'


class IcpBankReferenceDetails(models.Model):
    bank_reference_detail_id = models.AutoField(primary_key=True)
    reference_key = models.CharField(max_length=191)
    bank_terminology = models.TextField(blank=True, null=True)
    reference_value = models.CharField(max_length=191)
    entity_type = models.CharField(max_length=191)
    entity_source = models.CharField(max_length=191)
    entity_id = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_bank_reference_details'


class IcpBins(models.Model):
    bin = models.CharField(db_column='BIN', max_length=11, blank=True, null=True)  # Field name made lowercase.
    cardprovider = models.CharField(db_column='CARDPROVIDER', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BANKNAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    creditdebit = models.CharField(db_column='CREDITDEBIT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cardtype = models.CharField(db_column='CARDTYPE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='COUNTRYCODE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    isocountry = models.CharField(db_column='ISOCOUNTRY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    is_migrated_to_redis = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'icp_bins'


class IcpButtonItemTypes(models.Model):
    icp_button_item_types_id = models.AutoField(primary_key=True)
    icp_button_item_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_button_item_types'


class IcpButtonOrders(models.Model):
    icp_button_order_id = models.AutoField(primary_key=True)
    payment_token = models.CharField(max_length=255)
    total_amount = models.FloatField()
    amount_due = models.FloatField()
    amount_paid = models.FloatField()
    attempts = models.IntegerField()
    currency = models.CharField(max_length=10)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_button_orders'


class IcpButtonThemes(models.Model):
    icp_button_themes_id = models.AutoField(primary_key=True)
    icp_button_theme = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_button_themes'


class IcpButtonTypes(models.Model):
    icp_button_types_id = models.AutoField(primary_key=True)
    icp_button_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_button_types'


class IcpButtons(models.Model):
    icp_buttons_id = models.AutoField(primary_key=True)
    button_id = models.CharField(unique=True, max_length=50)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    merchant_id = models.CharField(max_length=50)
    button_title = models.CharField(max_length=255)
    button_label = models.CharField(max_length=100)
    icp_button_types_id = models.IntegerField()
    button_redirect_url = models.CharField(max_length=255, blank=True, null=True)
    icp_button_themes_id = models.IntegerField()
    brand_logo = models.CharField(max_length=255, blank=True, null=True)
    use_brand_logo = models.IntegerField()
    brand_color = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField()
    status_reason = models.CharField(max_length=255, blank=True, null=True)
    expire_by = models.DateTimeField()
    times_payable = models.IntegerField()
    times_paid = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_buttons'


class IcpCards(models.Model):
    icp_cards_id = models.AutoField(primary_key=True)
    card_id = models.CharField(unique=True, max_length=191)
    card_data = models.TextField()
    card_type = models.CharField(max_length=191, blank=True, null=True)
    is_saved = models.IntegerField(blank=True, null=True)
    customer_id = models.CharField(max_length=191)
    card_network = models.CharField(max_length=191, blank=True, null=True)
    card_hash = models.TextField(blank=True, null=True)
    bin = models.CharField(max_length=191, blank=True, null=True)
    last_four = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_cards'


class IcpCustomers(models.Model):
    icp_customers_id = models.AutoField(primary_key=True)
    customer_id = models.CharField(unique=True, max_length=191, blank=True, null=True)
    merchant_id = models.CharField(max_length=191)
    accounts_id = models.PositiveBigIntegerField()
    companies_id = models.PositiveBigIntegerField()
    users_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    email_id = models.CharField(max_length=191, blank=True, null=True)
    contact_number = models.CharField(max_length=191, blank=True, null=True)
    is_global = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_customers'


class IcpEntityHistories(models.Model):
    icp_entity_histories_id = models.AutoField(primary_key=True)
    entity_id = models.CharField(max_length=191)
    entity_type = models.CharField(max_length=191)
    action = models.CharField(max_length=191, blank=True, null=True)
    message = models.CharField(max_length=191, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    entity_source = models.CharField(max_length=191, blank=True, null=True)
    updated_status = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_entity_histories'


class IcpGatewayAtomCardRefunds(models.Model):
    atom_card_refund_id = models.BigAutoField(primary_key=True)
    pg_merchant_id = models.CharField(max_length=191, blank=True, null=True)
    pg_transaction_id = models.CharField(max_length=191, blank=True, null=True)
    pg_refund_status_code = models.CharField(max_length=191, blank=True, null=True)
    pg_refund_id = models.CharField(max_length=191, blank=True, null=True)
    refund_id = models.CharField(unique=True, max_length=191, blank=True, null=True)
    payment_id = models.CharField(max_length=191, blank=True, null=True)
    request_data = models.TextField(blank=True, null=True)
    response_data = models.TextField(blank=True, null=True)
    pg_refund_status = models.CharField(max_length=191, blank=True, null=True)
    pg_refund_message = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    refund_amount = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_gateway_atom_card_refunds'


class IcpGatewayAtomCardTransactions(models.Model):
    atom_netbanking_transactions_id = models.AutoField(primary_key=True)
    payment_id = models.CharField(unique=True, max_length=191, blank=True, null=True)
    payment_request_id = models.CharField(max_length=191)
    pg_merchant_id = models.CharField(max_length=191, blank=True, null=True)
    response_data = models.TextField(blank=True, null=True)
    request_data = models.TextField(blank=True, null=True)
    pg_status_code = models.CharField(max_length=50, blank=True, null=True)
    pg_status = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    pg_error_message = models.TextField(blank=True, null=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    pg_transaction_id = models.CharField(max_length=100, blank=True, null=True)
    bank_transaction_id = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    pg_created_at = models.CharField(max_length=100, blank=True, null=True)
    card_number = models.CharField(max_length=50, blank=True, null=True)
    internal_sync = models.IntegerField(blank=True, null=True)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_email_id = models.CharField(max_length=100, blank=True, null=True)
    customer_contact_number = models.CharField(max_length=50, blank=True, null=True)
    status_api_check = models.IntegerField(blank=True, null=True)
    status_api_check_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_gateway_atom_card_transactions'


class IcpGatewayAtomEmiTransactions(models.Model):
    atom_emi_transactions_id = models.AutoField(primary_key=True)
    payment_id = models.CharField(max_length=50)
    payment_request_id = models.CharField(max_length=50, blank=True, null=True)
    pg_merchant_id = models.CharField(max_length=50, blank=True, null=True)
    request_data = models.TextField(blank=True, null=True)
    response_data = models.TextField(blank=True, null=True)
    pg_status_code = models.CharField(max_length=20, blank=True, null=True)
    pg_status = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    pg_error_message = models.TextField(blank=True, null=True)
    transaction_id = models.CharField(max_length=50, blank=True, null=True)
    bank_code = models.CharField(max_length=10, blank=True, null=True)
    emi_tenure = models.CharField(max_length=3, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    bank_transaction_id = models.CharField(max_length=50, blank=True, null=True)
    pg_transaction_id = models.CharField(max_length=50, blank=True, null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    pg_created_at = models.CharField(max_length=30, blank=True, null=True)
    internal_sync = models.IntegerField(blank=True, null=True)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_email_id = models.CharField(max_length=80, blank=True, null=True)
    customer_contact_number = models.CharField(max_length=20, blank=True, null=True)
    status_api_check = models.IntegerField(blank=True, null=True)
    status_api_check_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_gateway_atom_emi_transactions'


class IcpGatewayAtomNetbankingRefunds(models.Model):
    atom_netbanking_refund_id = models.BigAutoField(primary_key=True)
    pg_merchant_id = models.CharField(max_length=191, blank=True, null=True)
    pg_transaction_id = models.CharField(max_length=191, blank=True, null=True)
    pg_refund_status_code = models.CharField(max_length=191, blank=True, null=True)
    pg_refund_id = models.CharField(max_length=191, blank=True, null=True)
    refund_id = models.CharField(unique=True, max_length=191, blank=True, null=True)
    payment_id = models.CharField(max_length=191, blank=True, null=True)
    request_data = models.TextField(blank=True, null=True)
    response_data = models.TextField(blank=True, null=True)
    pg_refund_status = models.CharField(max_length=191, blank=True, null=True)
    pg_refund_message = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    refund_amount = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_gateway_atom_netbanking_refunds'


class IcpGatewayAtomNetbankingTransactions(models.Model):
    atom_netbanking_transactions_id = models.AutoField(primary_key=True)
    payment_id = models.CharField(unique=True, max_length=191, blank=True, null=True)
    payment_request_id = models.CharField(max_length=191)
    pg_merchant_id = models.CharField(max_length=191, blank=True, null=True)
    response_data = models.TextField(blank=True, null=True)
    request_data = models.TextField(blank=True, null=True)
    pg_status_code = models.CharField(max_length=50, blank=True, null=True)
    pg_status = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    pg_error_message = models.TextField(blank=True, null=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    pg_transaction_id = models.CharField(max_length=100, blank=True, null=True)
    bank_transaction_id = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    pg_created_at = models.CharField(max_length=100, blank=True, null=True)
    internal_sync = models.IntegerField(blank=True, null=True)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_email_id = models.CharField(max_length=100, blank=True, null=True)
    customer_contact_number = models.CharField(max_length=100, blank=True, null=True)
    status_api_check = models.IntegerField(blank=True, null=True)
    status_api_check_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_gateway_atom_netbanking_transactions'


class IcpGatewayAtomWalletTransactions(models.Model):
    atom_wallet_transactions_id = models.AutoField(primary_key=True)
    payment_id = models.CharField(max_length=191, blank=True, null=True)
    payment_request_id = models.CharField(max_length=191, blank=True, null=True)
    pg_merchant_id = models.CharField(max_length=191, blank=True, null=True)
    request_data = models.TextField(blank=True, null=True)
    response_data = models.TextField(blank=True, null=True)
    pg_status_code = models.CharField(max_length=191, blank=True, null=True)
    pg_status = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    pg_error_message = models.TextField(blank=True, null=True)
    transaction_id = models.CharField(max_length=191, blank=True, null=True)
    bank_name = models.CharField(max_length=191, blank=True, null=True)
    pg_transaction_id = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    pg_created_at = models.CharField(max_length=191, blank=True, null=True)
    internal_sync = models.IntegerField(blank=True, null=True)
    customer_name = models.CharField(max_length=191, blank=True, null=True)
    customer_email_id = models.CharField(max_length=191, blank=True, null=True)
    customer_contact_number = models.CharField(max_length=191, blank=True, null=True)
    status_api_check = models.IntegerField(blank=True, null=True)
    status_api_check_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_gateway_atom_wallet_transactions'


class IcpGatewayAtomWebhooks(models.Model):
    icp_gateway_atom_webhooks_id = models.AutoField(primary_key=True)
    payment_id = models.CharField(max_length=191)
    pg_merchant_id = models.CharField(max_length=191, blank=True, null=True)
    pg_status = models.CharField(max_length=191, blank=True, null=True)
    bank_transaction_id = models.CharField(max_length=191, blank=True, null=True)
    bank_name = models.CharField(max_length=191, blank=True, null=True)
    pg_transaction_id = models.CharField(max_length=191, blank=True, null=True)
    pg_created_at = models.CharField(max_length=191, blank=True, null=True)
    pg_descriminator = models.CharField(max_length=191, blank=True, null=True)
    pg_surcharge = models.CharField(max_length=191, blank=True, null=True)
    pg_card_number = models.CharField(max_length=191, blank=True, null=True)
    pg_customer_id = models.CharField(max_length=191, blank=True, null=True)
    pg_client_code = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    payload = models.TextField()
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_gateway_atom_webhooks'


class IcpGatewayBilldeskCardTransactions(models.Model):
    billdesk_card_transactions_id = models.AutoField(primary_key=True)
    payment_id = models.CharField(max_length=50, blank=True, null=True)
    payment_request_id = models.CharField(max_length=50, blank=True, null=True)
    pg_merchant_id = models.CharField(max_length=20, blank=True, null=True)
    init_request_data = models.TextField(blank=True, null=True)
    init_response_data = models.TextField(blank=True, null=True)
    auth_request_data = models.TextField(blank=True, null=True)
    auth_response_data = models.TextField(blank=True, null=True)
    pg_status_code = models.CharField(max_length=20, blank=True, null=True)
    pg_status = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    pg_error_message = models.TextField(blank=True, null=True)
    transaction_id = models.CharField(max_length=50, blank=True, null=True)
    pg_transaction_id = models.CharField(max_length=100, blank=True, null=True)
    bank_ref_no = models.CharField(max_length=50, blank=True, null=True)
    amount = models.CharField(max_length=50, blank=True, null=True)
    filler1 = models.CharField(max_length=50, blank=True, null=True)
    filler2 = models.CharField(max_length=50, blank=True, null=True)
    filler3 = models.CharField(max_length=50, blank=True, null=True)
    filler4 = models.CharField(max_length=50, blank=True, null=True)
    filler5 = models.CharField(max_length=50, blank=True, null=True)
    txn_type = models.CharField(max_length=20, blank=True, null=True)
    pg_created_at = models.DateTimeField(blank=True, null=True)
    card_number = models.CharField(max_length=30, blank=True, null=True)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_email_id = models.CharField(max_length=100, blank=True, null=True)
    customer_contact_number = models.CharField(max_length=20, blank=True, null=True)
    internal_sync = models.IntegerField(blank=True, null=True)
    status_api_check = models.IntegerField(blank=True, null=True)
    status_api_check_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_gateway_billdesk_card_transactions'


class IcpGatewayBobCardRefunds(models.Model):
    bob_card_refund_id = models.AutoField(primary_key=True)
    payment_id = models.CharField(max_length=191, blank=True, null=True)
    refund_track_id = models.CharField(max_length=191, blank=True, null=True)
    pg_transaction_id = models.CharField(max_length=191, blank=True, null=True)
    refund_amount = models.CharField(max_length=191, blank=True, null=True)
    pg_refund_id = models.CharField(max_length=191, blank=True, null=True)
    payment_request_id = models.CharField(max_length=191, blank=True, null=True)
    request_data = models.TextField(blank=True, null=True)
    response_data = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    pg_status = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_gateway_bob_card_refunds'


class IcpGatewayBobCardTransactions(models.Model):
    bob_card_transactions_id = models.AutoField(primary_key=True)
    payment_id = models.CharField(max_length=191, blank=True, null=True)
    payment_request_id = models.CharField(max_length=191, blank=True, null=True)
    pg_merchant_id = models.CharField(max_length=191, blank=True, null=True)
    response_data = models.TextField(blank=True, null=True)
    request_data = models.TextField(blank=True, null=True)
    pg_status = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    pg_error_message = models.TextField(blank=True, null=True)
    transaction_id = models.CharField(max_length=191, blank=True, null=True)
    pg_transaction_id = models.CharField(max_length=191, blank=True, null=True)
    pg_ref_id = models.CharField(max_length=191, blank=True, null=True)
    pg_pay_id = models.CharField(max_length=191, blank=True, null=True)
    amount = models.CharField(max_length=191, blank=True, null=True)
    pg_created_at = models.DateTimeField(blank=True, null=True)
    card_number = models.CharField(max_length=191, blank=True, null=True)
    customer_name = models.CharField(max_length=191, blank=True, null=True)
    customer_email_id = models.CharField(max_length=191, blank=True, null=True)
    customer_contact_number = models.CharField(max_length=191, blank=True, null=True)
    internal_sync = models.IntegerField(blank=True, null=True)
    status_api_check = models.IntegerField(blank=True, null=True)
    status_api_check_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_gateway_bob_card_transactions'


class IcpGatewayBobUpiTransactions(models.Model):
    bob_upi_transactions_id = models.AutoField(primary_key=True)
    payment_id = models.CharField(max_length=191, blank=True, null=True)
    payment_request_id = models.CharField(max_length=191, blank=True, null=True)
    pg_merchant_id = models.CharField(max_length=191, blank=True, null=True)
    request_data = models.TextField(blank=True, null=True)
    response_data = models.TextField(blank=True, null=True)
    pg_status = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    pg_error_message = models.TextField(blank=True, null=True)
    pg_transaction_id = models.CharField(max_length=191, blank=True, null=True)
    amount = models.CharField(max_length=191, blank=True, null=True)
    vpa = models.CharField(max_length=191, blank=True, null=True)
    customer_name = models.CharField(max_length=191, blank=True, null=True)
    customer_email_id = models.CharField(max_length=191, blank=True, null=True)
    customer_contact_number = models.CharField(max_length=191, blank=True, null=True)
    pg_created_at = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_gateway_bob_upi_transactions'


class IcpGatewayIciciUpiRefunds(models.Model):
    icici_upi_refund_id = models.AutoField(primary_key=True)
    payment_id = models.CharField(max_length=191, blank=True, null=True)
    refund_id = models.CharField(max_length=191, blank=True, null=True)
    bank_rrn = models.CharField(max_length=191, blank=True, null=True)
    refund_amount = models.CharField(max_length=191, blank=True, null=True)
    request_data = models.TextField(blank=True, null=True)
    response_data = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    pg_refund_status_code = models.CharField(max_length=191, blank=True, null=True)
    pg_refund_status = models.CharField(max_length=191, blank=True, null=True)
    refund_reason = models.CharField(max_length=191, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_gateway_icici_upi_refunds'


class IcpGatewayIciciUpiTransactions(models.Model):
    icp_gateway_icici_upi_transactions_id = models.AutoField(primary_key=True)
    payment_id = models.CharField(unique=True, max_length=191)
    payment_request_id = models.CharField(max_length=191, blank=True, null=True)
    bank_reference_number = models.CharField(max_length=191, blank=True, null=True)
    pg_transaction_id = models.CharField(max_length=191, blank=True, null=True)
    vpa = models.CharField(max_length=191, blank=True, null=True)
    pg_status = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    collect_request_data = models.TextField(blank=True, null=True)
    callback_data = models.TextField(blank=True, null=True)
    callback_data_source = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_gateway_icici_upi_transactions'


class IcpGatewayStripeCardRefunds(models.Model):
    stripe_card_refund_id = models.AutoField(primary_key=True)
    payment_id = models.CharField(max_length=191, blank=True, null=True)
    refund_id = models.CharField(max_length=191, blank=True, null=True)
    pg_transaction_id = models.CharField(max_length=191, blank=True, null=True)
    refund_amount = models.CharField(max_length=191, blank=True, null=True)
    pg_refund_id = models.CharField(max_length=191, blank=True, null=True)
    payment_request_id = models.CharField(max_length=191, blank=True, null=True)
    request_data = models.TextField(blank=True, null=True)
    response_data = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    pg_refund_status = models.CharField(max_length=191, blank=True, null=True)
    refund_reason = models.CharField(max_length=191, blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_gateway_stripe_card_refunds'


class IcpGatewayTpslCardRefunds(models.Model):
    tpsl_card_refund_id = models.AutoField(primary_key=True)
    pg_refund_status_code = models.CharField(max_length=191, blank=True, null=True)
    pg_refund_status = models.CharField(max_length=191, blank=True, null=True)
    pg_refund_error_message = models.CharField(max_length=191, blank=True, null=True)
    payment_id = models.CharField(max_length=191, blank=True, null=True)
    pg_bank_code = models.CharField(max_length=191, blank=True, null=True)
    pg_transaction_id = models.CharField(max_length=191, blank=True, null=True)
    refund_amount = models.CharField(max_length=191, blank=True, null=True)
    pg_transaction_created_at = models.CharField(max_length=191, blank=True, null=True)
    pg_refund_id = models.CharField(max_length=191, blank=True, null=True)
    payment_amount_balance = models.CharField(max_length=191, blank=True, null=True)
    pg_request_id = models.CharField(max_length=191, blank=True, null=True)
    request_data = models.TextField(blank=True, null=True)
    response_data = models.TextField(blank=True, null=True)
    refund_id = models.CharField(unique=True, max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_gateway_tpsl_card_refunds'


class IcpGatewayTpslCardTransactions(models.Model):
    tpsl_card_transaction_id = models.AutoField(primary_key=True)
    payment_request_id = models.CharField(max_length=191)
    response_data = models.TextField(blank=True, null=True)
    request_data = models.TextField(blank=True, null=True)
    pg_status_code = models.CharField(max_length=50, blank=True, null=True)
    pg_status = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    pg_error_message = models.TextField(blank=True, null=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    pg_bank_code = models.CharField(max_length=50, blank=True, null=True)
    pg_transaction_id = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    pg_request_id = models.CharField(max_length=191, blank=True, null=True)
    pg_misc = models.CharField(max_length=191, blank=True, null=True)
    pg_created_at = models.CharField(max_length=100, blank=True, null=True)
    pg_hash = models.CharField(max_length=191, blank=True, null=True)
    internal_sync = models.IntegerField(blank=True, null=True)
    pg_merchant_key = models.CharField(max_length=100, blank=True, null=True)
    payment_id = models.CharField(unique=True, max_length=100, blank=True, null=True)
    status_api_check = models.IntegerField(blank=True, null=True)
    status_api_check_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_gateway_tpsl_card_transactions'


class IcpGatewayTpslNetbankingRefunds(models.Model):
    tpsl_netbanking_refund_id = models.AutoField(primary_key=True)
    pg_refund_status_code = models.CharField(max_length=191, blank=True, null=True)
    pg_refund_status = models.CharField(max_length=191, blank=True, null=True)
    refund_id = models.CharField(unique=True, max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    pg_refund_error_message = models.CharField(max_length=191, blank=True, null=True)
    payment_id = models.CharField(max_length=191, blank=True, null=True)
    pg_bank_code = models.CharField(max_length=191, blank=True, null=True)
    pg_transaction_id = models.CharField(max_length=191, blank=True, null=True)
    refund_amount = models.CharField(max_length=191, blank=True, null=True)
    pg_transaction_created_at = models.CharField(max_length=191, blank=True, null=True)
    pg_refund_id = models.CharField(max_length=191, blank=True, null=True)
    payment_amount_balance = models.CharField(max_length=191, blank=True, null=True)
    pg_request_id = models.CharField(max_length=191, blank=True, null=True)
    request_data = models.TextField(blank=True, null=True)
    response_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'icp_gateway_tpsl_netbanking_refunds'


class IcpGatewayTpslNetbankingTransactions(models.Model):
    tpsl_netbanking_transaction_id = models.AutoField(primary_key=True)
    payment_id = models.CharField(max_length=50, blank=True, null=True)
    payment_request_id = models.CharField(max_length=191)
    pg_merchant_key = models.CharField(max_length=191, blank=True, null=True)
    response_data = models.TextField(blank=True, null=True)
    request_data = models.TextField(blank=True, null=True)
    pg_status_code = models.CharField(max_length=50, blank=True, null=True)
    pg_status = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    pg_error_message = models.TextField(blank=True, null=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    pg_bank_code = models.CharField(max_length=100, blank=True, null=True)
    pg_transaction_id = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    pg_request_id = models.CharField(max_length=100, blank=True, null=True)
    pg_misc = models.CharField(max_length=191, blank=True, null=True)
    pg_created_at = models.CharField(max_length=100, blank=True, null=True)
    pg_hash = models.CharField(max_length=191, blank=True, null=True)
    internal_sync = models.IntegerField(blank=True, null=True)
    status_api_check = models.IntegerField(blank=True, null=True)
    status_api_check_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_gateway_tpsl_netbanking_transactions'


class IcpGateways(models.Model):
    gateway_id = models.CharField(unique=True, max_length=191)
    gateway_provider = models.CharField(max_length=191)
    payment_instrument_id = models.CharField(max_length=191)
    gateway_available = models.IntegerField()
    class_path = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    gateway_config = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_gateways'


class IcpItems(models.Model):
    icp_items_id = models.AutoField(primary_key=True)
    item_id = models.CharField(max_length=255)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    currency = models.CharField(max_length=10)
    tax_inclusive = models.IntegerField()
    tax_rate = models.IntegerField(blank=True, null=True)
    hsn_code = models.CharField(max_length=255, blank=True, null=True)
    sac_code = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_items'


class IcpLogs(models.Model):
    icp_logs_id = models.AutoField(primary_key=True)
    message = models.TextField(blank=True, null=True)
    meta = models.TextField(blank=True, null=True)
    request_url = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    request_id = models.CharField(max_length=191, blank=True, null=True)
    type = models.CharField(max_length=191, blank=True, null=True)
    runtime_type = models.CharField(max_length=191, blank=True, null=True)
    runtime = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_logs'


class IcpMerchantTerminalConfigurations(models.Model):
    merchant_terminal_id = models.CharField(max_length=191)
    config_key = models.CharField(max_length=191)
    config_value = models.CharField(max_length=191)
    is_available = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'icp_merchant_terminal_configurations'


class IcpMerchantTerminalMethods(models.Model):
    icp_merchant_terminal_methods_id = models.AutoField(primary_key=True)
    merchant_terminal_id = models.CharField(max_length=191)
    payment_instrument_id = models.IntegerField()
    merchant_terminal_method_available = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_merchant_terminal_methods'


class IcpMerchantTerminals(models.Model):
    icp_merchant_terminals_id = models.AutoField(primary_key=True)
    merchant_terminal_id = models.CharField(unique=True, max_length=191)
    merchant_id = models.CharField(max_length=191)
    accounts_id = models.PositiveIntegerField()
    companies_id = models.PositiveIntegerField()
    users_id = models.IntegerField(blank=True, null=True)
    terminal_id = models.CharField(max_length=191)
    merchant_terminal_available = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    merchant_terminal_priority = models.IntegerField(blank=True, null=True)
    is_processed = models.IntegerField(blank=True, null=True)
    merchant_mid = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    prodid = models.CharField(max_length=255, blank=True, null=True)
    request_hash_key = models.CharField(max_length=255, blank=True, null=True)
    response_hash_key = models.CharField(max_length=255, blank=True, null=True)
    request_enc_key_salt = models.CharField(max_length=255, blank=True, null=True)
    response_enc_key_salt = models.CharField(max_length=255, blank=True, null=True)
    gateway_id = models.CharField(max_length=50, blank=True, null=True)
    gateway_provider = models.CharField(max_length=100, blank=True, null=True)
    payment_instrument_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    merchant_mid_enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'icp_merchant_terminals'


class IcpMerchants(models.Model):
    icp_merchants_id = models.AutoField(primary_key=True)
    icp_merchant_id = models.CharField(unique=True, max_length=191)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    merchant_available = models.IntegerField(blank=True, null=True)
    icp_activation_date = models.DateTimeField(blank=True, null=True)
    icp_is_activation_date = models.DateTimeField(blank=True, null=True)
    admin_users_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_surcharge_enabled = models.IntegerField(blank=True, null=True)
    is_priority_user = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'icp_merchants'


class IcpOtp(models.Model):
    icp_otp_id = models.AutoField(primary_key=True)
    otp_id = models.CharField(unique=True, max_length=191, blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    email_id = models.CharField(max_length=50, blank=True, null=True)
    verified = models.IntegerField(blank=True, null=True)
    otp = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_otp'


class IcpPaymentInstruments(models.Model):
    payment_instrument_id = models.AutoField(primary_key=True)
    instrument_name = models.CharField(max_length=191)
    parent = models.IntegerField(blank=True, null=True)
    instrument_code = models.CharField(max_length=191, blank=True, null=True)
    parent_instrument_name = models.CharField(max_length=255, blank=True, null=True)
    parent_instrument_code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_payment_instruments'


class IcpPaymentRequestRedirections(models.Model):
    payment_request_redirection_id = models.BigAutoField(primary_key=True)
    payment_request_id = models.CharField(max_length=191)
    redirection_action = models.TextField()
    redirection_data = models.TextField()
    redirection_method = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_payment_request_redirections'


class IcpPaymentRequests(models.Model):
    icp_payment_requests_id = models.AutoField(primary_key=True)
    payment_request_id = models.CharField(unique=True, max_length=191)
    entity_type = models.CharField(max_length=191)
    entity_source = models.CharField(max_length=191)
    entity_id = models.CharField(max_length=191)
    merchant_terminal_id = models.CharField(max_length=191)
    payment_instrument = models.CharField(max_length=191, blank=True, null=True)
    payment_request_type = models.CharField(max_length=191)
    payment_request_status = models.CharField(max_length=191)
    user_agent_hash = models.TextField(blank=True, null=True)
    request_header = models.TextField(blank=True, null=True)
    ip = models.TextField(blank=True, null=True)
    request_debug_info = models.TextField(blank=True, null=True)
    merchant_callback_url = models.TextField(blank=True, null=True)
    merchant_callback_delivery = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_payment_requests'


class IcpPaymentTokenStatuses(models.Model):
    icp_payment_token_statuses_id = models.AutoField(primary_key=True)
    icp_payment_token_status = models.CharField(max_length=50)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_payment_token_statuses'


class IcpPaymentTokens(models.Model):
    icp_payment_tokens_id = models.AutoField(primary_key=True)
    payment_token_id = models.CharField(unique=True, max_length=191, blank=True, null=True)
    merchant_id = models.CharField(max_length=191)
    accounts_id = models.PositiveIntegerField()
    companies_id = models.PositiveIntegerField()
    users_id = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    convenience_fee = models.DecimalField(max_digits=10, decimal_places=2)
    customer_id = models.CharField(max_length=191, blank=True, null=True)
    currency = models.CharField(max_length=191)
    mtx = models.CharField(max_length=191, blank=True, null=True)
    button_id = models.CharField(max_length=255, blank=True, null=True)
    attempts = models.IntegerField(blank=True, null=True)
    payment_token_status = models.CharField(max_length=10)
    sub_accounts_id = models.CharField(max_length=100, blank=True, null=True)
    payment_instruments = models.CharField(max_length=191, blank=True, null=True)
    payment_instrument_types = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_payment_tokens'


class IcpPaymentToolsCustomAttributeDefinition(models.Model):
    attribute_definition_id = models.AutoField(primary_key=True)
    icp_payment_reference_id = models.CharField(max_length=255)
    attribute_name = models.CharField(max_length=255)
    attribute_type_id = models.IntegerField()
    default_value = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    required = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)
    field_setting = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_payment_tools_custom_attribute_definition'


class IcpPaymentToolsCustomAttributes(models.Model):
    icp_payment_reference_id = models.CharField(max_length=100)
    payment_token = models.CharField(max_length=100)
    attribute_definition_id = models.IntegerField()
    attribute_value = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_payment_tools_custom_attributes'


class IcpPaymentToolsPageItems(models.Model):
    icp_payment_tools_page_item_id = models.AutoField(primary_key=True)
    icp_payment_reference_id = models.CharField(max_length=100)
    items_id = models.CharField(max_length=100)
    is_optional = models.IntegerField()
    image_url = models.CharField(max_length=255, blank=True, null=True)
    min_order_limit = models.IntegerField(blank=True, null=True)
    max_order_limit = models.IntegerField(blank=True, null=True)
    min_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    max_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    total_quantity = models.IntegerField(blank=True, null=True)
    amount_field_type = models.IntegerField(blank=True, null=True)
    position = models.IntegerField()
    total_quantity_sold = models.IntegerField(blank=True, null=True)
    total_amount_paid = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_payment_tools_page_items'


class IcpPayments(models.Model):
    icp_payments_id = models.AutoField(primary_key=True)
    payment_id = models.CharField(unique=True, max_length=191)
    merchant_id = models.CharField(max_length=191)
    accounts_id = models.PositiveIntegerField()
    companies_id = models.PositiveIntegerField()
    payment_token_id = models.CharField(max_length=191)
    merchant_terminal_id = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    currency = models.CharField(max_length=10)
    payment_instrument = models.CharField(max_length=191, blank=True, null=True)
    card_id = models.CharField(max_length=191, blank=True, null=True)
    payment_status = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    pg_transaction_id = models.CharField(max_length=191, blank=True, null=True)
    pg_transaction_source = models.CharField(max_length=191, blank=True, null=True)
    sub_accounts_id = models.CharField(max_length=100, blank=True, null=True)
    payment_error_code = models.CharField(max_length=191, blank=True, null=True)
    payment_error_description = models.CharField(max_length=191, blank=True, null=True)
    vpa = models.CharField(max_length=191, blank=True, null=True)
    is_international_txn = models.IntegerField()
    stripe_id = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_payments'


class IcpPgLogs(models.Model):
    icp_pg_logs_id = models.BigAutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    payment_token = models.CharField(max_length=191, blank=True, null=True)
    payment_id = models.CharField(max_length=191, blank=True, null=True)
    request_id = models.CharField(max_length=191)
    message = models.TextField()
    level = models.CharField(max_length=191)
    level_name = models.CharField(max_length=191)
    mode = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    payment_gateway = models.CharField(max_length=100, blank=True, null=True)
    entity = models.CharField(max_length=191)
    event = models.CharField(max_length=191)
    api_name = models.CharField(max_length=191)
    end_point = models.CharField(max_length=191)
    request_headers = models.TextField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    response_code = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_pg_logs'


class IcpRefundActivationStatuses(models.Model):
    icp_refund_activation_statuses_id = models.AutoField(primary_key=True)
    icp_refund_activation_status = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_refund_activation_statuses'


class IcpRefundAdjustmentHistories(models.Model):
    icp_refund_adjustment_histories_id = models.AutoField(primary_key=True)
    icp_refund_adjustments_id = models.IntegerField(blank=True, null=True)
    adjusted_amount = models.DecimalField(max_digits=14, decimal_places=2)
    refund_id = models.CharField(max_length=191, blank=True, null=True)
    payment_id = models.CharField(max_length=191, blank=True, null=True)
    settlement_txn_id = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_refund_adjustment_histories'


class IcpRefundAdjustments(models.Model):
    icp_refund_adjustments_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    refund_id = models.CharField(max_length=191, blank=True, null=True)
    payment_id = models.CharField(max_length=191, blank=True, null=True)
    adjusted_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    adjustment_statuses_id = models.IntegerField(blank=True, null=True)
    amount_pending_to_adjust = models.DecimalField(max_digits=14, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_refund_adjustments'


class IcpRefunds(models.Model):
    icp_refunds_id = models.AutoField(primary_key=True)
    refund_id = models.CharField(unique=True, max_length=191)
    merchant_id = models.CharField(max_length=191)
    accounts_id = models.PositiveBigIntegerField()
    companies_id = models.PositiveBigIntegerField()
    users_id = models.IntegerField(blank=True, null=True)
    payment_id = models.CharField(max_length=191)
    refund_amount = models.DecimalField(max_digits=14, decimal_places=2)
    refund_status = models.CharField(max_length=191, blank=True, null=True)
    pg_refund_id = models.CharField(max_length=191, blank=True, null=True)
    pg_refund_source = models.CharField(max_length=191, blank=True, null=True)
    refund_type = models.CharField(max_length=191, blank=True, null=True)
    adjustment_statuses_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_refunds'


class IcpTerminalMethods(models.Model):
    terminal_id = models.CharField(max_length=191)
    payment_instrument_id = models.CharField(max_length=191)
    terminal_method_available = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_terminal_methods'


class IcpTerminals(models.Model):
    terminal_id = models.CharField(unique=True, max_length=191)
    gateway_id = models.CharField(max_length=191)
    payment_instrument_id = models.CharField(max_length=10)
    terminal_available = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_terminals'


class IcpUdf(models.Model):
    udf_id = models.AutoField(primary_key=True)
    udf_key = models.TextField()
    udf_value = models.TextField()
    entity_type = models.CharField(max_length=191)
    entity_source = models.TextField()
    entity_id = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_udf'


class IcpWebhookTriggerHistories(models.Model):
    icp_webhook_trigger_histories_id = models.AutoField(primary_key=True)
    webhook_id = models.CharField(max_length=191)
    delivery_report = models.TextField(blank=True, null=True)
    http_response_code = models.CharField(max_length=191, blank=True, null=True)
    url = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'icp_webhook_trigger_histories'


class IcpWebhooks(models.Model):
    icp_webhooks = models.AutoField(primary_key=True)
    webhook_id = models.CharField(unique=True, max_length=191)
    merchant_id = models.CharField(max_length=191)
    accounts_id = models.CharField(max_length=191)
    companies_id = models.CharField(max_length=191)
    users_id = models.IntegerField(blank=True, null=True)
    entity = models.CharField(max_length=191)
    entity_id = models.CharField(max_length=191)
    event = models.CharField(max_length=191)
    payload = models.TextField(blank=True, null=True)
    tries = models.IntegerField(blank=True, null=True)
    is_halted = models.IntegerField(blank=True, null=True)
    is_delivered = models.IntegerField(blank=True, null=True)
    app_source = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_webhooks'


class IcpWebhooksIncoming(models.Model):
    icp_webhooks_incoming_id = models.AutoField(primary_key=True)
    entity_id = models.CharField(max_length=191)
    entity_type = models.CharField(max_length=191)
    entity_source = models.CharField(max_length=191)
    payload = models.TextField(blank=True, null=True)
    service = models.CharField(max_length=191, blank=True, null=True)
    service_type = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icp_webhooks_incoming'


class IdfcConnectedAccounts(models.Model):
    idfc_connected_accounts_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    corp_id = models.IntegerField()
    bank_user_id = models.IntegerField()
    urn = models.CharField(max_length=200)
    bank_account_number = models.CharField(max_length=200, blank=True, null=True)
    account_balance = models.CharField(max_length=200, blank=True, null=True)
    registration_status = models.CharField(max_length=200, blank=True, null=True)
    account_status = models.CharField(max_length=200, blank=True, null=True)
    message = models.CharField(max_length=200, blank=True, null=True)
    ref_id = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idfc_connected_accounts'


class IdfcConnectedFundTransfers(models.Model):
    idfc_connected_fund_transfers_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    internal_transaction_ref_id = models.CharField(max_length=191, blank=True, null=True)
    debtor_name = models.CharField(max_length=191, blank=True, null=True)
    debit_account = models.CharField(max_length=191, blank=True, null=True)
    creditor_name = models.CharField(max_length=191, blank=True, null=True)
    credit_account = models.CharField(max_length=191, blank=True, null=True)
    ifsc_code = models.CharField(max_length=191, blank=True, null=True)
    amount = models.CharField(max_length=191, blank=True, null=True)
    transfer_mode = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.CharField(max_length=191, blank=True, null=True)
    bank_transaction_status_id = models.IntegerField(blank=True, null=True)
    external_fund_transfers_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    bank_error_code = models.CharField(max_length=191, blank=True, null=True)
    bank_error_message = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idfc_connected_fund_transfers'


class IdfcConnectedStatements(models.Model):
    idfc_connected_statements_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=191, blank=True, null=True)
    account_number = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    transaction_mode = models.CharField(max_length=191, blank=True, null=True)
    transaction_id = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    api_status = models.CharField(max_length=191, blank=True, null=True)
    date = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idfc_connected_statements'


class Images(models.Model):
    images_id = models.AutoField(primary_key=True)
    image_name = models.CharField(max_length=60)
    image_extension = models.CharField(max_length=20)
    reference_id = models.IntegerField(blank=True, null=True)
    reference_type = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'


class IncomeCategories(models.Model):
    income_categories_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    category_name = models.CharField(max_length=191, blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'income_categories'


class IndividualPanDetails(models.Model):
    individual_pan_details_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    individual_pan_first_name = models.CharField(max_length=191, blank=True, null=True)
    individual_pan_second_name = models.CharField(max_length=191, blank=True, null=True)
    individual_pan_last_name = models.CharField(max_length=191, blank=True, null=True)
    individual_pan_gender = models.CharField(max_length=191, blank=True, null=True)
    individual_pan_dob = models.DateField(blank=True, null=True)
    individual_pan_number = models.CharField(max_length=191, blank=True, null=True)
    name_as_per_pan = models.CharField(max_length=191, blank=True, null=True)
    has_verified = models.IntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_openbook_kyc = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'individual_pan_details'


class InitiatorTypes(models.Model):
    initiator_types_id = models.AutoField(primary_key=True)
    initiator_type = models.CharField(max_length=199)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'initiator_types'


class InstantLendingUsers(models.Model):
    instant_lending_users_id = models.AutoField(primary_key=True)
    users = models.OneToOneField('Users', models.DO_NOTHING)
    sanctioned_limit = models.IntegerField()
    roi = models.IntegerField()
    nbfc_id = models.IntegerField(blank=True, null=True)
    mob_business_types_id = models.IntegerField(blank=True, null=True)
    loan_type_id = models.IntegerField(blank=True, null=True)
    validated = models.IntegerField(blank=True, null=True)
    is_rejected = models.IntegerField(blank=True, null=True)
    rejected_reason = models.TextField(blank=True, null=True)
    onboarded = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instant_lending_users'


class InternalCommentTypes(models.Model):
    internal_comment_types_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'internal_comment_types'


class InternalComments(models.Model):
    internal_comments_id = models.AutoField(primary_key=True)
    admin_users_id = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=191, blank=True, null=True)
    internal_comment_types_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'internal_comments'


class InternalFundTransactions(models.Model):
    internal_fund_transactions_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    bank_transaction_status_id = models.IntegerField()
    internal_transaction_ref_id = models.CharField(max_length=191)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    fund_transfer_partner_banks_id = models.IntegerField()
    transaction_types_id = models.IntegerField()
    utr_number = models.CharField(max_length=191)
    remarks = models.TextField(blank=True, null=True)
    response_status = models.CharField(max_length=250, blank=True, null=True)
    payment_response_time = models.DateTimeField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'internal_fund_transactions'


class InviteReferralSettings(models.Model):
    invite_referral_settings_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    is_referral_enabled = models.IntegerField()
    referral_life_time_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    referral_current_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invite_referral_settings'


class InvoiceAuditLogs(models.Model):
    invoice_audit_log_id = models.BigAutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    api = models.CharField(max_length=264, blank=True, null=True)
    method = models.CharField(max_length=14, blank=True, null=True)
    request_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_audit_logs'


class InvoiceBulkIntermediaries(models.Model):
    invoice_bulk_intermediaries_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    order_id = models.CharField(max_length=100, blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    invoice_no = models.CharField(max_length=100, blank=True, null=True)
    invoice_date = models.DateTimeField(blank=True, null=True)
    transaction_type = models.CharField(max_length=100, blank=True, null=True)
    shipment_id = models.CharField(max_length=100, blank=True, null=True)
    shipment_date = models.DateTimeField(blank=True, null=True)
    shipment_item_id = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    item_desc = models.CharField(max_length=191, blank=True, null=True)
    sku = models.CharField(max_length=191, blank=True, null=True)
    hsn = models.IntegerField(blank=True, null=True)
    sgst_perc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cgst_perc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    igst_perc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cess_perc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sgst_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cgst_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    igst_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cess_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_tax_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    invoice_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rate_per_unit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ship_to_state = models.CharField(max_length=250, blank=True, null=True)
    display_name = models.CharField(max_length=250, blank=True, null=True)
    primary_contact = models.CharField(max_length=250, blank=True, null=True)
    shipping_name = models.CharField(max_length=250, blank=True, null=True)
    contact_type = models.CharField(max_length=250, blank=True, null=True)
    credit_note_no = models.CharField(max_length=250, blank=True, null=True)
    credit_note_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    raw_data = models.TextField(blank=True, null=True)
    is_complete = models.IntegerField()
    batch_id = models.CharField(max_length=191, blank=True, null=True)
    invoice_group = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invoice_bulk_intermediaries'


class InvoiceEwayBills(models.Model):
    invoice_eway_bills_id = models.AutoField(primary_key=True)
    invoices_id = models.BigIntegerField()
    invoice_sequence_id = models.CharField(max_length=191)
    companies_id = models.BigIntegerField()
    ewaybill_status = models.CharField(max_length=9, blank=True, null=True)
    eway_bill_number = models.CharField(max_length=191, blank=True, null=True)
    eway_bill_date = models.DateTimeField(blank=True, null=True)
    eway_bill_expiry = models.DateTimeField(blank=True, null=True)
    eway_bill_cancelled_on = models.DateTimeField(blank=True, null=True)
    hsn_code = models.CharField(max_length=191, blank=True, null=True)
    invoice_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    ewaybill_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    service_response = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_eway_bills'


class InvoiceExtraCharges(models.Model):
    invoice_extra_charges_id = models.AutoField(primary_key=True)
    invoices_id = models.BigIntegerField()
    l1_categories_id = models.IntegerField()
    l2_categories_id = models.IntegerField()
    l3_categories_id = models.IntegerField()
    l3_categories_name = models.CharField(max_length=191)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    hsn_sac_code = models.CharField(max_length=50, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_extra_charges'


class InvoiceGstLogins(models.Model):
    invoice_gst_logins_id = models.AutoField(primary_key=True)
    companies_id = models.BigIntegerField()
    accounts_id = models.BigIntegerField()
    username = models.CharField(max_length=191)
    password = models.TextField()
    descr = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_gst_logins'


class InvoiceGstSummary(models.Model):
    id = models.BigAutoField(primary_key=True)
    companies_id = models.IntegerField(blank=True, null=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    invoices_id = models.IntegerField(blank=True, null=True)
    merchant_type = models.IntegerField(blank=True, null=True)
    party_country = models.IntegerField(blank=True, null=True)
    party_type = models.IntegerField(blank=True, null=True)
    party_gstin = models.IntegerField(blank=True, null=True)
    transaction_type = models.IntegerField(blank=True, null=True)
    place_of_supply = models.IntegerField(blank=True, null=True)
    item_tax_category = models.IntegerField(blank=True, null=True)
    is_rcm = models.IntegerField(blank=True, null=True)
    is_ecom_transaction = models.IntegerField(blank=True, null=True)
    transaction_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    gstr_type = models.CharField(max_length=10, blank=True, null=True)
    section = models.CharField(max_length=5, blank=True, null=True)
    sub_section = models.CharField(max_length=5, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'invoice_gst_summary'


class InvoiceHistory(models.Model):
    invoice_histories_id = models.AutoField(primary_key=True)
    revision = models.IntegerField(blank=True, null=True)
    dt_datetime = models.DateTimeField(blank=True, null=True)
    invoices_id = models.PositiveIntegerField(blank=True, null=True)
    invoice_types_id = models.PositiveIntegerField(blank=True, null=True)
    users_id = models.PositiveIntegerField()
    accounts_id = models.PositiveIntegerField()
    companies_id = models.IntegerField(blank=True, null=True)
    discount_perc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    net_total = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    payments_terms_id = models.CharField(max_length=191, blank=True, null=True)
    customer_notes = models.TextField(blank=True, null=True)
    terms_and_conditions = models.TextField(blank=True, null=True)
    frequency_id = models.IntegerField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    last_send_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    recurring_invoices_id = models.IntegerField(blank=True, null=True)
    estimate_id = models.IntegerField(blank=True, null=True)
    estimate_invoices_id = models.IntegerField(blank=True, null=True)
    is_draft = models.CharField(max_length=191, blank=True, null=True)
    adjustment_field = models.CharField(max_length=191, blank=True, null=True)
    adjustment_value = models.IntegerField(blank=True, null=True)
    shipping_charge = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    item_ids = models.TextField(blank=True, null=True)
    allow_partial_payment = models.IntegerField(blank=True, null=True)
    total_amount_due = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    contacts_id = models.PositiveIntegerField(blank=True, null=True)
    invoice_statuses_id = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_history'


class InvoiceItemTaxes(models.Model):
    invoice_item_taxes_id = models.AutoField(primary_key=True)
    invoice_items_id = models.IntegerField()
    company_taxes_id = models.IntegerField()
    tax_perc = models.DecimalField(max_digits=5, decimal_places=2)
    tax_value = models.DecimalField(max_digits=16, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_item_taxes'


class InvoiceItems(models.Model):
    invoice_items_id = models.AutoField(primary_key=True)
    invoices_id = models.PositiveIntegerField(blank=True, null=True)
    items_id = models.PositiveIntegerField(blank=True, null=True)
    item_name = models.CharField(max_length=191)
    l2_categories_id = models.IntegerField(blank=True, null=True)
    l3_categories_id = models.IntegerField(blank=True, null=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    units = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    cgst_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    sgst_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    igst_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    cgst_perc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sgst_perc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    igst_perc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    rate_per_unit = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    net_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    round_off = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    hsn_sac_code = models.CharField(max_length=50, blank=True, null=True)
    basic_user_description = models.TextField(blank=True, null=True)
    basic_invoice_tax_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    inventory_master_id = models.CharField(max_length=300, blank=True, null=True)
    ledger_name = models.CharField(max_length=300, blank=True, null=True)
    ledger_entries_master_id = models.CharField(max_length=300, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    cess_perc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cess_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    gst_perc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    taxable_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_items'


class InvoiceOverridedSequenceIds(models.Model):
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    invoice_overrided_id = models.CharField(max_length=191, blank=True, null=True)
    invoice_types_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_overrided_sequence_ids'


class InvoicePayments(models.Model):
    invoice_payments_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField(blank=True, null=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    external_payments_id = models.IntegerField(blank=True, null=True)
    invoices_id = models.IntegerField(blank=True, null=True)
    contacts_id = models.IntegerField(blank=True, null=True)
    invoice_amount_tagged = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    transaction_ref_no = models.CharField(max_length=60, blank=True, null=True)
    pg_statuses_id = models.IntegerField(blank=True, null=True)
    is_offline = models.IntegerField(blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    mode_of_payment = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_payments'


class InvoiceQuickCollectLinks(models.Model):
    invoice_quick_collect_links_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    contacts_id = models.IntegerField()
    invoices_id = models.IntegerField()
    quick_collect_id = models.IntegerField()
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    is_processed = models.IntegerField()
    qc_journal_entry_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_quick_collect_links'


class InvoiceSentStatuses(models.Model):
    invoice_sent_statuses_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_sent_statuses'


class InvoiceSequenceIds(models.Model):
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField(blank=True, null=True)
    invoice_sequence_id = models.CharField(max_length=191, blank=True, null=True)
    invoice_types_id = models.IntegerField(blank=True, null=True)
    is_used = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_sequence_ids'


class InvoiceStatusHistory(models.Model):
    invoice_status_histories_id = models.AutoField(primary_key=True)
    invoices_id = models.IntegerField(blank=True, null=True)
    manual_transactions_id = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    invoice_statuses_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_token = models.CharField(max_length=199, blank=True, null=True)
    open_pg_txn_id = models.CharField(unique=True, max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_status_history'


class InvoiceStatuses(models.Model):
    invoice_statuses_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_statuses'


class InvoiceTags(models.Model):
    invoice_tags_id = models.AutoField(primary_key=True)
    invoices_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    tags_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invoice_tags'


class InvoiceTaxes(models.Model):
    invoice_taxes_id = models.AutoField(primary_key=True)
    invoices_id = models.IntegerField(blank=True, null=True)
    company_taxes_id = models.IntegerField(blank=True, null=True)
    tax_perc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tax_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_taxes'


class InvoiceTransfers(models.Model):
    invoice_transfers_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    external_transfers_id = models.IntegerField()
    invoices_id = models.IntegerField()
    contacts_id = models.IntegerField(blank=True, null=True)
    invoice_amount_tagged = models.DecimalField(max_digits=16, decimal_places=2)
    ref_no = models.CharField(max_length=250)
    is_offline = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    paid_at = models.DateTimeField()
    transfer_mode = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_transfers'


class InvoiceTransports(models.Model):
    invoice_transports_id = models.BigAutoField(primary_key=True)
    invoices_id = models.BigIntegerField()
    transporter_id = models.CharField(max_length=30, blank=True, null=True)
    transporter_name = models.CharField(max_length=191)
    doc_no = models.CharField(max_length=191, blank=True, null=True)
    doc_date = models.DateTimeField(blank=True, null=True)
    mode = models.CharField(max_length=4)
    distance = models.IntegerField(blank=True, null=True)
    vehicle_type = models.CharField(max_length=191, blank=True, null=True)
    vehicle_no = models.CharField(max_length=191, blank=True, null=True)
    from_place = models.CharField(max_length=191, blank=True, null=True)
    from_state_code = models.IntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_transports'


class InvoiceTypes(models.Model):
    invoice_types_id = models.AutoField(primary_key=True)
    invoice_type_name = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_types'


class InvoiceUserSettings(models.Model):
    invoice_user_settings_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    invoice_types_id = models.IntegerField(blank=True, null=True)
    invoice_header = models.CharField(max_length=50, blank=True, null=True)
    default_message_to_customer = models.TextField(blank=True, null=True)
    invoice_prefix = models.CharField(max_length=11, blank=True, null=True)
    number_sequence_initial_value = models.CharField(max_length=100, blank=True, null=True)
    invno_reset_fin_year = models.CharField(max_length=191, blank=True, null=True)
    is_invoice_sequence_id_updated = models.IntegerField(blank=True, null=True)
    terms_and_conditions = models.TextField(blank=True, null=True)
    email_id = models.CharField(max_length=160, blank=True, null=True)
    mobile_number = models.CharField(max_length=160, blank=True, null=True)
    company_seal_image_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    default_subject = models.CharField(max_length=191)
    invoice_template_id = models.IntegerField(blank=True, null=True)
    invoice_template_props = models.TextField(blank=True, null=True)
    fssai_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_user_settings'


class Invoices(models.Model):
    invoices_id = models.AutoField(primary_key=True)
    invoice_types_id = models.PositiveIntegerField()
    invoice_statuses_id = models.IntegerField(blank=True, null=True)
    batch_id = models.CharField(max_length=250, blank=True, null=True)
    creation_types_id = models.IntegerField(blank=True, null=True)
    users_id = models.PositiveIntegerField()
    accounts_id = models.PositiveIntegerField()
    companies_id = models.IntegerField(blank=True, null=True)
    invoice_user_input_reference_id = models.CharField(max_length=50, blank=True, null=True)
    invoice_sequence_id = models.CharField(max_length=100, blank=True, null=True)
    is_override = models.IntegerField(blank=True, null=True)
    contacts_id = models.PositiveIntegerField(blank=True, null=True)
    recepient_name = models.CharField(max_length=191, blank=True, null=True)
    email_id = models.CharField(max_length=191, blank=True, null=True)
    mobile_number = models.CharField(max_length=191, blank=True, null=True)
    gst_perc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gst_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_perc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    l2_categories_id = models.IntegerField(blank=True, null=True)
    l3_categories_id = models.IntegerField(blank=True, null=True)
    tds_perc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tds_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    tds_l3_categories_id = models.IntegerField(blank=True, null=True)
    gst_input_credit = models.IntegerField(blank=True, null=True)
    net_total = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    net_total_after_taxes = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    round_off = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    payments_terms_id = models.CharField(max_length=191, blank=True, null=True)
    invoice_note = models.TextField(blank=True, null=True)
    frequencies_id = models.IntegerField(blank=True, null=True)
    repeat_for = models.IntegerField(blank=True, null=True)
    is_one_time_payment = models.IntegerField()
    link_expired = models.IntegerField()
    is_amount_editable = models.IntegerField()
    payment_link_click_counter = models.IntegerField(blank=True, null=True)
    current_counter = models.IntegerField(blank=True, null=True)
    total_counter = models.IntegerField()
    payment_link_unique_id = models.CharField(max_length=500, blank=True, null=True)
    invoice_sent_date = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    last_send_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    is_recurring = models.IntegerField(blank=True, null=True)
    recurring_invoices_id = models.IntegerField(blank=True, null=True)
    estimate_id = models.IntegerField(blank=True, null=True)
    estimate_invoices_id = models.IntegerField(blank=True, null=True)
    is_draft = models.CharField(max_length=191, blank=True, null=True)
    adjustment_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    additional_charge = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    item_ids = models.TextField(blank=True, null=True)
    allow_partial_payment = models.IntegerField(blank=True, null=True)
    total_amount_due = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    reference_number = models.CharField(max_length=191, blank=True, null=True)
    receive_id = models.CharField(max_length=191, blank=True, null=True)
    is_emandate_requested = models.IntegerField(blank=True, null=True)
    emandate_statuses_id = models.IntegerField(blank=True, null=True)
    is_pg_enabled = models.IntegerField()
    is_tnc_required = models.IntegerField(blank=True, null=True)
    income_categories_id = models.IntegerField(blank=True, null=True)
    recurrence_completed = models.IntegerField(blank=True, null=True)
    recurrence_pending = models.IntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    last_paid_at = models.DateTimeField(blank=True, null=True)
    parent_invoices_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    bill_ref_no = models.CharField(max_length=191, blank=True, null=True)
    bill_due_date = models.DateField(blank=True, null=True)
    bill_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    order_no = models.CharField(max_length=191, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    challan_no = models.CharField(max_length=191, blank=True, null=True)
    challan_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    address_id_shipping = models.IntegerField(blank=True, null=True)
    address_id_billing = models.IntegerField(blank=True, null=True)
    place_of_supply = models.CharField(max_length=100, blank=True, null=True)
    is_international = models.IntegerField()
    currency = models.CharField(max_length=191, blank=True, null=True)
    converted_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    is_enterprise = models.IntegerField()
    extra_data = models.TextField(blank=True, null=True)
    is_service_transaction = models.IntegerField()
    reference_invoices_id = models.PositiveIntegerField(blank=True, null=True)
    payment_token = models.CharField(max_length=199, blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    payment_ref_num = models.CharField(max_length=199, blank=True, null=True)
    user_agent = models.CharField(max_length=20, blank=True, null=True)
    transaction_client_types_id = models.IntegerField(blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    qc_balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_rcm_transaction = models.IntegerField(blank=True, null=True)
    is_ecommerce_transaction = models.IntegerField(blank=True, null=True)
    ecommerce_operator_contacts_id = models.IntegerField(blank=True, null=True)
    gst_original_sales_value = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoices'


class InvoidDocVerificationDetails(models.Model):
    invoid_doc_verification_details_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    request = models.TextField()
    response = models.TextField()
    encrypted_payload = models.CharField(max_length=300, blank=True, null=True)
    decrypted_payload = models.CharField(max_length=300, blank=True, null=True)
    transaction_id = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    expiry = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoid_doc_verification_details'


class ItemCategories(models.Model):
    item_categories_id = models.AutoField(primary_key=True)
    parent_item_category = models.IntegerField(blank=True, null=True)
    level = models.PositiveIntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    companies_id = models.IntegerField()
    category_name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_categories'


class ItemTaxes(models.Model):
    item_taxes_id = models.AutoField(primary_key=True)
    items_id = models.IntegerField()
    company_taxes_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_taxes'


class Items(models.Model):
    items_id = models.AutoField(primary_key=True)
    users_id = models.PositiveIntegerField()
    accounts_id = models.PositiveIntegerField()
    companies_id = models.IntegerField()
    item_name = models.CharField(max_length=191, blank=True, null=True)
    sku = models.CharField(max_length=191, blank=True, null=True)
    item_code = models.CharField(max_length=191, blank=True, null=True)
    quantity = models.IntegerField()
    alert_quantity = models.IntegerField(blank=True, null=True)
    hsn_sac_code = models.CharField(max_length=191, blank=True, null=True)
    hsn_sac_type = models.CharField(max_length=191, blank=True, null=True)
    custom_item_type = models.CharField(max_length=191, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_including_tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    display_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    display_price_including_tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sales_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    inclusive_tax = models.IntegerField()
    units = models.CharField(max_length=40, blank=True, null=True)
    income_category = models.IntegerField(blank=True, null=True)
    expense_category = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    is_service = models.IntegerField()
    gst_perc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    item_categories_id = models.IntegerField(blank=True, null=True)
    pricing_type = models.CharField(max_length=8)
    gst_calc_type = models.CharField(max_length=8)
    tax_rate = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cess = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    is_reverse_chargable = models.IntegerField(blank=True, null=True)
    tally_item_guid = models.CharField(max_length=250, blank=True, null=True)
    tally_timestamp = models.DateTimeField(blank=True, null=True)
    inventory_master_id = models.IntegerField(blank=True, null=True)
    is_updated = models.IntegerField()
    is_tax_included = models.IntegerField()
    is_gst_applicable = models.IntegerField(blank=True, null=True)
    taxability_of_item = models.CharField(max_length=9, blank=True, null=True)
    eligible_for_itc = models.IntegerField(blank=True, null=True)
    is_rcm = models.IntegerField(blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'


class ItemsHistory(models.Model):
    items_history_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField(blank=True, null=True)
    items_id = models.IntegerField()
    item_name = models.CharField(max_length=191, blank=True, null=True)
    sku = models.CharField(max_length=191, blank=True, null=True)
    item_code = models.CharField(max_length=191, blank=True, null=True)
    quantity = models.IntegerField()
    alert_quantity = models.IntegerField(blank=True, null=True)
    hsn_sac_code = models.CharField(max_length=191, blank=True, null=True)
    hsn_sac_type = models.CharField(max_length=191, blank=True, null=True)
    custom_item_type = models.CharField(max_length=191, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_including_tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    display_price = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    display_price_including_tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sales_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    inclusive_tax = models.IntegerField()
    units = models.CharField(max_length=40, blank=True, null=True)
    income_category = models.IntegerField(blank=True, null=True)
    expense_category = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    is_service = models.IntegerField()
    gst_perc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    item_created_at = models.DateTimeField(blank=True, null=True)
    item_updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    item_categories_id = models.IntegerField(blank=True, null=True)
    pricing_type = models.CharField(max_length=8)
    gst_calc_type = models.CharField(max_length=8)
    tax_rate = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cess = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    is_reverse_chargable = models.IntegerField(blank=True, null=True)
    tally_item_guid = models.CharField(max_length=250, blank=True, null=True)
    tally_timestamp = models.DateTimeField(blank=True, null=True)
    inventory_master_id = models.IntegerField(blank=True, null=True)
    is_updated = models.IntegerField()
    is_tax_included = models.IntegerField()
    is_gst_applicable = models.IntegerField(blank=True, null=True)
    taxability_of_item = models.CharField(max_length=9, blank=True, null=True)
    eligible_for_itc = models.IntegerField(blank=True, null=True)
    is_rcm = models.IntegerField(blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items_history'


class ItemsStocks(models.Model):
    items_stocks_id = models.AutoField(primary_key=True)
    items_id = models.BigIntegerField()
    quantity = models.DecimalField(max_digits=8, decimal_places=3)
    rate = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    direction = models.CharField(max_length=3)
    invoices_id = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    godown = models.CharField(max_length=191, blank=True, null=True)
    batch = models.CharField(max_length=191, blank=True, null=True)
    stock_date = models.DateField(blank=True, null=True)
    updated_quantity = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items_stocks'


class IvrCallSupports(models.Model):
    ivr_call_supports_id = models.AutoField(primary_key=True)
    mobile_number = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    unique_id = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'ivr_call_supports'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    queue = models.CharField(max_length=191)
    payload = models.TextField()
    attempts = models.PositiveIntegerField()
    reserved_at = models.PositiveIntegerField(blank=True, null=True)
    available_at = models.PositiveIntegerField()
    created_at = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'jobs'


class JoiningStatuses(models.Model):
    joining_statuses_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'joining_statuses'


class JournalEntries(models.Model):
    journal_entries_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField(blank=True, null=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    open_services_id = models.IntegerField(blank=True, null=True)
    statuses_id = models.IntegerField(blank=True, null=True)
    journal_entry_rules_id = models.IntegerField(blank=True, null=True)
    journal_batch_id = models.CharField(max_length=191, blank=True, null=True)
    journal_entry_level_no = models.IntegerField(blank=True, null=True)
    source_type = models.CharField(max_length=200, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    l1_categories_id = models.IntegerField(blank=True, null=True)
    l2_categories_id = models.IntegerField(blank=True, null=True)
    l3_categories_id = models.IntegerField(blank=True, null=True)
    l3_category = models.CharField(max_length=200)
    l2_category = models.CharField(max_length=200)
    l1_category = models.CharField(max_length=200)
    type_cr_dr = models.CharField(max_length=25, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    hsn_sac_code = models.CharField(max_length=50, blank=True, null=True)
    journal_entry_date = models.DateTimeField(blank=True, null=True)
    journal_description = models.TextField(blank=True, null=True)
    unique_journal_id = models.CharField(max_length=100, blank=True, null=True)
    is_updated_atleast_once = models.IntegerField()
    balance = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    sr_no = models.IntegerField(blank=True, null=True)
    is_tally_synced = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'journal_entries'


class JournalEntryRules(models.Model):
    journal_entry_rules_id = models.AutoField(primary_key=True)
    open_services_id = models.IntegerField(blank=True, null=True)
    statuses_id = models.IntegerField(blank=True, null=True)
    status_type = models.CharField(max_length=150, blank=True, null=True)
    journal_entry_level_no = models.IntegerField(blank=True, null=True)
    l1_categories_id = models.IntegerField(blank=True, null=True)
    l2_categories_id = models.IntegerField(blank=True, null=True)
    l3_categories_id = models.IntegerField(blank=True, null=True)
    l3_category = models.CharField(max_length=200)
    l2_category = models.CharField(max_length=200)
    l1_category = models.CharField(max_length=200)
    type_cr_dr = models.CharField(max_length=20, blank=True, null=True)
    amount = models.CharField(max_length=350, blank=True, null=True)
    journal_entry_description_template = models.CharField(max_length=350, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'journal_entry_rules'


class KarzaCinDetails(models.Model):
    karza_cin_details_id = models.AutoField(primary_key=True)
    cin = models.CharField(max_length=191, blank=True, null=True)
    company_name = models.CharField(max_length=191, blank=True, null=True)
    roc_code = models.CharField(max_length=191, blank=True, null=True)
    registration_number = models.IntegerField(blank=True, null=True)
    company_category = models.CharField(max_length=191, blank=True, null=True)
    company_subcategory = models.CharField(max_length=191, blank=True, null=True)
    class_of_company = models.CharField(max_length=191, blank=True, null=True)
    authorised_capital = models.IntegerField(blank=True, null=True)
    paid_up_capital = models.IntegerField(blank=True, null=True)
    number_of_members = models.IntegerField(blank=True, null=True)
    date_of_incorporation = models.DateField(blank=True, null=True)
    registered_address = models.CharField(max_length=191, blank=True, null=True)
    alternative_address = models.CharField(max_length=191, blank=True, null=True)
    email_id = models.CharField(max_length=191, blank=True, null=True)
    whether_listed_or_not = models.CharField(max_length=191, blank=True, null=True)
    suspended_at_stock_exchange = models.CharField(max_length=191, blank=True, null=True)
    date_of_last_agm = models.DateField(blank=True, null=True)
    date_of_balance_sheet = models.DateField(blank=True, null=True)
    company_status = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'karza_cin_details'


class KarzaCompanyLlpMasterDatas(models.Model):
    karza_company_llp_master_datas_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    whether_listed_or_not = models.CharField(max_length=191)
    company_category = models.CharField(max_length=191)
    registered_address = models.CharField(max_length=191)
    roc_code = models.CharField(max_length=191)
    company_sub_category = models.CharField(max_length=191)
    email_id = models.CharField(max_length=191)
    suspended_at_stock_exchange = models.CharField(max_length=191)
    date_of_balance_sheet = models.CharField(max_length=191)
    cin = models.CharField(max_length=191)
    alternative_address = models.CharField(max_length=191)
    company_status = models.CharField(max_length=191)
    date_of_last_agm = models.CharField(max_length=191)
    class_of_company = models.CharField(max_length=191)
    company_name = models.CharField(max_length=191)
    paid_up_capital = models.CharField(max_length=191)
    authorised_capital = models.CharField(max_length=191)
    number_of_members = models.CharField(max_length=191)
    registration_number = models.CharField(max_length=191)
    date_of_incorporation = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'karza_company_llp_master_datas'


class KarzaGstinDetails(models.Model):
    karza_gstin_details_id = models.AutoField(primary_key=True)
    gstin = models.CharField(max_length=191, blank=True, null=True)
    legal_name = models.CharField(max_length=191, blank=True, null=True)
    trade_name = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    cancellation_flag = models.CharField(max_length=191, blank=True, null=True)
    business_type = models.CharField(max_length=191, blank=True, null=True)
    authorized_signatories = models.TextField(blank=True, null=True)
    nature_of_business = models.CharField(max_length=191, blank=True, null=True)
    taxpayer_type = models.CharField(max_length=191, blank=True, null=True)
    compliance_rating = models.CharField(max_length=191, blank=True, null=True)
    central_jurisdiction = models.TextField(blank=True, null=True)
    central_jurisdiction_code = models.CharField(max_length=191, blank=True, null=True)
    state_jurisdiction = models.TextField(blank=True, null=True)
    state_jurisdiction_code = models.CharField(max_length=191, blank=True, null=True)
    registered_address = models.TextField(blank=True, null=True)
    registered_address_email = models.TextField(blank=True, null=True)
    registered_address_mobile = models.TextField(blank=True, null=True)
    additional_address = models.TextField(blank=True, null=True)
    additional_address_email = models.TextField(blank=True, null=True)
    additional_address_mobile = models.TextField(blank=True, null=True)
    registered_email = models.TextField(blank=True, null=True)
    mobile_number = models.CharField(max_length=191, blank=True, null=True)
    date_of_registeration = models.DateField(blank=True, null=True)
    date_of_cancellation = models.DateField(blank=True, null=True)
    last_updated = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'karza_gstin_details'


class KarzaKycOcrs(models.Model):
    karza_kyc_ocrs_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    type_side = models.CharField(max_length=191, blank=True, null=True)
    type = models.CharField(max_length=191, blank=True, null=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    dob_day = models.CharField(max_length=191, blank=True, null=True)
    dob_month = models.CharField(max_length=191, blank=True, null=True)
    dob_year = models.CharField(max_length=191, blank=True, null=True)
    id_number = models.CharField(max_length=191, blank=True, null=True)
    url = models.CharField(max_length=191, blank=True, null=True)
    full_address = models.CharField(max_length=191, blank=True, null=True)
    city = models.CharField(max_length=191, blank=True, null=True)
    district = models.CharField(max_length=191, blank=True, null=True)
    pin = models.IntegerField(blank=True, null=True)
    locality = models.CharField(max_length=191, blank=True, null=True)
    line2 = models.CharField(max_length=191, blank=True, null=True)
    line1 = models.CharField(max_length=191, blank=True, null=True)
    state = models.CharField(max_length=191, blank=True, null=True)
    street = models.CharField(max_length=191, blank=True, null=True)
    landmark = models.CharField(max_length=191, blank=True, null=True)
    housenumber = models.CharField(db_column='houseNumber', max_length=191, blank=True, null=True)  # Field name made lowercase.
    id_proof_details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'karza_kyc_ocrs'


class KarzaMcaSignatories(models.Model):
    karza_mca_signatories_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    karza_company_llp_master_datas_id = models.IntegerField()
    cin = models.CharField(max_length=191)
    date_of_appointment = models.CharField(max_length=191)
    designation = models.CharField(max_length=191)
    dsc_expiry_date = models.CharField(max_length=191)
    wheather_dsc_registered = models.CharField(max_length=191)
    din_dpin_pan = models.CharField(max_length=191)
    full_name = models.CharField(max_length=191)
    address = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'karza_mca_signatories'


class KarzaPanDetails(models.Model):
    karza_pan_details_id = models.AutoField(primary_key=True)
    pan_no = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    dob = models.DateField()
    status = models.CharField(max_length=255)
    duplicate = models.IntegerField()
    namematch = models.IntegerField(db_column='nameMatch')  # Field name made lowercase.
    dobmatch = models.IntegerField(db_column='dobMatch')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'karza_pan_details'


class KarzaXmlDocuments(models.Model):
    karza_xml_documents_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    files_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'karza_xml_documents'


class KotakBankAccounts(models.Model):
    kotak_bank_accounts_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    customer_type = models.CharField(max_length=10, blank=True, null=True)
    crn = models.CharField(max_length=191)
    customer_id = models.CharField(max_length=191)
    account_number = models.CharField(max_length=191)
    bank_connection_statuses_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kotak_bank_accounts'


class KotakBankFundTransfers(models.Model):
    kotak_bank_fund_transfers_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    internal_transaction_ref_id = models.CharField(max_length=191, blank=True, null=True)
    debtor_name = models.CharField(max_length=191, blank=True, null=True)
    debit_account = models.CharField(max_length=191, blank=True, null=True)
    creditor_name = models.CharField(max_length=191, blank=True, null=True)
    credit_account = models.CharField(max_length=191, blank=True, null=True)
    ifsc_code = models.CharField(max_length=191, blank=True, null=True)
    amount = models.CharField(max_length=191, blank=True, null=True)
    transfer_mode = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.CharField(max_length=191, blank=True, null=True)
    bank_transaction_status_id = models.IntegerField(blank=True, null=True)
    external_fund_transfers_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    bank_error_code = models.CharField(max_length=191, blank=True, null=True)
    bank_error_message = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kotak_bank_fund_transfers'


class KotakBankStatements(models.Model):
    kotak_bank_statements_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    balance = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    currency_code = models.CharField(max_length=191, blank=True, null=True)
    account_number = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    closing_balance = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    transaction_mode = models.CharField(max_length=191, blank=True, null=True)
    transaction_id = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    date = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kotak_bank_statements'


class KotakBankingNodalStatements(models.Model):
    kotak_banking_nodal_statements_id = models.AutoField(primary_key=True)
    txn_date = models.CharField(max_length=191, blank=True, null=True)
    txn_ref_no = models.CharField(max_length=191, blank=True, null=True)
    e_coll_ac_no = models.CharField(max_length=191, blank=True, null=True)
    dealer_name = models.CharField(max_length=191, blank=True, null=True)
    master_ac_no = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bene_cust_acname = models.CharField(max_length=191, blank=True, null=True)
    send_cust_acname = models.CharField(max_length=191, blank=True, null=True)
    send_cust_ac_no = models.CharField(max_length=191, blank=True, null=True)
    remit_info = models.TextField(blank=True, null=True)
    snd_brn_ifsc = models.CharField(max_length=191, blank=True, null=True)
    credit_time = models.CharField(max_length=191, blank=True, null=True)
    ref1 = models.CharField(max_length=191, blank=True, null=True)
    ref2 = models.CharField(max_length=191, blank=True, null=True)
    ref3 = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kotak_banking_nodal_statements'


class KotakExternalFundTransferFiles(models.Model):
    kotak_external_fund_transfer_files_id = models.AutoField(primary_key=True)
    external_fund_transactions_id = models.IntegerField(blank=True, null=True)
    request_file_name = models.CharField(max_length=191, blank=True, null=True)
    request_file_generation_time = models.DateTimeField(blank=True, null=True)
    response_file_name = models.CharField(max_length=191, blank=True, null=True)
    response_file_received_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kotak_external_fund_transfer_files'


class KotakMapContactSettlementFiles(models.Model):
    kotak_map_contact_settlement_files_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    map_contacts_marketplace_payouts_id = models.IntegerField()
    request_file = models.CharField(max_length=191, blank=True, null=True)
    response_file = models.CharField(max_length=191, blank=True, null=True)
    request_data = models.TextField(blank=True, null=True)
    response_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kotak_map_contact_settlement_files'


class KotakMerchantSettlementFiles(models.Model):
    kotak_merchant_settlement_files_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    merchant_settlements_id = models.IntegerField()
    request_file = models.CharField(max_length=191, blank=True, null=True)
    response_file = models.CharField(max_length=191, blank=True, null=True)
    request_data = models.TextField(blank=True, null=True)
    response_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kotak_merchant_settlement_files'


class KotakNodalStatementsHistories(models.Model):
    kotak_banking_nodal_statements_id = models.AutoField(primary_key=True)
    txn_date = models.CharField(max_length=191, blank=True, null=True)
    txn_ref_no = models.CharField(max_length=191, blank=True, null=True)
    e_coll_ac_no = models.CharField(max_length=191, blank=True, null=True)
    dealer_name = models.CharField(max_length=191, blank=True, null=True)
    master_ac_no = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bene_cust_acname = models.CharField(max_length=191, blank=True, null=True)
    send_cust_acname = models.CharField(max_length=191, blank=True, null=True)
    send_cust_ac_no = models.CharField(max_length=191, blank=True, null=True)
    remit_info = models.TextField(blank=True, null=True)
    snd_brn_ifsc = models.CharField(max_length=191, blank=True, null=True)
    credit_time = models.CharField(max_length=191, blank=True, null=True)
    ref1 = models.CharField(max_length=191, blank=True, null=True)
    ref2 = models.CharField(max_length=191, blank=True, null=True)
    ref3 = models.CharField(max_length=191, blank=True, null=True)
    file_name = models.CharField(max_length=191, blank=True, null=True)
    date_of_upload = models.DateTimeField(blank=True, null=True)
    execution_type = models.CharField(max_length=191, blank=True, null=True)
    errors = models.TextField(blank=True, null=True)
    is_successfull = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kotak_nodal_statements_histories'


class KotakResponseFileData(models.Model):
    kotak_response_file_data_id = models.AutoField(primary_key=True)
    internal_transaction_ref_id = models.IntegerField(blank=True, null=True)
    client_code = models.CharField(max_length=191, blank=True, null=True)
    product_code = models.CharField(max_length=191, blank=True, null=True)
    payment_type = models.CharField(max_length=191, blank=True, null=True)
    payment_date = models.CharField(max_length=191, blank=True, null=True)
    instrument_date = models.CharField(max_length=191, blank=True, null=True)
    dr_ac_no = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bank_code_indicator = models.CharField(max_length=191, blank=True, null=True)
    beneficiary_name = models.CharField(max_length=250, blank=True, null=True)
    ifsc_code = models.CharField(max_length=191, blank=True, null=True)
    beneficiary_ac_no = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    response_time = models.CharField(max_length=191, blank=True, null=True)
    kotak_internal_reference_number = models.CharField(max_length=191, blank=True, null=True)
    utr_number = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kotak_response_file_data'


class KotakToFedralTransactionDetails(models.Model):
    kotak_to_fedral_trans_id = models.AutoField(primary_key=True)
    card_balance_histories_mapping_ids = models.TextField()
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    payment_date = models.CharField(max_length=191)
    transaction_type = models.CharField(max_length=191)
    ref_id = models.CharField(max_length=200, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    debit_account_no = models.CharField(max_length=191)
    recipient_name = models.CharField(max_length=191)
    ifsc_code = models.CharField(max_length=191)
    beneficiary_account_no = models.CharField(max_length=191)
    bank_transaction_status = models.CharField(max_length=191, blank=True, null=True)
    response_time = models.CharField(max_length=191, blank=True, null=True)
    kotak_internal_ref_no = models.CharField(max_length=191, blank=True, null=True)
    utr_no = models.CharField(max_length=191, blank=True, null=True)
    request_file_path = models.TextField(blank=True, null=True)
    response_file_path = models.TextField(blank=True, null=True)
    is_processed = models.IntegerField(blank=True, null=True)
    previous_transaction_id = models.IntegerField(blank=True, null=True)
    admin_users_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kotak_to_fedral_transaction_details'


class KotakVaFileGenerations(models.Model):
    kotak_va_file_generations_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=191)
    apac = models.CharField(max_length=191)
    distributor_code = models.CharField(max_length=191)
    distributor_name = models.CharField(max_length=191)
    debit_narration = models.IntegerField()
    credit_narration = models.IntegerField()
    email = models.CharField(max_length=191)
    mobile = models.CharField(max_length=191)
    other_info1 = models.CharField(max_length=191)
    other_info2 = models.CharField(max_length=191)
    remarks = models.CharField(max_length=191)
    map_virtual_apac = models.CharField(max_length=191)
    is_file_generated = models.IntegerField()
    is_account_mapped = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kotak_va_file_generations'


class KotakVirtualAccountNumbers(models.Model):
    kotak_virtual_account_numbers_id = models.AutoField(primary_key=True)
    company_va = models.CharField(max_length=191)
    beneficiary_va = models.CharField(max_length=191)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kotak_virtual_account_numbers'


class L1Categories(models.Model):
    l1_categories_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'l1_categories'


class L2Categories(models.Model):
    l2_categories_id = models.AutoField(primary_key=True)
    l1_categories_id = models.IntegerField()
    name = models.CharField(max_length=128)
    description = models.TextField()
    invoice_view = models.IntegerField()
    qc_view = models.IntegerField()
    bill_view = models.IntegerField()
    ft_view = models.IntegerField()
    withdraw_view = models.IntegerField()
    transaction_view = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'l2_categories'


class L3Categories(models.Model):
    l3_categories_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField()
    l1_categories_id = models.IntegerField(blank=True, null=True)
    l2_categories_id = models.IntegerField(blank=True, null=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    partner_banks_id = models.IntegerField(blank=True, null=True)
    link_types_id = models.IntegerField(blank=True, null=True)
    open_bank_accounts_id = models.IntegerField(blank=True, null=True)
    account_number = models.IntegerField(blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)
    ledger_entries_master_id = models.IntegerField(blank=True, null=True)
    tds_rate = models.FloatField(blank=True, null=True)
    tds_categories_id = models.IntegerField(blank=True, null=True)
    is_updated = models.IntegerField()
    is_deleted = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    contacts_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'l3_categories'


class LayerApiCalls(models.Model):
    layer_api_calls_id = models.AutoField(primary_key=True)
    request_id = models.CharField(max_length=191, blank=True, null=True)
    open_accounts_id = models.IntegerField()
    open_companies_id = models.IntegerField()
    open_users_id = models.IntegerField()
    user_accounts_id = models.IntegerField()
    user_companies_id = models.IntegerField()
    user_users_id = models.IntegerField()
    payment_purposes_id = models.IntegerField(blank=True, null=True)
    api_name = models.TextField(blank=True, null=True)
    api_url = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    contact_number = models.CharField(max_length=191, blank=True, null=True)
    email_id = models.CharField(max_length=191, blank=True, null=True)
    currency = models.CharField(max_length=191, blank=True, null=True)
    mtx = models.CharField(max_length=191, blank=True, null=True)
    payment_id = models.CharField(max_length=191, blank=True, null=True)
    payment_token = models.CharField(max_length=191, blank=True, null=True)
    payment_status = models.CharField(max_length=191, blank=True, null=True)
    udf = models.TextField(blank=True, null=True)
    request_header = models.TextField(blank=True, null=True)
    request_body = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    response_code = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layer_api_calls'


class LayerPaymentStatus(models.Model):
    layer_payment_status_id = models.AutoField(primary_key=True)
    layer_payment_status_name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layer_payment_status'


class LeadManagementGoogleAnalytics(models.Model):
    lead_management_google_analytics_id = models.AutoField(primary_key=True)
    utm_parameter = models.CharField(max_length=191, blank=True, null=True)
    utm_value = models.CharField(max_length=300, blank=True, null=True)
    users_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lead_management_google_analytics'


class LendingBankStatements(models.Model):
    statements_id = models.AutoField(primary_key=True)
    lending = models.ForeignKey('Lendings', models.DO_NOTHING)
    companies_id = models.IntegerField()
    users_id = models.PositiveIntegerField()
    application_id = models.IntegerField(blank=True, null=True)
    accounts_id = models.IntegerField()
    account_type = models.CharField(max_length=191, blank=True, null=True)
    encoded = models.TextField()
    document_id = models.CharField(max_length=200, blank=True, null=True)
    bank_name = models.CharField(max_length=200, blank=True, null=True)
    isprimaryacc = models.IntegerField(db_column='isPrimaryAcc', blank=True, null=True)  # Field name made lowercase.
    service_name = models.CharField(max_length=200, blank=True, null=True)
    document_name = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    stage_id = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lending_bank_statements'


class LendingLineDetail(models.Model):
    line_detail_id = models.AutoField(primary_key=True)
    lending_id = models.IntegerField(blank=True, null=True)
    nbfc_app_id = models.IntegerField(blank=True, null=True)
    loan_type_id = models.IntegerField(blank=True, null=True)
    line_detail_info = models.TextField(db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lending_line_detail'


class LendingLocTransactions(models.Model):
    lending_loc_transactions_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    debit_account_number = models.CharField(max_length=50, blank=True, null=True)
    source_type = models.CharField(max_length=50, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    bank_transaction_status_id = models.IntegerField(blank=True, null=True)
    internal_transaction_ref_id = models.CharField(max_length=50, blank=True, null=True)
    bene_account_number = models.CharField(max_length=50, blank=True, null=True)
    bene_name = models.CharField(max_length=200, blank=True, null=True)
    bene_ifsc = models.CharField(max_length=20, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    cid = models.CharField(max_length=100, blank=True, null=True)
    uid = models.CharField(max_length=100, blank=True, null=True)
    urn = models.CharField(max_length=100, blank=True, null=True)
    aggr_id = models.CharField(max_length=100, blank=True, null=True)
    aggr_name = models.CharField(max_length=100, blank=True, null=True)
    utr_number = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lending_loc_transactions'


class LendingOnboarding(models.Model):
    lending_onboarding_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    company_id = models.IntegerField()
    lending_id = models.IntegerField()
    iec = models.CharField(max_length=100, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    uan = models.CharField(max_length=100, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    aadhar_number = models.CharField(max_length=100, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    shop_est_reg_no = models.CharField(max_length=100, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    shop_est_area_code = models.CharField(max_length=10, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    fssai_reg_no = models.CharField(max_length=100, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    cas_accounts_id = models.TextField(db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    card_activated = models.IntegerField(blank=True, null=True)
    show_consent = models.IntegerField(blank=True, null=True)
    done_consent = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lending_onboarding'


class LendingOnboardingDocTypes(models.Model):
    lending_onboarding_doc_type_id = models.AutoField(primary_key=True)
    doc_type_key = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci')
    doc_type_name = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci')
    is_personal_doc = models.IntegerField(blank=True, null=True)
    is_business_doc = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lending_onboarding_doc_types'


class LendingRepayment(models.Model):
    lending_repay_id = models.AutoField(primary_key=True)
    sub_loan_id = models.IntegerField(blank=True, null=True)
    lending_id = models.IntegerField()
    nbfc_app_id = models.IntegerField()
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    transaction_id = models.CharField(max_length=100, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    payment_token = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    arzoo_repay_loan_id = models.IntegerField(blank=True, null=True)
    bank_transaction_status_id = models.IntegerField(blank=True, null=True)
    nbfc_transaction_status_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lending_repayment'


class LendingStatusMasters(models.Model):
    lending_status_masters_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lending_status_masters'


class LicenceSummary(models.Model):
    licence_summary_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    transaction_to_users_id = models.IntegerField(blank=True, null=True)
    licence_type = models.CharField(max_length=3, blank=True, null=True)
    transaction_type = models.CharField(max_length=8, blank=True, null=True)
    in_qty = models.IntegerField(blank=True, null=True)
    out_qty = models.IntegerField(blank=True, null=True)
    closing_qty = models.IntegerField(blank=True, null=True)
    type_based_total_qty = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    subscription_packages_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'licence_summary'


class LicenseUrlSettings(models.Model):
    license_url_settings_id = models.AutoField(primary_key=True)
    license_length = models.IntegerField()
    license_validity_months = models.IntegerField()
    license_package_limit = models.IntegerField()
    subscription_package_id = models.IntegerField()
    user_discount_price = models.DecimalField(max_digits=8, decimal_places=2)
    commission_perc = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'license_url_settings'


class LinkTypes(models.Model):
    link_types_id = models.AutoField(primary_key=True)
    link_type = models.CharField(max_length=200)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_types'


class LiveAccountBalanceHistories(models.Model):
    live_account_balance_histories_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField(blank=True, null=True)
    partner_banks_id = models.IntegerField()
    current_balance = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    type = models.CharField(max_length=2)
    ref_id = models.CharField(max_length=191)
    is_reversal = models.IntegerField()
    remarks = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'live_account_balance_histories'


class LiveAccountBalances(models.Model):
    live_account_balances_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField(blank=True, null=True)
    partner_banks_id = models.IntegerField()
    current_balance = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    closing_balance = models.DecimalField(max_digits=14, decimal_places=2)
    last_closing_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'live_account_balances'


class LiveSandboxUsers(models.Model):
    live_sandbox_users_id = models.AutoField(primary_key=True)
    live_users_id = models.IntegerField()
    live_companies_id = models.IntegerField(blank=True, null=True)
    sandbox_users_id = models.IntegerField()
    sandbox_companies_id = models.IntegerField()
    sandbox_accounts_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'live_sandbox_users'


class LoanTypes(models.Model):
    loan_types_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loan_types'


class Loans(models.Model):
    loans_id = models.AutoField(primary_key=True)
    application_number = models.CharField(max_length=191)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    first_name = models.CharField(max_length=191)
    last_name = models.CharField(max_length=191)
    company_name = models.CharField(max_length=191)
    loan_type = models.CharField(max_length=191)
    year_in_business = models.CharField(max_length=191, db_collation='utf8mb4_general_ci')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    turnover = models.DecimalField(max_digits=12, decimal_places=2)
    pan_number = models.CharField(max_length=191)
    business_pan_number = models.CharField(max_length=30)
    gst_number = models.CharField(max_length=191)
    nature_of_bussiness = models.CharField(max_length=191)
    vintage_month = models.CharField(max_length=30, blank=True, null=True)
    vintage_year = models.CharField(max_length=50, blank=True, null=True)
    industry = models.CharField(max_length=191)
    dob = models.DateField()
    application_date = models.DateTimeField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loans'


class LogAxisBankFundTransfers(models.Model):
    log_axis_bank_fund_transfers_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    request_url = models.TextField()
    request = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_axis_bank_fund_transfers'


class LogAxisBeneficiaryRegistrations(models.Model):
    log_axis_beneficiary_registrations_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    request_url = models.TextField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_axis_beneficiary_registrations'


class LogAxisCallbacks(models.Model):
    log_axis_callbacks_id = models.AutoField(primary_key=True)
    encrypted_callback = models.TextField(blank=True, null=True)
    decrypted_callback = models.TextField(blank=True, null=True)
    encoded_decrypted_callback = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_axis_callbacks'


class LogAxisDvBeneficiaryRegistrations(models.Model):
    log_axis_dv_beneficiary_registrations_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    encrypted_request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_axis_dv_beneficiary_registrations'


class LogAxisDvFundTransfers(models.Model):
    log_axis_dv_fund_transfers_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    encrypted_request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_axis_dv_fund_transfers'


class LogAxisDvOneTimeRegistrations(models.Model):
    log_axis_dv_one_time_registrations_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    encrypted_request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_axis_dv_one_time_registrations'


class LogAxisOneTimeRegistrations(models.Model):
    log_axis_one_time_registrations_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    request_url = models.TextField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_axis_one_time_registrations'


class LogDcbConnectedBalances(models.Model):
    log_dcb_connected_balances_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    requestuuid = models.CharField(db_column='requestUUID', max_length=191, blank=True, null=True)  # Field name made lowercase.
    otp = models.CharField(max_length=191, blank=True, null=True)
    refno = models.CharField(db_column='refNo', max_length=191, blank=True, null=True)  # Field name made lowercase.
    accountnumber = models.CharField(db_column='accountNumber', max_length=191, blank=True, null=True)  # Field name made lowercase.
    uniqueid = models.CharField(db_column='uniqueID', max_length=191, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(max_length=191, blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_dcb_connected_balances'


class LogDcbConnectedFundTransfers(models.Model):
    log_dcb_connected_fund_transfers_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    cifid = models.CharField(db_column='cifId', max_length=191, blank=True, null=True)  # Field name made lowercase.
    requestuuid = models.CharField(db_column='requestUUID', max_length=191, blank=True, null=True)  # Field name made lowercase.
    sessionid = models.CharField(db_column='sessionId', max_length=191, blank=True, null=True)  # Field name made lowercase.
    otp = models.CharField(max_length=191, blank=True, null=True)
    refno = models.CharField(db_column='refNo', max_length=191, blank=True, null=True)  # Field name made lowercase.
    accountnumber = models.CharField(db_column='accountNumber', max_length=191, blank=True, null=True)  # Field name made lowercase.
    uniqueid = models.CharField(db_column='uniqueID', max_length=191, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(max_length=191, blank=True, null=True)
    ifsccode = models.CharField(db_column='ifscCode', max_length=191, blank=True, null=True)  # Field name made lowercase.
    beneaccountnumber = models.CharField(db_column='beneAccountNumber', max_length=191, blank=True, null=True)  # Field name made lowercase.
    beneficiaryname = models.CharField(db_column='beneficiaryName', max_length=191, blank=True, null=True)  # Field name made lowercase.
    transfermode = models.CharField(db_column='transferMode', max_length=191, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    txndate = models.CharField(db_column='txnDate', max_length=191, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(max_length=191, blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_dcb_connected_fund_transfers'


class LogDcbConnectedGetAllAccounts(models.Model):
    log_dcb_connected_get_all_accounts_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    requestuuid = models.CharField(db_column='requestUUID', max_length=191, blank=True, null=True)  # Field name made lowercase.
    uniqueid = models.CharField(db_column='uniqueID', max_length=191, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(max_length=191, blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_dcb_connected_get_all_accounts'


class LogDcbConnectedGetTokens(models.Model):
    log_dcb_connected_get_tokens_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    cifid = models.CharField(db_column='cifId', max_length=191, blank=True, null=True)  # Field name made lowercase.
    requestuuid = models.CharField(db_column='requestUUID', max_length=191, blank=True, null=True)  # Field name made lowercase.
    uniqueid = models.CharField(db_column='uniqueID', max_length=191, blank=True, null=True)  # Field name made lowercase.
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_dcb_connected_get_tokens'


class LogDcbConnectedOtps(models.Model):
    log_dcb_connected_otps_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    cifid = models.CharField(db_column='cifId', max_length=191, blank=True, null=True)  # Field name made lowercase.
    requestuuid = models.CharField(db_column='requestUUID', max_length=191, blank=True, null=True)  # Field name made lowercase.
    uniqueid = models.CharField(db_column='uniqueID', max_length=191, blank=True, null=True)  # Field name made lowercase.
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_dcb_connected_otps'


class LogDcbConnectedPaymentStatuses(models.Model):
    log_dcb_connected_payment_status_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    cifid = models.CharField(db_column='cifId', max_length=191, blank=True, null=True)  # Field name made lowercase.
    requestuuid = models.CharField(db_column='requestUUID', max_length=191, blank=True, null=True)  # Field name made lowercase.
    languageid = models.IntegerField(db_column='languageId', blank=True, null=True)  # Field name made lowercase.
    sversion = models.CharField(db_column='sVersion', max_length=191, blank=True, null=True)  # Field name made lowercase.
    txnamount = models.DecimalField(db_column='txnAmount', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    txnstatus = models.CharField(db_column='txnStatus', max_length=191, blank=True, null=True)  # Field name made lowercase.
    txndate = models.CharField(db_column='txnDate', max_length=191, blank=True, null=True)  # Field name made lowercase.
    reqnetwork = models.CharField(db_column='reqNetwork', max_length=191, blank=True, null=True)  # Field name made lowercase.
    uniqueid = models.CharField(db_column='uniqueID', max_length=191, blank=True, null=True)  # Field name made lowercase.
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_dcb_connected_payment_statuses'


class LogDcbConnectedRegisters(models.Model):
    log_dcb_connected_registers_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    unique_id = models.CharField(max_length=191, blank=True, null=True)
    register_url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_dcb_connected_registers'


class LogEcwidRequests(models.Model):
    log_ecwid_requests_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    companies_id = models.IntegerField()
    request = models.CharField(max_length=255, blank=True, null=True)
    response = models.CharField(max_length=255, blank=True, null=True)
    request_type = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.CharField(max_length=255)
    updated_at = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_ecwid_requests'


class LogEquitasBankConnectedBankingLeads(models.Model):
    log_equitas_bank_connected_banking_leads_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    transaction_id = models.CharField(max_length=191)
    customer_id = models.CharField(max_length=191, blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    request_type = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_equitas_bank_connected_banking_leads'


class LogEquitasBankConnectedBankingNeftFundTransfers(models.Model):
    log_equitas_bank_connected_banking_neft_fund_transfers_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    transaction_id = models.CharField(max_length=191)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    transaction_type = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_equitas_bank_connected_banking_neft_fund_transfers'


class LogEquitasNriSavingsAccountLeads(models.Model):
    log_equitas_nri_savings_account_leads_id = models.AutoField(primary_key=True)
    mobile_number = models.CharField(max_length=191)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    request_type = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_equitas_nri_savings_account_leads'


class LogExternalWebhooks(models.Model):
    log_external_webhooks_id = models.AutoField(primary_key=True)
    module = models.CharField(max_length=191)
    request_uri = models.CharField(max_length=191)
    order_id = models.CharField(max_length=191, blank=True, null=True)
    raw_data = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_external_webhooks'


class LogGstSearchBasisPans(models.Model):
    log_gst_search_basis_pans_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_gst_search_basis_pans'


class LogIciciAccountOpenings(models.Model):
    log_icici_account_openings_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    request = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_icici_account_openings'


class LogIciciCompositePayoutUpi(models.Model):
    log_icici_composite_payout_upi_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    seq_no = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    payee_va = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    request = models.TextField(db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    encrypted_request = models.TextField(db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    response = models.TextField(db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    decrypted_response = models.TextField(db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_icici_composite_payout_upi'


class LogIciciConnectedBalances(models.Model):
    log_icici_connected_balances_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    response = models.CharField(max_length=191, blank=True, null=True)
    aggr_id = models.CharField(max_length=191, blank=True, null=True)
    corp_id = models.CharField(max_length=191, blank=True, null=True)
    user_id = models.CharField(max_length=191, blank=True, null=True)
    urn = models.CharField(max_length=191, blank=True, null=True)
    account_no = models.CharField(max_length=191, blank=True, null=True)
    date = models.CharField(max_length=191, blank=True, null=True)
    effective_balance = models.DecimalField(max_digits=20, decimal_places=2)
    currency = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_icici_connected_balances'


class LogIciciConnectedRegister(models.Model):
    log_icici_connected_register_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    account_no = models.CharField(max_length=191, blank=True, null=True)
    response = models.CharField(max_length=191, blank=True, null=True)
    message = models.CharField(max_length=191, blank=True, null=True)
    corp_id = models.CharField(max_length=191, blank=True, null=True)
    user_id = models.CharField(max_length=191, blank=True, null=True)
    aggr_id = models.CharField(max_length=191, blank=True, null=True)
    aggr_name = models.CharField(max_length=191, blank=True, null=True)
    urn = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    account_linked = models.CharField(max_length=191)
    account_status = models.CharField(max_length=191)
    account_type = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_icici_connected_register'


class LogIciciConnectedStatements(models.Model):
    log_icici_connected_statements_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    urn = models.CharField(db_column='URN', max_length=191, blank=True, null=True)  # Field name made lowercase.
    aggr_id = models.CharField(db_column='AGGR_ID', max_length=191, blank=True, null=True)  # Field name made lowercase.
    corp_id = models.CharField(db_column='CORP_ID', max_length=191, blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=191, blank=True, null=True)  # Field name made lowercase.
    valuedate = models.CharField(db_column='VALUEDATE', max_length=191, blank=True, null=True)  # Field name made lowercase.
    amount = models.CharField(db_column='AMOUNT', max_length=191, blank=True, null=True)  # Field name made lowercase.
    chequeno = models.CharField(db_column='CHEQUENO', max_length=191, blank=True, null=True)  # Field name made lowercase.
    txndate = models.CharField(db_column='TXNDATE', max_length=191, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='REMARKS', max_length=191, blank=True, null=True)  # Field name made lowercase.
    transactionid = models.CharField(db_column='TRANSACTIONID', max_length=191, blank=True, null=True)  # Field name made lowercase.
    hash = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(db_column='TYPE', max_length=191, blank=True, null=True)  # Field name made lowercase.
    balance = models.CharField(db_column='BALANCE', max_length=191, blank=True, null=True)  # Field name made lowercase.
    response = models.CharField(db_column='RESPONSE', max_length=191, blank=True, null=True)  # Field name made lowercase.
    accountno = models.CharField(db_column='ACCOUNTNO', max_length=191, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_icici_connected_statements'


class LogIciciConnectedTransactions(models.Model):
    log_icici_connected_transactions_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    corp_id = models.CharField(max_length=191, blank=True, null=True)
    user_id = models.CharField(max_length=191, blank=True, null=True)
    debit_ac = models.CharField(max_length=191, blank=True, null=True)
    credit_ac = models.CharField(max_length=191, blank=True, null=True)
    ifsc = models.CharField(max_length=191, blank=True, null=True)
    amount = models.CharField(max_length=191, blank=True, null=True)
    txn_type = models.CharField(max_length=191, blank=True, null=True)
    urn = models.CharField(max_length=191, blank=True, null=True)
    payee_name = models.CharField(max_length=191, blank=True, null=True)
    unique_id = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.CharField(max_length=191, blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_icici_connected_transactions'


class LogIciciInstaOdGuestLogins(models.Model):
    created_at = models.DateTimeField()
    name = models.CharField(max_length=191)
    email = models.CharField(max_length=191)
    mobile = models.CharField(max_length=191)
    sourceflag = models.CharField(db_column='sourceFlag', max_length=191)  # Field name made lowercase.
    constitution = models.CharField(max_length=191)
    request = models.TextField()
    response_raw = models.TextField()
    response = models.TextField()

    class Meta:
        managed = False
        db_table = 'log_icici_insta_od_guest_logins'


class LogIciciInstaOdOtpLopOffers(models.Model):
    log_icici_insta_od_otp_lop_offers_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    icici_insta_od_otp_lop_offers_id = models.IntegerField()
    api = models.CharField(max_length=191)
    plain_request = models.TextField()
    encrypt_request = models.TextField()
    encrypt_response = models.TextField()
    decrypt_response = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_icici_insta_od_otp_lop_offers'


class LogIciciInstaodApply(models.Model):
    log_icici_instaod_apply_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    source_flag = models.CharField(max_length=191)
    max_offer_amount = models.CharField(max_length=191)
    kyc_flag = models.CharField(max_length=191)
    account_no = models.CharField(max_length=191)
    pq_flg = models.CharField(max_length=191)
    adb = models.CharField(max_length=191)
    name = models.CharField(max_length=191)
    email = models.CharField(max_length=191)
    unsecured_exposure = models.CharField(max_length=191)
    spo_flag = models.CharField(max_length=191)
    mobile_no = models.CharField(max_length=191)
    ucc = models.CharField(max_length=191)
    mec_score = models.CharField(max_length=191)
    request = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_icici_instaod_apply'


class LogIciciInstaodCibLop(models.Model):
    log_icici_instaod_cib_lop_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    cid = models.CharField(max_length=191)
    uid = models.CharField(max_length=191)
    urn = models.CharField(max_length=191)
    account_no = models.CharField(max_length=191)
    request = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_icici_instaod_cib_lop'


class LogIciciOtps(models.Model):
    log_icici_otp_id = models.AutoField(primary_key=True)
    ref_no = models.CharField(max_length=191)
    request = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_icici_otps'


class LogIciciPennyDropP2As(models.Model):
    log_icici_penny_drop_p2as_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    bene_acc_no = models.CharField(max_length=191)
    bene_ifsc = models.CharField(max_length=191)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    tran_ref_no = models.CharField(max_length=191)
    payment_ref = models.CharField(max_length=191)
    rem_name = models.CharField(max_length=191)
    rem_mobile = models.CharField(max_length=191)
    retailer_code = models.CharField(max_length=191)
    transaction_date = models.CharField(max_length=191)
    request = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_icici_penny_drop_p2as'


class LogIciciPennyDropTransacionalInquiries(models.Model):
    log_icici_penny_drop_transacional_inquiries_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    tran_ref_no = models.CharField(max_length=191)
    request = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_icici_penny_drop_transacional_inquiries'


class LogIciciPrepaidCards(models.Model):
    log_icici_prepaid_cards_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    request_reference_number = models.IntegerField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_icici_prepaid_cards'


class LogIciciTaxPayments(models.Model):
    log_icici_tax_payments_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    encrypted_request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    decrypted_response = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_icici_tax_payments'


class LogIciciUpiCreateMandates(models.Model):
    log_icici_upi_create_mandates_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_icici_upi_create_mandates'


class LogIciciUpiExecuteMandateTransactionStatus(models.Model):
    log_icici_upi_execute_mandate_transaction_status_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    encrypted_request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    decrypted_response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_icici_upi_execute_mandate_transaction_status'


class LogIciciUpiExecuteMandates(models.Model):
    log_icici_upi_execute_mandates_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    encrypted_request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    decrypted_response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_icici_upi_execute_mandates'


class LogIciciUpiMandateNotificationTransactionStatus(models.Model):
    log_icici_upi_mandate_notification_transaction_status_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    encrypted_request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    decrypted_response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_icici_upi_mandate_notification_transaction_status'


class LogIciciUpiMandateTrasactionStatuses(models.Model):
    log_icici_upi_mandate_trasaction_statuses_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    encrypted_request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    decrypted_response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_icici_upi_mandate_trasaction_statuses'


class LogIciciUpiNotificationMandates(models.Model):
    log_icici_upi_notification_mandates_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    encrypted_request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    decrypted_response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_icici_upi_notification_mandates'


class LogIciciUpiRevokeMandates(models.Model):
    log_icici_upi_revoke_mandates_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    encrypted_request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    decrypted_response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_icici_upi_revoke_mandates'


class LogIdfcConnectedBankings(models.Model):
    log_idfc_connected_bankings_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    transaction_id = models.CharField(max_length=191, blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    request_type = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_idfc_connected_bankings'


class LogIdfcConnectedFundTransfers(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_idfc_connected_fund_transfers'


class LogKarzaAadharVerification(models.Model):
    log_karza_aadhar_verification_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    request = models.TextField()
    response = models.TextField()
    api_mode = models.CharField(max_length=100)
    merchant_ref_id = models.CharField(max_length=191, blank=True, null=True)
    is_enterprise = models.IntegerField()
    latitude = models.CharField(max_length=191, blank=True, null=True)
    longitude = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_karza_aadhar_verification'
        unique_together = (('companies_id', 'merchant_ref_id'),)


class LogKarzaCinAuthentication(models.Model):
    log_karza_cin_authentication_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    request_id = models.CharField(max_length=191, blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    cin = models.CharField(max_length=191, blank=True, null=True)
    status_code = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_karza_cin_authentication'


class LogKarzaCompanyLlpIdentifications(models.Model):
    log_karza_company_llp_identifications_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    request = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_karza_company_llp_identifications'


class LogKarzaCompanySearches(models.Model):
    log_karza_company_searches_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    request = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_karza_company_searches'


class LogKarzaGstinAuthentication(models.Model):
    log_karza_gstin_authentication_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    request_id = models.CharField(max_length=191, blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    status_code = models.IntegerField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    gstin = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_karza_gstin_authentication'


class LogKarzaKycOcrs(models.Model):
    log_karza_kyc_ocrs_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    request = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_karza_kyc_ocrs'


class LogKarzaMcaSignatories(models.Model):
    log_karza_mca_signatories_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    request = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    request_id = models.CharField(max_length=191, blank=True, null=True)
    status_code = models.IntegerField(blank=True, null=True)
    cin = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_karza_mca_signatories'


class LogLendingApiCalls(models.Model):
    log_lending_api_calls_id = models.AutoField(primary_key=True)
    lending_id = models.IntegerField()
    nbfc_partner_banks_id = models.IntegerField(blank=True, null=True)
    service_name = models.CharField(max_length=200)
    active_cron = models.IntegerField()
    request_url = models.TextField()
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_lending_api_calls'


class LogNpciRequests(models.Model):
    log_npci_requests_id = models.BigAutoField(primary_key=True)
    consumer_ref_num = models.CharField(max_length=255)
    mandate_request_id = models.CharField(max_length=255, blank=True, null=True)
    mandate_ref_num = models.CharField(max_length=191, blank=True, null=True)
    request_type = models.CharField(max_length=255)
    request = models.TextField()
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_npci_requests'


class LogSignzyAadharVerification(models.Model):
    log_signzy_aadhar_verification_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    request = models.TextField()
    response = models.TextField(blank=True, null=True)
    api_mode = models.CharField(max_length=200, blank=True, null=True)
    transaction_id = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_signzy_aadhar_verification'


class LogYesBankBeneAdditions(models.Model):
    log_yes_bank_bene_additions_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    contacts_id = models.IntegerField(blank=True, null=True)
    bene_account_number = models.CharField(max_length=191, blank=True, null=True)
    bene_code = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_yes_bank_bene_additions'


class LogYesBankConnectedBankingFundTransfers(models.Model):
    log_yes_bank_connected_banking_fund_transfers_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    app_id = models.CharField(max_length=191)
    customer_id = models.CharField(max_length=191)
    request_reference_no = models.CharField(max_length=191, blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_yes_bank_connected_banking_fund_transfers'


class LogYesBankConnectedBankingGetBalances(models.Model):
    log_yes_bank_connected_banking_get_balances_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    app_id = models.CharField(max_length=191)
    customer_id = models.CharField(max_length=191)
    request = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_yes_bank_connected_banking_get_balances'


class LogYesBankConnectedBankingGetStatuses(models.Model):
    log_yes_bank_connected_banking_get_statuses_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    app_id = models.CharField(max_length=191)
    customer_id = models.CharField(max_length=191)
    request_reference_no = models.CharField(max_length=191, blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_yes_bank_connected_banking_get_statuses'


class LogYesBankCreateLeads(models.Model):
    log_yes_bank_create_leads_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField(blank=True, null=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_yes_bank_create_leads'


class LogYesBankFts(models.Model):
    log_yes_bank_fts_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    contacts_id = models.IntegerField(blank=True, null=True)
    bene_account_number = models.CharField(max_length=191, blank=True, null=True)
    bene_code = models.CharField(max_length=191, blank=True, null=True)
    uniquerequestno = models.CharField(db_column='uniqueRequestNo', max_length=191, blank=True, null=True)  # Field name made lowercase.
    internal_transaction_ref_id = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_yes_bank_fts'


class LogYesBankGetLeadStatuses(models.Model):
    log_yes_bank_get_lead_statuses_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField(blank=True, null=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_yes_bank_get_lead_statuses'


class LogYesBankUpiPayouts(models.Model):
    link_id = models.CharField(max_length=191)
    link_attribute_name = models.CharField(max_length=191, blank=True, null=True)
    action = models.CharField(max_length=191, blank=True, null=True)
    request_log = models.TextField(blank=True, null=True)
    response_log = models.TextField(blank=True, null=True)
    debug_info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_yes_bank_upi_payouts'


class LogYesBankVpaCreations(models.Model):
    log_yes_bank_vpa_creations_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    sub_merchant_id = models.CharField(max_length=191, blank=True, null=True)
    vpa = models.CharField(max_length=191)
    mcc = models.CharField(max_length=191, blank=True, null=True)
    pan = models.CharField(max_length=191, blank=True, null=True)
    gst_num = models.CharField(max_length=191, blank=True, null=True)
    callback_url_1 = models.CharField(max_length=191, blank=True, null=True)
    callback_url_2 = models.CharField(max_length=191, blank=True, null=True)
    merchant_business_name = models.CharField(max_length=191, blank=True, null=True)
    business_type = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    external_mid = models.CharField(max_length=191, blank=True, null=True)
    external_tid = models.CharField(max_length=191, blank=True, null=True)
    mobile = models.CharField(max_length=191, blank=True, null=True)
    city = models.CharField(max_length=191, blank=True, null=True)
    state = models.CharField(max_length=191, blank=True, null=True)
    request_id = models.CharField(max_length=191, blank=True, null=True)
    pincode = models.CharField(max_length=191, blank=True, null=True)
    per_day_txn_count = models.IntegerField(blank=True, null=True)
    per_day_txn_limit = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    per_txn_limit = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_yes_bank_vpa_creations'


class LogYesToKotakInternalTransfers(models.Model):
    log_yes_to_kotak_internal_transfers_id = models.AutoField(primary_key=True)
    debit_account_no = models.CharField(max_length=100, blank=True, null=True)
    beneficiarycode = models.CharField(db_column='beneficiaryCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    transferamount = models.DecimalField(db_column='transferAmount', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=100, blank=True, null=True)
    uniqueresponseno = models.CharField(db_column='uniqueResponseNo', max_length=191, blank=True, null=True)  # Field name made lowercase.
    attemptno = models.CharField(db_column='attemptNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    transfertype = models.CharField(db_column='transferType', max_length=191, blank=True, null=True)  # Field name made lowercase.
    lowbalancealert = models.CharField(db_column='lowBalanceAlert', max_length=100, blank=True, null=True)  # Field name made lowercase.
    statuscode = models.CharField(db_column='statusCode', max_length=191, blank=True, null=True)  # Field name made lowercase.
    substatuscode = models.CharField(db_column='subStatusCode', max_length=191, blank=True, null=True)  # Field name made lowercase.
    bankreferenceno = models.CharField(db_column='bankReferenceNo', max_length=191, blank=True, null=True)  # Field name made lowercase.
    namewithbeneficiarybank = models.CharField(db_column='nameWithBeneficiaryBank', max_length=191, blank=True, null=True)  # Field name made lowercase.
    requestreferenceno = models.CharField(db_column='requestReferenceNo', max_length=191, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_yes_to_kotak_internal_transfers'


class Logs(models.Model):
    instance = models.CharField(max_length=191)
    channel = models.CharField(max_length=191)
    level = models.CharField(max_length=191)
    level_name = models.CharField(max_length=191)
    message = models.TextField()
    remote_addr = models.PositiveIntegerField(blank=True, null=True)
    user_agent = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    source = models.CharField(max_length=191)
    accounts_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    request = models.TextField()
    response = models.TextField()

    class Meta:
        managed = False
        db_table = 'logs'


class LookupTypes(models.Model):
    name = models.CharField(max_length=191)
    description = models.CharField(max_length=191)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lookup_types'


class LookupValues(models.Model):
    name = models.CharField(max_length=191)
    description = models.CharField(max_length=191)
    lookup_type_id = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lookup_values'


class M2PCardTransactions(models.Model):
    m2p_card_transactions_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    entity_id = models.CharField(max_length=200)
    business_id = models.CharField(max_length=199, blank=True, null=True)
    kit_no = models.CharField(max_length=200)
    txn_ref_no = models.CharField(max_length=200)
    external_transaction_id = models.CharField(max_length=399, blank=True, null=True)
    mobile_no = models.CharField(max_length=120, blank=True, null=True)
    auth_code = models.CharField(max_length=199, blank=True, null=True)
    txn_amount = models.DecimalField(max_digits=12, decimal_places=4)
    txn_currency = models.CharField(max_length=100, blank=True, null=True)
    bank_t_id = models.CharField(max_length=199, blank=True, null=True)
    billing_currency = models.CharField(max_length=100, blank=True, null=True)
    merchant_id = models.CharField(max_length=200, blank=True, null=True)
    merchant_name = models.CharField(max_length=200, blank=True, null=True)
    your_wallet = models.CharField(max_length=199, blank=True, null=True)
    merchant_location = models.CharField(max_length=200, blank=True, null=True)
    txn_currency_code = models.CharField(max_length=199, blank=True, null=True)
    txn_date = models.CharField(max_length=200, blank=True, null=True)
    balance = models.CharField(max_length=200, blank=True, null=True)
    bill_ref_no = models.CharField(max_length=199, blank=True, null=True)
    txn_type = models.CharField(max_length=200, blank=True, null=True)
    txn_origin = models.CharField(max_length=199, blank=True, null=True)
    sender_name = models.CharField(max_length=200, blank=True, null=True)
    retrival_reference_no = models.CharField(max_length=199, blank=True, null=True)
    mcc = models.CharField(max_length=200, blank=True, null=True)
    acquirer_id = models.CharField(max_length=199, blank=True, null=True)
    prod_type = models.CharField(max_length=200, blank=True, null=True)
    network_type = models.CharField(max_length=199, blank=True, null=True)
    txn_status = models.CharField(max_length=200, blank=True, null=True)
    txn_desc = models.TextField(blank=True, null=True)
    sor_txn_id = models.CharField(max_length=199, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm2p_card_transactions'


class M2PFederals(models.Model):
    m2p_federals_id = models.AutoField(primary_key=True)
    kit_no = models.CharField(max_length=200)
    card_number = models.CharField(max_length=200)
    is_assigned = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm2p_federals'


class M2PSbmLogs(models.Model):
    m2p_sbm_logs_id = models.AutoField(primary_key=True)
    entity_id = models.CharField(max_length=200)
    api_name = models.CharField(max_length=200)
    request = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm2p_sbm_logs'


class M2PSbmTransactions(models.Model):
    sbm_card_transactions_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    entity_id = models.CharField(max_length=200)
    kit_no = models.CharField(max_length=200)
    txn_ref_no = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=120, blank=True, null=True)
    txn_amount = models.DecimalField(max_digits=12, decimal_places=4)
    txn_currency = models.CharField(max_length=100, blank=True, null=True)
    billing_currency = models.CharField(max_length=100, blank=True, null=True)
    merchant_id = models.CharField(max_length=200, blank=True, null=True)
    merchant_name = models.CharField(max_length=200, blank=True, null=True)
    merchant_location = models.CharField(max_length=200, blank=True, null=True)
    txn_date = models.CharField(max_length=200, blank=True, null=True)
    balance = models.CharField(max_length=200, blank=True, null=True)
    txn_type = models.CharField(max_length=200, blank=True, null=True)
    sender_name = models.CharField(max_length=200, blank=True, null=True)
    mcc = models.CharField(max_length=200, blank=True, null=True)
    prod_type = models.CharField(max_length=200, blank=True, null=True)
    txn_status = models.CharField(max_length=200, blank=True, null=True)
    txn_desc = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm2p_sbm_transactions'


class MakerCheckerActivities(models.Model):
    maker_checker_activities = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    maker_users_id = models.IntegerField()
    checker_users_id = models.IntegerField()
    activities = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maker_checker_activities'


class MakerCheckerApprovals(models.Model):
    maker_checker_approvals_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    team_member_details_id = models.IntegerField()
    mob_stakeholder_details_id = models.IntegerField()
    maker_checker_groups_id = models.IntegerField()
    source = models.CharField(max_length=199, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    txn_ref_no = models.CharField(max_length=199, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    approved_on = models.DateTimeField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maker_checker_approvals'


class MakerCheckerGroups(models.Model):
    maker_checker_groups_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    group_identifier = models.CharField(max_length=100)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    checker_approved_at = models.DateTimeField(blank=True, null=True)
    maker_created_at = models.DateTimeField(blank=True, null=True)
    checker_users_id = models.IntegerField(blank=True, null=True)
    maker_users_id = models.IntegerField(blank=True, null=True)
    admin_maker_checker_statuses_id = models.IntegerField(blank=True, null=True)
    checker_reason = models.TextField(blank=True, null=True)
    maker_reason = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maker_checker_groups'


class MakerCheckerParameters(models.Model):
    maker_checker_parameters_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    parameter_name = models.CharField(max_length=199)
    parameter_criteria = models.CharField(max_length=199)
    amount_range_start = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    amount_range_end = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    no_of_people = models.IntegerField()
    parameter_rule = models.CharField(max_length=199)
    description = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()
    checker_approved_at = models.DateTimeField(blank=True, null=True)
    maker_created_at = models.DateTimeField(blank=True, null=True)
    checker_users_id = models.IntegerField(blank=True, null=True)
    admin_maker_checker_statuses_id = models.IntegerField(blank=True, null=True)
    maker_users_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    maker_reason = models.TextField(blank=True, null=True)
    checker_reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maker_checker_parameters'


class MakerCheckerRuleDetails(models.Model):
    maker_checker_rule_details_id = models.AutoField(primary_key=True)
    maker_checker_parameters_id = models.PositiveIntegerField()
    group_id = models.PositiveIntegerField()
    group_identifier = models.PositiveIntegerField()
    approval_count = models.PositiveIntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maker_checker_rule_details'


class ManualTransactions(models.Model):
    manual_transactions_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    contacts_id = models.IntegerField(blank=True, null=True)
    categories_id = models.IntegerField(blank=True, null=True)
    l3_categories_id = models.IntegerField(blank=True, null=True)
    l1_categories_id = models.IntegerField(blank=True, null=True)
    l2_categories_id = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    balance_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    transaction_mode = models.CharField(max_length=2)
    transaction_date = models.DateTimeField(blank=True, null=True)
    internal_ref_no = models.CharField(max_length=150, blank=True, null=True)
    user_ref_no = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manual_transactions'


class MapContactMarketPlacePayoutHistories(models.Model):
    map_contact_market_place_payout_histories_id = models.AutoField(primary_key=True)
    map_contact_market_place_payouts_id = models.IntegerField()
    bank_transaction_status_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'map_contact_market_place_payout_histories'


class MapContactTransactions(models.Model):
    map_contact_transactions_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    map_contacts_transactions_ref_id = models.CharField(max_length=100, blank=True, null=True)
    map_contacts_id = models.IntegerField(blank=True, null=True)
    map_contacts_ref_id = models.CharField(max_length=100, blank=True, null=True)
    contacts_id = models.IntegerField(blank=True, null=True)
    contacts_ref_id = models.CharField(max_length=100, blank=True, null=True)
    settlement_statuses_id = models.IntegerField(blank=True, null=True)
    vendor_contacts_id = models.IntegerField(blank=True, null=True)
    vendor_contacts_ref_id = models.CharField(max_length=100, blank=True, null=True)
    amount_collected = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    open_collect_ref_id = models.CharField(max_length=100, blank=True, null=True)
    bank_ref_id = models.CharField(max_length=100, blank=True, null=True)
    payee_name = models.CharField(max_length=200, blank=True, null=True)
    payee_account_number = models.CharField(max_length=80, blank=True, null=True)
    payee_ifsc_code = models.CharField(max_length=50, blank=True, null=True)
    partner_banks_id = models.IntegerField(blank=True, null=True)
    link_types_id = models.IntegerField(blank=True, null=True)
    bank_transaction_date = models.DateTimeField(blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    vpa = models.CharField(max_length=191, blank=True, null=True)
    transaction_types_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'map_contact_transactions'


class MapContactsMarketplacePayouts(models.Model):
    map_contacts_marketplace_payouts_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    marketplace_payouts_ref_id = models.CharField(max_length=100, blank=True, null=True)
    map_contacts_marketplace_payouts_ref_id = models.CharField(max_length=100, blank=True, null=True)
    marketplace_payouts_id = models.IntegerField(blank=True, null=True)
    map_contacts_ref_id = models.CharField(max_length=100, blank=True, null=True)
    map_contacts_id = models.IntegerField(blank=True, null=True)
    contacts_id = models.IntegerField(blank=True, null=True)
    contacts_ref_id = models.CharField(max_length=100, blank=True, null=True)
    vendor_contacts_ref_id = models.CharField(max_length=100, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    amount_settled_to_contact = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    amount_settled_to_merchant = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    commission_type = models.CharField(max_length=100, blank=True, null=True)
    commission_value = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    open_collect_ref_id = models.CharField(max_length=100, blank=True, null=True)
    settlement_account_number = models.CharField(max_length=100, blank=True, null=True)
    settlement_ifsc = models.CharField(max_length=50, blank=True, null=True)
    bank_reference_no = models.CharField(max_length=200, blank=True, null=True)
    mode = models.CharField(max_length=191, blank=True, null=True)
    settlement_created_at = models.DateTimeField(blank=True, null=True)
    settled_at = models.DateTimeField(blank=True, null=True)
    merchant_settlement_id = models.IntegerField(blank=True, null=True)
    contact_payout_status_id = models.IntegerField(blank=True, null=True)
    response_message_from_bank = models.CharField(max_length=191, blank=True, null=True)
    payout_type = models.CharField(max_length=191, blank=True, null=True)
    transaction_types_id = models.IntegerField(blank=True, null=True)
    bank_transaction_status_id = models.IntegerField(blank=True, null=True)
    partner_banks_id = models.IntegerField(blank=True, null=True)
    transaction_date = models.CharField(max_length=191, blank=True, null=True)
    internal_transaction_ref_id = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'map_contacts_marketplace_payouts'


class MapContactsMarketplacePayoutsBalanceHistories(models.Model):
    map_contacts_marketplace_payouts_balance_histories_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    map_contacts_id = models.IntegerField()
    vendor_contacts_id = models.IntegerField()
    current_balance = models.DecimalField(max_digits=14, decimal_places=2)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    type = models.CharField(max_length=20)
    transaction_ref_id = models.CharField(max_length=200)
    settle_to = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'map_contacts_marketplace_payouts_balance_histories'


class MapContactsMarketplacePayoutsBalances(models.Model):
    map_contacts_marketplace_payouts_balances_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    map_contacts_marketplace_payouts_balance_ref_id = models.CharField(max_length=200)
    map_contacts_id = models.IntegerField()
    map_contacts_ref_id = models.CharField(max_length=200)
    vendor_contacts_id = models.IntegerField()
    vendor_contacts_ref_id = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    settle_to = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'map_contacts_marketplace_payouts_balances'


class MarketplaceContactMappings(models.Model):
    marketplace_contact_mappings_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    contact_mapping_ref_id = models.CharField(max_length=191)
    contacts_id = models.IntegerField()
    contacts_ref_id = models.CharField(max_length=191)
    vendor_contacts_id = models.IntegerField()
    vendor_contacts_ref_id = models.CharField(max_length=191)
    account_number = models.CharField(max_length=191)
    ifsc = models.CharField(max_length=191)
    vpa = models.CharField(max_length=191)
    commission_type = models.CharField(max_length=191)
    commission = models.CharField(max_length=191)
    mapping_name = models.CharField(max_length=191, blank=True, null=True)
    partner_banks_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marketplace_contact_mappings'


class MarketplacePayouts(models.Model):
    marketplace_payouts_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    marketplace_payouts_ref_id = models.CharField(max_length=100)
    source_type = models.CharField(max_length=200)
    source_id = models.IntegerField()
    map_contact_transactions_id = models.IntegerField(blank=True, null=True)
    map_contacts_transactions_ref_id = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marketplace_payouts'


class MarketplacePgSubAccounts(models.Model):
    marketplace_pg_sub_accounts_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    sub_account_ref_id = models.CharField(unique=True, max_length=191, blank=True, null=True)
    icp_merchant_id = models.CharField(max_length=191, blank=True, null=True)
    bene_account_number = models.CharField(max_length=191, blank=True, null=True)
    ifsc_code = models.CharField(max_length=191, blank=True, null=True)
    recepient_name = models.CharField(max_length=191, blank=True, null=True)
    email_id = models.CharField(max_length=191, blank=True, null=True)
    mobile_number = models.CharField(max_length=191, blank=True, null=True)
    bank_name = models.CharField(max_length=191, blank=True, null=True)
    branch_name = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    settlement_modes_id = models.IntegerField()
    use_withdrawal_account = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marketplace_pg_sub_accounts'


class MccPgSettings(models.Model):
    mcc_pg_settings_id = models.AutoField(primary_key=True)
    platform_type = models.CharField(max_length=191)
    company_mcc_types_id = models.IntegerField()
    subscription_packages_id = models.IntegerField()
    visa_master_cc_perc = models.FloatField(blank=True, null=True)
    amex_jcb_diners_cc_perc = models.FloatField(blank=True, null=True)
    debit_card_perc = models.FloatField(blank=True, null=True)
    netbanking_perc = models.FloatField(blank=True, null=True)
    netbanking_price = models.FloatField(blank=True, null=True)
    wallet_perc = models.FloatField(blank=True, null=True)
    same_day_settlement_charge_type = models.CharField(max_length=5)
    same_day_settlement_charge = models.DecimalField(max_digits=12, decimal_places=2)
    is_fixed = models.IntegerField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mcc_pg_settings'


class MerchantCategoryCodes(models.Model):
    merchant_category_codes_id = models.AutoField(primary_key=True)
    mcc = models.CharField(max_length=8)
    icon_url = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=80)
    description = models.TextField()
    combined_description = models.TextField()
    usda_description = models.TextField()
    irs_description = models.TextField()
    irs_reportable = models.TextField()
    card_network_acceptance = models.CharField(max_length=10)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    open_merchant_category_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchant_category_codes'


class MerchantCompanySettings(models.Model):
    merchant_company_settings_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    is_flagged = models.IntegerField()
    source_table = models.CharField(max_length=199, blank=True, null=True)
    source_table_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchant_company_settings'


class MerchantDetails(models.Model):
    merchant_id = models.AutoField(primary_key=True)
    merchant_alias_name = models.CharField(max_length=255)
    merchant_name = models.CharField(max_length=255)
    merchant_logo = models.TextField(blank=True, null=True)
    compare_string = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchant_details'


class MerchantIcpActivationStatuses(models.Model):
    merchant_icp_activation_statuses_id = models.AutoField(primary_key=True)
    merchant_icp_activation_status = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchant_icp_activation_statuses'


class MerchantPayoutSettings(models.Model):
    merchant_payout_settings_id = models.AutoField(primary_key=True)
    open_bank_accounts_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    partner_banks_id = models.IntegerField()
    link_types_id = models.IntegerField()
    is_payout_enabled = models.IntegerField()
    is_transaction_limit_enabled = models.IntegerField()
    txn_amt_daily_limit = models.DecimalField(max_digits=14, decimal_places=2)
    txn_amt_monthly_limit = models.DecimalField(max_digits=14, decimal_places=2)
    txn_amt_current_daily_limit = models.DecimalField(max_digits=14, decimal_places=2)
    txn_amt_current_monthly_limit = models.DecimalField(max_digits=14, decimal_places=2)
    txn_count_daily_limit = models.IntegerField()
    txn_count_monthly_limit = models.IntegerField()
    txn_count_current_daily_limit = models.IntegerField()
    txn_count_current_monthly_limit = models.IntegerField()
    per_txn_amt_limit = models.DecimalField(max_digits=14, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchant_payout_settings'


class MerchantPgModes(models.Model):
    merchant_pg_modes_id = models.AutoField(primary_key=True)
    merchant_pg_settings_id = models.CharField(max_length=100)
    transaction_types = models.CharField(max_length=20)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchant_pg_modes'


class MerchantPgSettings(models.Model):
    merchant_pg_settings_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    companies_id = models.IntegerField()
    default_transaction_types_id = models.IntegerField()
    default_settlement_account_name = models.CharField(max_length=191)
    default_settlement_bank_branch = models.CharField(max_length=191)
    default_settlement_ifsc_code = models.CharField(max_length=191)
    default_settlement_account_number = models.CharField(max_length=191)
    default_settlement_bank_name = models.CharField(max_length=191)
    pg_settlement_status_id = models.CharField(max_length=191, blank=True, null=True)
    settlement_status_reason = models.CharField(max_length=191, blank=True, null=True)
    daily_txn_limit = models.DecimalField(max_digits=16, decimal_places=2)
    monthly_txn_limit = models.DecimalField(max_digits=16, decimal_places=2)
    current_daily_txn = models.DecimalField(max_digits=16, decimal_places=2)
    current_monthly_txn = models.DecimalField(max_digits=16, decimal_places=2)
    pg_activation_status_id = models.IntegerField()
    is_card_activated = models.CharField(max_length=10)
    is_net_banking_activated = models.CharField(max_length=10)
    is_va_activated = models.CharField(max_length=10)
    is_upi_activated = models.IntegerField()
    is_cash_activated = models.IntegerField()
    has_user_enabled_payment_link = models.IntegerField()
    is_auto_settlement_enabled = models.IntegerField()
    stripe_debit_card_tdr_old = models.DecimalField(max_digits=5, decimal_places=2)
    stripe_mesh_tdr = models.DecimalField(max_digits=5, decimal_places=2)
    tpsl_credit_card_tdr_old = models.DecimalField(max_digits=5, decimal_places=2)
    tpsl_debit_card_tdr_old = models.DecimalField(max_digits=5, decimal_places=2)
    tpsl_netbanking_tdr_old = models.DecimalField(max_digits=5, decimal_places=2)
    atom_credit_card_tdr_old = models.DecimalField(max_digits=5, decimal_places=2)
    atom_debit_card_tdr_old = models.DecimalField(max_digits=5, decimal_places=2)
    atom_netbanking_tdr_old = models.DecimalField(max_digits=5, decimal_places=2)
    icici_upi_commision_perc = models.DecimalField(max_digits=5, decimal_places=2)
    icici_upi_fixed = models.DecimalField(max_digits=10, decimal_places=2)
    is_direct_card = models.IntegerField()
    merchant_pg_settlement_types_id = models.IntegerField()
    pg_website_url = models.TextField(blank=True, null=True)
    icp_merchant_id = models.CharField(max_length=191, blank=True, null=True)
    merchant_icp_activation_statuses_id = models.SmallIntegerField()
    mesh_activation_statuses_id = models.IntegerField()
    mesh_requested_on = models.DateTimeField()
    icp_refund_activation_statuses_id = models.IntegerField()
    mesh_settlement_activation_statuses_id = models.IntegerField()
    type_of_settlement = models.CharField(max_length=191, blank=True, null=True)
    market_place_merchant_commission_type = models.CharField(max_length=191, blank=True, null=True)
    market_place_merchant_commission_value = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    is_split_settlement_enabled = models.IntegerField()
    is_sub_acc_settlement_enabled = models.IntegerField()
    va_collection_limit = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    atom_wallet_tdr = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    atom_international_tdr = models.DecimalField(max_digits=5, decimal_places=2)
    is_custom_mid_required = models.IntegerField()
    lifetime_pg_collection_limit = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    total_pg_collections = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    atom_rupay_dc_tdr_old = models.DecimalField(max_digits=5, decimal_places=2)
    tpsl_rupay_dc_tdr_old = models.DecimalField(max_digits=5, decimal_places=2)
    stripe_rupay_dc_tdr_old = models.DecimalField(max_digits=5, decimal_places=2)
    debit_card_tdr_limit = models.DecimalField(max_digits=14, decimal_places=2)
    debit_card_tdr_less_than_limit = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    netbanking_tdr_type = models.CharField(max_length=5)
    atom_amex_tdr_old = models.DecimalField(max_digits=5, decimal_places=2)
    pennydrop_credits = models.DecimalField(max_digits=14, decimal_places=2)
    salt_tdr = models.DecimalField(max_digits=5, decimal_places=2)
    credit_card_tdr = models.DecimalField(max_digits=5, decimal_places=2)
    debit_card_tdr = models.DecimalField(max_digits=5, decimal_places=2)
    netbanking_tdr = models.DecimalField(max_digits=5, decimal_places=2)
    rupay_dc_tdr = models.DecimalField(max_digits=5, decimal_places=2)
    rupay_cc_tdr = models.DecimalField(max_digits=5, decimal_places=2)
    amex_tdr = models.DecimalField(max_digits=5, decimal_places=2)
    deleted_at = models.DateTimeField(blank=True, null=True)
    bob_credit_card_tdr_old = models.DecimalField(max_digits=14, decimal_places=2)
    bob_debit_card_tdr_old = models.DecimalField(max_digits=14, decimal_places=2)
    bob_netbanking_tdr_old = models.DecimalField(max_digits=14, decimal_places=2)
    bob_rupay_dc_tdr_old = models.DecimalField(max_digits=14, decimal_places=2)
    bob_rupay_cc_tdr_old = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    stripe_rupay_cc_tdr_old = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tpsl_rupay_cc_tdr_old = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    atom_rupay_cc_tdr_old = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    bob_amex_tdr_old = models.DecimalField(max_digits=14, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    mac_address = models.CharField(max_length=100, blank=True, null=True)
    enterprise_dynamic_vpa_prefix = models.CharField(max_length=10, blank=True, null=True)
    emi_tdr = models.FloatField()
    same_day_settlement_status_id = models.IntegerField()
    same_day_settlement_enabled = models.IntegerField(blank=True, null=True)
    same_day_settlement_charge_type = models.CharField(max_length=10)
    same_day_settlement_charge = models.DecimalField(max_digits=12, decimal_places=2)
    is_daily_settlement_enabled = models.IntegerField(blank=True, null=True)
    done_process = models.IntegerField(blank=True, null=True)
    stripe_credit_card_tdr_old = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    is_tdr_updated_cc = models.IntegerField(blank=True, null=True)
    is_tdr_updated_amx = models.IntegerField(blank=True, null=True)
    is_tdr_updated_dc = models.IntegerField(blank=True, null=True)
    is_tdr_updated_rupay_dc = models.IntegerField(blank=True, null=True)
    is_tdr_updated_rupay_cc = models.IntegerField(blank=True, null=True)
    is_tdr_updated_nb = models.IntegerField(blank=True, null=True)
    payswiff_tdr = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchant_pg_settings'


class MerchantPgSettlementTypes(models.Model):
    merchant_pg_settlement_types_id = models.AutoField(primary_key=True)
    settlement_type = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchant_pg_settlement_types'


class MerchantQrCodeMappings(models.Model):
    merchant_qr_code_mappings_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    vpa_series = models.CharField(max_length=191, blank=True, null=True)
    vpa = models.CharField(max_length=191)
    url = models.CharField(max_length=191)
    qr_sticker_url = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    contacts_id = models.IntegerField(blank=True, null=True)
    is_contact = models.IntegerField()
    link_types_id = models.IntegerField(blank=True, null=True)
    partner_banks_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchant_qr_code_mappings'


class MerchantSettlementHistories(models.Model):
    merchant_settlement_histories_id = models.AutoField(primary_key=True)
    merchant_settlements_id = models.IntegerField()
    bank_transaction_status_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchant_settlement_histories'


class MerchantSettlements(models.Model):
    merchant_settlements_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    partner_banks_id = models.IntegerField(blank=True, null=True)
    bene_name = models.CharField(max_length=200, blank=True, null=True)
    bene_email_id = models.CharField(max_length=200, blank=True, null=True)
    bene_mobile_number = models.CharField(max_length=200, blank=True, null=True)
    bene_account_number = models.CharField(max_length=200, blank=True, null=True)
    bene_ifsc_code = models.CharField(max_length=200, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    transaction_types_id = models.IntegerField(blank=True, null=True)
    internal_transaction_ref_id = models.CharField(max_length=200, blank=True, null=True)
    bank_transaction_status_id = models.IntegerField(blank=True, null=True)
    bank_response = models.TextField(blank=True, null=True)
    bank_response_time = models.DateTimeField(blank=True, null=True)
    purpose = models.TextField(blank=True, null=True)
    transaction_date = models.DateTimeField(blank=True, null=True)
    utr_number = models.CharField(max_length=200, blank=True, null=True)
    is_settlement_complete = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchant_settlements'


class MerchantSubscriptionMeteringChargeHistories(models.Model):
    merchant_subscription_metering_charge_histories_id = models.BigAutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    transaction_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    open_charge = models.DecimalField(max_digits=14, decimal_places=3)
    open_ref_id = models.CharField(max_length=255, blank=True, null=True)
    bank_ref_id = models.CharField(max_length=255, blank=True, null=True)
    transaction_category = models.CharField(max_length=255, blank=True, null=True)
    transaction_types_id = models.IntegerField(blank=True, null=True)
    transaction_mode = models.CharField(max_length=255, blank=True, null=True)
    transaction_min_range = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    transaction_max_range = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    subscription_packages_id = models.IntegerField(blank=True, null=True)
    transaction_charging_rate_type = models.CharField(max_length=255, blank=True, null=True)
    transaction_charging_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    is_queue_processed = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchant_subscription_metering_charge_histories'
        unique_together = (('open_ref_id', 'bank_ref_id'),)


class MerchantSubscriptionMeteringCharges(models.Model):
    merchant_subscription_metering_charges_id = models.BigAutoField(primary_key=True)
    accounts_id = models.IntegerField(unique=True, blank=True, null=True)
    companies_id = models.IntegerField(unique=True, blank=True, null=True)
    users_id = models.IntegerField(unique=True, blank=True, null=True)
    pricing_category_modes_id = models.IntegerField(blank=True, null=True)
    subscription_metering_charge = models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchant_subscription_metering_charges'


class MeshActivationStatuses(models.Model):
    mesh_activation_statuses_id = models.AutoField(primary_key=True)
    mesh_activation_status = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mesh_activation_statuses'


class MeshPaymentsDetails(models.Model):
    mesh_payments_details_id = models.BigAutoField(primary_key=True)
    invoices_id = models.BigIntegerField(blank=True, null=True)
    request_amount = models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)
    request_currency = models.CharField(max_length=5, blank=True, null=True)
    receive_currency = models.CharField(max_length=5, blank=True, null=True)
    payer_full_name = models.CharField(max_length=100, blank=True, null=True)
    payer_company_name = models.CharField(max_length=100, blank=True, null=True)
    country_code = models.CharField(max_length=6, blank=True, null=True)
    payer_phone = models.CharField(max_length=20, blank=True, null=True)
    payer_email = models.CharField(max_length=100, blank=True, null=True)
    due_date = models.CharField(max_length=30, blank=True, null=True)
    payer_country = models.CharField(max_length=100, blank=True, null=True)
    receiver_phone = models.CharField(max_length=15, blank=True, null=True)
    receiver_email = models.CharField(max_length=60, blank=True, null=True)
    receiver_country = models.CharField(max_length=10, blank=True, null=True)
    receiver_company_name = models.CharField(max_length=191, blank=True, null=True)
    requested_amount = models.CharField(max_length=14, blank=True, null=True)
    requested_symbol = models.CharField(max_length=5, blank=True, null=True)
    received_amount = models.CharField(max_length=14, blank=True, null=True)
    received_symbol = models.CharField(max_length=5, blank=True, null=True)
    fx_rate = models.CharField(max_length=14, blank=True, null=True)
    mesh_created_date = models.CharField(max_length=15, blank=True, null=True)
    mesh_status = models.CharField(max_length=50, blank=True, null=True)
    mesh_transaction_id = models.CharField(max_length=50, blank=True, null=True)
    payment_status = models.CharField(max_length=100, blank=True, null=True)
    mesh_response_note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mesh_payments_details'


class MeshSettlementActivationStatuses(models.Model):
    mesh_settlement_activation_statuses_id = models.AutoField(primary_key=True)
    mesh_settlement_activation_status = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mesh_settlement_activation_statuses'


class MigratingPlatformLists(models.Model):
    migrating_platform_lists_id = models.AutoField(primary_key=True)
    platform_name = models.CharField(max_length=200, blank=True, null=True)
    platform_url = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'migrating_platform_lists'


class Migrations(models.Model):
    migration = models.CharField(max_length=191)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class MobAddressDetails(models.Model):
    mob_address_details_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField(unique=True)
    registered_address_id = models.IntegerField(blank=True, null=True)
    operation_address_id = models.IntegerField(blank=True, null=True)
    mob_master_id = models.IntegerField(blank=True, null=True)
    aadhaar_details_id = models.IntegerField(blank=True, null=True)
    is_operational_address_different = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mob_address_details'


class MobBusinessCategories(models.Model):
    mob_business_categories_id = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=191, blank=True, null=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    yes_bank_vpa_mcc = models.CharField(max_length=11, blank=True, null=True)
    payswiff_category_code = models.IntegerField(blank=True, null=True)
    payswiff_sub_category_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mob_business_categories'


class MobBusinessDetails(models.Model):
    mob_business_details_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField(unique=True)
    mob_business_types_id = models.IntegerField(blank=True, null=True)
    business_pan = models.CharField(max_length=100, blank=True, null=True)
    company_website = models.CharField(max_length=100, blank=True, null=True)
    pan_details_id = models.IntegerField(blank=True, null=True)
    brand_name = models.CharField(max_length=191, blank=True, null=True)
    cin = models.CharField(max_length=191, blank=True, null=True)
    gstin_number = models.CharField(max_length=150, blank=True, null=True)
    business_email = models.CharField(max_length=191, blank=True, null=True)
    business_phone = models.CharField(max_length=12, blank=True, null=True)
    date_of_incorporation = models.DateField(blank=True, null=True)
    mob_master_id = models.IntegerField()
    pan_type = models.CharField(max_length=10)
    mob_business_categories_id = models.IntegerField(blank=True, null=True)
    mob_categories_id = models.IntegerField(blank=True, null=True)
    mob_industries_id = models.IntegerField(blank=True, null=True)
    registered_business_name = models.CharField(max_length=191, blank=True, null=True)
    industry = models.CharField(max_length=200, blank=True, null=True)
    company_turnover = models.CharField(max_length=200, blank=True, null=True)
    has_credit_facility = models.IntegerField()
    branch_name = models.CharField(max_length=200, blank=True, null=True)
    branch_address = models.CharField(max_length=200, blank=True, null=True)
    type_of_facility = models.CharField(max_length=200, blank=True, null=True)
    amount_of_facility = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product_types = models.TextField(blank=True, null=True)
    business_address_pin = models.IntegerField(blank=True, null=True)
    no_of_employees = models.IntegerField(blank=True, null=True)
    no_website_link = models.IntegerField()
    demo_request = models.IntegerField()
    business_doc_skipped = models.IntegerField()
    is_trust = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mob_business_details'


class MobBusinessTypes(models.Model):
    mob_business_types_id = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=191, blank=True, null=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    yes_bank_vpa_business_types_id = models.IntegerField(blank=True, null=True)
    payswiff_filing_types = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mob_business_types'


class MobCategories(models.Model):
    mob_categories_id = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mob_categories'


class MobContractDetails(models.Model):
    mob_contract_details_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField(unique=True)
    users_id = models.IntegerField()
    mob_master_id = models.IntegerField()
    aadhaar_details_id = models.IntegerField()
    esign_type = models.CharField(max_length=191)
    has_esign_completed = models.IntegerField()
    esign_completed_at = models.DateTimeField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mob_contract_details'


class MobDirectorDetails(models.Model):
    mob_director_details_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    mob_master_id = models.IntegerField()
    din = models.IntegerField(blank=True, null=True)
    designation = models.CharField(max_length=191, blank=True, null=True)
    date_of_appointment = models.DateField(blank=True, null=True)
    dsc_expiry_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    whether_dsc_registered = models.IntegerField(blank=True, null=True)
    address_line = models.TextField(blank=True, null=True)
    address_district = models.CharField(max_length=191, blank=True, null=True)
    address_state = models.CharField(max_length=191, blank=True, null=True)
    address_city = models.CharField(max_length=191, blank=True, null=True)
    pincode = models.CharField(max_length=191, blank=True, null=True)
    country = models.CharField(max_length=191, blank=True, null=True)
    father_name = models.CharField(max_length=191, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    pan = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mob_director_details'


class MobIndustries(models.Model):
    mob_industries_id = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mob_industries'


class MobMaster(models.Model):
    mob_master_id = models.AutoField(primary_key=True)
    mob_business_types_id = models.IntegerField(blank=True, null=True)
    current_step = models.CharField(max_length=191, blank=True, null=True)
    current_sub_step = models.CharField(max_length=191, blank=True, null=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField(unique=True)
    mob_statuses_id = models.IntegerField()
    is_manual = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mob_master'


class MobStakeholderDetails(models.Model):
    mob_stakeholder_details_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email_id = models.CharField(max_length=100, blank=True, null=True)
    mobile_number = models.CharField(max_length=100, blank=True, null=True)
    individual_pan_details_id = models.IntegerField(blank=True, null=True)
    aadhaar_details_id = models.IntegerField(blank=True, null=True)
    team_member_details_id = models.IntegerField(blank=True, null=True)
    mob_master_id = models.IntegerField(blank=True, null=True)
    current_address_id = models.IntegerField(blank=True, null=True)
    permanent_address_id = models.IntegerField(blank=True, null=True)
    is_current_address_different = models.IntegerField()
    title = models.CharField(max_length=191, blank=True, null=True)
    middle_name = models.CharField(max_length=191, blank=True, null=True)
    mothers_maiden_name = models.CharField(max_length=191, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    aadhaar_number = models.CharField(max_length=200, blank=True, null=True)
    father_name = models.CharField(max_length=200, blank=True, null=True)
    spouse_name = models.CharField(max_length=200, blank=True, null=True)
    marital_status = models.CharField(max_length=200, blank=True, null=True)
    annual_income = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_stakeholder_verified = models.IntegerField()
    is_authorized_signatory = models.IntegerField()
    stakeholder_hash = models.CharField(max_length=199, blank=True, null=True)
    is_aadhar_online = models.IntegerField()
    is_openbook_kyc = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mob_stakeholder_details'


class MobStatuses(models.Model):
    mob_statuses_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mob_statuses'


class MposDeviceActivationStatuses(models.Model):
    mpos_device_activation_statuses_id = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mpos_device_activation_statuses'


class NbfcPartnerBanks(models.Model):
    nbfc_partner_banks_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nbfc_partner_banks'


class NbfcTransactionStatuses(models.Model):
    nbfc_transaction_status_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=190, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nbfc_transaction_statuses'


class NeftBankHolidays(models.Model):
    neft_bank_holidays_id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    type = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'neft_bank_holidays'


class NeverBounceEmailLogs(models.Model):
    never_bounce_email_logs_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=191)
    never_bounce_response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'never_bounce_email_logs'


class NodalFundTransferTypes(models.Model):
    nodal_fund_transfer_types_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nodal_fund_transfer_types'


class NodalFundTransfers(models.Model):
    nodal_fund_transfers_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    nodal_fund_transfer_types_id = models.IntegerField()
    services_id = models.IntegerField()
    src_account_number = models.CharField(max_length=200, blank=True, null=True)
    dst_account_number = models.CharField(max_length=200, blank=True, null=True)
    source_type = models.CharField(max_length=250)
    source_id = models.IntegerField()
    utr_number = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    transaction_date = models.DateTimeField()
    transaction_types_id = models.IntegerField()
    bank_transaction_statuses_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nodal_fund_transfers'


class NotificationAdmin(models.Model):
    fname = models.CharField(max_length=191)
    lname = models.CharField(max_length=191)
    email = models.CharField(unique=True, max_length=191)
    password = models.CharField(max_length=191)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notification_admin'


class NotificationEmailPlateform(models.Model):
    name = models.CharField(max_length=191)
    from_email = models.CharField(max_length=191)
    support_email = models.CharField(max_length=191)
    notification_service_provider_id = models.IntegerField(blank=True, null=True)
    from_name = models.CharField(max_length=191, blank=True, null=True)
    support_name = models.CharField(max_length=191, blank=True, null=True)
    status = models.IntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_email_plateform'


class NotificationPrivileges(models.Model):
    name = models.CharField(max_length=191)
    description = models.CharField(max_length=191, blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_privileges'


class NotificationRolePrivileges(models.Model):
    role_id = models.IntegerField()
    privilege_id = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_role_privileges'


class NotificationRoles(models.Model):
    name = models.CharField(max_length=191)
    description = models.CharField(max_length=191, blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_roles'


class NotificationServiceProviders(models.Model):
    name = models.CharField(max_length=191)
    is_default = models.IntegerField()
    status = models.IntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_service_providers'


class NotificationSmsPlateform(models.Model):
    name = models.CharField(max_length=191)
    notification_service_provider_id = models.IntegerField()
    sender_id = models.CharField(max_length=191, blank=True, null=True)
    user_name = models.CharField(max_length=191, blank=True, null=True)
    password = models.CharField(max_length=191, blank=True, null=True)
    auth_key = models.CharField(max_length=191, blank=True, null=True)
    status = models.IntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_sms_plateform'


class NotificationTriggerHistories(models.Model):
    notification_trigger_histories_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    separatokey_key = models.CharField(max_length=191)
    communication_channels_id = models.IntegerField()
    channel_value = models.CharField(max_length=200)
    is_delivered = models.IntegerField()
    campaign_details_id = models.IntegerField(blank=True, null=True)
    campaign_event_details_id = models.IntegerField(blank=True, null=True)
    is_one_time = models.IntegerField()
    no_of_tries_allowed = models.IntegerField()
    current_notification_count = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_trigger_histories'


class NotificationUserDetails(models.Model):
    notification_user_details_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    communication_channels_id = models.IntegerField()
    channel_value = models.CharField(max_length=200)
    is_verified = models.IntegerField()
    is_enabled = models.IntegerField()
    is_email_verified_by_user = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_user_details'


class NotificationUserPrivileges(models.Model):
    user_id = models.IntegerField()
    privilege_id = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_user_privileges'


class NotificationUserSettings(models.Model):
    notification_user_settings_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    is_sms_enabled = models.IntegerField()
    is_email_enabled = models.IntegerField()
    is_whatsapp_enabled = models.IntegerField()
    is_push_notification_enabled = models.IntegerField()
    is_layer_merchant_notification_enabled = models.IntegerField()
    is_layer_customer_notification_enabled = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_user_settings'


class NotificationWhatsappPlateform(models.Model):
    name = models.CharField(max_length=191)
    notification_service_provider_id = models.IntegerField()
    from_mobile_number = models.CharField(max_length=191, blank=True, null=True)
    user_name = models.CharField(max_length=191, blank=True, null=True)
    password = models.CharField(max_length=191, blank=True, null=True)
    auth_key = models.CharField(max_length=191, blank=True, null=True)
    status = models.IntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_whatsapp_plateform'


class NpciMandateRegistrations(models.Model):
    npci_mandate_registrations_id = models.BigAutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    corporate_name = models.CharField(max_length=255, blank=True, null=True)
    consumer_ref_num = models.CharField(max_length=255, blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    mandate_ref_num = models.CharField(max_length=255, blank=True, null=True)
    deduction_amount = models.CharField(max_length=255, blank=True, null=True)
    maximum_amount = models.CharField(max_length=255, blank=True, null=True)
    sequence_type = models.CharField(max_length=255, blank=True, null=True)
    frequency = models.CharField(max_length=255, blank=True, null=True)
    debit_type = models.CharField(max_length=14)
    deduction_frequency = models.CharField(max_length=255, blank=True, null=True)
    deduction_start_date = models.CharField(max_length=255, blank=True, null=True)
    deduction_end_date = models.CharField(max_length=255, blank=True, null=True)
    account_num = models.CharField(max_length=255, blank=True, null=True)
    customer_ifsc_code = models.CharField(max_length=255, blank=True, null=True)
    account_type = models.CharField(max_length=7)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    email_id = models.CharField(max_length=255, blank=True, null=True)
    pan = models.CharField(max_length=255, blank=True, null=True)
    acpt_refrence_no = models.CharField(max_length=255, blank=True, null=True)
    umrn = models.CharField(max_length=255, blank=True, null=True)
    request_result = models.TextField(blank=True, null=True)
    perp_of_mandate = models.CharField(max_length=255, blank=True, null=True)
    emandate_statuses_id = models.CharField(max_length=255, blank=True, null=True)
    auth_mode = models.CharField(max_length=255, blank=True, null=True)
    bank_id = models.CharField(max_length=255, blank=True, null=True)
    next_deduction_date = models.CharField(max_length=255, blank=True, null=True)
    last_deduction_date = models.CharField(max_length=255, blank=True, null=True)
    current_decduction_count = models.IntegerField()
    source_id = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'npci_mandate_registrations'


class OnboardingStatusHistories(models.Model):
    onboarding_status_histories_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    onboarding_statuses_id = models.IntegerField()
    migrated_onboarding_statuses_id = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onboarding_status_histories'


class OnboardingStatuses(models.Model):
    onboarding_statuses_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=100)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onboarding_statuses'


class Onesignals(models.Model):
    onesignals_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    client_type = models.CharField(max_length=100, blank=True, null=True)
    player_id = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onesignals'


class OpenApps(models.Model):
    open_apps_id = models.BigAutoField(primary_key=True)
    app_name = models.CharField(max_length=191)
    app_key = models.CharField(max_length=191)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'open_apps'


class OpenBankAccountTypes(models.Model):
    open_bank_account_types_id = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=191)
    name = models.CharField(max_length=191)
    description = models.CharField(max_length=191)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'open_bank_account_types'


class OpenBankAccounts(models.Model):
    open_bank_accounts_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField(blank=True, null=True)
    account_holder_name = models.CharField(max_length=200, blank=True, null=True)
    account_nickname = models.CharField(max_length=128, blank=True, null=True)
    is_default_settlement_account = models.IntegerField()
    is_default_transfer_account = models.IntegerField()
    open_bank_account_number = models.CharField(max_length=191, blank=True, null=True)
    open_bank_branch = models.CharField(max_length=191, blank=True, null=True)
    open_bank_ifsc = models.CharField(max_length=191, blank=True, null=True)
    open_bank_account_types_id = models.CharField(max_length=191)
    link_types_id = models.IntegerField(blank=True, null=True)
    bank_connection_statuses_id = models.IntegerField(blank=True, null=True)
    source_type = models.CharField(max_length=200, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    partner_banks_id = models.IntegerField(blank=True, null=True)
    current_balance = models.DecimalField(max_digits=14, decimal_places=2)
    is_transaction_otp_required = models.IntegerField()
    balance_last_updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    open_bank_account_number_temp = models.CharField(max_length=191, blank=True, null=True)
    open_bank_branch_temp = models.CharField(max_length=191, blank=True, null=True)
    open_bank_ifsc_temp = models.CharField(max_length=191, blank=True, null=True)
    partner_banks_id_temp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'open_bank_accounts'


class OpenBankAccountsBk(models.Model):
    open_bank_accounts_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField(blank=True, null=True)
    account_holder_name = models.CharField(max_length=200, blank=True, null=True)
    account_nickname = models.CharField(max_length=128, blank=True, null=True)
    is_default_settlement_account = models.IntegerField()
    is_default_transfer_account = models.IntegerField()
    open_bank_account_number = models.CharField(max_length=191, blank=True, null=True)
    open_bank_branch = models.CharField(max_length=191, blank=True, null=True)
    open_bank_ifsc = models.CharField(max_length=191, blank=True, null=True)
    open_bank_account_types_id = models.CharField(max_length=191)
    link_types_id = models.IntegerField(blank=True, null=True)
    bank_connection_statuses_id = models.IntegerField(blank=True, null=True)
    source_type = models.CharField(max_length=200, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    partner_banks_id = models.IntegerField(blank=True, null=True)
    current_balance = models.DecimalField(max_digits=14, decimal_places=2)
    is_transaction_otp_required = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    open_bank_account_number_temp = models.CharField(max_length=191, blank=True, null=True)
    open_bank_branch_temp = models.CharField(max_length=191, blank=True, null=True)
    open_bank_ifsc_temp = models.CharField(max_length=191, blank=True, null=True)
    partner_banks_id_temp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'open_bank_accounts_bk'


class OpenBankingNodalStatements(models.Model):
    open_banking_nodal_statements_id = models.BigAutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    partner_banks_id = models.IntegerField()
    contacts_id = models.IntegerField(blank=True, null=True)
    is_contact = models.IntegerField(blank=True, null=True)
    categories_id = models.IntegerField(blank=True, null=True)
    category_name = models.CharField(max_length=199, blank=True, null=True)
    l2_categories_id = models.IntegerField(blank=True, null=True)
    l3_categories_id = models.IntegerField(blank=True, null=True)
    is_reviewed = models.IntegerField()
    withdraw_bank_accounts_id = models.IntegerField(blank=True, null=True)
    open_bank_accounts_id = models.IntegerField(blank=True, null=True)
    link_types_id = models.IntegerField(blank=True, null=True)
    account_number = models.CharField(max_length=250, blank=True, null=True)
    bank_name = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    ref_no = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    source_type = models.CharField(max_length=200, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    transaction_types_id = models.CharField(max_length=191)
    transaction_mode = models.CharField(max_length=13)
    transaction_date = models.DateTimeField(blank=True, null=True)
    settlement_date = models.DateTimeField(blank=True, null=True)
    is_journal_entry_created = models.IntegerField()
    mapped_to_open_banking_nodal_statements_id = models.IntegerField(blank=True, null=True)
    va_number = models.CharField(max_length=191)
    wallet_user_code = models.CharField(db_column='wallet-user-code', max_length=191)  # Field renamed to remove unsuitable characters.
    is_voucher_created = models.IntegerField()
    closing_balance = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'open_banking_nodal_statements'


class OpenBookInvoiceTemplates(models.Model):
    template_id = models.AutoField(primary_key=True)
    template_name = models.CharField(max_length=50, blank=True, null=True)
    template_file = models.CharField(max_length=50, blank=True, null=True)
    template_image_thumb = models.TextField(blank=True, null=True)
    template_image = models.TextField(blank=True, null=True)
    template_props = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'open_book_invoice_templates'


class OpenFosEmployeeCodes(models.Model):
    open_fos_employee_codes_id = models.AutoField(primary_key=True)
    fos_emp_id = models.CharField(unique=True, max_length=191, blank=True, null=True)
    candidates_name = models.CharField(max_length=191, blank=True, null=True)
    contact_no = models.CharField(max_length=191, blank=True, null=True)
    location = models.CharField(max_length=191, blank=True, null=True)
    designation = models.CharField(max_length=191, blank=True, null=True)
    final_status = models.CharField(max_length=191, blank=True, null=True)
    vendor = models.CharField(max_length=191, blank=True, null=True)
    admin_users_id = models.IntegerField()
    remarks = models.CharField(max_length=191)
    sales_manager = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'open_fos_employee_codes'


class OpenMerchantCategories(models.Model):
    open_merchant_category_id = models.AutoField(primary_key=True)
    open_merchant_category_name = models.CharField(max_length=255)
    open_merchant_category_url = models.CharField(max_length=255, blank=True, null=True)
    color_code = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'open_merchant_categories'


class OpenPaySettlements(models.Model):
    open_pay_settlements_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    txn_unique_request_num = models.CharField(max_length=191)
    debit_account_num = models.CharField(max_length=191)
    yes_bank_beneficiaries_id = models.CharField(max_length=191)
    transaction_types_id = models.CharField(max_length=191)
    statement_description = models.CharField(max_length=291)
    initiator_types_id = models.IntegerField()
    bank_transaction_statuses_id = models.CharField(max_length=191)
    response_message = models.CharField(max_length=391)
    bank_ref_num = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'open_pay_settlements'


class OpenPayrollTransactions(models.Model):
    open_payroll_transactions_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField(blank=True, null=True)
    transactions_json_payload = models.TextField()
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=14, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'open_payroll_transactions'


class OpenRoles(models.Model):
    open_roles_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=191)
    permissions = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'open_roles'


class OpenServiceCharges(models.Model):
    open_service_charges_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    internal_refrence_descr = models.CharField(max_length=191, blank=True, null=True)
    sac_code = models.CharField(max_length=191, blank=True, null=True)
    gst_rate = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    definition = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'open_service_charges'


class OpenServices(models.Model):
    open_services_id = models.AutoField(primary_key=True)
    open_service_name = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'open_services'


class OpenTraits(models.Model):
    open_traits_id = models.AutoField(primary_key=True)
    trait_name = models.CharField(max_length=250)
    trait_cta = models.CharField(max_length=200)
    trait_description = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'open_traits'


class OpenTraitsCopy(models.Model):
    open_traits_id = models.AutoField(primary_key=True)
    trait_name = models.CharField(max_length=250)
    trait_cta = models.CharField(max_length=200)
    trait_description = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'open_traits_copy'


class OpenbookBanners(models.Model):
    openbook_banners_id = models.AutoField(primary_key=True)
    banner_type = models.CharField(max_length=100)
    banner_type_id = models.IntegerField()
    url = models.CharField(max_length=200)
    deep_link = models.CharField(max_length=200, blank=True, null=True)
    language_id = models.IntegerField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'openbook_banners'


class OpenbookCampaignDetails(models.Model):
    openbook_campaign_details = models.AutoField(primary_key=True)
    campaign_id = models.IntegerField()
    language_id = models.IntegerField()
    language = models.CharField(max_length=30)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'openbook_campaign_details'


class OpenbookKycDetails(models.Model):
    openbook_kyc_details_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    onboarding_statuses_id = models.IntegerField()
    is_gst_online = models.IntegerField(blank=True, null=True)
    gstin_verification_status = models.CharField(max_length=20, blank=True, null=True)
    kyc_step = models.IntegerField(blank=True, null=True)
    document_1_type = models.IntegerField(blank=True, null=True)
    document_1_value = models.CharField(max_length=100, blank=True, null=True)
    document_2_type = models.IntegerField(blank=True, null=True)
    document_2_value = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'openbook_kyc_details'


class OpenbookReferralDetails(models.Model):
    openbook_referral_details_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    mobile_number = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'openbook_referral_details'


class OpenbookUserFeedbacks(models.Model):
    openbook_user_feedbacks_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    rating = models.IntegerField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    screen_name = models.CharField(max_length=100, blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    device_type = models.CharField(max_length=100, blank=True, null=True)
    app_version_code = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'openbook_user_feedbacks'


class OpenpayPayouts(models.Model):
    openpay_payouts_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    source_type = models.CharField(max_length=199, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    bank_transaction_status_id = models.IntegerField(blank=True, null=True)
    internal_transaction_ref_id = models.CharField(max_length=199, blank=True, null=True)
    cid = models.CharField(max_length=199, blank=True, null=True)
    uid = models.CharField(max_length=199, blank=True, null=True)
    urn = models.CharField(max_length=199, blank=True, null=True)
    aggr_id = models.CharField(max_length=199, blank=True, null=True)
    aggr_name = models.CharField(max_length=199, blank=True, null=True)
    utr_number = models.CharField(max_length=199, blank=True, null=True)
    debit_account_number = models.CharField(max_length=199, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'openpay_payouts'


class OptoSettlements(models.Model):
    opto_settlements_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    total_transaction_amount = models.DecimalField(max_digits=14, decimal_places=2)
    open_total_charges = models.DecimalField(max_digits=14, decimal_places=2)
    merchant_settlement_amount = models.DecimalField(max_digits=14, decimal_places=2)
    outward_settlement_statuses = models.IntegerField()
    settlement_txn_id = models.CharField(unique=True, max_length=191)
    files_id = models.IntegerField(blank=True, null=True)
    transactions_count = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opto_settlements'


class OptotaxTransactionLogs(models.Model):
    optotax_transaction_logs_id = models.AutoField(primary_key=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    kit_no = models.IntegerField(blank=True, null=True)
    entity_id = models.CharField(max_length=250, blank=True, null=True)
    transaction_ref_no = models.CharField(max_length=250, blank=True, null=True)
    retrival_ref_no = models.CharField(max_length=250, blank=True, null=True)
    transaction_amount = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    status_code = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'optotax_transaction_logs'


class Otp(models.Model):

    class Meta:
        managed = False
        db_table = 'otp'


class Otps(models.Model):
    otps_id = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    otp = models.CharField(max_length=191)
    is_used = models.IntegerField()
    attempts = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'otps'


class OutwardSettlementStatuses(models.Model):
    outward_settlement_statuses_id = models.AutoField(primary_key=True)
    outward_settlement_status = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'outward_settlement_statuses'


class PanVerifications(models.Model):
    pan_verifications_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    pan = models.CharField(max_length=10)
    name_on_pan = models.CharField(max_length=191, blank=True, null=True)
    verification_status = models.CharField(max_length=191)
    request = models.CharField(max_length=391, blank=True, null=True)
    response = models.CharField(max_length=391, blank=True, null=True)
    merchant_ref_id = models.CharField(max_length=191)
    is_enterprise = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pan_verifications'
        unique_together = (('companies_id', 'merchant_ref_id'),)


class PartnerBanks(models.Model):
    partner_banks_id = models.AutoField(primary_key=True)
    bank_name = models.CharField(max_length=191)
    bank_logo = models.CharField(max_length=191, blank=True, null=True)
    bank_branch = models.CharField(max_length=191)
    bank_ifsc = models.CharField(max_length=191)
    bank_address = models.CharField(max_length=191)
    is_connected_banking_supported = models.IntegerField(blank=True, null=True)
    is_fund_transfer_supported = models.IntegerField(blank=True, null=True)
    is_ecollection_supported = models.IntegerField(blank=True, null=True)
    is_balance_fetch_supported = models.IntegerField(blank=True, null=True)
    is_statement_fetch_supported = models.IntegerField(blank=True, null=True)
    is_transaction_enquiry_supported = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    mobile_bank_logo = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partner_banks'


class PartnerBanksBk(models.Model):
    partner_banks_id = models.AutoField(primary_key=True)
    bank_name = models.CharField(max_length=191)
    bank_logo = models.CharField(max_length=191, blank=True, null=True)
    bank_branch = models.CharField(max_length=191)
    bank_ifsc = models.CharField(max_length=191)
    bank_address = models.CharField(max_length=191)
    is_connected_banking_supported = models.IntegerField(blank=True, null=True)
    is_fund_transfer_supported = models.IntegerField(blank=True, null=True)
    is_ecollection_supported = models.IntegerField(blank=True, null=True)
    is_balance_fetch_supported = models.IntegerField(blank=True, null=True)
    is_statement_fetch_supported = models.IntegerField(blank=True, null=True)
    is_transaction_enquiry_supported = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    mobile_bank_logo = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partner_banks_bk'


class Payables(models.Model):
    payables_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    contacts_id = models.IntegerField(blank=True, null=True)
    contact_name = models.CharField(max_length=191)
    amount_paid = models.DecimalField(max_digits=16, decimal_places=2)
    paid_on = models.DateField()
    last_paid_amount = models.DecimalField(max_digits=16, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payables'


class PaymentGatewaySettlementRequestStatuses(models.Model):
    payment_gateway_settlement_request_statuses_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=100)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_gateway_settlement_request_statuses'


class PaymentGatewaySettlementRequests(models.Model):
    payment_gateway_settlement_requests_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    payment_gateway_settlement_request_statuses_id = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    admin_users_id = models.IntegerField(blank=True, null=True)
    approved_on = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_gateway_settlement_requests'


class PaymentGateways(models.Model):
    payment_gateways_id = models.AutoField(primary_key=True)
    payment_gateways_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_gateways'


class PaymentLinkTransactions(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_link_transactions'


class PaymentLinks(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_links'


class PaymentPurposes(models.Model):
    payment_purposes_id = models.AutoField(primary_key=True)
    payment_purpose = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_purposes'


class PaymentRequestBreakupDetails(models.Model):
    payment_request_breakup_details_id = models.AutoField(primary_key=True)
    payment_requests_id = models.PositiveIntegerField()
    recepient_name = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    ifsc_code = models.CharField(max_length=191, blank=True, null=True)
    beneficiary_account_number = models.CharField(max_length=191, blank=True, null=True)
    purpose = models.CharField(max_length=191, blank=True, null=True)
    read_status = models.CharField(max_length=191, blank=True, null=True)
    errors = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_request_breakup_details'


class PaymentRequestCheckers(models.Model):
    payment_request_checkers_id = models.AutoField(primary_key=True)
    payment_requests_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    group_id = models.PositiveIntegerField()
    status_id = models.PositiveIntegerField()
    approved_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_request_checkers'


class PaymentRequestStatues(models.Model):
    payment_request_statues_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_request_statues'


class PaymentRequests(models.Model):
    payment_requests_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    source_id = models.IntegerField()
    source_type = models.CharField(max_length=191)
    total_requested_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    total_approved_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    transaction_ref_no = models.CharField(max_length=55, blank=True, null=True)
    external_fund_transfers_id = models.IntegerField(blank=True, null=True)
    transaction_statuses_id = models.IntegerField(blank=True, null=True)
    transaction_date = models.DateField(blank=True, null=True)
    open_bank_accounts_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    payment_request_statuses_id = models.IntegerField(blank=True, null=True)
    rejection_reasons = models.TextField(blank=True, null=True)
    maker_checker_parameters_id = models.PositiveIntegerField(blank=True, null=True)
    cron_processed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'payment_requests'


class PaymentSchedules(models.Model):
    payment_schedules_id = models.AutoField(primary_key=True)
    schedule_name = models.CharField(max_length=191)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_schedules'


class PaymentTerms(models.Model):
    payment_terms_id = models.AutoField(primary_key=True)
    term_name = models.CharField(max_length=191, blank=True, null=True)
    term_duration = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_terms'


class PaymentTransactionSchedules(models.Model):
    payment_transaction_schedules_id = models.AutoField(primary_key=True)
    payment_transactions_id = models.IntegerField()
    payment_schedules_id = models.IntegerField()
    is_paid = models.IntegerField()
    payment_date = models.DateTimeField(blank=True, null=True)
    frequencies_id = models.IntegerField(blank=True, null=True)
    repeat_for = models.IntegerField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_transaction_schedules'


class PaymentTransactionTags(models.Model):
    payment_transaction_tags_id = models.AutoField(primary_key=True)
    payment_transactions_id = models.IntegerField()
    tags_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_transaction_tags'


class PaymentTransactions(models.Model):
    payment_transactions_id = models.AutoField(primary_key=True)
    bank_accounts_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    contacts_id = models.IntegerField(blank=True, null=True)
    expense_categories_id = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    purpose = models.CharField(max_length=191, blank=True, null=True)
    transaction_ref_no = models.CharField(max_length=191, blank=True, null=True)
    transaction_status = models.CharField(max_length=191, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_transactions'


class PaymentTypes(models.Model):
    payment_types_id = models.AutoField(primary_key=True)
    payment_type = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_types'


class PayoneerCompanyMaps(models.Model):
    payoneer_company_maps_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    payee_id = models.CharField(max_length=30)
    client_session_id = models.CharField(max_length=30)
    registration_status = models.CharField(max_length=8)
    payoneer_id = models.IntegerField()
    decline_reason = models.CharField(max_length=150, blank=True, null=True)
    registration_link = models.CharField(max_length=250, blank=True, null=True)
    kyc_status = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payoneer_company_maps'


class PayoneerPaymentDetails(models.Model):
    payoneer_payment_details_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    invoices_id = models.IntegerField()
    client_session_id = models.CharField(max_length=40)
    payment_status = models.CharField(max_length=12)
    payoneer_id = models.IntegerField()
    payee_id = models.CharField(max_length=30)
    payment_id = models.IntegerField()
    event_time = models.TimeField()
    reason_code = models.CharField(max_length=199)
    reason_description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.CharField(max_length=5)
    countries_id = models.IntegerField()
    descriptions = models.TextField(blank=True, null=True)
    res_audit_id = models.CharField(max_length=240, blank=True, null=True)
    res_code = models.IntegerField(blank=True, null=True)
    res_description = models.CharField(max_length=240, blank=True, null=True)
    payment_request_id = models.CharField(max_length=240, blank=True, null=True)
    payment_link = models.CharField(max_length=240, blank=True, null=True)
    payoneer_request_response_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payoneer_payment_details'


class PayoneerRequestResponses(models.Model):
    payoneer_request_responses_id = models.AutoField(primary_key=True)
    client_session_id = models.CharField(max_length=40)
    url = models.CharField(max_length=240)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payoneer_request_responses'


class PayoneerWebhookLogs(models.Model):
    payoneer_webhook_logs_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    payee_id = models.CharField(max_length=30)
    client_session_id = models.CharField(max_length=30)
    payment_status = models.CharField(max_length=12)
    payoneer_id = models.IntegerField()
    payment_id = models.IntegerField()
    event_time = models.TimeField()
    reason_code = models.CharField(max_length=199)
    reason_description = models.CharField(max_length=255)
    data = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payoneer_webhook_logs'


class PayswiffMerchants(models.Model):
    payswiff_merchant_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    merchant_id = models.CharField(unique=True, max_length=191, blank=True, null=True)
    merchant_name = models.CharField(max_length=191, blank=True, null=True)
    package = models.CharField(max_length=191, blank=True, null=True)
    mobile_number = models.CharField(max_length=191, blank=True, null=True)
    api_key = models.CharField(max_length=191, blank=True, null=True)
    city = models.CharField(max_length=191, blank=True, null=True)
    registration_date = models.DateTimeField(blank=True, null=True)
    t_and_c_confirmed_at = models.DateTimeField(blank=True, null=True)
    hash = models.CharField(max_length=200, blank=True, null=True)
    is_t_and_c_confirmed = models.IntegerField()
    status = models.CharField(max_length=191, blank=True, null=True)
    mid_or_tid_status = models.CharField(max_length=191, blank=True, null=True)
    pos_device_serial_num = models.CharField(max_length=191, blank=True, null=True)
    payswiff_onboarding_files_id = models.IntegerField(blank=True, null=True)
    tnc_files_id = models.IntegerField(blank=True, null=True)
    payswiff_merchant_onbaording_status_id = models.IntegerField(blank=True, null=True)
    mpos_device_activation_statuses_id = models.IntegerField(blank=True, null=True)
    payswiff_onboarding_rejection_reason = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payswiff_merchants'


class PayswiffOnboardingStatuses(models.Model):
    payswiff_onboarding_statuses_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payswiff_onboarding_statuses'


class PayswiffSettlements(models.Model):
    payswiff_settlements_id = models.AutoField(primary_key=True)
    accounts_id = models.PositiveIntegerField(blank=True, null=True)
    companies_id = models.PositiveIntegerField(blank=True, null=True)
    users_id = models.PositiveIntegerField(blank=True, null=True)
    open_pg_txn_id = models.CharField(unique=True, max_length=191, blank=True, null=True)
    pg_txn_ref_num = models.CharField(unique=True, max_length=191, blank=True, null=True)
    total_amount = models.FloatField()
    open_tdr = models.FloatField()
    open_gst = models.FloatField()
    open_total_fee = models.FloatField()
    open_net_amount = models.FloatField()
    settlement_source = models.CharField(max_length=191)
    settlement_txn_id = models.CharField(max_length=191, blank=True, null=True)
    settlement_status_id = models.PositiveIntegerField()
    settled_by = models.CharField(max_length=191, blank=True, null=True)
    settled_to_open_date = models.DateTimeField(blank=True, null=True)
    settled_to_merchant_date = models.DateTimeField(blank=True, null=True)
    settlement_modes_id = models.PositiveIntegerField()
    is_held = models.IntegerField()
    hold_by = models.PositiveIntegerField(blank=True, null=True)
    hold_reason = models.CharField(max_length=191, blank=True, null=True)
    available_on = models.DateTimeField(blank=True, null=True)
    source_type = models.CharField(max_length=191)
    source_id = models.PositiveIntegerField()
    description = models.CharField(max_length=191, blank=True, null=True)
    payswiff_merchant_id = models.CharField(max_length=191, blank=True, null=True)
    merchant_name = models.CharField(max_length=191, blank=True, null=True)
    merchant_ref_num = models.CharField(max_length=191, blank=True, null=True)
    payswiff_payment_id = models.CharField(max_length=191, blank=True, null=True)
    payswiff_txn_id = models.CharField(max_length=191, blank=True, null=True)
    txn_time = models.CharField(max_length=191, blank=True, null=True)
    device_serial_num = models.CharField(max_length=191, blank=True, null=True)
    device_model = models.CharField(max_length=191, blank=True, null=True)
    transaction_type = models.CharField(max_length=191, blank=True, null=True)
    card_type = models.CharField(max_length=191, blank=True, null=True)
    card_holder_name = models.CharField(max_length=191, blank=True, null=True)
    card_number = models.CharField(max_length=191, blank=True, null=True)
    customer_mobile_number = models.CharField(max_length=191, blank=True, null=True)
    payswiff_txn_amount = models.FloatField(blank=True, null=True)
    payswiff_txn_type = models.CharField(max_length=191, blank=True, null=True)
    payswiff_tdr_perc = models.CharField(max_length=191, blank=True, null=True)
    payswiff_tdr = models.FloatField(blank=True, null=True)
    payswiff_gst = models.FloatField(blank=True, null=True)
    payswiff_net_amount = models.FloatField(blank=True, null=True)
    payswiff_record_type = models.CharField(max_length=191, blank=True, null=True)
    is_processed = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payswiff_settlements'


class PayswiffTransactions(models.Model):
    payswiff_transactions_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    amount = models.FloatField()
    pg_transaction_statuses_id = models.PositiveIntegerField(blank=True, null=True)
    pg_txn_time = models.DateTimeField(blank=True, null=True)
    open_pg_txn_id = models.CharField(max_length=191, blank=True, null=True)
    pg_txn_ref_num = models.CharField(unique=True, max_length=191, blank=True, null=True)
    settlement_txn_id = models.CharField(max_length=191, blank=True, null=True)
    merchant_id = models.CharField(max_length=191, blank=True, null=True)
    transaction_id = models.CharField(max_length=191, blank=True, null=True)
    payment_id = models.CharField(max_length=191, blank=True, null=True)
    merchant_ref_invoice_no = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    card_type = models.CharField(max_length=191, blank=True, null=True)
    card_holder_name = models.CharField(max_length=191, blank=True, null=True)
    terminal_id = models.CharField(max_length=191, blank=True, null=True)
    auth_id = models.CharField(max_length=191, blank=True, null=True)
    card_number = models.CharField(max_length=191, blank=True, null=True)
    card_brand = models.CharField(max_length=191, blank=True, null=True)
    transaction_type = models.CharField(max_length=191, blank=True, null=True)
    response_code = models.CharField(max_length=191, blank=True, null=True)
    response_message = models.CharField(max_length=191, blank=True, null=True)
    merchant_mobile_number = models.CharField(max_length=191, blank=True, null=True)
    customer_mobile_number = models.CharField(max_length=191, blank=True, null=True)
    payment_method = models.CharField(max_length=191, blank=True, null=True)
    secure_hash = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payswiff_transactions'


class PennyDrops(models.Model):
    penny_drops_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    bene_account_number = models.CharField(max_length=191)
    ifsc_code = models.CharField(max_length=191)
    recepient_name = models.CharField(max_length=191, blank=True, null=True)
    email_id = models.CharField(max_length=191, blank=True, null=True)
    mobile_number = models.CharField(max_length=191, blank=True, null=True)
    merchant_ref_id = models.CharField(max_length=191)
    open_transaction_ref_id = models.CharField(max_length=191, blank=True, null=True)
    bank_ref_num = models.CharField(max_length=191, blank=True, null=True)
    verification_status = models.CharField(max_length=191, blank=True, null=True)
    is_pennydrop_success = models.IntegerField()
    verification_message = models.CharField(max_length=191, blank=True, null=True)
    partner_banks_id = models.IntegerField()
    description = models.TextField()
    is_enterprise = models.IntegerField()
    account_holder_name = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'penny_drops'


class PerfiosAccountTransactions(models.Model):
    perfios_account_transactions_id = models.BigAutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    user_unique_id = models.CharField(max_length=191, blank=True, null=True)
    acc_status = models.CharField(max_length=191, blank=True, null=True)
    bank_name = models.CharField(max_length=191, blank=True, null=True)
    itype = models.CharField(max_length=191, blank=True, null=True)
    user_account_id = models.IntegerField(blank=True, null=True)
    inst_id = models.IntegerField(blank=True, null=True)
    inst_link_code = models.IntegerField(blank=True, null=True)
    currency_code = models.CharField(max_length=191, blank=True, null=True)
    currency_symbol = models.CharField(max_length=191, blank=True, null=True)
    txn_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    txn_id = models.IntegerField(blank=True, null=True)
    txn_date = models.CharField(max_length=191, blank=True, null=True)
    txn_details = models.CharField(max_length=191, blank=True, null=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    user_comment = models.CharField(max_length=191, blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfios_account_transactions'


class PerfiosConnectedAccountDetails(models.Model):
    perfios_connected_account_details_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    user_unique_id = models.CharField(max_length=191, blank=True, null=True)
    user_account_id = models.IntegerField(blank=True, null=True)
    account_name = models.CharField(max_length=191, blank=True, null=True)
    account_status = models.CharField(max_length=191, blank=True, null=True)
    inst_id = models.IntegerField(blank=True, null=True)
    inst_link_code = models.IntegerField(blank=True, null=True)
    link_number = models.IntegerField(blank=True, null=True)
    currency_code = models.CharField(max_length=191, blank=True, null=True)
    currency_symbol = models.CharField(max_length=191, blank=True, null=True)
    itype = models.CharField(max_length=191, blank=True, null=True)
    current_balance = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cur_balance_last_update = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfios_connected_account_details'


class PerfiosListInstitutions(models.Model):
    perfios_list_institutions_id = models.AutoField(primary_key=True)
    institution_id = models.IntegerField(blank=True, null=True)
    itype = models.CharField(max_length=191, blank=True, null=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    bank_logo = models.TextField(blank=True, null=True)
    mobile_bank_logo = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    geography = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfios_list_institutions'


class PerfiosSiteMetadataInstitutions(models.Model):
    perfios_site_metadata_institutions_id = models.AutoField(primary_key=True)
    display_id_type_identifiers = models.IntegerField(blank=True, null=True)
    inst_code = models.IntegerField(blank=True, null=True)
    inst_desc = models.CharField(max_length=191, blank=True, null=True)
    inst_id = models.IntegerField(blank=True, null=True)
    inst_name = models.CharField(max_length=191, blank=True, null=True)
    bank_logo = models.TextField(blank=True, null=True)
    is_discovery_supported = models.CharField(max_length=191, blank=True, null=True)
    labels_confirm_password = models.CharField(max_length=191, blank=True, null=True)
    labels_password = models.CharField(max_length=191, blank=True, null=True)
    labels_userid = models.CharField(db_column='labels_userId', max_length=191, blank=True, null=True)  # Field name made lowercase.
    mfa_requirement = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfios_site_metadata_institutions'


class PerfiosUsers(models.Model):
    perfios_users_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    user_unique_id = models.CharField(max_length=191, blank=True, null=True)
    user_reg_status_code = models.IntegerField(blank=True, null=True)
    user_reg_status_message = models.CharField(max_length=191, blank=True, null=True)
    user_reg_status_created_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfios_users'


class Persistences(models.Model):
    users_id = models.PositiveIntegerField(blank=True, null=True)
    code = models.CharField(unique=True, max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persistences'


class PgActivationStatus(models.Model):
    pg_activation_status_id = models.AutoField(primary_key=True)
    pg_activation_status = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_activation_status'


class PgCharges(models.Model):
    pg_charges_id = models.AutoField(primary_key=True)
    pg_settlements_id = models.IntegerField()
    payment_gateways_id = models.IntegerField()
    transaction_amount = models.DecimalField(max_digits=16, decimal_places=2)
    pg_tdr_type = models.CharField(max_length=20)
    pg_tdr_value = models.DecimalField(max_digits=10, decimal_places=2)
    pg_tdr_amount = models.DecimalField(max_digits=16, decimal_places=2)
    pg_tax_amount = models.DecimalField(max_digits=16, decimal_places=2)
    pg_settled_to_open_amount = models.DecimalField(max_digits=16, decimal_places=2)
    open_tdr_type = models.CharField(max_length=20)
    open_tdr_value = models.DecimalField(max_digits=10, decimal_places=2)
    open_tdr_amount = models.DecimalField(max_digits=10, decimal_places=2)
    open_tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    open_settled_to_merchant_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_charges'


class PgConfigurations(models.Model):
    pg_configurations_id = models.BigAutoField(primary_key=True)
    config_type = models.CharField(max_length=191, blank=True, null=True)
    config_value = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_configurations'


class PgCustomerCards(models.Model):
    pg_customer_cards_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    mobile_number = models.CharField(max_length=200)
    card_number = models.TextField()
    card_nick_name = models.CharField(max_length=200)
    card_last_4_digits = models.CharField(max_length=200)
    expiry_mm = models.TextField()
    expiry_yy = models.TextField()
    card_type = models.CharField(max_length=200)
    card_provider = models.CharField(max_length=200)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_customer_cards'


class PgCustomers(models.Model):
    pg_customers_id = models.AutoField(primary_key=True)
    mobile_number = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_customers'


class PgMarketPlaceSettlementTransactions(models.Model):
    pg_market_place_settlement_transactions_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    marketplace_pg_sub_accounts_id = models.IntegerField(blank=True, null=True)
    sub_account_ref_id = models.CharField(max_length=191, blank=True, null=True)
    total_transaction_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    tdr = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    gst = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    open_total_charges = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    commision_type = models.CharField(max_length=10, blank=True, null=True)
    commision_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    commision_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    merchant_settlement_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    source_type = models.CharField(max_length=199, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    outward_settlement_statuses_id = models.IntegerField(blank=True, null=True)
    settlement_source = models.CharField(max_length=191)
    settlement_txn_id = models.CharField(max_length=191, blank=True, null=True)
    settlement_modes_id = models.IntegerField()
    pg_transactions_id = models.IntegerField(blank=True, null=True)
    file_id = models.CharField(max_length=191, blank=True, null=True)
    has_mail_sent = models.IntegerField()
    description = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_market_place_settlement_transactions'


class PgMarketPlaceSettlements(models.Model):
    pg_market_place_settlements_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    total_transaction_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    open_total_charges = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    commision_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    merchant_settlement_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    transactions_count = models.IntegerField(blank=True, null=True)
    outward_settlement_statuses_id = models.IntegerField(blank=True, null=True)
    merchant_outward_settlement_statuses_id = models.IntegerField()
    settlement_txn_id = models.CharField(unique=True, max_length=191, blank=True, null=True)
    internal_transaction_ref_id = models.CharField(max_length=191, blank=True, null=True)
    transaction_types_id = models.IntegerField(blank=True, null=True)
    bank_transaction_id = models.CharField(max_length=191, blank=True, null=True)
    external_fund_transfers_id = models.CharField(max_length=191, blank=True, null=True)
    fund_transfer_bulk_intermediaries_id = models.CharField(max_length=191, blank=True, null=True)
    sub_account_ref_id = models.CharField(max_length=191, blank=True, null=True)
    marketplace_pg_sub_accounts_id = models.CharField(max_length=191, blank=True, null=True)
    bene_account_number = models.CharField(max_length=191, blank=True, null=True)
    ifsc_code = models.CharField(max_length=191, blank=True, null=True)
    recepient_name = models.CharField(max_length=191, blank=True, null=True)
    email_id = models.CharField(max_length=191, blank=True, null=True)
    mobile_number = models.CharField(max_length=191, blank=True, null=True)
    bank_name = models.CharField(max_length=191, blank=True, null=True)
    request_file = models.CharField(max_length=191, blank=True, null=True)
    response_file = models.CharField(max_length=191, blank=True, null=True)
    request_data = models.TextField(blank=True, null=True)
    response_data = models.TextField(blank=True, null=True)
    bank_transaction_status_id = models.IntegerField(blank=True, null=True)
    utr_number = models.CharField(max_length=191, blank=True, null=True)
    purpose = models.CharField(max_length=191, blank=True, null=True)
    bank_response = models.CharField(max_length=191, blank=True, null=True)
    bank_response_time = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    settlement_modes_id = models.IntegerField()
    use_withdrawal_account = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_market_place_settlements'


class PgMerchantRefIds(models.Model):
    pg_merchant_ref_id = models.CharField(max_length=191)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_merchant_ref_ids'


class PgOpenRefIds(models.Model):
    pg_open_ref_id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pg_open_ref_ids'


class PgOutwardSettlementHistories(models.Model):
    pg_outward_settlement_histories_id = models.AutoField(primary_key=True)
    pg_outward_settlements_id = models.IntegerField(blank=True, null=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    pg_transactions_id = models.IntegerField(blank=True, null=True)
    total_transaction_amount = models.DecimalField(max_digits=14, decimal_places=2)
    open_total_charges = models.DecimalField(max_digits=14, decimal_places=2)
    merchant_settlement_amount = models.DecimalField(max_digits=14, decimal_places=2)
    outward_settlement_statuses_id = models.IntegerField()
    settlement_txn_id = models.CharField(max_length=191)
    transactions_count = models.IntegerField()
    total_adjusted_amount = models.DecimalField(max_digits=14, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_outward_settlement_histories'


class PgOutwardSettlements(models.Model):
    pg_outward_settlements_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    total_transaction_amount = models.DecimalField(max_digits=14, decimal_places=2)
    open_total_charges = models.DecimalField(max_digits=14, decimal_places=2)
    merchant_settlement_amount = models.DecimalField(max_digits=14, decimal_places=2)
    outward_settlement_statuses_id = models.IntegerField()
    settlement_txn_id = models.CharField(unique=True, max_length=191)
    internal_transaction_ref_id = models.CharField(max_length=191, blank=True, null=True)
    files_id = models.IntegerField(blank=True, null=True)
    fund_transfer_types_id = models.IntegerField(blank=True, null=True)
    bank_transaction_id = models.CharField(max_length=191, blank=True, null=True)
    transactions_count = models.IntegerField()
    merchant_pg_settlement_types_id = models.IntegerField(blank=True, null=True)
    external_fund_transfers_id = models.IntegerField(blank=True, null=True)
    fund_transfer_bulk_intermediaries_id = models.IntegerField(blank=True, null=True)
    is_adjustment_available = models.IntegerField()
    total_adjusted_amount = models.DecimalField(max_digits=14, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    admin_users_id = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_outward_settlements'


class PgOutwardSettlementsIds(models.Model):
    pg_outward_settlements_id = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'pg_outward_settlements_ids'


class PgPaymentSources(models.Model):
    pg_payment_sources_id = models.AutoField(primary_key=True)
    pg_payment_source = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_payment_sources'


class PgSettings(models.Model):
    pg_account_settings_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    is_pg_enabled = models.IntegerField()
    payment_response_time = models.DateTimeField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_settings'


class PgSettlementReports(models.Model):
    pg_settlement_reports_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    transaction_amount = models.FloatField(blank=True, null=True)
    open_tdr = models.FloatField(blank=True, null=True)
    same_day_settlement_charge = models.DecimalField(max_digits=12, decimal_places=2)
    open_gst = models.FloatField(blank=True, null=True)
    open_total_charges = models.FloatField(blank=True, null=True)
    pg_transactions_id = models.CharField(max_length=191, blank=True, null=True)
    pg_txn_ref_num = models.CharField(unique=True, max_length=191)
    first_name = models.CharField(max_length=191, blank=True, null=True)
    last_name = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    username = models.CharField(max_length=191, blank=True, null=True)
    api_version = models.CharField(max_length=20, blank=True, null=True)
    company_gstin = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    payment_purpose = models.CharField(max_length=191, blank=True, null=True)
    sac_code = models.CharField(max_length=100, blank=True, null=True)
    pg_merchant_ref_id = models.CharField(max_length=191, blank=True, null=True)
    address_available = models.CharField(max_length=191, blank=True, null=True)
    payment_gateways_id = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    source_of_registration = models.CharField(max_length=150, blank=True, null=True)
    migrated_to = models.CharField(max_length=150, blank=True, null=True)
    open_pg_txn_id = models.CharField(max_length=50, blank=True, null=True)
    transaction_date = models.DateTimeField(blank=True, null=True)
    settlement_date = models.DateTimeField()
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    card_provider = models.CharField(max_length=100, blank=True, null=True)
    transaction_type = models.CharField(max_length=255, blank=True, null=True)
    payment_gateway = models.IntegerField(blank=True, null=True)
    current_subscription_package = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_settlement_reports'


class PgSettlementStatus(models.Model):
    pg_settlement_status_id = models.AutoField(primary_key=True)
    pg_settlement_status = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_settlement_status'


class PgSettlements(models.Model):
    pg_settlements_id = models.AutoField(primary_key=True)
    pg_transactions_id = models.CharField(max_length=200)
    open_transactions_id = models.CharField(max_length=200)
    transaction_amount = models.DecimalField(max_digits=16, decimal_places=2)
    payment_date = models.CharField(max_length=20)
    settlement_date = models.CharField(max_length=20)
    source = models.CharField(max_length=200)
    source_id = models.IntegerField()
    settlement_status_id = models.IntegerField()
    payment_gateways_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_settlements'


class PgTransactionRequests(models.Model):
    pg_transaction_requests_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    pg_transactions_id = models.CharField(max_length=191)
    enterprise_pg_transaction_statuses_id = models.CharField(max_length=2)
    customer_name = models.CharField(max_length=191)
    customer_mob_num = models.CharField(max_length=10)
    customer_email = models.CharField(max_length=191)
    pg_transaction_request_statuses_id = models.CharField(max_length=2)
    pg_txn_req_ref_id = models.CharField(max_length=191)
    currency = models.CharField(max_length=191)
    pg_merchant_ref_id = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    payment_purposes_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pg_transaction_requests'


class PgTransactionRequestsStatuses(models.Model):
    pg_transaction_requests_statuses_id = models.AutoField(primary_key=True)
    pg_transaction_requests_status = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_transaction_requests_statuses'


class PgTransactionStatuses(models.Model):
    pg_transaction_statuses_id = models.AutoField(primary_key=True)
    pg_transaction_status = models.CharField(max_length=80)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_transaction_statuses'


class PgTransactions(models.Model):
    pg_transactions_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    contacts_id = models.IntegerField(blank=True, null=True)
    source_type = models.CharField(max_length=191, blank=True, null=True)
    source_id = models.CharField(max_length=191, blank=True, null=True)
    amount = models.CharField(max_length=191, blank=True, null=True)
    convenience_fee = models.DecimalField(max_digits=10, decimal_places=2)
    merchant_transaction_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    open_pg_txn_id = models.CharField(unique=True, max_length=191, blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    customer_email = models.CharField(max_length=255, blank=True, null=True)
    customer_mobile_number = models.CharField(max_length=255, blank=True, null=True)
    customer_ip = models.CharField(max_length=255, blank=True, null=True)
    payment_gateways_id = models.IntegerField(blank=True, null=True)
    transaction_types_id = models.IntegerField(blank=True, null=True)
    card_types_id = models.CharField(max_length=255, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    redirect_url = models.CharField(max_length=255, blank=True, null=True)
    notify_url = models.CharField(max_length=255, blank=True, null=True)
    pg_transaction_statuses_id = models.IntegerField(blank=True, null=True)
    pg_txn_time = models.CharField(max_length=255, blank=True, null=True)
    pg_txn_ref_num = models.CharField(max_length=191, blank=True, null=True)
    payment_link_unique_id = models.CharField(max_length=255, blank=True, null=True)
    is_enterprise_checkout_txn = models.CharField(max_length=255)
    settlement_source = models.CharField(max_length=191)
    settlement_txn_id = models.CharField(max_length=191, blank=True, null=True)
    merchant_pg_settlement_types_id = models.IntegerField()
    pg_payment_sources_id = models.IntegerField()
    payment_types_id = models.IntegerField(blank=True, null=True)
    payment_purposes_id = models.IntegerField(blank=True, null=True)
    pg_merchant_ref_id = models.CharField(max_length=191, blank=True, null=True)
    merchant_terminal_id = models.CharField(max_length=191, blank=True, null=True)
    is_settlement_available = models.IntegerField(blank=True, null=True)
    sub_accounts_id = models.CharField(max_length=191, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_international_txn = models.IntegerField()
    merchant_id = models.CharField(max_length=100, blank=True, null=True)
    payment_token_id = models.CharField(max_length=100, blank=True, null=True)
    currency = models.CharField(max_length=30, blank=True, null=True)
    payment_instrument = models.IntegerField(blank=True, null=True)
    card_id = models.CharField(max_length=100, blank=True, null=True)
    payment_status = models.CharField(max_length=60, blank=True, null=True)
    pg_transaction_source = models.CharField(max_length=255, blank=True, null=True)
    payment_error_code = models.CharField(max_length=100, blank=True, null=True)
    payment_error_description = models.CharField(max_length=255, blank=True, null=True)
    vpa = models.CharField(max_length=255, blank=True, null=True)
    stripe_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pg_transactions'
        unique_together = (('pg_txn_ref_num', 'payment_gateways_id'),)


class Pincodes(models.Model):
    pincodes_id = models.AutoField(primary_key=True)
    pincode = models.IntegerField()
    post_office = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    sbm_city_code = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=40, blank=True, null=True)
    sbm_state_code = models.IntegerField(blank=True, null=True)
    state_code = models.CharField(max_length=2, blank=True, null=True)
    division = models.CharField(max_length=40, blank=True, null=True)
    region = models.CharField(max_length=40, blank=True, null=True)
    circle = models.CharField(max_length=40, blank=True, null=True)
    taluk = models.CharField(max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pincodes'


class PosDeviceDetails(models.Model):
    pos_device_details_id = models.AutoField(primary_key=True)
    device_serial_number = models.CharField(unique=True, max_length=100, blank=True, null=True)
    part_number = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    is_assigned = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_device_details'


class PosUsers(models.Model):
    pos_users_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    fos_emp_id = models.CharField(max_length=199)
    latitude = models.CharField(max_length=199, blank=True, null=True)
    longitude = models.CharField(max_length=199, blank=True, null=True)
    pos_device_serial_num = models.CharField(max_length=199, blank=True, null=True)
    pos_deposit_waveoff_coupon_code_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_users'


class PreAuthBalances(models.Model):
    pre_auth_balances_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    card_number = models.CharField(max_length=191, blank=True, null=True)
    ref_id = models.CharField(max_length=200)
    source_type = models.CharField(max_length=200)
    source_id = models.IntegerField()
    is_debit_complete = models.IntegerField()
    partner_banks_id = models.IntegerField()
    balance = models.DecimalField(max_digits=14, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pre_auth_balances'


class ProcessedBulkEntries(models.Model):
    processed_bulk_entries_id = models.AutoField(primary_key=True)
    fund_transfer_bulk_intermediaries_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'processed_bulk_entries'


class ProductTypes(models.Model):
    product_types_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    additional_details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_types'


class ProofFiles(models.Model):
    proof_files_id = models.AutoField(primary_key=True)
    files_id = models.IntegerField(blank=True, null=True)
    address_proofs_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proof_files'


class PushNotificationServiceProviders(models.Model):
    name = models.CharField(max_length=191)
    is_default = models.IntegerField()
    status = models.IntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'push_notification_service_providers'


class QrReferenceIds(models.Model):
    qr_reference_id = models.AutoField(primary_key=True)
    partner_banks_id = models.IntegerField()
    reference_id = models.CharField(max_length=191, blank=True, null=True)
    mode_of_generation = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'qr_reference_ids'


class QuickCollectBulkIntermediaries(models.Model):
    quick_collect_bulk_intermediaries_id = models.AutoField(primary_key=True)
    files_bulk_id = models.IntegerField()
    batch_id = models.CharField(max_length=15)
    users_id = models.PositiveIntegerField()
    accounts_id = models.PositiveIntegerField()
    companies_id = models.PositiveIntegerField()
    contacts_id = models.IntegerField()
    income_categories_id = models.IntegerField(blank=True, null=True)
    income_category_name = models.CharField(max_length=191, blank=True, null=True)
    recepient_name = models.CharField(max_length=128)
    email_id = models.CharField(max_length=60, blank=True, null=True)
    mobile_number = models.CharField(max_length=30)
    is_complete = models.IntegerField()
    read_status = models.CharField(max_length=10)
    reason = models.TextField()
    invoice_user_input_reference_id = models.CharField(max_length=50)
    invoice_note = models.TextField()
    total_amount_due = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    is_recurring = models.IntegerField()
    frequencies_id = models.CharField(max_length=20)
    repeat_for = models.IntegerField()
    start_date = models.DateField(blank=True, null=True)
    is_emandate_requested = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    invoices_id = models.IntegerField(blank=True, null=True)
    do_update = models.IntegerField(blank=True, null=True)
    linked_contacts_id = models.IntegerField(blank=True, null=True)
    transaction_client_types_id = models.IntegerField(blank=True, null=True)
    allow_partial_payment = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quick_collect_bulk_intermediaries'


class Receivables(models.Model):
    receivables_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    contacts_id = models.IntegerField()
    contact_name = models.CharField(max_length=191)
    total_billed = models.DecimalField(max_digits=16, decimal_places=2)
    total_received = models.DecimalField(max_digits=16, decimal_places=2)
    outstanding = models.DecimalField(max_digits=16, decimal_places=2)
    dso = models.IntegerField()
    last_received_amount = models.DecimalField(max_digits=16, decimal_places=2)
    paid_at = models.DateTimeField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'receivables'


class ReconcileInvoiceBulkIntermediaries(models.Model):
    id = models.BigAutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField(blank=True, null=True)
    invoices_id = models.IntegerField(blank=True, null=True)
    open_services_id = models.IntegerField(blank=True, null=True)
    journal_entry_date = models.DateTimeField(blank=True, null=True)
    journal_description = models.TextField(blank=True, null=True)
    is_complete = models.IntegerField()
    batch_id = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reconcile_invoice_bulk_intermediaries'


class ReconcileInvoiceJournalEntries(models.Model):
    id = models.BigAutoField(primary_key=True)
    reconcile_invoice_bulk_id = models.IntegerField()
    l1_categories_id = models.IntegerField()
    l1_category = models.CharField(max_length=200)
    l2_categories_id = models.IntegerField()
    l2_category = models.CharField(max_length=200)
    l3_categories_id = models.IntegerField()
    l3_category = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type_cr_dr = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reconcile_invoice_journal_entries'


class ReconciliationAtomSettlements(models.Model):
    reconciliation_atom_settlements_id = models.AutoField(primary_key=True)
    atom_transaction_id = models.CharField(unique=True, max_length=255)
    transaction_state = models.CharField(max_length=255)
    settlement_date = models.DateTimeField()
    merchant_txn_id = models.CharField(max_length=255)
    client_code = models.CharField(max_length=255)
    bank_reference_no = models.CharField(max_length=255)
    refund_reference_no = models.CharField(max_length=255)
    gross_txn_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_charges = models.DecimalField(max_digits=10, decimal_places=2)
    service_tax = models.DecimalField(max_digits=10, decimal_places=2)
    sb_cess = models.DecimalField(max_digits=10, decimal_places=2)
    krishi_kalyan_cess = models.DecimalField(max_digits=10, decimal_places=2)
    total_chargable = models.DecimalField(max_digits=10, decimal_places=2)
    net_amount_to_be_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=255)
    admin_reconciliation_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    tpsl_transaction_id = models.CharField(unique=True, max_length=191)

    class Meta:
        managed = False
        db_table = 'reconciliation_atom_settlements'


class ReconciliationAtomTransactions(models.Model):
    reconciliation_atom_transactions_id = models.AutoField(primary_key=True)
    atom_transaction_id = models.CharField(unique=True, max_length=191)
    merchant_txn_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    currency = models.CharField(max_length=255)
    transaction_date = models.DateTimeField()
    status = models.CharField(max_length=255)
    is_refunded = models.IntegerField()
    bank_reference_no = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    transaction_charges = models.DecimalField(max_digits=16, decimal_places=2)
    gst = models.DecimalField(max_digits=10, decimal_places=2)
    sb_cess = models.DecimalField(max_digits=10, decimal_places=2)
    krishi_kalyan_cess = models.DecimalField(max_digits=10, decimal_places=2)
    total_chargable = models.DecimalField(max_digits=16, decimal_places=2)
    net_amount_to_be_paid = models.DecimalField(max_digits=16, decimal_places=2)
    refund_amount = models.DecimalField(max_digits=16, decimal_places=2)
    refund_initiated_date = models.DateTimeField()
    refund_processed_date = models.DateTimeField()
    refund_closed_date = models.DateTimeField()
    refund_closing_remarks = models.CharField(max_length=255)
    admin_reconciliation_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reconciliation_atom_transactions'


class ReconciliationCardsM2PTransactions(models.Model):
    reconciliation_cards_m2p_transactions_id = models.AutoField(primary_key=True)
    transaction_date = models.DateTimeField()
    txn_ref_num = models.CharField(max_length=255)
    card_number = models.CharField(max_length=255)
    credit_debit_flag = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    balance = models.DecimalField(max_digits=16, decimal_places=2)
    transaction_amount = models.DecimalField(max_digits=16, decimal_places=2)
    transaction_currency = models.IntegerField()
    rrn = models.CharField(max_length=255)
    auth_code = models.CharField(max_length=255)
    network_data = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    kit_num = models.CharField(max_length=255)
    txn_type = models.CharField(max_length=255)
    admin_reconciliation_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reconciliation_cards_m2p_transactions'


class ReconciliationEazypays(models.Model):
    reconciliation_eazypay_id = models.AutoField(primary_key=True)
    reference_no = models.CharField(unique=True, max_length=191)
    transaction_date = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    eazypay_status = models.CharField(max_length=191, blank=True, null=True)
    transaction_id_from_eazypay = models.CharField(max_length=191, blank=True, null=True)
    admin_reconciliation_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reconciliation_eazypays'


class ReconciliationIcicis(models.Model):
    reconciliation_icici_id = models.AutoField(primary_key=True)
    reference_no = models.CharField(unique=True, max_length=191, blank=True, null=True)
    transaction_date = models.DateField(blank=True, null=True)
    date_from_icici = models.DateTimeField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    transaction_type = models.CharField(max_length=191, blank=True, null=True)
    transaction_mode = models.CharField(max_length=191, blank=True, null=True)
    transaction_id_from_icici = models.CharField(max_length=191, blank=True, null=True)
    admin_reconciliation_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    payment_gateway_id = models.IntegerField()
    sub_transactions_type = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.CharField(max_length=191, blank=True, null=True)
    admin_user_id = models.IntegerField(blank=True, null=True)
    is_reconciled = models.IntegerField()
    reconciled_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reconciliation_icicis'


class ReconciliationKotaks(models.Model):
    reconciliation_kotaks_id = models.AutoField(primary_key=True)
    reference_no = models.CharField(max_length=191, blank=True, null=True)
    utr_number = models.CharField(max_length=191, blank=True, null=True)
    transaction_date = models.DateField()
    date_from_kotak = models.DateTimeField()
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=191, blank=True, null=True)
    transaction_mode = models.CharField(max_length=191)
    admin_reconciliation_id = models.IntegerField()
    description = models.CharField(max_length=191)
    is_tpsl = models.IntegerField()
    is_stripe = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_atom = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reconciliation_kotaks'


class ReconciliationStripeSettlements(models.Model):
    reconciliation_stripe_settlements_id = models.AutoField(primary_key=True)
    balance_transaction_id = models.CharField(unique=True, max_length=191)
    pg_transactions_id = models.IntegerField()
    description = models.CharField(max_length=255)
    settlement_date_utc = models.DateTimeField()
    settlement_date_ist = models.DateTimeField()
    currency = models.CharField(max_length=255)
    gross_amount = models.DecimalField(max_digits=10, decimal_places=2)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    net_amount = models.DecimalField(max_digits=16, decimal_places=2)
    reporting_category = models.CharField(max_length=255)
    customer_facing_amount = models.DecimalField(max_digits=10, decimal_places=2)
    customer_facing_currency = models.CharField(max_length=255)
    source_id = models.CharField(max_length=255)
    charge_id = models.CharField(max_length=255)
    admin_reconciliation_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reconciliation_stripe_settlements'


class ReconciliationStripeTransactions(models.Model):
    reconciliation_stripe_transactions_id = models.AutoField(primary_key=True)
    balance_transaction_id = models.CharField(unique=True, max_length=191)
    description = models.CharField(max_length=255)
    transaction_date_utc = models.DateTimeField()
    transaction_date_ist = models.DateTimeField()
    currency = models.CharField(max_length=255)
    gross_amount = models.DecimalField(max_digits=16, decimal_places=2)
    fee = models.DecimalField(max_digits=16, decimal_places=2)
    net_amount = models.DecimalField(max_digits=16, decimal_places=2)
    reporting_category = models.CharField(max_length=255)
    customer_facing_amount = models.DecimalField(max_digits=10, decimal_places=2)
    customer_facing_currency = models.CharField(max_length=255)
    source_id = models.CharField(max_length=255)
    charge_id = models.CharField(max_length=255)
    admin_reconciliation_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reconciliation_stripe_transactions'


class ReconciliationTpslSettlements(models.Model):
    reconciliation_tpsl_settlements_id = models.AutoField(primary_key=True)
    sm_transaction_id = models.CharField(max_length=255)
    tpsl_transaction_id = models.CharField(unique=True, max_length=191)
    pg_transactions_id = models.IntegerField()
    settlement_date = models.DateTimeField()
    gross_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tpsl_charges = models.DecimalField(max_digits=10, decimal_places=6)
    net_amount = models.DecimalField(max_digits=16, decimal_places=2)
    bank_name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    payment_remarks = models.CharField(max_length=255)
    refund_date = models.DateTimeField(blank=True, null=True)
    refund_remarks = models.CharField(max_length=255)
    refund_status = models.CharField(max_length=255)
    refund_amount = models.DecimalField(max_digits=10, decimal_places=6)
    is_refunded = models.IntegerField()
    admin_reconciliation_id = models.IntegerField()
    transaction_date = models.DateTimeField()
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reconciliation_tpsl_settlements'


class ReconciliationTpslTransactions(models.Model):
    reconciliation_tpsl_transactions_id = models.AutoField(primary_key=True)
    sm_transaction_id = models.CharField(max_length=255)
    tpsl_transaction_id = models.CharField(max_length=255)
    transaction_date = models.DateTimeField()
    gross_amount = models.DecimalField(max_digits=16, decimal_places=2)
    tpsl_charges = models.DecimalField(max_digits=10, decimal_places=6)
    net_amount = models.DecimalField(max_digits=16, decimal_places=2)
    bank_name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    payment_remarks = models.CharField(max_length=255)
    refund_date = models.DateTimeField(blank=True, null=True)
    refund_status = models.CharField(max_length=255)
    refund_amount = models.DecimalField(max_digits=16, decimal_places=2)
    admin_reconciliation_id = models.IntegerField()
    payment_date = models.DateTimeField()
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reconciliation_tpsl_transactions'


class ReconciliationYesBanks(models.Model):
    reconciliation_yes_banks_id = models.AutoField(primary_key=True)
    reference_no = models.CharField(unique=True, max_length=191)
    utr_number = models.CharField(max_length=191, blank=True, null=True)
    transaction_date = models.DateField()
    date_from_yes_bank = models.DateTimeField()
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=191, blank=True, null=True)
    transaction_mode = models.CharField(max_length=191)
    admin_reconciliation_id = models.IntegerField()
    is_stripe = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reconciliation_yes_banks'


class Referees(models.Model):
    referees_id = models.AutoField(primary_key=True)
    referrers_id = models.IntegerField()
    referees_name = models.CharField(max_length=191)
    referees_email = models.CharField(max_length=191)
    referees_mobile = models.CharField(max_length=191)
    referees_android_id = models.CharField(max_length=191)
    referees_ios_ifa = models.CharField(max_length=191)
    referees_coupon = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referees'


class Referrers(models.Model):
    referrers_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    referrers_name = models.CharField(max_length=191)
    referrers_email = models.CharField(max_length=191)
    referrers_mobile = models.CharField(max_length=191)
    referrers_invites = models.IntegerField()
    referrers_clicks = models.IntegerField()
    referrers_converts = models.IntegerField()
    referrers_coupon = models.CharField(max_length=191)
    referrers_device = models.CharField(max_length=191)
    campaign_id = models.IntegerField()
    brand_id = models.IntegerField()
    goal_complete = models.IntegerField()
    order_id = models.CharField(max_length=191)
    purchase_value = models.IntegerField()
    reward_types_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referrers'


class RegistrationProofTypes(models.Model):
    registration_proof_types_id = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=191)
    name = models.CharField(max_length=191)
    type = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registration_proof_types'


class ReimbursementStatuses(models.Model):
    reimbursement_statuses_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=100)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reimbursement_statuses'


class Reimbursements(models.Model):
    reimbursements_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    reimbursement_statuses_id = models.IntegerField()
    team_member_details_id = models.IntegerField()
    employee_name = models.CharField(max_length=200)
    source_type = models.CharField(max_length=200, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    total_reimbursable_amount = models.DecimalField(max_digits=14, decimal_places=2)
    total_reimbursed_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    transaction_ref_no = models.CharField(max_length=100, blank=True, null=True)
    external_fund_transfers_id = models.IntegerField(blank=True, null=True)
    transaction_statuses_id = models.IntegerField(blank=True, null=True)
    transaction_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reimbursements'


class Reminders(models.Model):
    user_id = models.PositiveIntegerField()
    code = models.CharField(max_length=191, blank=True, null=True)
    completed = models.IntegerField(blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reminders'


class ReportSequenceIds(models.Model):
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    report_sequence_id = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_sequence_ids'


class ReportStatuses(models.Model):
    report_statuses_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_statuses'


class Reports(models.Model):
    reports_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    approver_users_id = models.IntegerField()
    team_member_details_id = models.IntegerField(blank=True, null=True)
    report_seq_id = models.CharField(max_length=200)
    report_name = models.CharField(max_length=200)
    total_value = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    total_reimbursable_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_reimbursed_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    is_reimbursement_complete = models.IntegerField()
    transaction_ref_no = models.CharField(max_length=200, blank=True, null=True)
    report_statuses_id = models.IntegerField()
    processed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reports'


class RequestStatuses(models.Model):
    request_statuses_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=40)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'request_statuses'


class Requests(models.Model):
    requests_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    source_type = models.CharField(max_length=200, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    request_statuses_id = models.IntegerField()
    team_member_details_id = models.IntegerField()
    requested_on = models.DateTimeField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    request_type = models.CharField(max_length=191, blank=True, null=True)
    request_description = models.CharField(max_length=191, blank=True, null=True)
    card_type = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requests'


class ResellerLicenseTransactions(models.Model):
    reseller_license_transactions_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    transaction_ref_id = models.CharField(max_length=50)
    enterprise_pg_transaction_statuses_id = models.IntegerField()
    no_of_licenses = models.IntegerField()
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    actual_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    discount_perc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    transaction_date = models.DateField()
    invoices_id = models.IntegerField(blank=True, null=True)
    invoice_pdf_url = models.TextField(blank=True, null=True)
    payment_token = models.CharField(max_length=150, blank=True, null=True)
    pg_payment_status = models.CharField(max_length=25, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    subscription_packages_id = models.IntegerField(blank=True, null=True)
    licence_validity_days = models.IntegerField(blank=True, null=True)
    is_offer_applied = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reseller_license_transactions'


class ResellerLicenses(models.Model):
    reseller_licenses_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    type = models.CharField(max_length=1)
    license_number = models.CharField(max_length=25, blank=True, null=True)
    assigned_by_users_id = models.IntegerField(blank=True, null=True)
    assigned_on = models.DateField(blank=True, null=True)
    is_shared = models.IntegerField()
    is_used = models.IntegerField()
    is_delink_enabled = models.IntegerField()
    used_by_users_id = models.IntegerField(blank=True, null=True)
    used_by_name = models.CharField(max_length=250, blank=True, null=True)
    used_on = models.DateField(blank=True, null=True)
    is_valid = models.IntegerField()
    user_paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    reseller_paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    commission_rate = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    mpartner_users_id = models.IntegerField(blank=True, null=True)
    mpartner_commission_rate = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    license_expiry_date = models.DateField(blank=True, null=True)
    subscription_packages_id = models.IntegerField(blank=True, null=True)
    reseller_license_transactions_id = models.IntegerField(blank=True, null=True)
    is_settlement_done = models.IntegerField()
    user_subscriptions_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_expiry_enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reseller_licenses'


class ResellerLogo(models.Model):
    reseller_logo_id = models.AutoField(primary_key=True)
    user_reseller_profile_id = models.IntegerField()
    title = models.CharField(max_length=150, blank=True, null=True)
    file_name = models.CharField(max_length=175, blank=True, null=True)
    path = models.CharField(max_length=175, blank=True, null=True)
    file_size = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    verified_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reseller_logo'


class ResellerLogoOld(models.Model):
    reseller_logo_id = models.IntegerField(primary_key=True)
    user_reseller_profile_id = models.IntegerField()
    title = models.CharField(max_length=150)
    path = models.CharField(max_length=250)
    file_size = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    verified_by = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    file_name = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'reseller_logo_old'


class ResellerPartnerPurchaseInvoices(models.Model):
    reseller_partner_purchase_invoices_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField(blank=True, null=True)
    invoices_id = models.IntegerField(blank=True, null=True)
    invoices_files_id = models.IntegerField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    company_gstin = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reseller_partner_purchase_invoices'


class ResellerSettings(models.Model):
    reseller_settings_id = models.AutoField(primary_key=True)
    user_reseller_profile_id = models.IntegerField()
    commission_perc = models.FloatField()
    is_active_commission_perc = models.IntegerField()
    account_number = models.CharField(max_length=35, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    ifsc_code = models.CharField(max_length=25, blank=True, null=True)
    branch_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    max_credit_limit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reseller_settings'


class ResellerUserRoleHistories(models.Model):
    reseller_user_role_histories_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    open_roles_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reseller_user_role_histories'


class RetryOpenpayPayouts(models.Model):
    retry_openpay_payouts_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    old_internal_transaction_ref_id = models.CharField(max_length=199, blank=True, null=True)
    new_internal_transaction_ref_id = models.CharField(max_length=199, blank=True, null=True)
    source_type = models.CharField(max_length=199, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    retry_initiated_on = models.DateTimeField()
    bank_transaction_statuses_id = models.IntegerField()
    admin_users_id = models.IntegerField()
    admin_remarks = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'retry_openpay_payouts'


class RewardStatues(models.Model):
    reward_statues_id = models.AutoField(primary_key=True)
    reward_status = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reward_statues'


class RewardTypes(models.Model):
    reward_types_id = models.AutoField(primary_key=True)
    reward_types_name = models.CharField(max_length=191)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reward_types'


class Rewards(models.Model):
    rewards_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    reward_types_id = models.IntegerField()
    reward_statues_id = models.IntegerField()
    referrers_id = models.IntegerField()
    referees_id = models.IntegerField()
    ref_no = models.CharField(max_length=191)
    remarks = models.CharField(max_length=191)
    transaction_date = models.DateTimeField()
    reward_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rewards'


class RiskBusinessCategories(models.Model):
    risk_business_categories_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'risk_business_categories'


class RiskChecks(models.Model):
    risk_checks_id = models.BigAutoField(primary_key=True)
    checks = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_disabled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'risk_checks'


class RiskDefaultPayoutSettings(models.Model):
    risk_default_payout_settings_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=191)
    txn_amt_daily_limit = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    txn_amt_monthly_limit = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    txn_amt_current_daily_limit = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    txn_amt_current_monthly_limit = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    txn_count_daily_limit = models.IntegerField(blank=True, null=True)
    txn_count_monthly_limit = models.IntegerField(blank=True, null=True)
    txn_count_current_daily_limit = models.IntegerField(blank=True, null=True)
    txn_count_current_monthly_limit = models.IntegerField(blank=True, null=True)
    per_txn_amt_limit = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    admin_users_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'risk_default_payout_settings'


class RiskIndustryCategories(models.Model):
    risk_industry_categories_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'risk_industry_categories'


class RiskIndustrySubCategories(models.Model):
    risk_industry_sub_categories_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=191)
    risk_industry_categories_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'risk_industry_sub_categories'


class RocRegisteredBusinessAddress(models.Model):
    roc_registered_business_address_id = models.AutoField(primary_key=True)
    mob_master_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField(unique=True)
    users_id = models.IntegerField()
    address_line = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=191, blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    district = models.CharField(max_length=191, blank=True, null=True)
    country = models.CharField(max_length=191, blank=True, null=True)
    pincode = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roc_registered_business_address'


class RoleUsers(models.Model):
    user_id = models.PositiveIntegerField(primary_key=True)
    role_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role_users'
        unique_together = (('user_id', 'role_id'),)


class Roles(models.Model):
    slug = models.CharField(unique=True, max_length=191)
    name = models.CharField(max_length=191)
    description = models.CharField(max_length=191)
    permissions = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class SacCodes(models.Model):
    sac_codes_id = models.AutoField(primary_key=True)
    sac_description = models.TextField(blank=True, null=True)
    sac_code = models.CharField(max_length=191, blank=True, null=True)
    sac_rate = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sac_codes'


class SaltAdminUserTypes(models.Model):
    salt_admin_user_types_id = models.AutoField(primary_key=True)
    salt_admin_user_type = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salt_admin_user_types'


class SaltAdminUsers(models.Model):
    salt_admin_users_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    mobile = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    pincode = models.CharField(max_length=191, blank=True, null=True)
    city = models.CharField(max_length=191, blank=True, null=True)
    state = models.CharField(max_length=191, blank=True, null=True)
    source_of_registration = models.CharField(max_length=191, blank=True, null=True)
    sub_account_ref_id = models.CharField(max_length=191)
    salt_admin_user_types_id = models.IntegerField()
    salt_store_types_id = models.IntegerField(blank=True, null=True)
    salt_ref_code = models.CharField(max_length=191, blank=True, null=True)
    payment_status = models.CharField(max_length=191, blank=True, null=True)
    payment_reference_id = models.CharField(max_length=191, blank=True, null=True)
    subscription_payment_statuses_id = models.IntegerField(blank=True, null=True)
    is_subscribed = models.IntegerField()
    user_subscriptions_id = models.IntegerField(blank=True, null=True)
    subscription_packages_id = models.IntegerField(blank=True, null=True)
    subscription_types_id = models.IntegerField(blank=True, null=True)
    subscription_start_date = models.DateTimeField(blank=True, null=True)
    subscription_end_date = models.DateTimeField(blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    payment_id = models.CharField(max_length=191, blank=True, null=True)
    payment_token = models.CharField(max_length=191, blank=True, null=True)
    lat = models.CharField(max_length=191, blank=True, null=True)
    long = models.CharField(max_length=191, blank=True, null=True)
    store_name = models.CharField(max_length=191, blank=True, null=True)
    display_store_name = models.CharField(max_length=191, blank=True, null=True)
    store_phone_number = models.CharField(max_length=191, blank=True, null=True)
    display_address = models.TextField(blank=True, null=True)
    yelo_merchant_id = models.CharField(max_length=191, blank=True, null=True)
    already_on_yelo = models.CharField(max_length=191)
    is_picked = models.IntegerField()
    is_manually_migrated = models.IntegerField(blank=True, null=True)
    is_store_active = models.CharField(max_length=191)
    is_store_blocked = models.CharField(max_length=191)
    source_type = models.CharField(max_length=191, blank=True, null=True)
    source_id = models.CharField(max_length=191, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salt_admin_users'


class SaltApiCalls(models.Model):
    salt_api_calls_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    api_provider = models.CharField(max_length=191, blank=True, null=True)
    api_name = models.CharField(max_length=191, blank=True, null=True)
    api_url_endpoint = models.CharField(max_length=191, blank=True, null=True)
    request_header = models.TextField(blank=True, null=True)
    request_body = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    response_status_code = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salt_api_calls'


class SaltFranchiseeDetails(models.Model):
    salt_franchisee_details_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    email = models.CharField(unique=True, max_length=191)
    mobile = models.CharField(unique=True, max_length=191)
    franchisee_code = models.CharField(unique=True, max_length=191)
    franchisee_type = models.CharField(max_length=191)
    location = models.CharField(max_length=191)
    pincode = models.TextField()
    pan_number = models.CharField(max_length=191)
    gst_number = models.CharField(max_length=191, blank=True, null=True)
    address = models.TextField()
    mob_business_types_id = models.IntegerField()
    sub_account_ref_id = models.CharField(max_length=191)
    marketplace_pg_sub_accounts_id = models.IntegerField()
    account_number = models.CharField(max_length=191)
    account_holder_name = models.CharField(max_length=191)
    ifsc_code = models.CharField(max_length=191)
    bank_name = models.CharField(max_length=191)
    branch_name = models.CharField(max_length=191)
    variable_commission_perc = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    tier_id = models.IntegerField()
    available_free_registrations = models.IntegerField()
    total_allowed_free_registration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'salt_franchisee_details'


class SaltMerchantFranchiseeMapping(models.Model):
    salt_merchant_franchisee_mapping_id = models.BigAutoField(primary_key=True)
    users_id = models.IntegerField()
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    salt_admin_users_id = models.IntegerField(unique=True)
    salt_franchisee_details_id = models.IntegerField()
    yelo_merchant_id = models.CharField(max_length=191)
    is_franchisee_delivery = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salt_merchant_franchisee_mapping'


class SaltPaymentHistories(models.Model):
    salt_payment_histories_id = models.AutoField(primary_key=True)
    salt_admin_users_id = models.IntegerField(blank=True, null=True)
    salt_ref_code = models.CharField(max_length=191, blank=True, null=True)
    user_subscriptions_id = models.IntegerField(blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    payment_id = models.CharField(max_length=191, blank=True, null=True)
    payment_token = models.CharField(max_length=191, blank=True, null=True)
    payment_reference_id = models.CharField(max_length=191, blank=True, null=True)
    subscription_start_date = models.DateTimeField(blank=True, null=True)
    subscription_end_date = models.DateTimeField(blank=True, null=True)
    subscription_payment_statuses_id = models.IntegerField(blank=True, null=True)
    subscription_packages_id = models.IntegerField(blank=True, null=True)
    invoices_id = models.IntegerField(blank=True, null=True)
    invoices_files_id = models.IntegerField(blank=True, null=True)
    invoice_sent_statuses_id = models.IntegerField()
    is_old_pdf_format = models.IntegerField(blank=True, null=True)
    invoice_sent_on = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_invoice_data_migrated_from_user_sub = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_migrated = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salt_payment_histories'


class SaltRefCodes(models.Model):
    salt_ref_code = models.CharField(unique=True, max_length=191)
    is_used = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'salt_ref_codes'


class SaltSettlements(models.Model):
    salt_settlements_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    yelo_merchant_id = models.IntegerField()
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    open_total_charges = models.DecimalField(max_digits=10, decimal_places=2)
    merchant_settlement_amount = models.DecimalField(max_digits=10, decimal_places=2)
    settlement_txn_id = models.CharField(max_length=190)
    open_pg_txn_id = models.CharField(max_length=191, blank=True, null=True)
    open_outward_settlement_statuses_id = models.IntegerField()
    merchant_outward_settlement_statuses_id = models.IntegerField()
    franchise_outward_settlement_statuses_id = models.IntegerField()
    franchise_settlement_date = models.DateTimeField()
    merchant_account_settlement_date = models.DateTimeField()
    internal_account_settlement_date = models.DateTimeField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salt_settlements'


class SaltStoreConfigurations(models.Model):
    salt_store_configurations_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    salt_admin_users_id = models.IntegerField(blank=True, null=True)
    store_name = models.CharField(max_length=191, blank=True, null=True)
    store_category = models.CharField(max_length=191, blank=True, null=True)
    is_all_day_available = models.IntegerField(blank=True, null=True)
    from_day_available = models.CharField(max_length=9, blank=True, null=True)
    to_day_available = models.CharField(max_length=9, blank=True, null=True)
    from_time_available = models.TimeField(blank=True, null=True)
    to_time_available = models.TimeField(blank=True, null=True)
    minimum_order_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    minimum_take_away_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salt_store_configurations'


class SaltStoreTypes(models.Model):
    salt_store_types_id = models.IntegerField(primary_key=True)
    salt_store_type = models.CharField(max_length=191, blank=True, null=True)
    yelo_store_types_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salt_store_types'


class SaltTierFreeRegistrationHistories(models.Model):
    salt_tier_free_registration_histories_id = models.BigAutoField(primary_key=True)
    salt_franchisee_details_id = models.IntegerField(blank=True, null=True)
    free_registration_count = models.IntegerField(blank=True, null=True)
    total_allowed_free_registration = models.IntegerField(blank=True, null=True)
    free_registration_balance = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salt_tier_free_registration_histories'


class SaltTierSettings(models.Model):
    salt_tier_settings_id = models.BigAutoField(primary_key=True)
    tier_id = models.IntegerField()
    slug = models.CharField(max_length=191)
    tier_name = models.CharField(max_length=191)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    free_registration_count = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salt_tier_settings'


class SaltTierSettingsHistories(models.Model):
    salt_tier_settings_histories_id = models.BigAutoField(primary_key=True)
    tier_id = models.IntegerField()
    current_amount = models.DecimalField(max_digits=8, decimal_places=2)
    new_amount = models.DecimalField(max_digits=8, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salt_tier_settings_histories'


class SameDaySettlementStatus(models.Model):
    same_day_settlement_status_id = models.AutoField(primary_key=True)
    same_day_settlement_settlement_status = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'same_day_settlement_status'


class SbmAuthTransactions(models.Model):
    transaction_ref_no = models.CharField(max_length=100, blank=True, null=True)
    retrieval_ref_no = models.CharField(max_length=20, blank=True, null=True)
    entity_id = models.CharField(max_length=100, blank=True, null=True)
    raw_request = models.TextField(blank=True, null=True)
    decrypted_request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status_code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sbm_auth_transactions'


class SbmAuthTransactionsDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    users_id = models.IntegerField()
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    card_details_id = models.IntegerField()
    transaction_ref_no = models.CharField(max_length=100)
    original_rrn = models.CharField(max_length=100)
    kit_number = models.IntegerField()
    entity_id = models.IntegerField()
    amount = models.DecimalField(max_digits=14, decimal_places=4)
    auth_type = models.CharField(max_length=50, blank=True, null=True)
    txn_currency = models.CharField(max_length=20, blank=True, null=True)
    international = models.CharField(max_length=3, blank=True, null=True)
    merchantid = models.CharField(db_column='merchantID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    merchantname = models.CharField(db_column='merchantName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    transaction_type = models.CharField(max_length=20, blank=True, null=True)
    markup_applied = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)
    original_txn_date = models.CharField(max_length=100, blank=True, null=True)
    crdr = models.CharField(max_length=10, blank=True, null=True)
    stan = models.CharField(max_length=10, blank=True, null=True)
    mcc = models.CharField(max_length=10, blank=True, null=True)
    txnid = models.CharField(db_column='txnId', max_length=25, blank=True, null=True)  # Field name made lowercase.
    conversionrate = models.DecimalField(db_column='conversionRate', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    maskedcardnumber = models.CharField(db_column='maskedCardNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sbm_auth_transactions_id = models.IntegerField()
    response = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sbm_auth_transactions_details'


class SbmCallbackLogs(models.Model):
    sbm_callback_logs_id = models.AutoField(primary_key=True)
    entity_id = models.CharField(max_length=200, blank=True, null=True)
    data = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sbm_callback_logs'


class SbmCardKycDetails(models.Model):
    sbm_card_kyc_details_id = models.AutoField(primary_key=True)
    card_details_id = models.PositiveIntegerField()
    users_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    team_member_details_id = models.IntegerField(blank=True, null=True)
    pan_number = models.CharField(max_length=255, blank=True, null=True)
    pan_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=191, blank=True, null=True)
    middle_name = models.CharField(max_length=191, blank=True, null=True)
    last_name = models.CharField(max_length=191, blank=True, null=True)
    okyc_passcode = models.TextField()
    okyc_file_id = models.PositiveIntegerField()
    retries = models.IntegerField()
    sbm_kyc_verified = models.IntegerField()
    permanent_address_line_1 = models.CharField(max_length=255, blank=True, null=True)
    permanent_address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    permanent_address_line_3 = models.CharField(max_length=255, blank=True, null=True)
    permanent_address_city = models.CharField(max_length=255, blank=True, null=True)
    permanent_address_state = models.CharField(max_length=255, blank=True, null=True)
    permanent_address_country = models.CharField(max_length=255, blank=True, null=True)
    permanent_address_pincode = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sbm_card_kyc_details'


class SbmCardPreferences(models.Model):
    id = models.BigAutoField(primary_key=True)
    card_details_id = models.PositiveBigIntegerField()
    service = models.CharField(max_length=13)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sbm_card_preferences'


class SbmCurrentAccounts(models.Model):
    sbm_current_accounts_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    customer_id = models.CharField(max_length=200, blank=True, null=True)
    company_customer_id = models.CharField(max_length=200, blank=True, null=True)
    bank_account_number = models.CharField(max_length=200, blank=True, null=True)
    bank_connection_statuses_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sbm_current_accounts'


class SbmCustomerAddressTypes(models.Model):
    sbm_customer_address_types_id = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=191)
    name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sbm_customer_address_types'


class SbmCustomerAddresses(models.Model):
    sbm_customer_addresses_id = models.AutoField(primary_key=True)
    sbm_customer_details_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    accounts_id = models.PositiveIntegerField()
    companies_id = models.IntegerField(blank=True, null=True)
    sbm_customer_address_types_id = models.IntegerField()
    address_line_1 = models.CharField(max_length=191, blank=True, null=True)
    address_line_2 = models.CharField(max_length=191, blank=True, null=True)
    address_line_3 = models.CharField(max_length=191, blank=True, null=True)
    landmark = models.CharField(max_length=191, blank=True, null=True)
    city = models.CharField(max_length=191, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=191, blank=True, null=True)
    country = models.CharField(max_length=191, blank=True, null=True)
    address_category = models.CharField(max_length=191, blank=True, null=True)
    residence_type = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sbm_customer_addresses'


class SbmCustomerDetails(models.Model):
    sbm_customer_details_id = models.AutoField(primary_key=True)
    users_id = models.PositiveIntegerField()
    accounts_id = models.PositiveIntegerField()
    companies_id = models.IntegerField(blank=True, null=True)
    tnc = models.CharField(max_length=191, blank=True, null=True)
    bank_details = models.CharField(max_length=191, blank=True, null=True)
    first_name = models.CharField(max_length=191, blank=True, null=True)
    middle_name = models.CharField(max_length=191, blank=True, null=True)
    last_name = models.CharField(max_length=191, blank=True, null=True)
    salutation = models.CharField(max_length=10, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    is_senior_citizen = models.CharField(max_length=10, blank=True, null=True)
    country_of_birth = models.CharField(max_length=191, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    aadhaar_number = models.CharField(max_length=191, blank=True, null=True)
    marital_status = models.CharField(max_length=191, blank=True, null=True)
    account_type = models.CharField(max_length=50, blank=True, null=True)
    cust_type = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=191, blank=True, null=True)
    region = models.CharField(max_length=191, blank=True, null=True)
    pin_code = models.CharField(max_length=191, blank=True, null=True)
    mother_maiden_name = models.CharField(max_length=191, blank=True, null=True)
    qualification = models.CharField(max_length=191, blank=True, null=True)
    customer_photo_id = models.IntegerField(blank=True, null=True)
    customer_signature_id = models.IntegerField(blank=True, null=True)
    occupation = models.CharField(max_length=191, blank=True, null=True)
    constitution_code = models.CharField(max_length=191, blank=True, null=True)
    sector = models.CharField(max_length=191, blank=True, null=True)
    sub_sector = models.CharField(max_length=191, blank=True, null=True)
    segmentation_class = models.CharField(max_length=191, blank=True, null=True)
    tax = models.CharField(max_length=191, blank=True, null=True)
    nature_of_income = models.CharField(max_length=191, blank=True, null=True)
    employment = models.CharField(max_length=191, blank=True, null=True)
    employer = models.CharField(max_length=191, blank=True, null=True)
    type_of_company = models.CharField(max_length=191, blank=True, null=True)
    nominee_name = models.CharField(max_length=191, blank=True, null=True)
    nominee_email_address = models.CharField(max_length=191, blank=True, null=True)
    nominee_phone_number = models.CharField(max_length=191, blank=True, null=True)
    nominee_dob = models.DateField(blank=True, null=True)
    nominee_is_minor = models.CharField(max_length=191, blank=True, null=True)
    nominee_relationship_with_depositor = models.CharField(max_length=191, blank=True, null=True)
    guardian_name = models.CharField(max_length=191, blank=True, null=True)
    guardian_dob = models.DateField(blank=True, null=True)
    guardian_phone = models.CharField(max_length=191, blank=True, null=True)
    guardian_email = models.CharField(max_length=191, blank=True, null=True)
    business_name = models.CharField(max_length=191, blank=True, null=True)
    business_nature = models.CharField(max_length=191, blank=True, null=True)
    industry_type = models.CharField(max_length=191, blank=True, null=True)
    business_category = models.CharField(max_length=191, blank=True, null=True)
    registration_number = models.CharField(max_length=191, blank=True, null=True)
    validity = models.DateField(blank=True, null=True)
    incorporation_date = models.DateField(blank=True, null=True)
    years_into_business = models.PositiveIntegerField(blank=True, null=True)
    annual_turnover = models.CharField(max_length=191, blank=True, null=True)
    listed = models.CharField(max_length=191, blank=True, null=True)
    listing_code = models.CharField(max_length=191, blank=True, null=True)
    channel_access_request = models.CharField(max_length=191, blank=True, null=True)
    internet_banking = models.CharField(max_length=191, blank=True, null=True)
    debit_card = models.CharField(max_length=191, blank=True, null=True)
    account_statement = models.CharField(max_length=191, blank=True, null=True)
    fatca_section_a = models.TextField(blank=True, null=True)
    fatca_section_b = models.TextField(blank=True, null=True)
    customer_aof = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    sub_segment = models.CharField(max_length=191, blank=True, null=True)
    form_state = models.CharField(max_length=50, blank=True, null=True)
    sqs_processed = models.IntegerField()
    admin_users_id = models.IntegerField(blank=True, null=True)
    admin_processed_at = models.DateTimeField(blank=True, null=True)
    connected_lead_status_id = models.IntegerField(blank=True, null=True)
    admin_sbm_verification_status_id = models.IntegerField()
    reason = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sbm_customer_details'


class SbmCustomerDocuments(models.Model):
    sbm_customer_documents_id = models.AutoField(primary_key=True)
    sbm_customer_details_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    accounts_id = models.PositiveIntegerField()
    companies_id = models.IntegerField(blank=True, null=True)
    document_type = models.CharField(max_length=191)
    doc_code = models.CharField(max_length=191, blank=True, null=True)
    name_on_document = models.CharField(max_length=191, blank=True, null=True)
    type_code = models.CharField(max_length=191, blank=True, null=True)
    place_of_issue = models.CharField(max_length=191, blank=True, null=True)
    document_number = models.CharField(max_length=191, blank=True, null=True)
    id_issued_organisation = models.CharField(max_length=191, blank=True, null=True)
    preferred_unique_id = models.CharField(max_length=191, blank=True, null=True)
    document_image_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    issue_date = models.CharField(max_length=191, blank=True, null=True)
    document_type_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sbm_customer_documents'


class SbmCustomerExtraDetails(models.Model):
    sbm_customer_extra_details_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    sbm_savings_accounts_id = models.IntegerField()
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    sub_class_segment = models.CharField(max_length=200, blank=True, null=True)
    class_segment = models.CharField(max_length=200, blank=True, null=True)
    sector = models.CharField(max_length=200, blank=True, null=True)
    sub_sector = models.CharField(max_length=200, blank=True, null=True)
    city_code = models.CharField(max_length=200, blank=True, null=True)
    state_code = models.CharField(max_length=200, blank=True, null=True)
    region = models.CharField(max_length=200, blank=True, null=True)
    staff_employee_id = models.CharField(max_length=200, blank=True, null=True)
    staff_flag = models.CharField(max_length=200, blank=True, null=True)
    name_of_the_employer = models.CharField(max_length=200, blank=True, null=True)
    nature_of_income = models.CharField(max_length=200, blank=True, null=True)
    other_limits = models.CharField(max_length=200, blank=True, null=True)
    out_standing_mortgage = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sbm_customer_extra_details'


class SbmFederals(models.Model):
    sbm_federals_id = models.AutoField(primary_key=True)
    kit_no = models.CharField(max_length=20)
    card_number = models.CharField(max_length=20)
    expiry_date = models.DateTimeField(blank=True, null=True)
    is_assigned = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    card_type = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sbm_federals'


class SbmFundTransfers(models.Model):
    sbm_fund_transfers_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    account_number = models.CharField(max_length=191, blank=True, null=True)
    transaction_reference_number = models.CharField(max_length=191, blank=True, null=True)
    transaction_time_stamp = models.CharField(max_length=255, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    is_otp_verification_successful = models.IntegerField(blank=True, null=True)
    external_fund_transactions_id = models.CharField(max_length=191, blank=True, null=True)
    external_fund_transfers_id = models.CharField(max_length=191, blank=True, null=True)
    bank_unique_reference_number = models.CharField(max_length=191, blank=True, null=True)
    bank_transaction_status_id = models.CharField(max_length=191, blank=True, null=True)
    payment_reference_number = models.CharField(max_length=191, blank=True, null=True)
    bank_transfer_type = models.CharField(max_length=191, blank=True, null=True)
    utr = models.CharField(max_length=191, blank=True, null=True)
    bank_error_code = models.CharField(max_length=191, blank=True, null=True)
    bank_error_text = models.CharField(max_length=191, blank=True, null=True)
    bank_currency_code = models.CharField(max_length=191, blank=True, null=True)
    bank_reference_number = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sbm_fund_transfers'


class SbmM2PCreditPending(models.Model):
    id = models.BigAutoField(primary_key=True)
    transaction_ref_no = models.CharField(max_length=100)
    original_rrn = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=4)
    original_txn_date = models.CharField(max_length=100, blank=True, null=True)
    merchantid = models.CharField(db_column='merchantID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    merchantname = models.CharField(db_column='merchantName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=10, blank=True, null=True)
    kit_number = models.IntegerField()
    entity_id = models.IntegerField()
    processed_state = models.IntegerField()
    processed_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sbm_m2p_credit_pending'


class SbmPrepaidCards(models.Model):
    sbm_prepaid_cards_id = models.AutoField(primary_key=True)
    kit_no = models.CharField(max_length=20)
    card_number = models.CharField(max_length=20)
    expiry_date = models.DateTimeField()
    is_assigned = models.IntegerField()
    card_type = models.CharField(max_length=8, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sbm_prepaid_cards'


class SbmPrepaidCardsCopy(models.Model):
    sbm_federals_id = models.AutoField(primary_key=True)
    kit_no = models.CharField(max_length=20)
    card_number = models.CharField(max_length=20)
    expiry_date = models.DateTimeField(blank=True, null=True)
    is_assigned = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    card_type = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sbm_prepaid_cards_copy'


class SbmPrepaids(models.Model):
    sbm_prepaids_id = models.AutoField(primary_key=True)
    kit_no = models.CharField(max_length=20)
    card_number = models.CharField(max_length=20)
    expiry_date = models.DateTimeField(blank=True, null=True)
    is_assigned = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()
    card_type = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sbm_prepaids'


class SellerTypes(models.Model):
    seller_types_id = models.AutoField(primary_key=True)
    seller_type = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    subscription_discount_type = models.CharField(max_length=5)
    subscription_discount_value = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seller_types'


class Sessions(models.Model):
    id = models.CharField(unique=True, max_length=191)
    user_id = models.PositiveIntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    payload = models.TextField()
    last_activity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sessions'


class SetBalanceFailedJobs(models.Model):
    set_balance_failed_jobs_id = models.AutoField(primary_key=True)
    exception_message = models.CharField(max_length=250)
    exception_object = models.JSONField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'set_balance_failed_jobs'


class SetBalanceJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    source = models.CharField(max_length=255)
    source_id = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    type = models.CharField(max_length=2)
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'set_balance_jobs'
        unique_together = (('source', 'source_id'),)


class SettlementLiveAccountBalanceHistories(models.Model):
    settlement_live_account_balance_histories_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    partner_banks_id = models.IntegerField()
    current_balance = models.DecimalField(max_digits=12, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=60)
    ref_id = models.CharField(max_length=199)
    remarks = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settlement_live_account_balance_histories'


class SettlementLiveAccountBalances(models.Model):
    settlement_live_account_balances_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    partner_banks_id = models.IntegerField()
    current_balance = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settlement_live_account_balances'


class SettlementModes(models.Model):
    settlement_modes_id = models.AutoField(primary_key=True)
    settlement_mode = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settlement_modes'


class SettlementStatuses(models.Model):
    settlement_statuses_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settlement_statuses'


class ShareSmsEmailHistory(models.Model):
    share_sms_email_history_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    share_type = models.CharField(max_length=5, blank=True, null=True)
    value_type = models.CharField(max_length=21, blank=True, null=True)
    shared_to = models.CharField(max_length=175, blank=True, null=True)
    is_sms_sent = models.IntegerField()
    is_email_sent = models.IntegerField()
    reseller_licenses_id = models.IntegerField(blank=True, null=True)
    is_share_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'share_sms_email_history'


class ShareSmsEmailHistoryOld(models.Model):
    share_sms_email_history_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField(blank=True, null=True)
    share_type = models.CharField(max_length=5, blank=True, null=True)
    value_type = models.CharField(max_length=21, blank=True, null=True)
    shared_to = models.CharField(max_length=175, blank=True, null=True)
    is_sms_sent = models.IntegerField()
    is_email_sent = models.IntegerField()
    reseller_licenses_id = models.IntegerField(blank=True, null=True)
    is_share_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'share_sms_email_history_old'


class ShippingStatuses(models.Model):
    shipping_statuses_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=100)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipping_statuses'


class ShortUrls(models.Model):
    short_urls_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    short_url = models.CharField(unique=True, max_length=199, blank=True, null=True)
    long_url = models.CharField(max_length=199, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    source_type = models.CharField(max_length=199, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'short_urls'


class SmartChequeBulkIntermediaries(models.Model):
    smart_cheque_bulk_intermediaries_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    batch_id = models.CharField(max_length=100)
    files_bulk_id = models.IntegerField()
    open_bank_accounts_id = models.IntegerField()
    partner_banks_id = models.IntegerField()
    link_types_id = models.IntegerField()
    smart_cheque_transfers_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    external_ref_id = models.CharField(max_length=200)
    description = models.TextField()
    read_status = models.CharField(max_length=200, blank=True, null=True)
    is_complete = models.IntegerField()
    reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smart_cheque_bulk_intermediaries'


class SmartChequeStatusHistories(models.Model):
    smart_cheque_status_histories_id = models.AutoField(primary_key=True)
    smart_cheque_id = models.IntegerField(blank=True, null=True)
    smart_cheque_statuses_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smart_cheque_status_histories'


class SmartChequeStatuses(models.Model):
    smart_cheque_statuses_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=191)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smart_cheque_statuses'


class SmartChequeTransfers(models.Model):
    smart_cheque_transfers_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    contacts_id = models.IntegerField(blank=True, null=True)
    batch_id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    mobile_number = models.CharField(max_length=30, blank=True, null=True)
    email_id = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    hash = models.CharField(max_length=300, blank=True, null=True)
    l3_categories_id = models.IntegerField(blank=True, null=True)
    external_ref_id = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    bene_account_number = models.CharField(max_length=191, blank=True, null=True)
    bene_ifsc_code = models.CharField(max_length=191, blank=True, null=True)
    bene_bank_branch = models.CharField(max_length=191, blank=True, null=True)
    bene_bank_name = models.CharField(max_length=191, blank=True, null=True)
    open_bank_accounts_id = models.IntegerField(blank=True, null=True)
    is_maker_checker_enabled = models.IntegerField(blank=True, null=True)
    smart_cheque_statuses_id = models.IntegerField()
    payment_internal_transaction_ref_id = models.CharField(max_length=191, blank=True, null=True)
    payment_bank_transaction_statuses_id = models.IntegerField(blank=True, null=True)
    payment_bank_response_message = models.TextField(blank=True, null=True)
    payment_transaction_date = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    withdraw_bank_response_message = models.TextField(blank=True, null=True)
    withdraw_bank_accounts_id = models.IntegerField(blank=True, null=True)
    withdraw_internal_transaction_ref_id = models.CharField(max_length=191, blank=True, null=True)
    withdraw_bank_transaction_statues_id = models.CharField(max_length=191, blank=True, null=True)
    withdraw_transaction_date = models.DateTimeField(blank=True, null=True)
    is_communication_required = models.IntegerField(blank=True, null=True)
    creation_types_id = models.IntegerField()
    link_identifier = models.CharField(max_length=191)
    link_expiry_date = models.DateTimeField()
    smart_cheque_bulk_intermediaries_id = models.IntegerField(blank=True, null=True)
    sc_merchant_ref_id = models.CharField(max_length=200)
    is_sandbox = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    l2_categories_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smart_cheque_transfers'


class SmartLoanUsers(models.Model):
    smart_loan_users_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    second_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    mob_business_types_id = models.IntegerField(blank=True, null=True)
    mob_business_categories_id = models.IntegerField(blank=True, null=True)
    adhaar_number = models.CharField(max_length=12, blank=True, null=True)
    pan_number = models.CharField(max_length=10, blank=True, null=True)
    gstin_number = models.CharField(max_length=20, blank=True, null=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    address_line = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    company_turnover = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    date_of_incorporation = models.DateField(blank=True, null=True)
    loan_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    is_processed = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smart_loan_users'


class SmartloanPayments(models.Model):
    smartloan_payments_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=191)
    email_id = models.CharField(max_length=191)
    contact_number = models.CharField(max_length=25)
    amount = models.FloatField()
    payment_status = models.CharField(max_length=20)
    merchant_redirect_url = models.TextField()
    payment_token_id = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smartloan_payments'


class SmartloanSubOrderDetails(models.Model):
    smartloan_sub_order_details_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    order_id = models.CharField(max_length=191)
    sub_order_id = models.CharField(max_length=191)
    amount = models.FloatField()
    payment_status = models.CharField(max_length=20)
    payment_token_id = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smartloan_sub_order_details'


class SmsServiceProviders(models.Model):
    sms_service_providers_id = models.AutoField(primary_key=True)
    provider_name = models.CharField(max_length=191)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_service_providers'


class SmsTemplates(models.Model):
    sms_templates_id = models.AutoField(primary_key=True)
    template_id = models.IntegerField()
    sms_template = models.TextField()
    description = models.TextField()
    template_code = models.CharField(unique=True, max_length=191, blank=True, null=True)
    msg_91_flow_id = models.CharField(max_length=191, blank=True, null=True)
    platform = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    sms_template_node = models.TextField()
    dlt_template_id = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_templates'


class SocialLoginProviders(models.Model):
    social_login_providers_id = models.AutoField(primary_key=True)
    provider_name = models.CharField(max_length=191)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'social_login_providers'


class SplitTransactions(models.Model):
    split_transactions_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    parent_open_banking_nodal_statements_id = models.IntegerField()
    l1_categories_id = models.IntegerField()
    l2_categories_id = models.IntegerField()
    l3_categories_id = models.IntegerField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'split_transactions'


class StatesList(models.Model):
    states_list_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=150)
    slug = models.CharField(max_length=50, blank=True, null=True)
    state_code = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    yes_bank_vpa_state_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'states_list'


class Stories(models.Model):
    stories_id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=200)
    is_active = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    deep_link = models.CharField(max_length=199, blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)
    os = models.CharField(max_length=20, blank=True, null=True)
    button_value = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stories'


class StoryHistories(models.Model):
    story_histories_id = models.AutoField(primary_key=True)
    stories_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'story_histories'


class StripeCharges(models.Model):
    stripe_transactions_id = models.AutoField(primary_key=True)
    pg_transactions_id = models.IntegerField(blank=True, null=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    status_message = models.CharField(max_length=191, blank=True, null=True)
    amount = models.CharField(max_length=191, blank=True, null=True)
    stripe_source_id = models.CharField(max_length=191, blank=True, null=True)
    type = models.CharField(max_length=191, blank=True, null=True)
    client_secret = models.CharField(max_length=191, blank=True, null=True)
    currency = models.CharField(max_length=191, blank=True, null=True)
    flow = models.CharField(max_length=191, blank=True, null=True)
    live_mode = models.CharField(max_length=191, blank=True, null=True)
    usage = models.CharField(max_length=191, blank=True, null=True)
    redirect_failure_reason = models.CharField(max_length=191, blank=True, null=True)
    redirect_return_url = models.CharField(max_length=191, blank=True, null=True)
    redirect_status = models.CharField(max_length=191, blank=True, null=True)
    redirect_url = models.CharField(max_length=191, blank=True, null=True)
    three_d_secure_card = models.CharField(max_length=191, blank=True, null=True)
    three_d_secure_address_zip_check = models.CharField(max_length=191, blank=True, null=True)
    three_d_secure_brand = models.CharField(max_length=191, blank=True, null=True)
    three_d_secure_card_automatically_updated = models.CharField(max_length=191, blank=True, null=True)
    three_d_secure_country = models.CharField(max_length=191, blank=True, null=True)
    three_d_secure_cvc_check = models.CharField(max_length=191, blank=True, null=True)
    three_d_secure_exp_month = models.CharField(max_length=191, blank=True, null=True)
    three_d_secure_exp_year = models.CharField(max_length=191, blank=True, null=True)
    three_d_secure_fingerprint = models.CharField(max_length=191, blank=True, null=True)
    three_d_secure_funding = models.CharField(max_length=191, blank=True, null=True)
    three_d_secure_last4 = models.CharField(max_length=191, blank=True, null=True)
    is_three_d_secure_required = models.CharField(max_length=191, blank=True, null=True)
    three_d_secure_authenticated = models.CharField(max_length=191, blank=True, null=True)
    three_d_secure_customer = models.CharField(max_length=191, blank=True, null=True)
    three_d_secure_name = models.CharField(max_length=191, blank=True, null=True)
    three_d_secure_address_line1_check = models.CharField(max_length=191, blank=True, null=True)
    three_d_secure_tokenization_method = models.CharField(max_length=191, blank=True, null=True)
    three_d_secure_tokenization_method_dynamic_last4 = models.CharField(max_length=191, blank=True, null=True)
    current_state = models.CharField(max_length=191, blank=True, null=True)
    is_layer_payment = models.IntegerField()
    pg_txn_ref_num = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    payment_request_id = models.CharField(max_length=191, blank=True, null=True)
    payment_id = models.CharField(max_length=191, blank=True, null=True)
    pg_merchant_id = models.CharField(max_length=191, blank=True, null=True)
    request_data = models.TextField(blank=True, null=True)
    pg_transaction_id = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stripe_charges'


class StripeConnects(models.Model):
    stripe_connects_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.CharField(max_length=191)
    stripe_account_id = models.CharField(max_length=244)
    is_activated = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stripe_connects'


class StripeCustomerSources(models.Model):
    stripe_customer_sources_id = models.AutoField(primary_key=True)
    stripe_customers_id = models.IntegerField()
    stripe_source_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stripe_customer_sources'


class StripeCustomers(models.Model):
    stripe_customers_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.CharField(max_length=191)
    customer_email = models.CharField(max_length=191)
    stripe_customer_id = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stripe_customers'


class StripePayouts(models.Model):
    stripe_payouts_id = models.AutoField(primary_key=True)
    payout_id = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    arrival_date = models.CharField(max_length=60)
    balance_transaction = models.CharField(max_length=300)
    source_type = models.CharField(max_length=100)
    statement_descriptor = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stripe_payouts'


class StripeSettlements(models.Model):
    stripe_settlements_id = models.AutoField(primary_key=True)
    balance_transaction = models.CharField(max_length=200)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    merchant_transaction_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    convenience_fee = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    pg_transactions_id = models.IntegerField(unique=True, blank=True, null=True)
    available_on = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)
    stripe_total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_gst = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_fee = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_net_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    open_total_charge = models.DecimalField(max_digits=10, decimal_places=2)
    open_net_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pg_txn_ref_num = models.CharField(unique=True, max_length=100)
    open_gst = models.DecimalField(max_digits=10, decimal_places=2)
    open_tdr = models.DecimalField(max_digits=10, decimal_places=2)
    same_day_settlement_charge = models.DecimalField(max_digits=12, decimal_places=2)
    source_type = models.CharField(max_length=200, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    settlement_status_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    client_secret = models.CharField(max_length=300)
    settled_by = models.IntegerField()
    hold_reason = models.CharField(max_length=191, blank=True, null=True)
    hold_by = models.IntegerField(blank=True, null=True)
    settled_to_open_date = models.DateTimeField()
    settled_to_merchant_date = models.DateTimeField()
    settlement_source = models.CharField(max_length=191)
    settlement_txn_id = models.CharField(max_length=191, blank=True, null=True)
    is_held = models.IntegerField()
    settlement_modes_id = models.IntegerField()
    is_picked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stripe_settlements'


class StripeWebhookCalls(models.Model):
    stripe_webhook_calls_id = models.AutoField(primary_key=True)
    bank_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stripe_webhook_calls'


class SubLoans(models.Model):
    sub_loan_id = models.AutoField(primary_key=True)
    lending_id = models.IntegerField()
    nbfc_app_id = models.IntegerField()
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    transaction_id = models.CharField(max_length=100, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    payment_token = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    sub_loan_details = models.TextField(db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    closure_date = models.DateTimeField(blank=True, null=True)
    action = models.CharField(max_length=100, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    arzoo_repay_loan_id = models.IntegerField(blank=True, null=True)
    bank_transaction_status_id = models.IntegerField(blank=True, null=True)
    nbfc_transaction_status_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_loans'


class SubscriptionCardPlans(models.Model):
    subscription_packages_id = models.IntegerField(primary_key=True)
    card_type = models.CharField(max_length=14)
    card_count = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_card_plans'
        unique_together = (('subscription_packages_id', 'card_type'),)


class SubscriptionDailyDeductions(models.Model):
    accounts_id = models.PositiveIntegerField()
    companies_id = models.PositiveIntegerField()
    users_id = models.PositiveIntegerField()
    subscription_histories_id = models.PositiveIntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    internal_txn_id = models.CharField(max_length=191, blank=True, null=True)
    deducted_at = models.DateTimeField(blank=True, null=True)
    is_deducted = models.IntegerField()
    description = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_daily_deductions'


class SubscriptionHistories(models.Model):
    subscription_histories_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    payment_token = models.CharField(max_length=255, blank=True, null=True)
    payment_id = models.CharField(max_length=255, blank=True, null=True)
    payment_ref_no = models.CharField(max_length=255, blank=True, null=True)
    internal_transaction_ref_id = models.CharField(max_length=255, blank=True, null=True)
    payment_method = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    subscription_payment_statuses_id = models.IntegerField(blank=True, null=True)
    subscription_packages_id = models.IntegerField(blank=True, null=True)
    subscription_types_id = models.IntegerField(blank=True, null=True)
    is_expired = models.IntegerField()
    subscription_start_date = models.DateTimeField(blank=True, null=True)
    subscription_end_date = models.DateTimeField(blank=True, null=True)
    subscription_mode = models.CharField(max_length=255)
    app_subscription_packages_id = models.CharField(max_length=255, blank=True, null=True)
    app_subscriptions_id = models.CharField(max_length=255, blank=True, null=True)
    app_types_id = models.CharField(max_length=255, blank=True, null=True)
    source_type = models.CharField(max_length=255, blank=True, null=True)
    source_id = models.CharField(max_length=255, blank=True, null=True)
    is_upgrade_payment = models.IntegerField()
    subscription_coupon_code = models.CharField(max_length=191, blank=True, null=True)
    invoices_id = models.IntegerField(blank=True, null=True)
    invoices_files_id = models.IntegerField(blank=True, null=True)
    invoice_sent_on = models.DateTimeField(blank=True, null=True)
    invoice_sent_statuses_id = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_histories'


class SubscriptionJoinWaitingList(models.Model):
    subscription_join_waiting_list_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField(blank=True, null=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=191)
    mobile_number = models.CharField(max_length=191, blank=True, null=True)
    is_subscribed = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_join_waiting_list'


class SubscriptionLayerWebhooks(models.Model):
    subscription_layer_webhooks_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    subscription_type = models.CharField(max_length=191)
    response_type = models.CharField(max_length=191, blank=True, null=True)
    payment_purposes_id = models.IntegerField()
    internal_transaction_ref_id = models.CharField(max_length=191, blank=True, null=True)
    payment_method = models.CharField(max_length=191, blank=True, null=True)
    payment_token = models.CharField(max_length=191, blank=True, null=True)
    payment_ref_no = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    internal_payment_ref_id = models.CharField(max_length=191, blank=True, null=True)
    payment_status = models.CharField(max_length=191, blank=True, null=True)
    event = models.CharField(max_length=191, blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_layer_webhooks'


class SubscriptionMerchantPricingConfigurationHistories(models.Model):
    subscription_merchant_pricing_configuration_histories_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    transaction_category = models.CharField(max_length=191, blank=True, null=True)
    transaction_types_id = models.IntegerField(blank=True, null=True)
    transaction_mode = models.CharField(max_length=191, blank=True, null=True)
    transaction_min_range = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    transaction_max_range = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    subscription_packages_id = models.IntegerField(blank=True, null=True)
    transaction_charging_rate_type = models.CharField(max_length=5)
    transaction_charging_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    admin_users_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_merchant_pricing_configuration_histories'


class SubscriptionMerchantPricingConfigurations(models.Model):
    subscription_merchant_pricing_configurations_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    transaction_category = models.CharField(max_length=191, blank=True, null=True)
    transaction_types_id = models.IntegerField(blank=True, null=True)
    transaction_mode = models.CharField(max_length=191, blank=True, null=True)
    pricing_category_modes_id = models.IntegerField(blank=True, null=True)
    transaction_min_range = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    transaction_max_range = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    subscription_packages_id = models.IntegerField(blank=True, null=True)
    transaction_charging_rate_type = models.CharField(max_length=5)
    transaction_charging_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_merchant_pricing_configurations'


class SubscriptionModes(models.Model):
    subscription_modes_id = models.AutoField(primary_key=True)
    subscription_mode = models.CharField(max_length=191)
    subscription_type_source = models.CharField(max_length=191)
    subscription_package_source = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_modes'


class SubscriptionModules(models.Model):
    subscription_modules_id = models.AutoField(primary_key=True)
    module_name = models.CharField(max_length=191)
    description = models.TextField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_modules'


class SubscriptionPackages(models.Model):
    subscription_packages_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    subscription_modules_ids = models.CharField(max_length=350, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    discount_price = models.CharField(max_length=255, blank=True, null=True)
    package_level = models.CharField(max_length=255, blank=True, null=True)
    package_duration = models.IntegerField(blank=True, null=True)
    package_type = models.CharField(max_length=255, blank=True, null=True)
    no_of_times_allowed = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_packages'


class SubscriptionPaymentStatuses(models.Model):
    subscription_payment_statuses_id = models.AutoField(primary_key=True)
    subscription_payment_status = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_payment_statuses'


class SubscriptionPricingConfigurations(models.Model):
    subscription_pricing_configurations_id = models.AutoField(primary_key=True)
    transaction_category = models.CharField(max_length=191, blank=True, null=True)
    transaction_types_id = models.IntegerField(blank=True, null=True)
    transaction_mode = models.CharField(max_length=191, blank=True, null=True)
    pricing_category_modes_id = models.CharField(max_length=255, blank=True, null=True)
    transaction_min_range = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    transaction_max_range = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    subscription_packages_id = models.IntegerField(blank=True, null=True)
    transaction_charging_rate_type = models.CharField(max_length=5)
    transaction_charging_rate = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_pricing_configurations'


class SubscriptionSettlementRevenuePercentages(models.Model):
    subscription_settlement_revenue_percentages_id = models.AutoField(primary_key=True)
    open_role_and_description = models.TextField()
    revenue_percentage = models.DecimalField(max_digits=14, decimal_places=2)
    open_roles_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_settlement_revenue_percentages'


class SubscriptionSplitSettlements(models.Model):
    subscription_split_settlements_id = models.AutoField(primary_key=True)
    user_accounts_id = models.IntegerField()
    user_companies_id = models.IntegerField()
    user_users_id = models.IntegerField()
    franchise_accounts_id = models.IntegerField()
    franchise_companies_id = models.IntegerField()
    franchise_users_id = models.IntegerField()
    subscription_modes_id = models.IntegerField(blank=True, null=True)
    subscription_type_source = models.CharField(max_length=191, blank=True, null=True)
    subscription_type_source_id = models.IntegerField(blank=True, null=True)
    subscription_package_source = models.CharField(max_length=191, blank=True, null=True)
    subscription_package_source_id = models.IntegerField(blank=True, null=True)
    subsciption_source = models.CharField(max_length=191, blank=True, null=True)
    subscription_souce_id = models.CharField(max_length=191, blank=True, null=True)
    source_type = models.CharField(max_length=191, blank=True, null=True)
    source_id = models.CharField(max_length=191, blank=True, null=True)
    user_paid_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    subscription_period = models.TextField(blank=True, null=True)
    commision_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    commision_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    open_roles_id = models.IntegerField(blank=True, null=True)
    outward_settlement_stauses_id = models.IntegerField(blank=True, null=True)
    settlement_txn_id = models.CharField(max_length=191, blank=True, null=True)
    settlement_source = models.CharField(max_length=191, blank=True, null=True)
    settlement_source_id = models.CharField(max_length=191, blank=True, null=True)
    settlement_reference_id = models.CharField(max_length=191, blank=True, null=True)
    payment_source = models.CharField(max_length=191, blank=True, null=True)
    payment_source_id = models.CharField(max_length=191, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_split_settlements'


class SubscriptionTypes(models.Model):
    subscription_types_id = models.AutoField(primary_key=True)
    subscription_type = models.CharField(max_length=191)
    description = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_types'


class SysProperties(models.Model):
    name = models.CharField(unique=True, max_length=191)
    value = models.CharField(max_length=191)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_properties'


class Tags(models.Model):
    tags_id = models.AutoField(primary_key=True)
    tags_name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'


class TallyCompanies(models.Model):
    tally_companies_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    company_name = models.CharField(max_length=300)
    company_guid = models.CharField(max_length=300)
    company_period = models.CharField(max_length=200, blank=True, null=True)
    company_is_security_on = models.CharField(max_length=200)
    company_address = models.TextField(blank=True, null=True)
    company_gstin = models.CharField(max_length=200, blank=True, null=True)
    last_synced = models.DateTimeField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tally_companies'


class TallyDues(models.Model):
    tally_dues_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    company_guid = models.CharField(max_length=300)
    bill_ref_num = models.CharField(max_length=300)
    bill_date = models.DateTimeField(blank=True, null=True)
    bill_guid = models.CharField(max_length=300, blank=True, null=True)
    total_bill_amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_on = models.DateTimeField(blank=True, null=True)
    party_name = models.CharField(max_length=300, blank=True, null=True)
    party_guid = models.CharField(max_length=300)
    is_bill_by_bill = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tally_dues'


class TallyInvoiceSequenceIds(models.Model):
    tally_invoice_sequence_id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tally_invoice_sequence_ids'


class TallyLedgerEntries(models.Model):
    tally_ledger_entries_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    invoices_id = models.IntegerField()
    transaction_guid = models.CharField(max_length=300)
    company_guid = models.CharField(max_length=300)
    bill_guid = models.CharField(max_length=300, blank=True, null=True)
    ledger_name = models.CharField(max_length=300)
    ledger_entry_amount = models.DecimalField(max_digits=10, decimal_places=2)
    hsn_sac_code = models.CharField(max_length=50, blank=True, null=True)
    basic_user_description = models.TextField(blank=True, null=True)
    basic_invoice_tax_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_dr_cr = models.CharField(max_length=300)
    party_master_id = models.CharField(max_length=300, blank=True, null=True)
    party_guid = models.CharField(max_length=300, blank=True, null=True)
    ledger_entry_master_id = models.CharField(max_length=300, blank=True, null=True)
    is_party_ledger_entry = models.IntegerField(blank=True, null=True)
    journal_entries_id = models.IntegerField(blank=True, null=True)
    invoice_extra_charges_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tally_ledger_entries'


class TallyLedgers(models.Model):
    tally_ledgers_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    contacts_id = models.IntegerField(blank=True, null=True)
    party_name = models.CharField(max_length=191, blank=True, null=True)
    guid = models.CharField(max_length=191, blank=True, null=True)
    address = models.CharField(max_length=191, blank=True, null=True)
    mobile = models.CharField(max_length=191, blank=True, null=True)
    email_id = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.CharField(max_length=200, blank=True, null=True)
    contact_person = models.CharField(max_length=200, blank=True, null=True)
    name_of_bank = models.CharField(max_length=191, blank=True, null=True)
    bank_account_number = models.CharField(max_length=191, blank=True, null=True)
    ifsc_code = models.CharField(max_length=191, blank=True, null=True)
    masters_id = models.CharField(max_length=200, blank=True, null=True)
    mailing_name = models.CharField(max_length=200, blank=True, null=True)
    landline_number = models.CharField(max_length=200, blank=True, null=True)
    payment_favouring = models.CharField(max_length=200, blank=True, null=True)
    is_contact = models.IntegerField(blank=True, null=True)
    hsn_sac_code = models.CharField(max_length=200, blank=True, null=True)
    igst_rate = models.CharField(max_length=200, blank=True, null=True)
    cess_rate = models.CharField(max_length=200, blank=True, null=True)
    tax_type = models.CharField(max_length=200, blank=True, null=True)
    duty_head = models.CharField(max_length=200, blank=True, null=True)
    type_of_supply = models.CharField(max_length=200, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    tds_rate = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    tds_categories_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tally_ledgers'


class TallyLedgersDump(models.Model):
    tally_ledgers_dump_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    contacts_id = models.IntegerField(blank=True, null=True)
    partyname = models.CharField(db_column='PartyName', max_length=191, blank=True, null=True)  # Field name made lowercase.
    partyguid = models.CharField(db_column='PartyGuid', max_length=191, blank=True, null=True)  # Field name made lowercase.
    contactaddress = models.CharField(db_column='ContactAddress', max_length=191, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=191, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=200, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pincode = models.CharField(db_column='Pincode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    contactperson = models.CharField(db_column='ContactPerson', max_length=200, blank=True, null=True)  # Field name made lowercase.
    name_of_bank = models.CharField(max_length=191, blank=True, null=True)
    bankaccountnumber = models.CharField(db_column='BankAccountNumber', max_length=191, blank=True, null=True)  # Field name made lowercase.
    ifsccode = models.CharField(db_column='IFSCCode', max_length=191, blank=True, null=True)  # Field name made lowercase.
    partymasterid = models.CharField(db_column='PartyMasterID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mailingname = models.CharField(db_column='MailingName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='ContactNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    paymentfavouring = models.CharField(db_column='PaymentFavouring', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ispartyledger = models.CharField(db_column='IsPartyLedger', max_length=199, blank=True, null=True)  # Field name made lowercase.
    hsnsaccode = models.CharField(db_column='HSNSACCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    igstrateoftax = models.CharField(db_column='IGSTRateofTax', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cessrateoftax = models.CharField(db_column='CessRateofTax', max_length=200, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.CharField(db_column='TaxType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dutyhead = models.CharField(db_column='DutyHead', max_length=200, blank=True, null=True)  # Field name made lowercase.
    typeofsupply = models.CharField(db_column='TypeOfSupply', max_length=200, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.CharField(db_column='TimeStamp', max_length=199, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    tds = models.CharField(db_column='TDS', max_length=199, blank=True, null=True)  # Field name made lowercase.
    billcreditperiod = models.CharField(db_column='BillCreditPeriod', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pancardnumber = models.CharField(db_column='PanCardNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gstregistrationtype = models.CharField(db_column='GSTRegistrationType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    natureofsupply = models.CharField(db_column='NatureOfSupply', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gstin = models.CharField(db_column='GSTIN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    isecomoperator = models.CharField(db_column='IsEcomOperator', max_length=200, blank=True, null=True)  # Field name made lowercase.
    istransporter = models.CharField(db_column='IsTransporter', max_length=200, blank=True, null=True)  # Field name made lowercase.
    openingbalance = models.CharField(db_column='OpeningBalance', max_length=200, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    l1categoriesid = models.IntegerField(db_column='L1CategoriesId', blank=True, null=True)  # Field name made lowercase.
    l2categoriesid = models.IntegerField(db_column='L2CategoriesId', blank=True, null=True)  # Field name made lowercase.
    is_picked = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tally_ledgers_dump'


class TallyOpenLinks(models.Model):
    tally_open_links_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    tally_license = models.CharField(max_length=200)
    company_guid = models.CharField(max_length=200)
    remarks = models.TextField()
    last_sync = models.DateTimeField(blank=True, null=True)
    open_txn_cutoff_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tally_open_links'


class TallyPayables(models.Model):
    tally_payables_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    company_name = models.CharField(max_length=191, blank=True, null=True)
    party_name = models.CharField(max_length=191, blank=True, null=True)
    guid = models.CharField(max_length=191, blank=True, null=True)
    address = models.CharField(max_length=191, blank=True, null=True)
    mobile = models.CharField(max_length=191, blank=True, null=True)
    name_of_bank = models.CharField(max_length=191, blank=True, null=True)
    bank_account_number = models.CharField(max_length=191, blank=True, null=True)
    ifsc_code = models.CharField(max_length=191, blank=True, null=True)
    total_outstanding = models.CharField(max_length=191, blank=True, null=True)
    partial_payment_available = models.IntegerField(blank=True, null=True)
    is_paid = models.CharField(max_length=191, blank=True, null=True)
    due_date = models.DateTimeField()
    batch_id = models.CharField(max_length=200)
    bank_ledger_number = models.CharField(max_length=200)
    voucher_type = models.CharField(max_length=200)
    voucher_number = models.CharField(max_length=200)
    narration = models.CharField(max_length=300)
    invoices_id = models.CharField(max_length=200)
    is_voucher_created = models.IntegerField()
    bill_ref_num = models.CharField(max_length=200)
    company_guid = models.CharField(max_length=200)
    is_bill_by_bill = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tally_payables'


class TallyPayablesCopy(models.Model):
    tally_payables_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    company_name = models.CharField(max_length=191, blank=True, null=True)
    party_name = models.CharField(max_length=191, blank=True, null=True)
    guid = models.CharField(max_length=191, blank=True, null=True)
    address = models.CharField(max_length=191, blank=True, null=True)
    mobile = models.CharField(max_length=191, blank=True, null=True)
    name_of_bank = models.CharField(max_length=191, blank=True, null=True)
    bank_account_number = models.CharField(max_length=191, blank=True, null=True)
    ifsc_code = models.CharField(max_length=191, blank=True, null=True)
    total_outstanding = models.CharField(max_length=191, blank=True, null=True)
    is_paid = models.CharField(max_length=191, blank=True, null=True)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    batch_id = models.CharField(max_length=200)
    bank_ledger_number = models.CharField(max_length=200)
    voucher_type = models.CharField(max_length=200)
    voucher_number = models.CharField(max_length=200)
    narration = models.CharField(max_length=300)
    invoices_id = models.CharField(max_length=200)
    is_voucher_created = models.IntegerField()
    bill_ref_num = models.CharField(max_length=200)
    company_guid = models.CharField(max_length=200)
    is_bill_by_bill = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tally_payables_copy'


class TallyReconciliations(models.Model):
    tally_reconciliations_id = models.BigAutoField(primary_key=True)
    name_of_bank = models.CharField(max_length=191, blank=True, null=True)
    bank_account_number = models.CharField(max_length=191, blank=True, null=True)
    ifsc_code = models.CharField(max_length=191, blank=True, null=True)
    transaction_id = models.CharField(max_length=200, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_paid = models.IntegerField()
    payment_mode = models.CharField(max_length=200, blank=True, null=True)
    bank_ledger_number = models.CharField(max_length=200, blank=True, null=True)
    voucher_type = models.CharField(max_length=200, blank=True, null=True)
    voucher_number = models.CharField(max_length=200, blank=True, null=True)
    narration = models.CharField(max_length=300, blank=True, null=True)
    tally_payables_id = models.IntegerField()
    invoice_payments_id = models.IntegerField(blank=True, null=True)
    invoice_transfers_id = models.IntegerField(blank=True, null=True)
    is_voucher_created = models.IntegerField()
    paid_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tally_reconciliations'


class TallySyncs(models.Model):
    tally_syncs_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    tally_dues_id = models.IntegerField()
    bill_ref_num = models.CharField(max_length=200)
    company_guid = models.CharField(max_length=300)
    bill_guid = models.CharField(max_length=300, blank=True, null=True)
    due_type = models.CharField(max_length=300)
    due_date = models.DateTimeField(blank=True, null=True)
    voucher_number = models.CharField(max_length=300)
    batch_id = models.CharField(max_length=200)
    contacts_id = models.IntegerField()
    bank_ledger_number = models.CharField(max_length=200, blank=True, null=True)
    transaction_guid = models.CharField(max_length=300)
    voucher_type_name = models.CharField(max_length=300)
    party_name = models.CharField(max_length=300, blank=True, null=True)
    transaction_date = models.DateTimeField()
    narration = models.TextField(blank=True, null=True)
    transaction_reference = models.CharField(max_length=300, blank=True, null=True)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    stock_value = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_creation_date = models.DateTimeField(blank=True, null=True)
    tally_timestamp = models.DateTimeField(blank=True, null=True)
    enter_alter_by = models.CharField(max_length=300, blank=True, null=True)
    is_paid = models.IntegerField()
    last_paid_at = models.DateTimeField(blank=True, null=True)
    invoices_id = models.IntegerField()
    is_bill_by_bill = models.IntegerField()
    tds_amount = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_tdr_synced = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tally_syncs'


class TallySyncsHistories(models.Model):
    tally_syncs_histories_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    tally_syncs_id = models.IntegerField()
    transaction_guid = models.CharField(max_length=300)
    due_type = models.CharField(max_length=300)
    voucher_type_name = models.CharField(max_length=300)
    transaction_date = models.DateTimeField()
    narration = models.TextField(blank=True, null=True)
    transaction_reference = models.CharField(max_length=300, blank=True, null=True)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_creation_date = models.DateTimeField(blank=True, null=True)
    invoices_id = models.IntegerField()
    is_bill_by_bill = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tally_syncs_histories'


class TaxStateCodes(models.Model):
    tax_state_codes_id = models.AutoField(primary_key=True)
    states_list_id = models.IntegerField()
    tax_state_code = models.IntegerField()
    tax_state_name = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_state_codes'


class Taxes(models.Model):
    taxes_id = models.AutoField(primary_key=True)
    tax_name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taxes'


class TdsCategories(models.Model):
    tds_categories_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    section = models.CharField(max_length=15)
    payment_code = models.CharField(max_length=15)
    default_rate = models.FloatField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tds_categories'


class TeamInvites(models.Model):
    team_invites_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    request_data = models.TextField()
    sent_to_email = models.CharField(max_length=191, blank=True, null=True)
    invite_sent_on = models.DateTimeField()
    hash = models.CharField(max_length=300)
    is_invite_accepted = models.IntegerField()
    joining_statuses_id = models.IntegerField(blank=True, null=True)
    emp_code = models.CharField(max_length=150, blank=True, null=True)
    invite_accepted_on = models.DateTimeField(blank=True, null=True)
    is_invite_link_disabled = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_invites'


class TeamMemberDetails(models.Model):
    team_member_details_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    companies_id = models.IntegerField()
    team_invites_id = models.IntegerField()
    emp_code = models.CharField(max_length=150, blank=True, null=True)
    full_name = models.CharField(max_length=300, blank=True, null=True)
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    approver_name = models.CharField(max_length=191, blank=True, null=True)
    approver_users_id = models.IntegerField(blank=True, null=True)
    invite_sent_on = models.DateTimeField(blank=True, null=True)
    invite_accepted_on = models.DateTimeField(blank=True, null=True)
    is_invite_accepted = models.IntegerField()
    joining_statuses_id = models.IntegerField(blank=True, null=True)
    date_of_joining = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=300, blank=True, null=True)
    designation = models.CharField(max_length=250, blank=True, null=True)
    departments_id = models.IntegerField(blank=True, null=True)
    reporting_manager_name = models.CharField(max_length=191, blank=True, null=True)
    reporting_manager_users_id = models.IntegerField(blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    email_id = models.CharField(max_length=250, blank=True, null=True)
    date_of_birth = models.CharField(max_length=100, blank=True, null=True)
    is_kyc_uploaded = models.IntegerField()
    is_kyc_verified = models.IntegerField()
    verification_date = models.DateField(blank=True, null=True)
    verified_by = models.IntegerField(blank=True, null=True)
    is_maker = models.IntegerField()
    is_checker = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    profile_image = models.CharField(max_length=500, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_member_details'


class TempManualUpiCallbacks(models.Model):
    temp_manual_upi_callbacks_id = models.AutoField(primary_key=True)
    accountnumber = models.CharField(db_column='accountNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    merchantid = models.CharField(db_column='merchantID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    merchantname = models.CharField(db_column='merchantName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    submerchantid = models.CharField(db_column='subMerchantID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    submerchantname = models.CharField(db_column='subMerchantName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    merchanttranid = models.CharField(db_column='merchantTranID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    banktranid = models.CharField(db_column='bankTranID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=200, blank=True, null=True)
    time = models.CharField(max_length=200, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payerva = models.CharField(db_column='payerVA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=200, blank=True, null=True)
    commission = models.CharField(db_column='Commission', max_length=200, blank=True, null=True)  # Field name made lowercase.
    servicetax = models.CharField(db_column='ServiceTax', max_length=200, blank=True, null=True)  # Field name made lowercase.
    netamount = models.CharField(db_column='NetAmount', max_length=200, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=200, blank=True, null=True)  # Field name made lowercase.
    is_picked = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_manual_upi_callbacks'


class TempStripeSettlements(models.Model):
    temp_stripe_settlements_id = models.AutoField(primary_key=True)
    balance_transaction = models.CharField(max_length=191, blank=True, null=True)
    total_amount = models.CharField(max_length=191, blank=True, null=True)
    available_on = models.CharField(max_length=191, blank=True, null=True)
    currency = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    stripe_total_fee = models.CharField(max_length=191, blank=True, null=True)
    stripe_gst = models.CharField(max_length=191, blank=True, null=True)
    stripe_fee = models.CharField(max_length=191, blank=True, null=True)
    stripe_net_amount = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    type = models.CharField(max_length=191, blank=True, null=True)
    pg_txn_ref_num = models.CharField(max_length=191, blank=True, null=True)
    settled_to_open_date = models.CharField(max_length=191, blank=True, null=True)
    available_in_stripe_settlements = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_stripe_settlements'


class Test(models.Model):
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    fiscalyear = models.SmallIntegerField(db_column='fiscalYear')  # Field name made lowercase.
    fiscalmonth = models.IntegerField(db_column='fiscalMonth')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test'
        unique_together = (('product', 'fiscalyear', 'fiscalmonth'),)


class Testchanges(models.Model):
    salesid = models.IntegerField(db_column='salesId', blank=True, null=True)  # Field name made lowercase.
    beforequantity = models.IntegerField(db_column='beforeQuantity', blank=True, null=True)  # Field name made lowercase.
    afterquantity = models.IntegerField(db_column='afterQuantity', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='changedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'testChanges'


class TestAccountDetails(models.Model):
    test_account_details_id = models.BigAutoField(primary_key=True)
    subscription_companies_id = models.IntegerField(unique=True, blank=True, null=True)
    salt_subscription_companies_id = models.IntegerField(unique=True, blank=True, null=True)
    app_subscription_companies_id = models.IntegerField(unique=True, blank=True, null=True)
    old_auth_companies_id = models.IntegerField(unique=True, blank=True, null=True)
    test_card_limit_users_ids = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_account_details'


class TestTable(models.Model):
    string_1 = models.CharField(max_length=191, blank=True, null=True)
    string_2 = models.CharField(max_length=191, blank=True, null=True)
    string_3 = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_table'


class Throttle(models.Model):
    user_id = models.PositiveIntegerField(blank=True, null=True)
    type = models.CharField(max_length=191, blank=True, null=True)
    ip = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'throttle'


class TodoTodoitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'todo_todoitem'


class TpslBankCodes(models.Model):
    tpsl_bank_codes_id = models.AutoField(primary_key=True)
    bank_code = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tpsl_bank_codes'


class TpslSettlements(models.Model):
    tpsl_settlements_id = models.AutoField(primary_key=True)
    bank_id = models.CharField(max_length=5)
    bank_name = models.CharField(max_length=300)
    transaction_id_from_tpsl = models.CharField(unique=True, max_length=100)
    sm_transaction_id = models.CharField(unique=True, max_length=100)
    pg_transactions_id = models.IntegerField(unique=True, blank=True, null=True)
    bank_transaction_id = models.CharField(max_length=200)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    merchant_transaction_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    convenience_fee = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    tpsl_charges = models.DecimalField(max_digits=10, decimal_places=2)
    tpsl_service_tax = models.DecimalField(max_digits=10, decimal_places=2)
    tpsl_total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    tpsl_net_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.CharField(max_length=20)
    transaction_time = models.CharField(max_length=10)
    payment_date = models.CharField(max_length=20)
    src_itc = models.CharField(max_length=300)
    tdr = models.DecimalField(max_digits=10, decimal_places=2)
    same_day_settlement_charge = models.DecimalField(max_digits=12, decimal_places=2)
    gst = models.DecimalField(max_digits=10, decimal_places=2)
    open_total_charges = models.DecimalField(max_digits=10, decimal_places=2)
    open_net_amount = models.DecimalField(max_digits=10, decimal_places=2)
    source_type = models.CharField(max_length=200, blank=True, null=True)
    source_id = models.CharField(max_length=191, blank=True, null=True)
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    companies_id = models.IntegerField()
    status = models.CharField(max_length=191, blank=True, null=True)
    hold_reason = models.CharField(max_length=191, blank=True, null=True)
    hold_by = models.IntegerField(blank=True, null=True)
    settled_by = models.IntegerField()
    settled_to_open_date = models.DateTimeField()
    settled_to_merchant_date = models.DateTimeField()
    settlement_source = models.CharField(max_length=191)
    settlement_txn_id = models.CharField(max_length=191, blank=True, null=True)
    is_held = models.IntegerField()
    settlement_modes_id = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_processed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tpsl_settlements'


class TpslTransactions(models.Model):
    tpsl_transactions_id = models.AutoField(primary_key=True)
    tpsl_merchant_code = models.CharField(max_length=100, blank=True, null=True)
    tpsl_request_type = models.CharField(max_length=20, blank=True, null=True)
    merchant_txn_ref_no = models.CharField(max_length=100, blank=True, null=True)
    transaction_amount = models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True)
    tpsl_currency_code = models.CharField(max_length=20, blank=True, null=True)
    tpsl_return_url = models.CharField(max_length=200, blank=True, null=True)
    tpsl_s2s_url = models.CharField(max_length=200, blank=True, null=True)
    shopping_cart_details = models.CharField(max_length=100, blank=True, null=True)
    transaction_date = models.CharField(max_length=100, blank=True, null=True)
    bank_code = models.CharField(max_length=20, blank=True, null=True)
    tpsl_locator_url = models.CharField(max_length=200, blank=True, null=True)
    customer_mobile_no = models.CharField(max_length=20, blank=True, null=True)
    customer_email_id = models.CharField(max_length=35, blank=True, null=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    txn_status = models.CharField(max_length=50, blank=True, null=True)
    txn_msg = models.CharField(max_length=50, blank=True, null=True)
    txn_err_msg = models.CharField(max_length=200, blank=True, null=True)
    tpsl_txn_time = models.CharField(max_length=60, blank=True, null=True)
    rqst_token = models.CharField(max_length=200, blank=True, null=True)
    hash = models.CharField(max_length=200, blank=True, null=True)
    txn_id_from_tpsl = models.CharField(max_length=200, blank=True, null=True)
    customer_name = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tpsl_transactions'


class TraitMigrations(models.Model):
    trait_migrations_id = models.AutoField(primary_key=True)
    trait_migration_name = models.TextField()
    is_migration_complete = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trait_migrations'


class TraitMigrationsCopy(models.Model):
    trait_migrations_id = models.AutoField(primary_key=True)
    trait_migration_name = models.TextField()
    is_migration_complete = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trait_migrations_copy'


class TraitPermissions(models.Model):
    trait_permissions_id = models.AutoField(primary_key=True)
    open_traits_id = models.IntegerField()
    open_roles_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trait_permissions'


class TraitPermissionsCopy(models.Model):
    trait_permissions_id = models.AutoField(primary_key=True)
    open_traits_id = models.IntegerField()
    open_roles_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trait_permissions_copy'


class TransactionClientTypes(models.Model):
    transaction_client_types_id = models.AutoField(primary_key=True)
    user_agent_client_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction_client_types'


class TransactionIds(models.Model):
    transaction_id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'transaction_ids'


class TransactionTypes(models.Model):
    transaction_types_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction_types'


class TrulyCrossBorderSettlements(models.Model):
    truly_cross_border_settlements_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    client_customer_ref = models.CharField(max_length=50)
    entity_id = models.CharField(max_length=100, blank=True, null=True)
    bank_account_id = models.CharField(max_length=191, blank=True, null=True)
    account_ledger_id = models.CharField(max_length=191, blank=True, null=True)
    currency_code = models.CharField(max_length=50)
    amount = models.FloatField()
    ledger_operation = models.CharField(max_length=191, blank=True, null=True)
    particulars = models.CharField(max_length=191, blank=True, null=True)
    reconciliation_status = models.CharField(max_length=191, blank=True, null=True)
    truly_transaction_time = models.CharField(max_length=191, blank=True, null=True)
    value_date = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'truly_cross_border_settlements'


class TrulyCrossBorderTransactions(models.Model):
    truly_cross_border_transactions_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    client_customer_ref = models.CharField(max_length=50)
    entity_id = models.CharField(max_length=100, blank=True, null=True)
    bank_account_id = models.CharField(max_length=191, blank=True, null=True)
    account_ledger_id = models.CharField(max_length=191, blank=True, null=True)
    currency_code = models.CharField(max_length=50)
    amount = models.FloatField()
    ledger_operation = models.CharField(max_length=191, blank=True, null=True)
    particulars = models.CharField(max_length=191, blank=True, null=True)
    reconciliation_status = models.CharField(max_length=191, blank=True, null=True)
    truly_transaction_time = models.CharField(max_length=191, blank=True, null=True)
    value_date = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'truly_cross_border_transactions'


class TrulyCrossBorderUsers(models.Model):
    truly_cross_border_users_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    client_customer_ref = models.CharField(max_length=50)
    entity_id = models.CharField(max_length=50, blank=True, null=True)
    entity_status = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'truly_cross_border_users'


class TrulyCustomerBankAccounts(models.Model):
    truly_customer_bank_accounts_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    client_customer_ref = models.CharField(max_length=191)
    bank_account_id = models.CharField(max_length=191, blank=True, null=True)
    account_holder_name = models.CharField(max_length=191, blank=True, null=True)
    bank_name = models.CharField(max_length=191, blank=True, null=True)
    account_type = models.CharField(max_length=100, blank=True, null=True)
    account_number = models.CharField(max_length=100, blank=True, null=True)
    iban = models.CharField(max_length=100, blank=True, null=True)
    routing_code_type_1 = models.CharField(max_length=100, blank=True, null=True)
    routing_code_value_1 = models.CharField(max_length=100, blank=True, null=True)
    routing_code_type_2 = models.CharField(max_length=100, blank=True, null=True)
    routing_code_value_2 = models.CharField(max_length=100, blank=True, null=True)
    routing_code_type_3 = models.CharField(max_length=100, blank=True, null=True)
    routing_code_value_3 = models.CharField(max_length=100, blank=True, null=True)
    bank_country_code = models.CharField(max_length=50, blank=True, null=True)
    bank_branch_address = models.CharField(max_length=191, blank=True, null=True)
    currency_code = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'truly_customer_bank_accounts'


class TrulyUserDetails(models.Model):
    truly_user_details_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(unique=True)
    companies_id = models.IntegerField(unique=True)
    users_id = models.IntegerField()
    client_customer_ref = models.CharField(max_length=191)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    personal_email = models.CharField(max_length=100, blank=True, null=True)
    personal_mobile = models.CharField(max_length=20, blank=True, null=True)
    personal_pan = models.CharField(max_length=20, blank=True, null=True)
    aadhaar_number = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    citizenship_country_code = models.CharField(max_length=5, blank=True, null=True)
    pep = models.IntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=191, blank=True, null=True)
    position = models.CharField(max_length=191, blank=True, null=True)
    brand_name = models.CharField(max_length=191, blank=True, null=True)
    business_email = models.CharField(max_length=100, blank=True, null=True)
    business_mobile = models.CharField(max_length=20, blank=True, null=True)
    website = models.CharField(max_length=191, blank=True, null=True)
    industry_naics_code = models.CharField(max_length=50, blank=True, null=True)
    source_of_funds = models.CharField(max_length=191, blank=True, null=True)
    number_of_employees = models.IntegerField(blank=True, null=True)
    iec_code = models.CharField(max_length=191, blank=True, null=True)
    incorporation_number = models.CharField(max_length=100, blank=True, null=True)
    gstin_number = models.CharField(max_length=100, blank=True, null=True)
    entity_type = models.CharField(max_length=10, blank=True, null=True)
    entity_sub_type = models.CharField(max_length=100, blank=True, null=True)
    nature_of_business = models.CharField(max_length=100, blank=True, null=True)
    annual_revenue = models.CharField(max_length=100, blank=True, null=True)
    address_line_1 = models.CharField(max_length=191, blank=True, null=True)
    address_line_2 = models.CharField(max_length=191, blank=True, null=True)
    landmark = models.CharField(max_length=191, blank=True, null=True)
    city = models.CharField(max_length=191, blank=True, null=True)
    state_code = models.CharField(max_length=10, blank=True, null=True)
    state_name = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'truly_user_details'


class Units(models.Model):
    units_id = models.AutoField(primary_key=True)
    abbrivation = models.CharField(max_length=191)
    name = models.CharField(max_length=191)
    descritpion = models.CharField(max_length=191)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'units'


class UpiCallbacks(models.Model):
    upi_callbacks_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    merchant_id = models.CharField(max_length=200)
    sub_merchant_id = models.CharField(max_length=200)
    terminal_id = models.CharField(max_length=200)
    bank_rrn = models.CharField(unique=True, max_length=191)
    merchant_tran_id = models.CharField(max_length=200)
    payer_name = models.CharField(max_length=200)
    payer_mobile = models.CharField(max_length=191)
    payer_va = models.CharField(max_length=200)
    payer_amount = models.DecimalField(max_digits=10, decimal_places=2)
    txn_status = models.CharField(max_length=200)
    txn_init_date = models.DateTimeField()
    txn_completion_date = models.DateTimeField()
    source_id = models.CharField(max_length=191, blank=True, null=True)
    source_type = models.CharField(max_length=191, blank=True, null=True)
    is_qr_payment = models.CharField(max_length=191)
    is_processed = models.IntegerField()
    settlement_source_type = models.CharField(max_length=191, blank=True, null=True)
    settlement_source_id = models.CharField(max_length=191, blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    payer_remarks_note = models.CharField(max_length=255, blank=True, null=True)
    partner_banks_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upi_callbacks'


class UpiRequestStatuses(models.Model):
    upi_request_statuses_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upi_request_statuses'


class UpiRequests(models.Model):
    upi_requests_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    payer_va = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=200)
    collect_by_date = models.DateTimeField()
    merchant_id = models.CharField(max_length=200)
    merchant_name = models.CharField(max_length=200)
    sub_merchant_id = models.CharField(max_length=200)
    sub_merchant_name = models.CharField(max_length=200)
    terminal_id = models.CharField(max_length=200)
    merchant_tran_id = models.CharField(max_length=200)
    bill_number = models.CharField(max_length=200)
    upi_request_statuses_id = models.IntegerField()
    upi_request_status_message = models.CharField(max_length=200)
    response = models.CharField(max_length=200)
    upi_request_status = models.CharField(max_length=200)
    bank_rrn = models.CharField(max_length=200)
    source_id = models.CharField(max_length=191, blank=True, null=True)
    source_type = models.CharField(max_length=191, blank=True, null=True)
    upi_transaction_statuses_id = models.IntegerField()
    upi_transaction_status = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upi_requests'


class UpiTransactionStatuses(models.Model):
    upi_transaction_statuses_id = models.AutoField(primary_key=True)
    upi_transaction_status = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upi_transaction_statuses'


class UserAccounts(models.Model):
    user_accounts_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_accounts'


class UserApprovalHistories(models.Model):
    user_approval_histories_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    approver_users_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_approval_histories'


class UserApprovals(models.Model):
    user_approvals_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    approver_users_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_approvals'


class UserCardPlans(models.Model):
    card_plan_id = models.AutoField(primary_key=True)
    card_type = models.CharField(max_length=7)
    users_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    card_count = models.IntegerField()
    cards_used = models.IntegerField(blank=True, null=True)
    activation_period = models.CharField(max_length=16)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    subscription_card_count = models.IntegerField(blank=True, null=True)
    extra_card_order_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_card_plans'
        unique_together = (('card_plan_id', 'card_type', 'activation_period'),)


class UserCardPlansHistory(models.Model):
    user_card_plans_history_id = models.AutoField(primary_key=True)
    request = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_card_plans_history'


class UserCompanies(models.Model):
    user_companies_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_companies'


class UserDepartmentHistories(models.Model):
    user_department_histories_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    departments_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_department_histories'


class UserDepartments(models.Model):
    user_departments_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    departments_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_departments'


class UserDeviceDetails(models.Model):
    user_device_details_id = models.BigAutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    client_type = models.CharField(max_length=100, blank=True, null=True)
    app_version_name = models.CharField(max_length=100, blank=True, null=True)
    app_version_code = models.IntegerField(blank=True, null=True)
    os = models.CharField(max_length=100, blank=True, null=True)
    os_version = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    device_brand = models.CharField(max_length=100, blank=True, null=True)
    device_model = models.CharField(max_length=100, blank=True, null=True)
    device_id = models.CharField(max_length=100, blank=True, null=True)
    app_name = models.CharField(max_length=100, blank=True, null=True)
    ip = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=191, blank=True, null=True)
    longitude = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_device_details'


class UserFirebaseNotificationDetails(models.Model):
    user_firebase_notification_details_id = models.BigAutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    firebase_notification_id = models.CharField(max_length=199, blank=True, null=True)
    one_signal_id = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_firebase_notification_details'


class UserIntercoms(models.Model):
    user_intercoms_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField(blank=True, null=True)
    intercom_id = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_intercoms'


class UserKotakCardRequests(models.Model):
    user_kotak_card_requests_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    team_member_details_id = models.IntegerField()
    email_id = models.CharField(max_length=191)
    phone_no = models.CharField(max_length=191)
    dob = models.DateField()
    full_name = models.CharField(max_length=191)
    applied_at = models.DateTimeField()
    address = models.CharField(max_length=191, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    ref_no = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_kotak_card_requests'


class UserLinkedKotakCardDetails(models.Model):
    user_linked_kotak_card_details_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    team_member_details_id = models.IntegerField()
    card_number = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=191, blank=True, null=True)
    account_number = models.BigIntegerField(blank=True, null=True)
    current_balance = models.BigIntegerField(blank=True, null=True)
    credit_limit = models.BigIntegerField(blank=True, null=True)
    credit_used = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    status = models.IntegerField()
    payment_token = models.CharField(max_length=200, blank=True, null=True)
    payment_verification = models.IntegerField()
    payment_ref_id = models.CharField(max_length=200, blank=True, null=True)
    payment_id = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_linked_kotak_card_details'


class UserLoginHistories(models.Model):
    user_login_histories_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    login_time = models.DateTimeField()
    client_ip = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_login_histories'


class UserMpins(models.Model):
    user_mpins_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    user_mpin = models.CharField(max_length=191)
    username = models.CharField(max_length=191)
    email = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_mpins'


class UserNominees(models.Model):
    user_nominees_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    nominee_full_name = models.CharField(max_length=200, blank=True, null=True)
    nominee_email = models.CharField(max_length=200, blank=True, null=True)
    nominee_mob = models.CharField(max_length=200, blank=True, null=True)
    nominee_dob = models.CharField(max_length=200, blank=True, null=True)
    is_nominee_minor = models.IntegerField()
    nominee_relation = models.CharField(max_length=200, blank=True, null=True)
    nominee_addresses_id = models.IntegerField(blank=True, null=True)
    guardian_full_name = models.CharField(max_length=200, blank=True, null=True)
    guardian_email = models.CharField(max_length=200, blank=True, null=True)
    guardian_mob = models.CharField(max_length=200, blank=True, null=True)
    guardian_addresses_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_nominees'


class UserProfileDetails(models.Model):
    user_profile_details_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    marital_status = models.CharField(max_length=100, blank=True, null=True)
    employment_status = models.CharField(max_length=100, blank=True, null=True)
    profile_image_files_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_profile_details'


class UserResellerProfile(models.Model):
    user_reseller_profile_id = models.AutoField(primary_key=True)
    reseller_code = models.CharField(unique=True, max_length=15)
    users_id = models.IntegerField(unique=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    open_roles_id = models.IntegerField()
    work_email_id = models.CharField(max_length=191)
    business_name = models.CharField(max_length=191, blank=True, null=True)
    business_sector_id = models.IntegerField(blank=True, null=True)
    pan_number = models.CharField(max_length=25)
    gstin_number = models.CharField(max_length=25, blank=True, null=True)
    reseller_url = models.CharField(max_length=100)
    lead_from_reseller_profile_id = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_reseller_profile'


class UserRoleHistories(models.Model):
    user_role_histories_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    open_roles_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_role_histories'


class UserRoles(models.Model):
    user_roles_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    open_roles_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_roles'


class UserSubscriptionPaymentHistories(models.Model):
    user_subscription_payment_histories_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    payment_token = models.CharField(max_length=191, blank=True, null=True)
    payment_id = models.CharField(max_length=200, blank=True, null=True)
    payment_ref_no = models.CharField(max_length=191, blank=True, null=True)
    internal_transaction_ref_id = models.CharField(max_length=191, blank=True, null=True)
    payment_method = models.CharField(max_length=191, blank=True, null=True)
    is_picked = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    subscription_payment_statuses_id = models.IntegerField(blank=True, null=True)
    subscription_packages_id = models.IntegerField(blank=True, null=True)
    user_subscriptions_id = models.IntegerField(blank=True, null=True)
    no_of_attempt = models.IntegerField(blank=True, null=True)
    subscription_mode = models.CharField(max_length=191)
    app_subscription_packages_id = models.CharField(max_length=191, blank=True, null=True)
    app_subscriptions_id = models.CharField(max_length=191, blank=True, null=True)
    app_types_id = models.CharField(max_length=191, blank=True, null=True)
    source_type = models.CharField(max_length=191, blank=True, null=True)
    source_id = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.IntegerField(blank=True, null=True)
    is_upgrade_payment = models.IntegerField(blank=True, null=True)
    is_coupon_code_subscription = models.IntegerField()
    subscription_coupon_code = models.CharField(max_length=191, blank=True, null=True)
    invoices_id = models.IntegerField(blank=True, null=True)
    invoices_files_id = models.IntegerField(blank=True, null=True)
    invoice_sent_on = models.DateTimeField(blank=True, null=True)
    invoice_sent_statuses_id = models.IntegerField()
    is_migrated = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_subscription_payment_histories'


class UserSubscriptions(models.Model):
    user_subscriptions_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField(unique=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField(unique=True)
    amount_paid = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    is_subscribed = models.IntegerField(blank=True, null=True)
    is_trialed = models.IntegerField()
    is_expired = models.IntegerField(blank=True, null=True)
    payment_status = models.CharField(max_length=191, blank=True, null=True)
    subscription_payment_statuses_id = models.IntegerField(blank=True, null=True)
    payment_ref_no = models.CharField(max_length=200, blank=True, null=True)
    internal_payment_ref_id = models.CharField(max_length=191, blank=True, null=True)
    payment_token = models.CharField(max_length=191, blank=True, null=True)
    is_picked = models.IntegerField(blank=True, null=True)
    internal_transaction_ref_id = models.CharField(max_length=191, blank=True, null=True)
    payment_method = models.CharField(max_length=191, blank=True, null=True)
    current_package_user_subscription_id = models.IntegerField(blank=True, null=True)
    subscription_start_date = models.DateTimeField()
    subscription_end_date = models.DateTimeField()
    subscription_packages_id = models.IntegerField(blank=True, null=True)
    subscription_types_id = models.IntegerField()
    invoices_id = models.IntegerField(blank=True, null=True)
    invoices_files_id = models.IntegerField(blank=True, null=True)
    invoice_sent_on = models.DateTimeField(blank=True, null=True)
    invoice_sent_statuses_id = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_picked_for_invoice = models.IntegerField(blank=True, null=True)
    is_sub_metering_migrated = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_subscriptions'


class UserSubscriptionsOld(models.Model):
    user_subscriptions_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    amount_paid = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    is_subscribed = models.IntegerField(blank=True, null=True)
    is_trialed = models.IntegerField()
    is_expired = models.IntegerField()
    payment_status = models.CharField(max_length=191, blank=True, null=True)
    subscription_payment_statuses_id = models.IntegerField(blank=True, null=True)
    payment_ref_no = models.CharField(max_length=200, blank=True, null=True)
    internal_payment_ref_id = models.CharField(max_length=191, blank=True, null=True)
    payment_token = models.CharField(max_length=191, blank=True, null=True)
    is_picked = models.IntegerField(blank=True, null=True)
    internal_transaction_ref_id = models.CharField(max_length=191, blank=True, null=True)
    payment_method = models.CharField(max_length=191, blank=True, null=True)
    current_package_user_subscription_id = models.IntegerField(blank=True, null=True)
    subscription_start_date = models.DateTimeField()
    subscription_end_date = models.DateTimeField()
    subscription_packages_id = models.IntegerField(blank=True, null=True)
    subscription_types_id = models.IntegerField()
    invoices_id = models.IntegerField(blank=True, null=True)
    invoices_files_id = models.IntegerField(blank=True, null=True)
    invoice_sent_on = models.DateTimeField(blank=True, null=True)
    invoice_sent_statuses_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_picked_for_invoice = models.IntegerField(blank=True, null=True)
    is_migrated = models.IntegerField(blank=True, null=True)
    is_trial_migrated = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_subscriptions_old'


class UserTeamMemberDetails(models.Model):
    user_team_member_details_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    team_member_details_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_team_member_details'


class UserUsedApps(models.Model):
    user_used_apps_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    used_apps = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_used_apps'


class Users(models.Model):
    users_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    username = models.CharField(max_length=191)
    first_name = models.CharField(max_length=191, blank=True, null=True)
    last_name = models.CharField(max_length=191, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=191, blank=True, null=True)
    permissions = models.TextField(blank=True, null=True)
    is_banned = models.IntegerField(blank=True, null=True)
    ban_reason = models.CharField(max_length=191, blank=True, null=True)
    skip_onboarding = models.IntegerField()
    last_login = models.DateTimeField(blank=True, null=True)
    has_email_verified = models.IntegerField(blank=True, null=True)
    has_mobile_number_verified = models.IntegerField(blank=True, null=True)
    is_journal_entry_created = models.IntegerField()
    my_referral_code = models.CharField(max_length=191, blank=True, null=True)
    api_version = models.CharField(max_length=191, blank=True, null=True)
    mobile_app_version = models.IntegerField(blank=True, null=True)
    source_of_registration = models.CharField(max_length=200, blank=True, null=True)
    is_disabled = models.IntegerField()
    disabled_reason = models.TextField(blank=True, null=True)
    email_verification_status = models.IntegerField()
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_data_migrated = models.IntegerField(blank=True, null=True)
    is_migration_notified = models.IntegerField(blank=True, null=True)
    user_role_in_company = models.CharField(max_length=200, blank=True, null=True)
    social_login_providers_id = models.IntegerField()
    client_ip = models.CharField(max_length=100, blank=True, null=True)
    is_user_used_app_migrated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'


class UsersBk07082020(models.Model):
    users_id = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=191)
    username = models.CharField(unique=True, max_length=191)
    first_name = models.CharField(max_length=191, blank=True, null=True)
    last_name = models.CharField(max_length=191, blank=True, null=True)
    password = models.CharField(max_length=191, blank=True, null=True)
    permissions = models.TextField(blank=True, null=True)
    is_banned = models.IntegerField(blank=True, null=True)
    ban_reason = models.CharField(max_length=191, blank=True, null=True)
    skip_onboarding = models.IntegerField()
    last_login = models.DateTimeField(blank=True, null=True)
    has_email_verified = models.IntegerField(blank=True, null=True)
    has_mobile_number_verified = models.IntegerField(blank=True, null=True)
    is_journal_entry_created = models.IntegerField()
    my_referral_code = models.CharField(max_length=191, blank=True, null=True)
    api_version = models.CharField(max_length=191, blank=True, null=True)
    source_of_registration = models.CharField(max_length=200, blank=True, null=True)
    is_disabled = models.IntegerField()
    disabled_reason = models.TextField(blank=True, null=True)
    email_verification_status = models.IntegerField()
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_data_migrated = models.IntegerField(blank=True, null=True)
    is_migration_notified = models.IntegerField(blank=True, null=True)
    user_role_in_company = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_bk_07-08-2020'


class UsersExternalMappings(models.Model):
    users_external_mappings_id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveIntegerField()
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    external_source = models.CharField(max_length=191)
    external_sources_id = models.IntegerField(blank=True, null=True)
    external_identifier = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_external_mappings'


class UsersGstReportsClaims(models.Model):
    users_gst_reports_claims_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField(blank=True, null=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    users_id = models.IntegerField(blank=True, null=True)
    company_gstin_user_name = models.CharField(max_length=100, blank=True, null=True)
    company_gstin = models.CharField(max_length=50, blank=True, null=True)
    last_logged_in_at = models.DateTimeField(blank=True, null=True)
    certificate_url = models.TextField(blank=True, null=True)
    is_claimed = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_gst_reports_claims'


class UsersLoginTokens(models.Model):
    users_login_tokens_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    token = models.TextField()
    is_deleted = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_login_tokens'


class V2UsersOpenbookMigrationsTemp(models.Model):
    v2_users_openbook_migrations_temp_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    api_version = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v2_users_openbook_migrations_temp'


class VaDetails(models.Model):
    va_details_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField(blank=True, null=True)
    contacts_id = models.IntegerField()
    is_contact = models.IntegerField()
    va_number = models.CharField(max_length=191)
    va_series = models.CharField(max_length=191)
    partner_banks_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    link_types_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'va_details'


class ValidationMappings(models.Model):
    validation_id = models.PositiveIntegerField(blank=True, null=True)
    source_type = models.CharField(max_length=191, blank=True, null=True)
    source_id = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'validation_mappings'


class Validations(models.Model):
    name = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    validation_path = models.CharField(max_length=191)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'validations'


class VersionMigrations(models.Model):
    version_migrations_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    old_api_version = models.CharField(max_length=191, blank=True, null=True)
    onboarding_statuses_id = models.IntegerField(blank=True, null=True)
    version_migration_date = models.DateTimeField(blank=True, null=True)
    admin_users_id = models.IntegerField(blank=True, null=True)
    open_roles_id = models.IntegerField(blank=True, null=True)
    source_of_migration = models.CharField(max_length=200, blank=True, null=True)
    migrated_to = models.CharField(max_length=200, blank=True, null=True)
    user_subscriptions_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'version_migrations'


class VirtualAccountNumbers(models.Model):
    virtual_account_numbers_id = models.AutoField(primary_key=True)
    partner_banks_id = models.IntegerField()
    company_va = models.CharField(max_length=191)
    beneficiary_va = models.CharField(max_length=191)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'virtual_account_numbers'


class VitalInsurancePlans(models.Model):
    vital_insurance_plan_id = models.AutoField(primary_key=True)
    plan_name = models.CharField(max_length=191)
    price = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vital_insurance_plans'


class VitalInsurances(models.Model):
    vital_insurance_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    vital_insurance_plan_id = models.IntegerField()
    company_name = models.CharField(max_length=191)
    number_of_employees = models.IntegerField()
    contact_person = models.CharField(max_length=191)
    phone_number = models.CharField(max_length=191)
    email = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vital_insurances'


class VpaPayouts(models.Model):
    vpa_payouts_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    bene_vpa = models.CharField(max_length=191)
    recepient_name = models.CharField(max_length=191, blank=True, null=True)
    email_id = models.CharField(max_length=191, blank=True, null=True)
    mobile_number = models.CharField(max_length=191, blank=True, null=True)
    debit_account_number = models.CharField(max_length=191)
    amount = models.CharField(max_length=191)
    merchant_ref_id = models.CharField(unique=True, max_length=191)
    partner_banks_id = models.IntegerField(blank=True, null=True)
    provider = models.CharField(max_length=191, blank=True, null=True)
    is_enterprise = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vpa_payouts'


class WelcomeKitShippings(models.Model):
    welcome_kit_shippings_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    subscription_packages_id = models.IntegerField(blank=True, null=True)
    shipment_mob_num = models.CharField(max_length=191, blank=True, null=True)
    partner_banks_id = models.IntegerField(blank=True, null=True)
    addresses_id = models.IntegerField(blank=True, null=True)
    kit_content = models.CharField(max_length=191, blank=True, null=True)
    shipping_statuses_id = models.IntegerField(blank=True, null=True)
    shipment_tracking_code = models.CharField(max_length=191, blank=True, null=True)
    admin_users_id = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'welcome_kit_shippings'


class WhatsappCallbacks(models.Model):
    whatsapp_callbacks_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    api_name = models.CharField(max_length=200)
    recipient_mobile_number = models.CharField(max_length=191)
    source_mobile_number = models.CharField(max_length=191)
    reply_id = models.CharField(max_length=200)
    msg_id = models.CharField(max_length=200)
    msg_type = models.CharField(max_length=200)
    msg_received_by_gupshup = models.DateTimeField(blank=True, null=True)
    media_url = models.CharField(max_length=191, blank=True, null=True)
    mime_type = models.CharField(max_length=200)
    image_caption = models.CharField(max_length=200)
    text_msg = models.CharField(max_length=200, blank=True, null=True)
    response = models.TextField()
    is_optin = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'whatsapp_callbacks'


class WhatsappTemplates(models.Model):
    whatsapp_templates_id = models.AutoField(primary_key=True)
    template_name = models.CharField(max_length=200)
    template_content = models.TextField()
    template_title = models.CharField(max_length=191, blank=True, null=True)
    is_active = models.IntegerField()
    platform = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'whatsapp_templates'


class WithdrawAccountVerifications(models.Model):
    withdraw_account_verifications_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    withdraw_bank_accounts_id = models.IntegerField()
    amount = models.DecimalField(max_digits=12, decimal_places=4)
    bene_account_number = models.CharField(max_length=200)
    bene_ifsc_code = models.CharField(max_length=100)
    bene_account_verification_sources_id = models.CharField(max_length=200)
    bene_account_verification_response = models.TextField(blank=True, null=True)
    bene_account_verification_bene_name = models.CharField(max_length=200, blank=True, null=True)
    bene_account_verification_ref_no = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'withdraw_account_verifications'


class WithdrawBankAccounts(models.Model):
    withdraw_bank_accounts_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    beneficiary_name = models.CharField(max_length=191, blank=True, null=True)
    mobile_number = models.CharField(max_length=191, blank=True, null=True)
    bank_account_number = models.CharField(max_length=191)
    bank_name = models.CharField(max_length=191)
    branch_name = models.CharField(max_length=191)
    ifsc_code = models.CharField(max_length=191)
    is_account_verified = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    verification_method_source = models.CharField(max_length=200, blank=True, null=True)
    verification_method_source_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_penny_drop_attempted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'withdraw_bank_accounts'


class YesBankBeneficiaries(models.Model):
    yes_bank_beneficiaries_id = models.AutoField(primary_key=True)
    contacts_id = models.IntegerField()
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField(blank=True, null=True)
    bene_account_number = models.CharField(max_length=191)
    bene_ifsc = models.CharField(max_length=191)
    bene_bank_branch = models.CharField(max_length=191)
    bene_name = models.CharField(max_length=191)
    bank_name = models.CharField(max_length=191)
    bene_limit = models.CharField(max_length=255)
    transaction_types_id = models.IntegerField()
    bene_type = models.CharField(max_length=191)
    bene_expiry_date = models.CharField(max_length=191)
    req_ref_number = models.CharField(max_length=191)
    bene_code = models.CharField(max_length=191)
    bene_addition_status = models.CharField(max_length=191)
    action = models.CharField(max_length=191)
    activated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yes_bank_beneficiaries'


class YesBankBranchMasters(models.Model):
    yes_bank_branch_masters_id = models.AutoField(primary_key=True)
    pincode = models.IntegerField()
    state = models.CharField(max_length=191)
    city = models.CharField(max_length=191)
    branch_code = models.CharField(max_length=191)
    branch_name = models.CharField(max_length=191, blank=True, null=True)
    address = models.TextField()
    ifsc = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yes_bank_branch_masters'


class YesBankConnectedAccounts(models.Model):
    yes_bank_connected_accounts_id = models.AutoField(primary_key=True)
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    users_id = models.IntegerField()
    app_id = models.CharField(max_length=191)
    customer_id = models.CharField(max_length=191)
    account_number = models.CharField(max_length=191)
    bank_connection_statuses_id = models.IntegerField()
    br_file_id = models.CharField(max_length=191, blank=True, null=True)
    mc_file_id = models.CharField(max_length=191, blank=True, null=True)
    setup_file_url = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    setup_file_id = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yes_bank_connected_accounts'


class YesBankConnectedBankingFundTransfers(models.Model):
    yes_bank_connected_banking_fund_transfers_id = models.AutoField(primary_key=True)
    companies_id = models.CharField(max_length=191, blank=True, null=True)
    accounts_id = models.CharField(max_length=191, blank=True, null=True)
    users_id = models.CharField(max_length=191, blank=True, null=True)
    bank_app_id = models.CharField(max_length=191, blank=True, null=True)
    bank_customer_id = models.CharField(max_length=191, blank=True, null=True)
    account_number = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    is_otp_verification_successful = models.CharField(max_length=191, blank=True, null=True)
    external_fund_transactions_id = models.CharField(max_length=191, blank=True, null=True)
    external_fund_transfers_id = models.CharField(max_length=191, blank=True, null=True)
    bank_unique_reference_number = models.CharField(max_length=191, blank=True, null=True)
    bank_transaction_status_id = models.CharField(max_length=191, blank=True, null=True)
    bank_request_reference_number = models.CharField(max_length=191, blank=True, null=True)
    bank_attempt_number = models.CharField(max_length=191, blank=True, null=True)
    bank_unique_response_number = models.CharField(max_length=191, blank=True, null=True)
    bank_transfer_type = models.CharField(max_length=191, blank=True, null=True)
    bank_initial_status = models.CharField(max_length=191, blank=True, null=True)
    bank_final_status = models.CharField(max_length=191, blank=True, null=True)
    bank_beneficiary_reference_number = models.CharField(max_length=191, blank=True, null=True)
    bank_error_code = models.CharField(max_length=191, blank=True, null=True)
    bank_error_text = models.CharField(max_length=191, blank=True, null=True)
    bank_currency_code = models.CharField(max_length=191, blank=True, null=True)
    bank_reference_number = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.CharField(max_length=191, blank=True, null=True)
    od_fd_limit_consent = models.IntegerField(blank=True, null=True)
    updated_via = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yes_bank_connected_banking_fund_transfers'


class YesBankConnectedBankingStatements(models.Model):
    yes_bank_connected_banking_statements_id = models.AutoField(primary_key=True)
    validation_reference_number = models.CharField(max_length=191)
    companies_id = models.CharField(max_length=191, blank=True, null=True)
    accounts_id = models.CharField(max_length=191, blank=True, null=True)
    users_id = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    transaction_mode = models.CharField(max_length=10)
    narration = models.TextField(blank=True, null=True)
    balance = models.DecimalField(max_digits=13, decimal_places=2)
    bank_transaction_reference_number = models.CharField(max_length=191, blank=True, null=True)
    bank_transaction_date = models.CharField(max_length=191, blank=True, null=True)
    bank_post_date = models.CharField(max_length=191, blank=True, null=True)
    bank_customer_id = models.CharField(max_length=191, blank=True, null=True)
    bank_account_number = models.CharField(max_length=191, blank=True, null=True)
    bank_customer_name = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yes_bank_connected_banking_statements'


class YesBankConnectedBankingStatuses(models.Model):
    yes_bank_connected_banking_statuses_id = models.AutoField(primary_key=True)
    status_code = models.CharField(max_length=51)
    sub_status_code = models.CharField(max_length=51)
    status = models.CharField(max_length=51)
    bank_transaction_statuses_id = models.IntegerField()
    description = models.CharField(max_length=361)
    reason_for_error = models.CharField(max_length=360)
    recommended_action = models.CharField(max_length=360)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yes_bank_connected_banking_statuses'


class YesBankCreateLeads(models.Model):
    yes_bank_create_leads_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField(blank=True, null=True)
    accounts_id = models.IntegerField(blank=True, null=True)
    companies_id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=191, blank=True, null=True)
    last_name = models.CharField(max_length=191, blank=True, null=True)
    phone_no = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    source_reference_id = models.CharField(max_length=191, blank=True, null=True)
    referral_id = models.CharField(max_length=191, blank=True, null=True)
    offer_code = models.CharField(max_length=191, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=191, blank=True, null=True)
    state = models.CharField(max_length=191, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=191, blank=True, null=True)
    lead_id = models.CharField(max_length=191, blank=True, null=True)
    lead_status_internal = models.CharField(max_length=191, blank=True, null=True)
    lead_status_external = models.CharField(max_length=191, blank=True, null=True)
    lead_status_text = models.CharField(max_length=191, blank=True, null=True)
    error_response = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yes_bank_create_leads'


class YesBankFundTransactionResponses(models.Model):
    yes_bank_fund_transaction_responses_id = models.AutoField(primary_key=True)
    internal_transaction_ref_id = models.IntegerField(blank=True, null=True)
    version = models.CharField(max_length=30, blank=True, null=True)
    uniqueresponseno = models.CharField(db_column='uniqueResponseNo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    attemptno = models.IntegerField(db_column='attemptNo', blank=True, null=True)  # Field name made lowercase.
    transfertype = models.CharField(db_column='transferType', max_length=90, blank=True, null=True)  # Field name made lowercase.
    lowbalancealert = models.CharField(db_column='lowBalanceAlert', max_length=30, blank=True, null=True)  # Field name made lowercase.
    statuscode = models.CharField(db_column='statusCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    substatuscode = models.CharField(db_column='subStatusCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bankreferenceno = models.CharField(db_column='bankReferenceNo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    beneficiaryreferenceno = models.CharField(db_column='beneficiaryReferenceNo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    requestreferenceno = models.CharField(db_column='requestReferenceNo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    reqtransfertype = models.CharField(db_column='reqTransferType', max_length=40, blank=True, null=True)  # Field name made lowercase.
    transactiondate = models.CharField(db_column='transactionDate', max_length=60, blank=True, null=True)  # Field name made lowercase.
    transferamount = models.CharField(db_column='transferAmount', max_length=60, blank=True, null=True)  # Field name made lowercase.
    transfercurrencycode = models.CharField(db_column='transferCurrencyCode', max_length=40, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yes_bank_fund_transaction_responses'


class YesBankFundTransfers(models.Model):
    yes_bank_fund_transfers_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField(blank=True, null=True)
    contacts_id = models.IntegerField()
    app_id = models.IntegerField()
    purpose_code = models.CharField(max_length=191)
    unique_request_no = models.CharField(max_length=191)
    transfer_type = models.CharField(max_length=191)
    transfer_currency_code = models.CharField(max_length=191)
    remitter_beneficiary_info = models.CharField(max_length=255)
    unique_response_no = models.CharField(max_length=191)
    attempt_no = models.IntegerField()
    transaction_amount = models.CharField(max_length=191)
    low_balance_alert = models.CharField(max_length=191)
    transaction_status_code = models.CharField(max_length=191)
    sub_status_code = models.CharField(max_length=191)
    bank_reference_no = models.CharField(max_length=191)
    bene_reference_no = models.CharField(max_length=191)
    bene_code = models.CharField(max_length=191, blank=True, null=True)
    name_with_beneficiary_bank = models.CharField(max_length=191)
    request_reference_no = models.CharField(max_length=191)
    source_type = models.CharField(max_length=191)
    source_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yes_bank_fund_transfers'


class YesBankMandateDebitFileDetails(models.Model):
    yes_bank_mandate_debit_file_details_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    lan_no = models.CharField(max_length=191)
    umrn = models.CharField(max_length=191)
    amount = models.CharField(max_length=191)
    settlement_date = models.CharField(max_length=191)
    user_number = models.CharField(max_length=191)
    mandate_id = models.CharField(max_length=191)
    debit_filename = models.CharField(max_length=191)
    debit_filename_index = models.CharField(max_length=191)
    item_type = models.CharField(max_length=191)
    item_reference = models.CharField(max_length=191)
    item_sequence_no = models.CharField(max_length=191)
    status = models.CharField(max_length=191)
    clearing_status = models.CharField(max_length=191)
    value_date = models.CharField(max_length=191)
    sender = models.CharField(max_length=191)
    receiver = models.CharField(max_length=191)
    reason_code = models.CharField(max_length=191)
    currency = models.CharField(max_length=191)
    receiver_account = models.CharField(max_length=191)
    name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yes_bank_mandate_debit_file_details'


class YesBankMandateResponseDetails(models.Model):
    yes_bank_mandate_response_details_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    digio_e_nach_details_id = models.IntegerField()
    mandate_date = models.DateField()
    mandate_id = models.CharField(max_length=191)
    umrn = models.CharField(max_length=191, blank=True, null=True)
    cust_ref_no = models.CharField(max_length=191, blank=True, null=True)
    sch_ref_no = models.CharField(max_length=191, blank=True, null=True)
    cust_name = models.CharField(max_length=191, blank=True, null=True)
    bank = models.CharField(max_length=191, blank=True, null=True)
    branch = models.CharField(max_length=191, blank=True, null=True)
    bank_code = models.CharField(max_length=191, blank=True, null=True)
    ac_type = models.CharField(max_length=191, blank=True, null=True)
    ac_no = models.CharField(max_length=191, blank=True, null=True)
    amount = models.CharField(max_length=191, blank=True, null=True)
    frequency = models.CharField(max_length=191, blank=True, null=True)
    debit_type = models.CharField(max_length=191, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    until_cancel = models.CharField(max_length=10, blank=True, null=True)
    tel_no = models.CharField(max_length=100, blank=True, null=True)
    mobile_no = models.CharField(max_length=100, blank=True, null=True)
    mail_id = models.CharField(max_length=100, blank=True, null=True)
    upload_date = models.CharField(max_length=100, blank=True, null=True)
    response_date = models.DateField(blank=True, null=True)
    utility_code = models.CharField(max_length=191, blank=True, null=True)
    utility_name = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    status_code = models.CharField(max_length=191, blank=True, null=True)
    reason = models.CharField(max_length=191, blank=True, null=True)
    aadhaar_number = models.CharField(max_length=191, blank=True, null=True)
    file_name = models.CharField(max_length=191)
    last_debit_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yes_bank_mandate_response_details'


class YesBankNodalStatementHistories(models.Model):
    yes_bank_nodal_statement_histories_id = models.AutoField(primary_key=True)
    customer_code = models.CharField(max_length=191)
    bene_account_no = models.CharField(max_length=191)
    bene_account_ifsc = models.CharField(max_length=191)
    bene_full_name = models.CharField(max_length=191, blank=True, null=True)
    transfer_type = models.CharField(max_length=191)
    transfer_unique_no = models.CharField(max_length=191)
    transfer_timestamp = models.CharField(max_length=191)
    transfer_ccy = models.CharField(max_length=191)
    transfer_amt = models.DecimalField(max_digits=10, decimal_places=2)
    rmtr_account_no = models.CharField(max_length=191)
    rmtr_account_ifsc = models.CharField(max_length=191)
    rmtr_account_type = models.CharField(max_length=191, blank=True, null=True)
    rmtr_full_name = models.CharField(max_length=191)
    rmtr_address = models.CharField(max_length=191, blank=True, null=True)
    attempt_no = models.IntegerField(blank=True, null=True)
    rmtr_to_bene_note = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    credit_acct_no = models.CharField(max_length=191, blank=True, null=True)
    credited_at = models.CharField(max_length=191, blank=True, null=True)
    returned_at = models.CharField(max_length=191, blank=True, null=True)
    setting1 = models.CharField(max_length=191, blank=True, null=True)
    setting2 = models.CharField(max_length=191, blank=True, null=True)
    setting3 = models.CharField(max_length=191, blank=True, null=True)
    setting4 = models.CharField(max_length=191, blank=True, null=True)
    setting5 = models.CharField(max_length=191, blank=True, null=True)
    validate_response = models.CharField(max_length=191)
    notify_response = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yes_bank_nodal_statement_histories'


class YesBankNodalStatements(models.Model):
    yes_bank_nodal_statements_id = models.AutoField(primary_key=True)
    customer_code = models.CharField(max_length=191)
    bene_account_no = models.CharField(max_length=191)
    bene_account_ifsc = models.CharField(max_length=191)
    bene_full_name = models.CharField(max_length=191, blank=True, null=True)
    transfer_type = models.CharField(max_length=191)
    transfer_unique_no = models.CharField(max_length=191)
    transfer_timestamp = models.CharField(max_length=191)
    transfer_ccy = models.CharField(max_length=191)
    transfer_amt = models.DecimalField(max_digits=10, decimal_places=2)
    rmtr_account_no = models.CharField(max_length=191)
    rmtr_account_ifsc = models.CharField(max_length=191)
    rmtr_account_type = models.CharField(max_length=191, blank=True, null=True)
    rmtr_full_name = models.CharField(max_length=191)
    rmtr_address = models.CharField(max_length=191, blank=True, null=True)
    attempt_no = models.IntegerField(blank=True, null=True)
    rmtr_to_bene_note = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    credit_acct_no = models.CharField(max_length=191, blank=True, null=True)
    credited_at = models.CharField(max_length=191, blank=True, null=True)
    returned_at = models.CharField(max_length=191, blank=True, null=True)
    setting1 = models.CharField(max_length=191, blank=True, null=True)
    setting2 = models.CharField(max_length=191, blank=True, null=True)
    setting3 = models.CharField(max_length=191, blank=True, null=True)
    setting4 = models.CharField(max_length=191, blank=True, null=True)
    setting5 = models.CharField(max_length=191, blank=True, null=True)
    notify_response = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yes_bank_nodal_statements'


class YesBankUpiPayouts(models.Model):
    yes_bank_upi_payouts_id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    companies_id = models.IntegerField()
    accounts_id = models.IntegerField()
    external_fund_transactions_id = models.IntegerField()
    internal_transaction_ref_id = models.CharField(max_length=191)
    bank_transaction_ref_id = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    bank_status = models.IntegerField(blank=True, null=True)
    bank_status_description = models.CharField(max_length=191, blank=True, null=True)
    bank_response_code = models.CharField(max_length=191, blank=True, null=True)
    bank_approval_number = models.CharField(max_length=191, blank=True, null=True)
    payer_vpa = models.CharField(max_length=191, blank=True, null=True)
    npci_transaction_id = models.CharField(max_length=191, blank=True, null=True)
    customer_reference_id = models.CharField(max_length=191, blank=True, null=True)
    payer_account_number = models.CharField(max_length=191, blank=True, null=True)
    payer_ifsc = models.CharField(max_length=191, blank=True, null=True)
    payer_account_name = models.CharField(max_length=191, blank=True, null=True)
    bank_error_code = models.CharField(max_length=191, blank=True, null=True)
    bank_response_error_code = models.CharField(max_length=191, blank=True, null=True)
    error_description = models.CharField(max_length=191, blank=True, null=True)
    response_description = models.CharField(max_length=191, blank=True, null=True)
    transfer_type = models.CharField(max_length=191, blank=True, null=True)
    payee_vpa = models.CharField(max_length=191, blank=True, null=True)
    payee_ifsc = models.CharField(max_length=191, blank=True, null=True)
    payee_account_number = models.CharField(max_length=191, blank=True, null=True)
    payee_account_aadhaar = models.CharField(max_length=191, blank=True, null=True)
    payee_account_name = models.CharField(max_length=191, blank=True, null=True)
    updated_via = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yes_bank_upi_payouts'


class YesBankVpas(models.Model):
    yesbank_vpas_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    vpa_series = models.CharField(unique=True, max_length=100)
    vpa = models.CharField(unique=True, max_length=100)
    sub_merchant_id = models.CharField(max_length=191, blank=True, null=True)
    url = models.CharField(max_length=191, blank=True, null=True)
    qr_sticker_url = models.CharField(max_length=191, blank=True, null=True)
    is_contact_vpa = models.IntegerField()
    contacts_id = models.IntegerField(blank=True, null=True)
    link_types_id = models.IntegerField(blank=True, null=True)
    is_enterprise = models.IntegerField()
    description = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yes_bank_vpas'


class YesbankConnectedLeadStatusHistories(models.Model):
    yesbank_connected_lead_status_histories_id = models.AutoField(primary_key=True)
    yes_bank_create_leads_id = models.IntegerField(blank=True, null=True)
    lead_status_internal = models.CharField(max_length=191, blank=True, null=True)
    lead_status_external = models.CharField(max_length=191, blank=True, null=True)
    lead_status_text = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yesbank_connected_lead_status_histories'


class YodleeAccountTransactions(models.Model):
    yodlee_account_transactions_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    container = models.CharField(db_column='CONTAINER', max_length=191, blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=191, blank=True, null=True)
    subtype = models.CharField(db_column='subType', max_length=191, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=191, blank=True, null=True)
    basetype = models.CharField(db_column='baseType', max_length=191, blank=True, null=True)  # Field name made lowercase.
    categorytype = models.CharField(db_column='categoryType', max_length=191, blank=True, null=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='categoryId', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=191, blank=True, null=True)
    categorysource = models.CharField(db_column='categorySource', max_length=191, blank=True, null=True)  # Field name made lowercase.
    highlevelcategoryid = models.IntegerField(db_column='highLevelCategoryId', blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='createdDate', max_length=191, blank=True, null=True)  # Field name made lowercase.
    lastupdated = models.CharField(db_column='lastUpdated', max_length=191, blank=True, null=True)  # Field name made lowercase.
    description_original = models.CharField(max_length=191, blank=True, null=True)
    description_simple = models.CharField(max_length=191, blank=True, null=True)
    date = models.CharField(max_length=191, blank=True, null=True)
    postdate = models.CharField(db_column='postDate', max_length=191, blank=True, null=True)  # Field name made lowercase.
    ismanual = models.CharField(db_column='isManual', max_length=191, blank=True, null=True)  # Field name made lowercase.
    sourcetype = models.CharField(db_column='sourceType', max_length=191, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=191, blank=True, null=True)
    accountid = models.IntegerField(db_column='accountId', blank=True, null=True)  # Field name made lowercase.
    balance_amount = models.CharField(max_length=191, blank=True, null=True)
    balance_currency = models.CharField(max_length=191, blank=True, null=True)
    checknumber = models.CharField(db_column='checkNumber', max_length=191, blank=True, null=True)  # Field name made lowercase.
    merchant_id = models.CharField(max_length=191, blank=True, null=True)
    merchant_name = models.CharField(max_length=191, blank=True, null=True)
    merchant_source = models.CharField(max_length=191, blank=True, null=True)
    merchant_categorylabel = models.CharField(db_column='merchant_categoryLabel', max_length=191, blank=True, null=True)  # Field name made lowercase.
    merchant_coordinates_latitude = models.CharField(max_length=191, blank=True, null=True)
    merchant_coordinates_longitude = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yodlee_account_transactions'


class YodleeConnectedAccountDetails(models.Model):
    yodlee_connected_account_details_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    accountname = models.CharField(db_column='accountName', max_length=191, blank=True, null=True)  # Field name made lowercase.
    currentbalance_amount = models.DecimalField(db_column='currentBalance_amount', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    currentbalance_currency = models.CharField(db_column='currentBalance_currency', max_length=191, blank=True, null=True)  # Field name made lowercase.
    accounttype = models.CharField(db_column='accountType', max_length=191, blank=True, null=True)  # Field name made lowercase.
    displayedname = models.CharField(db_column='displayedName', max_length=191, blank=True, null=True)  # Field name made lowercase.
    accountnumber = models.CharField(db_column='accountNumber', max_length=191, blank=True, null=True)  # Field name made lowercase.
    availablebalance_amount = models.DecimalField(db_column='availableBalance_amount', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    availablebalance_currency = models.CharField(db_column='availableBalance_currency', max_length=191, blank=True, null=True)  # Field name made lowercase.
    accountstatus = models.CharField(db_column='accountStatus', max_length=191, blank=True, null=True)  # Field name made lowercase.
    lastupdated = models.CharField(db_column='lastUpdated', max_length=191, blank=True, null=True)  # Field name made lowercase.
    isasset = models.IntegerField(db_column='isAsset', blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='createdDate', max_length=191, blank=True, null=True)  # Field name made lowercase.
    aggregationsource = models.CharField(db_column='aggregationSource', max_length=191, blank=True, null=True)  # Field name made lowercase.
    balance_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    balance_currency = models.CharField(max_length=191, blank=True, null=True)
    overdraftlimit_amount = models.DecimalField(db_column='overDraftLimit_amount', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    overdraftlimit_currency = models.CharField(db_column='overDraftLimit_currency', max_length=191, blank=True, null=True)  # Field name made lowercase.
    providerid = models.IntegerField(db_column='providerId', blank=True, null=True)  # Field name made lowercase.
    provideraccountid = models.IntegerField(db_column='providerAccountId', blank=True, null=True)  # Field name made lowercase.
    container = models.CharField(db_column='CONTAINER', max_length=191, blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(blank=True, null=True)
    userclassification = models.CharField(db_column='userClassification', max_length=191, blank=True, null=True)  # Field name made lowercase.
    providername = models.CharField(db_column='providerName', max_length=191, blank=True, null=True)  # Field name made lowercase.
    banktransfercode = models.CharField(db_column='bankTransferCode', max_length=191, blank=True, null=True)  # Field name made lowercase.
    dataset = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yodlee_connected_account_details'


class YodleeUsers(models.Model):
    yodlee_users_id = models.AutoField(primary_key=True)
    accounts_id = models.IntegerField()
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    loginname = models.CharField(db_column='loginName', max_length=191)  # Field name made lowercase.
    email = models.CharField(max_length=191)
    currency = models.CharField(max_length=50)
    timezone = models.CharField(db_column='timeZone', max_length=191)  # Field name made lowercase.
    yodlee_user_id = models.IntegerField()
    roletype = models.CharField(db_column='roleType', max_length=191)  # Field name made lowercase.
    usersession = models.CharField(db_column='userSession', max_length=191)  # Field name made lowercase.
    usersession_created_at = models.DateTimeField(db_column='userSession_created_at')  # Field name made lowercase.
    user_access_token = models.CharField(max_length=191)
    user_access_token_created_at = models.DateTimeField()
    dateformat = models.CharField(db_column='dateFormat', max_length=191)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yodlee_users'


class ZeroBounceEmailLogs(models.Model):
    zero_bounce_email_logs_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=191)
    zero_bounce_response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zero_bounce_email_logs'


class ZpayPayroll(models.Model):
    companies_id = models.IntegerField()
    users_id = models.IntegerField()
    emps_01 = models.DecimalField(max_digits=23, decimal_places=0, blank=True, null=True)
    emps_02 = models.DecimalField(max_digits=23, decimal_places=0, blank=True, null=True)
    emps_03 = models.DecimalField(max_digits=23, decimal_places=0, blank=True, null=True)
    emps_04 = models.DecimalField(max_digits=23, decimal_places=0, blank=True, null=True)
    emps_05 = models.DecimalField(max_digits=23, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zpay_payroll'
