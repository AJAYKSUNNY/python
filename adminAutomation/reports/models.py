from django.db import models

# Create your models here.

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
        managed = True
        db_table = 'users'