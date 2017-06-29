# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AdminLog(models.Model):
    user_id = models.SmallIntegerField(blank=True, null=True)
    action = models.CharField(max_length=100, blank=True, null=True)
    client_ip = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_log'


class AdminMenu(models.Model):
    menu_id = models.SmallIntegerField(primary_key=True)
    menu_title = models.CharField(max_length=30)
    menu_level = models.IntegerField()
    parent_id = models.IntegerField()
    menu_url = models.CharField(max_length=255, blank=True, null=True)
    menu_icon = models.CharField(max_length=50, blank=True, null=True)
    system = models.IntegerField()
    status = models.IntegerField()
    display_order = models.SmallIntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'admin_menu'


class AdminPrivilege(models.Model):
    privilege_id = models.SmallIntegerField(primary_key=True)
    privilege_title = models.CharField(max_length=30, blank=True, null=True)
    menu_id = models.SmallIntegerField(blank=True, null=True)
    action = models.CharField(max_length=100, blank=True, null=True)
    display_order = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'admin_privilege'


class AdminRole(models.Model):
    role_id = models.SmallIntegerField(primary_key=True)
    role_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'admin_role'


class AdminRolePrivilege(models.Model):
    role_id = models.SmallIntegerField()
    privilege_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'admin_role_privilege'
        unique_together = (('role_id', 'privilege_id'),)


class AdminUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    realname = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    login_count = models.IntegerField(blank=True, null=True)
    last_login_ip = models.CharField(max_length=100, blank=True, null=True)
    last_login_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_user'


class AdminUserRole(models.Model):
    user_id = models.IntegerField()
    role_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'admin_user_role'
        unique_together = (('user_id', 'role_id'),)


class Alarm(models.Model):
    server_id = models.SmallIntegerField()
    tags = models.CharField(max_length=50, blank=True, null=True)
    host = models.CharField(max_length=30, blank=True, null=True)
    port = models.CharField(max_length=10, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    db_type = models.CharField(max_length=30, blank=True, null=True)
    alarm_item = models.CharField(max_length=50, blank=True, null=True)
    alarm_value = models.CharField(max_length=50, blank=True, null=True)
    level = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    send_mail = models.IntegerField(blank=True, null=True)
    send_mail_to_list = models.CharField(max_length=255, blank=True, null=True)
    send_sms = models.IntegerField(blank=True, null=True)
    send_sms_to_list = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alarm'


class AlarmHistory(models.Model):
    server_id = models.SmallIntegerField()
    tags = models.CharField(max_length=50, blank=True, null=True)
    host = models.CharField(max_length=30, blank=True, null=True)
    port = models.CharField(max_length=10, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    db_type = models.CharField(max_length=30, blank=True, null=True)
    alarm_item = models.CharField(max_length=50, blank=True, null=True)
    alarm_value = models.CharField(max_length=50, blank=True, null=True)
    level = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    send_mail = models.IntegerField(blank=True, null=True)
    send_mail_to_list = models.CharField(max_length=255, blank=True, null=True)
    send_sms = models.IntegerField(blank=True, null=True)
    send_sms_to_list = models.CharField(max_length=255, blank=True, null=True)
    send_mail_status = models.IntegerField()
    send_sms_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alarm_history'


class AlarmTemp(models.Model):
    server_id = models.SmallIntegerField()
    ip = models.CharField(max_length=50, blank=True, null=True)
    db_type = models.CharField(max_length=30, blank=True, null=True)
    alarm_item = models.CharField(max_length=50, blank=True, null=True)
    alarm_type = models.CharField(max_length=30, blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'alarm_temp'


class DbServersMongodb(models.Model):
    host = models.CharField(max_length=30)
    port = models.CharField(max_length=10)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    tags = models.CharField(max_length=50, blank=True, null=True)
    monitor = models.IntegerField(blank=True, null=True)
    send_mail = models.IntegerField(blank=True, null=True)
    send_mail_to_list = models.CharField(max_length=255, blank=True, null=True)
    send_sms = models.IntegerField(blank=True, null=True)
    send_sms_to_list = models.CharField(max_length=255, blank=True, null=True)
    alarm_connections_current = models.IntegerField()
    alarm_active_clients = models.IntegerField()
    alarm_current_queue = models.IntegerField()
    threshold_warning_connections_current = models.IntegerField()
    threshold_warning_active_clients = models.SmallIntegerField()
    threshold_warning_current_queue = models.SmallIntegerField()
    threshold_critical_connections_current = models.IntegerField()
    threshold_critical_active_clients = models.SmallIntegerField()
    threshold_critical_current_queue = models.SmallIntegerField()
    is_delete = models.IntegerField()
    display_order = models.SmallIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_servers_mongodb'


class DbServersMysql(models.Model):
    host = models.CharField(max_length=30)
    port = models.CharField(max_length=10)
    username = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    tags = models.CharField(max_length=50, blank=True, null=True)
    monitor = models.IntegerField(blank=True, null=True)
    send_mail = models.IntegerField(blank=True, null=True)
    send_mail_to_list = models.CharField(max_length=255, blank=True, null=True)
    send_sms = models.IntegerField(blank=True, null=True)
    send_sms_to_list = models.CharField(max_length=255, blank=True, null=True)
    send_slowquery_to_list = models.CharField(max_length=255, blank=True, null=True)
    alarm_threads_connected = models.IntegerField(blank=True, null=True)
    alarm_threads_running = models.IntegerField(blank=True, null=True)
    alarm_threads_waits = models.IntegerField(blank=True, null=True)
    alarm_repl_status = models.IntegerField(blank=True, null=True)
    alarm_repl_delay = models.IntegerField(blank=True, null=True)
    threshold_warning_threads_connected = models.IntegerField(blank=True, null=True)
    threshold_warning_threads_running = models.IntegerField(blank=True, null=True)
    threshold_warning_threads_waits = models.IntegerField(blank=True, null=True)
    threshold_warning_repl_delay = models.IntegerField(blank=True, null=True)
    threshold_critical_threads_connected = models.IntegerField(blank=True, null=True)
    threshold_critical_threads_running = models.IntegerField(blank=True, null=True)
    threshold_critical_threads_waits = models.IntegerField(blank=True, null=True)
    threshold_critical_repl_delay = models.IntegerField(blank=True, null=True)
    slow_query = models.IntegerField()
    binlog_auto_purge = models.IntegerField()
    binlog_store_days = models.SmallIntegerField()
    bigtable_monitor = models.IntegerField()
    bigtable_size = models.IntegerField()
    is_delete = models.IntegerField()
    display_order = models.SmallIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_servers_mysql'


class DbServersOracle(models.Model):
    host = models.CharField(max_length=30, blank=True, null=True)
    port = models.CharField(max_length=10, blank=True, null=True)
    dsn = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    tags = models.CharField(max_length=100, blank=True, null=True)
    monitor = models.IntegerField(blank=True, null=True)
    send_mail = models.IntegerField(blank=True, null=True)
    send_mail_to_list = models.CharField(max_length=255, blank=True, null=True)
    send_sms = models.IntegerField(blank=True, null=True)
    send_sms_to_list = models.CharField(max_length=255, blank=True, null=True)
    alarm_session_total = models.IntegerField()
    alarm_session_actives = models.IntegerField()
    alarm_session_waits = models.IntegerField()
    alarm_tablespace = models.IntegerField()
    threshold_warning_session_total = models.SmallIntegerField()
    threshold_warning_session_actives = models.SmallIntegerField()
    threshold_warning_session_waits = models.IntegerField()
    threshold_warning_tablespace = models.SmallIntegerField()
    threshold_critical_session_total = models.SmallIntegerField()
    threshold_critical_session_actives = models.SmallIntegerField()
    threshold_critical_session_waits = models.SmallIntegerField()
    threshold_critical_tablespace = models.SmallIntegerField()
    is_delete = models.IntegerField()
    display_order = models.SmallIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_servers_oracle'


class DbServersOs(models.Model):
    host = models.CharField(max_length=30, blank=True, null=True)
    community = models.CharField(max_length=50, blank=True, null=True)
    tags = models.CharField(max_length=30, blank=True, null=True)
    monitor = models.IntegerField(blank=True, null=True)
    send_mail = models.IntegerField(blank=True, null=True)
    send_mail_to_list = models.CharField(max_length=255, blank=True, null=True)
    send_sms = models.IntegerField(blank=True, null=True)
    send_sms_to_list = models.CharField(max_length=255, blank=True, null=True)
    alarm_os_process = models.IntegerField()
    alarm_os_load = models.IntegerField()
    alarm_os_cpu = models.IntegerField()
    alarm_os_network = models.IntegerField()
    alarm_os_disk = models.IntegerField()
    alarm_os_memory = models.IntegerField()
    threshold_warning_os_process = models.IntegerField()
    threshold_warning_os_load = models.IntegerField()
    threshold_warning_os_cpu = models.IntegerField()
    threshold_warning_os_network = models.IntegerField()
    threshold_warning_os_disk = models.IntegerField()
    threshold_warning_os_memory = models.IntegerField()
    threshold_critical_os_process = models.IntegerField()
    threshold_critical_os_load = models.IntegerField()
    threshold_critical_os_cpu = models.IntegerField()
    threshold_critical_os_network = models.IntegerField()
    threshold_critical_os_disk = models.IntegerField()
    threshold_critical_os_memory = models.IntegerField()
    filter_os_disk = models.CharField(max_length=100, blank=True, null=True)
    is_delete = models.IntegerField()
    display_order = models.SmallIntegerField()
    remark = models.CharField(max_length=1000, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_servers_os'


class DbServersRedis(models.Model):
    host = models.CharField(max_length=30)
    port = models.CharField(max_length=10)
    password = models.CharField(max_length=50, blank=True, null=True)
    tags = models.CharField(max_length=50, blank=True, null=True)
    monitor = models.IntegerField(blank=True, null=True)
    send_mail = models.IntegerField(blank=True, null=True)
    send_mail_to_list = models.CharField(max_length=255, blank=True, null=True)
    send_sms = models.IntegerField(blank=True, null=True)
    send_sms_to_list = models.CharField(max_length=255, blank=True, null=True)
    alarm_connected_clients = models.IntegerField()
    alarm_command_processed = models.IntegerField()
    alarm_blocked_clients = models.IntegerField()
    threshold_warning_connected_clients = models.SmallIntegerField()
    threshold_warning_command_processed = models.SmallIntegerField()
    threshold_warning_blocked_clients = models.SmallIntegerField()
    threshold_critical_connected_clients = models.SmallIntegerField()
    threshold_critical_command_processed = models.SmallIntegerField()
    threshold_critical_blocked_clients = models.SmallIntegerField()
    is_delete = models.IntegerField()
    display_order = models.SmallIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_servers_redis'


class DbStatus(models.Model):
    server_id = models.SmallIntegerField()
    host = models.CharField(max_length=30)
    port = models.CharField(max_length=10)
    db_type = models.CharField(max_length=10)
    db_type_sort = models.IntegerField()
    tags = models.CharField(max_length=50)
    role = models.CharField(max_length=30)
    version = models.CharField(max_length=30)
    connect = models.IntegerField()
    connect_tips = models.CharField(max_length=500)
    sessions = models.IntegerField()
    sessions_tips = models.CharField(max_length=500)
    actives = models.IntegerField()
    actives_tips = models.CharField(max_length=500)
    waits = models.IntegerField()
    waits_tips = models.CharField(max_length=500)
    repl = models.IntegerField()
    repl_tips = models.CharField(max_length=500)
    repl_delay = models.IntegerField()
    repl_delay_tips = models.CharField(max_length=500)
    tablespace = models.IntegerField()
    tablespace_tips = models.CharField(max_length=500)
    snmp = models.IntegerField()
    snmp_tips = models.CharField(max_length=500)
    process = models.IntegerField()
    process_tips = models.CharField(max_length=500)
    load_1 = models.IntegerField()
    load_1_tips = models.CharField(max_length=500)
    cpu = models.IntegerField()
    cpu_tips = models.CharField(max_length=500)
    network = models.IntegerField()
    network_tips = models.CharField(max_length=500)
    memory = models.IntegerField()
    memory_tips = models.CharField(max_length=500)
    disk = models.IntegerField()
    disk_tips = models.CharField(max_length=500)
    uptime_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'db_status'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class LepusStatus(models.Model):
    lepus_variables = models.CharField(max_length=255)
    lepus_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'lepus_status'


class MongodbStatus(models.Model):
    server_id = models.SmallIntegerField()
    host = models.CharField(max_length=50)
    port = models.CharField(max_length=30)
    tags = models.CharField(max_length=50, blank=True, null=True)
    connect = models.SmallIntegerField()
    replset = models.SmallIntegerField()
    repl_role = models.CharField(max_length=30)
    ok = models.IntegerField()
    uptime = models.IntegerField()
    version = models.CharField(max_length=50)
    connections_current = models.IntegerField()
    connections_available = models.IntegerField()
    globallock_currentqueue = models.SmallIntegerField(db_column='globalLock_currentQueue')  # Field name made lowercase.
    globallock_activeclients = models.SmallIntegerField(db_column='globalLock_activeClients')  # Field name made lowercase.
    indexcounters_accesses = models.BigIntegerField(db_column='indexCounters_accesses')  # Field name made lowercase.
    indexcounters_hits = models.BigIntegerField(db_column='indexCounters_hits')  # Field name made lowercase.
    indexcounters_misses = models.BigIntegerField(db_column='indexCounters_misses')  # Field name made lowercase.
    indexcounters_resets = models.IntegerField(db_column='indexCounters_resets')  # Field name made lowercase.
    indexcounters_missratio = models.CharField(db_column='indexCounters_missRatio', max_length=10)  # Field name made lowercase.
    cursors_totalopen = models.SmallIntegerField(db_column='cursors_totalOpen')  # Field name made lowercase.
    cursors_timeout = models.IntegerField(db_column='cursors_timeOut')  # Field name made lowercase.
    dur_commits = models.SmallIntegerField()
    dur_journaledmb = models.CharField(db_column='dur_journaledMB', max_length=30)  # Field name made lowercase.
    dur_writetodatafilesmb = models.CharField(db_column='dur_writeToDataFilesMB', max_length=30)  # Field name made lowercase.
    dur_compression = models.CharField(max_length=30)
    dur_commitsinwritelock = models.SmallIntegerField(db_column='dur_commitsInWriteLock')  # Field name made lowercase.
    dur_earlycommits = models.SmallIntegerField(db_column='dur_earlyCommits')  # Field name made lowercase.
    dur_timems_dt = models.SmallIntegerField(db_column='dur_timeMs_dt')  # Field name made lowercase.
    dur_timems_preplogbuffer = models.SmallIntegerField(db_column='dur_timeMs_prepLogBuffer')  # Field name made lowercase.
    dur_timems_writetojournal = models.SmallIntegerField(db_column='dur_timeMs_writeToJournal')  # Field name made lowercase.
    dur_timems_writetodatafiles = models.SmallIntegerField(db_column='dur_timeMs_writeToDataFiles')  # Field name made lowercase.
    dur_timems_remapprivateview = models.SmallIntegerField(db_column='dur_timeMs_remapPrivateView')  # Field name made lowercase.
    mem_bits = models.SmallIntegerField()
    mem_resident = models.IntegerField()
    mem_virtual = models.IntegerField()
    mem_supported = models.CharField(max_length=10)
    mem_mapped = models.IntegerField()
    mem_mappedwithjournal = models.IntegerField(db_column='mem_mappedWithJournal')  # Field name made lowercase.
    network_bytesin_persecond = models.IntegerField(db_column='network_bytesIn_persecond')  # Field name made lowercase.
    network_bytesout_persecond = models.IntegerField(db_column='network_bytesOut_persecond')  # Field name made lowercase.
    network_numrequests_persecond = models.IntegerField(db_column='network_numRequests_persecond')  # Field name made lowercase.
    opcounters_insert_persecond = models.SmallIntegerField()
    opcounters_query_persecond = models.SmallIntegerField()
    opcounters_update_persecond = models.SmallIntegerField()
    opcounters_delete_persecond = models.SmallIntegerField()
    opcounters_command_persecond = models.SmallIntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mongodb_status'


class MongodbStatusHistory(models.Model):
    server_id = models.SmallIntegerField()
    host = models.CharField(max_length=50)
    port = models.CharField(max_length=30)
    tags = models.CharField(max_length=50, blank=True, null=True)
    connect = models.SmallIntegerField()
    replset = models.IntegerField()
    repl_role = models.CharField(max_length=30)
    ok = models.IntegerField()
    uptime = models.IntegerField()
    version = models.CharField(max_length=50)
    connections_current = models.IntegerField()
    connections_available = models.IntegerField()
    globallock_currentqueue = models.SmallIntegerField(db_column='globalLock_currentQueue')  # Field name made lowercase.
    globallock_activeclients = models.SmallIntegerField(db_column='globalLock_activeClients')  # Field name made lowercase.
    indexcounters_accesses = models.BigIntegerField(db_column='indexCounters_accesses')  # Field name made lowercase.
    indexcounters_hits = models.BigIntegerField(db_column='indexCounters_hits')  # Field name made lowercase.
    indexcounters_misses = models.BigIntegerField(db_column='indexCounters_misses')  # Field name made lowercase.
    indexcounters_resets = models.IntegerField(db_column='indexCounters_resets')  # Field name made lowercase.
    indexcounters_missratio = models.CharField(db_column='indexCounters_missRatio', max_length=10)  # Field name made lowercase.
    cursors_totalopen = models.SmallIntegerField(db_column='cursors_totalOpen')  # Field name made lowercase.
    cursors_timeout = models.IntegerField(db_column='cursors_timeOut')  # Field name made lowercase.
    dur_commits = models.SmallIntegerField()
    dur_journaledmb = models.CharField(db_column='dur_journaledMB', max_length=30)  # Field name made lowercase.
    dur_writetodatafilesmb = models.CharField(db_column='dur_writeToDataFilesMB', max_length=30)  # Field name made lowercase.
    dur_compression = models.CharField(max_length=30)
    dur_commitsinwritelock = models.SmallIntegerField(db_column='dur_commitsInWriteLock')  # Field name made lowercase.
    dur_earlycommits = models.SmallIntegerField(db_column='dur_earlyCommits')  # Field name made lowercase.
    dur_timems_dt = models.SmallIntegerField(db_column='dur_timeMs_dt')  # Field name made lowercase.
    dur_timems_preplogbuffer = models.SmallIntegerField(db_column='dur_timeMs_prepLogBuffer')  # Field name made lowercase.
    dur_timems_writetojournal = models.SmallIntegerField(db_column='dur_timeMs_writeToJournal')  # Field name made lowercase.
    dur_timems_writetodatafiles = models.SmallIntegerField(db_column='dur_timeMs_writeToDataFiles')  # Field name made lowercase.
    dur_timems_remapprivateview = models.SmallIntegerField(db_column='dur_timeMs_remapPrivateView')  # Field name made lowercase.
    mem_bits = models.SmallIntegerField()
    mem_resident = models.IntegerField()
    mem_virtual = models.IntegerField()
    mem_supported = models.CharField(max_length=10)
    mem_mapped = models.IntegerField()
    mem_mappedwithjournal = models.IntegerField(db_column='mem_mappedWithJournal')  # Field name made lowercase.
    network_bytesin_persecond = models.IntegerField(db_column='network_bytesIn_persecond')  # Field name made lowercase.
    network_bytesout_persecond = models.IntegerField(db_column='network_bytesOut_persecond')  # Field name made lowercase.
    network_numrequests_persecond = models.IntegerField(db_column='network_numRequests_persecond')  # Field name made lowercase.
    opcounters_insert_persecond = models.SmallIntegerField()
    opcounters_query_persecond = models.SmallIntegerField()
    opcounters_update_persecond = models.SmallIntegerField()
    opcounters_delete_persecond = models.SmallIntegerField()
    opcounters_command_persecond = models.SmallIntegerField()
    create_time = models.DateTimeField()
    ymdhi = models.BigIntegerField(db_column='YmdHi')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mongodb_status_history'


class MysqlBigtable(models.Model):
    server_id = models.SmallIntegerField(blank=True, null=True)
    host = models.CharField(max_length=30)
    port = models.CharField(max_length=10)
    tags = models.CharField(max_length=50)
    db_name = models.CharField(max_length=50, blank=True, null=True)
    table_name = models.CharField(max_length=100, blank=True, null=True)
    table_size = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    table_comment = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mysql_bigtable'


class MysqlBigtableHistory(models.Model):
    server_id = models.SmallIntegerField(blank=True, null=True)
    host = models.CharField(max_length=30)
    port = models.CharField(max_length=10)
    tags = models.CharField(max_length=50)
    db_name = models.CharField(max_length=50, blank=True, null=True)
    table_name = models.CharField(max_length=100, blank=True, null=True)
    table_size = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    table_comment = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    ymd = models.IntegerField(db_column='Ymd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mysql_bigtable_history'


class MysqlConnected(models.Model):
    server_id = models.SmallIntegerField()
    host = models.CharField(max_length=30)
    port = models.CharField(max_length=10)
    tags = models.CharField(max_length=50)
    connect_server = models.CharField(max_length=100)
    connect_user = models.CharField(max_length=50, blank=True, null=True)
    connect_db = models.CharField(max_length=50, blank=True, null=True)
    connect_count = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mysql_connected'


class MysqlProcesslist(models.Model):
    server_id = models.SmallIntegerField(blank=True, null=True)
    host = models.CharField(max_length=30)
    port = models.CharField(max_length=10)
    tags = models.CharField(max_length=50)
    pid = models.IntegerField(blank=True, null=True)
    p_user = models.CharField(max_length=50, blank=True, null=True)
    p_host = models.CharField(max_length=50, blank=True, null=True)
    p_db = models.CharField(max_length=30, blank=True, null=True)
    command = models.CharField(max_length=30, blank=True, null=True)
    time = models.CharField(max_length=200)
    status = models.CharField(max_length=50, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mysql_processlist'


class MysqlReplication(models.Model):
    server_id = models.SmallIntegerField(blank=True, null=True)
    tags = models.CharField(max_length=50)
    host = models.CharField(max_length=30, blank=True, null=True)
    port = models.CharField(max_length=20, blank=True, null=True)
    is_master = models.IntegerField(blank=True, null=True)
    is_slave = models.IntegerField(blank=True, null=True)
    read_only = models.CharField(max_length=10, blank=True, null=True)
    gtid_mode = models.CharField(max_length=10, blank=True, null=True)
    master_server = models.CharField(max_length=30, blank=True, null=True)
    master_port = models.CharField(max_length=20, blank=True, null=True)
    slave_io_run = models.CharField(max_length=20, blank=True, null=True)
    slave_sql_run = models.CharField(max_length=20, blank=True, null=True)
    delay = models.CharField(max_length=20, blank=True, null=True)
    current_binlog_file = models.CharField(max_length=30, blank=True, null=True)
    current_binlog_pos = models.CharField(max_length=30, blank=True, null=True)
    master_binlog_file = models.CharField(max_length=30, blank=True, null=True)
    master_binlog_pos = models.CharField(max_length=30, blank=True, null=True)
    master_binlog_space = models.BigIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mysql_replication'


class MysqlReplicationHistory(models.Model):
    server_id = models.SmallIntegerField()
    tags = models.CharField(max_length=50)
    host = models.CharField(max_length=30, blank=True, null=True)
    port = models.CharField(max_length=20, blank=True, null=True)
    is_master = models.IntegerField(blank=True, null=True)
    is_slave = models.IntegerField(blank=True, null=True)
    read_only = models.CharField(max_length=10, blank=True, null=True)
    gtid_mode = models.CharField(max_length=10, blank=True, null=True)
    master_server = models.CharField(max_length=30, blank=True, null=True)
    master_port = models.CharField(max_length=20, blank=True, null=True)
    slave_io_run = models.CharField(max_length=20, blank=True, null=True)
    slave_sql_run = models.CharField(max_length=20, blank=True, null=True)
    delay = models.CharField(max_length=20, blank=True, null=True)
    current_binlog_file = models.CharField(max_length=30, blank=True, null=True)
    current_binlog_pos = models.CharField(max_length=30, blank=True, null=True)
    master_binlog_file = models.CharField(max_length=30, blank=True, null=True)
    master_binlog_pos = models.CharField(max_length=30, blank=True, null=True)
    master_binlog_space = models.BigIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    ymdhi = models.BigIntegerField(db_column='YmdHi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mysql_replication_history'


class MysqlSlowQueryReview(models.Model):
    checksum = models.BigIntegerField(primary_key=True)
    fingerprint = models.TextField()
    sample = models.TextField()
    first_seen = models.DateTimeField(blank=True, null=True)
    last_seen = models.DateTimeField(blank=True, null=True)
    reviewed_by = models.CharField(max_length=20, blank=True, null=True)
    reviewed_on = models.DateTimeField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mysql_slow_query_review'


class MysqlSlowQueryReviewHistory(models.Model):
    serverid_max = models.SmallIntegerField()
    db_max = models.CharField(max_length=100, blank=True, null=True)
    user_max = models.CharField(max_length=100, blank=True, null=True)
    checksum = models.BigIntegerField()
    sample = models.TextField()
    ts_min = models.DateTimeField()
    ts_max = models.DateTimeField()
    ts_cnt = models.FloatField(blank=True, null=True)
    query_time_sum = models.FloatField(db_column='Query_time_sum', blank=True, null=True)  # Field name made lowercase.
    query_time_min = models.FloatField(db_column='Query_time_min', blank=True, null=True)  # Field name made lowercase.
    query_time_max = models.FloatField(db_column='Query_time_max', blank=True, null=True)  # Field name made lowercase.
    query_time_pct_95 = models.FloatField(db_column='Query_time_pct_95', blank=True, null=True)  # Field name made lowercase.
    query_time_stddev = models.FloatField(db_column='Query_time_stddev', blank=True, null=True)  # Field name made lowercase.
    query_time_median = models.FloatField(db_column='Query_time_median', blank=True, null=True)  # Field name made lowercase.
    lock_time_sum = models.FloatField(db_column='Lock_time_sum', blank=True, null=True)  # Field name made lowercase.
    lock_time_min = models.FloatField(db_column='Lock_time_min', blank=True, null=True)  # Field name made lowercase.
    lock_time_max = models.FloatField(db_column='Lock_time_max', blank=True, null=True)  # Field name made lowercase.
    lock_time_pct_95 = models.FloatField(db_column='Lock_time_pct_95', blank=True, null=True)  # Field name made lowercase.
    lock_time_stddev = models.FloatField(db_column='Lock_time_stddev', blank=True, null=True)  # Field name made lowercase.
    lock_time_median = models.FloatField(db_column='Lock_time_median', blank=True, null=True)  # Field name made lowercase.
    rows_sent_sum = models.FloatField(db_column='Rows_sent_sum', blank=True, null=True)  # Field name made lowercase.
    rows_sent_min = models.FloatField(db_column='Rows_sent_min', blank=True, null=True)  # Field name made lowercase.
    rows_sent_max = models.FloatField(db_column='Rows_sent_max', blank=True, null=True)  # Field name made lowercase.
    rows_sent_pct_95 = models.FloatField(db_column='Rows_sent_pct_95', blank=True, null=True)  # Field name made lowercase.
    rows_sent_stddev = models.FloatField(db_column='Rows_sent_stddev', blank=True, null=True)  # Field name made lowercase.
    rows_sent_median = models.FloatField(db_column='Rows_sent_median', blank=True, null=True)  # Field name made lowercase.
    rows_examined_sum = models.FloatField(db_column='Rows_examined_sum', blank=True, null=True)  # Field name made lowercase.
    rows_examined_min = models.FloatField(db_column='Rows_examined_min', blank=True, null=True)  # Field name made lowercase.
    rows_examined_max = models.FloatField(db_column='Rows_examined_max', blank=True, null=True)  # Field name made lowercase.
    rows_examined_pct_95 = models.FloatField(db_column='Rows_examined_pct_95', blank=True, null=True)  # Field name made lowercase.
    rows_examined_stddev = models.FloatField(db_column='Rows_examined_stddev', blank=True, null=True)  # Field name made lowercase.
    rows_examined_median = models.FloatField(db_column='Rows_examined_median', blank=True, null=True)  # Field name made lowercase.
    rows_affected_sum = models.FloatField(db_column='Rows_affected_sum', blank=True, null=True)  # Field name made lowercase.
    rows_affected_min = models.FloatField(db_column='Rows_affected_min', blank=True, null=True)  # Field name made lowercase.
    rows_affected_max = models.FloatField(db_column='Rows_affected_max', blank=True, null=True)  # Field name made lowercase.
    rows_affected_pct_95 = models.FloatField(db_column='Rows_affected_pct_95', blank=True, null=True)  # Field name made lowercase.
    rows_affected_stddev = models.FloatField(db_column='Rows_affected_stddev', blank=True, null=True)  # Field name made lowercase.
    rows_affected_median = models.FloatField(db_column='Rows_affected_median', blank=True, null=True)  # Field name made lowercase.
    rows_read_sum = models.FloatField(db_column='Rows_read_sum', blank=True, null=True)  # Field name made lowercase.
    rows_read_min = models.FloatField(db_column='Rows_read_min', blank=True, null=True)  # Field name made lowercase.
    rows_read_max = models.FloatField(db_column='Rows_read_max', blank=True, null=True)  # Field name made lowercase.
    rows_read_pct_95 = models.FloatField(db_column='Rows_read_pct_95', blank=True, null=True)  # Field name made lowercase.
    rows_read_stddev = models.FloatField(db_column='Rows_read_stddev', blank=True, null=True)  # Field name made lowercase.
    rows_read_median = models.FloatField(db_column='Rows_read_median', blank=True, null=True)  # Field name made lowercase.
    merge_passes_sum = models.FloatField(db_column='Merge_passes_sum', blank=True, null=True)  # Field name made lowercase.
    merge_passes_min = models.FloatField(db_column='Merge_passes_min', blank=True, null=True)  # Field name made lowercase.
    merge_passes_max = models.FloatField(db_column='Merge_passes_max', blank=True, null=True)  # Field name made lowercase.
    merge_passes_pct_95 = models.FloatField(db_column='Merge_passes_pct_95', blank=True, null=True)  # Field name made lowercase.
    merge_passes_stddev = models.FloatField(db_column='Merge_passes_stddev', blank=True, null=True)  # Field name made lowercase.
    merge_passes_median = models.FloatField(db_column='Merge_passes_median', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_ops_min = models.FloatField(db_column='InnoDB_IO_r_ops_min', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_ops_max = models.FloatField(db_column='InnoDB_IO_r_ops_max', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_ops_pct_95 = models.FloatField(db_column='InnoDB_IO_r_ops_pct_95', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_ops_stddev = models.FloatField(db_column='InnoDB_IO_r_ops_stddev', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_ops_median = models.FloatField(db_column='InnoDB_IO_r_ops_median', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_bytes_min = models.FloatField(db_column='InnoDB_IO_r_bytes_min', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_bytes_max = models.FloatField(db_column='InnoDB_IO_r_bytes_max', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_bytes_pct_95 = models.FloatField(db_column='InnoDB_IO_r_bytes_pct_95', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_bytes_stddev = models.FloatField(db_column='InnoDB_IO_r_bytes_stddev', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_bytes_median = models.FloatField(db_column='InnoDB_IO_r_bytes_median', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_wait_min = models.FloatField(db_column='InnoDB_IO_r_wait_min', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_wait_max = models.FloatField(db_column='InnoDB_IO_r_wait_max', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_wait_pct_95 = models.FloatField(db_column='InnoDB_IO_r_wait_pct_95', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_wait_stddev = models.FloatField(db_column='InnoDB_IO_r_wait_stddev', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_wait_median = models.FloatField(db_column='InnoDB_IO_r_wait_median', blank=True, null=True)  # Field name made lowercase.
    innodb_rec_lock_wait_min = models.FloatField(db_column='InnoDB_rec_lock_wait_min', blank=True, null=True)  # Field name made lowercase.
    innodb_rec_lock_wait_max = models.FloatField(db_column='InnoDB_rec_lock_wait_max', blank=True, null=True)  # Field name made lowercase.
    innodb_rec_lock_wait_pct_95 = models.FloatField(db_column='InnoDB_rec_lock_wait_pct_95', blank=True, null=True)  # Field name made lowercase.
    innodb_rec_lock_wait_stddev = models.FloatField(db_column='InnoDB_rec_lock_wait_stddev', blank=True, null=True)  # Field name made lowercase.
    innodb_rec_lock_wait_median = models.FloatField(db_column='InnoDB_rec_lock_wait_median', blank=True, null=True)  # Field name made lowercase.
    innodb_queue_wait_min = models.FloatField(db_column='InnoDB_queue_wait_min', blank=True, null=True)  # Field name made lowercase.
    innodb_queue_wait_max = models.FloatField(db_column='InnoDB_queue_wait_max', blank=True, null=True)  # Field name made lowercase.
    innodb_queue_wait_pct_95 = models.FloatField(db_column='InnoDB_queue_wait_pct_95', blank=True, null=True)  # Field name made lowercase.
    innodb_queue_wait_stddev = models.FloatField(db_column='InnoDB_queue_wait_stddev', blank=True, null=True)  # Field name made lowercase.
    innodb_queue_wait_median = models.FloatField(db_column='InnoDB_queue_wait_median', blank=True, null=True)  # Field name made lowercase.
    innodb_pages_distinct_min = models.FloatField(db_column='InnoDB_pages_distinct_min', blank=True, null=True)  # Field name made lowercase.
    innodb_pages_distinct_max = models.FloatField(db_column='InnoDB_pages_distinct_max', blank=True, null=True)  # Field name made lowercase.
    innodb_pages_distinct_pct_95 = models.FloatField(db_column='InnoDB_pages_distinct_pct_95', blank=True, null=True)  # Field name made lowercase.
    innodb_pages_distinct_stddev = models.FloatField(db_column='InnoDB_pages_distinct_stddev', blank=True, null=True)  # Field name made lowercase.
    innodb_pages_distinct_median = models.FloatField(db_column='InnoDB_pages_distinct_median', blank=True, null=True)  # Field name made lowercase.
    qc_hit_cnt = models.FloatField(db_column='QC_Hit_cnt', blank=True, null=True)  # Field name made lowercase.
    qc_hit_sum = models.FloatField(db_column='QC_Hit_sum', blank=True, null=True)  # Field name made lowercase.
    full_scan_cnt = models.FloatField(db_column='Full_scan_cnt', blank=True, null=True)  # Field name made lowercase.
    full_scan_sum = models.FloatField(db_column='Full_scan_sum', blank=True, null=True)  # Field name made lowercase.
    full_join_cnt = models.FloatField(db_column='Full_join_cnt', blank=True, null=True)  # Field name made lowercase.
    full_join_sum = models.FloatField(db_column='Full_join_sum', blank=True, null=True)  # Field name made lowercase.
    tmp_table_cnt = models.FloatField(db_column='Tmp_table_cnt', blank=True, null=True)  # Field name made lowercase.
    tmp_table_sum = models.FloatField(db_column='Tmp_table_sum', blank=True, null=True)  # Field name made lowercase.
    tmp_table_on_disk_cnt = models.FloatField(db_column='Tmp_table_on_disk_cnt', blank=True, null=True)  # Field name made lowercase.
    tmp_table_on_disk_sum = models.FloatField(db_column='Tmp_table_on_disk_sum', blank=True, null=True)  # Field name made lowercase.
    filesort_cnt = models.FloatField(db_column='Filesort_cnt', blank=True, null=True)  # Field name made lowercase.
    filesort_sum = models.FloatField(db_column='Filesort_sum', blank=True, null=True)  # Field name made lowercase.
    filesort_on_disk_cnt = models.FloatField(db_column='Filesort_on_disk_cnt', blank=True, null=True)  # Field name made lowercase.
    filesort_on_disk_sum = models.FloatField(db_column='Filesort_on_disk_sum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mysql_slow_query_review_history'
        unique_together = (('checksum', 'ts_min', 'ts_max'),)


class MysqlSlowQuerySendmailLog(models.Model):
    server_id = models.SmallIntegerField()
    sendmail_status = models.IntegerField()
    sendmail_info = models.CharField(max_length=50, blank=True, null=True)
    sendmail_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mysql_slow_query_sendmail_log'


class MysqlStatus(models.Model):
    server_id = models.SmallIntegerField()
    host = models.CharField(max_length=30)
    port = models.CharField(max_length=10)
    tags = models.CharField(max_length=50)
    connect = models.SmallIntegerField()
    role = models.CharField(max_length=30)
    uptime = models.IntegerField()
    version = models.CharField(max_length=50)
    max_connections = models.SmallIntegerField()
    max_connect_errors = models.SmallIntegerField()
    open_files_limit = models.IntegerField()
    open_files = models.SmallIntegerField()
    table_open_cache = models.SmallIntegerField()
    open_tables = models.SmallIntegerField()
    max_tmp_tables = models.SmallIntegerField()
    max_heap_table_size = models.IntegerField()
    max_allowed_packet = models.IntegerField()
    threads_connected = models.IntegerField()
    threads_running = models.IntegerField()
    threads_waits = models.IntegerField()
    threads_created = models.IntegerField()
    threads_cached = models.IntegerField()
    connections = models.IntegerField()
    aborted_clients = models.IntegerField()
    aborted_connects = models.IntegerField()
    connections_persecond = models.SmallIntegerField()
    bytes_received_persecond = models.IntegerField()
    bytes_sent_persecond = models.IntegerField()
    com_select_persecond = models.SmallIntegerField()
    com_insert_persecond = models.SmallIntegerField()
    com_update_persecond = models.SmallIntegerField()
    com_delete_persecond = models.SmallIntegerField()
    com_commit_persecond = models.SmallIntegerField()
    com_rollback_persecond = models.SmallIntegerField()
    questions_persecond = models.IntegerField()
    queries_persecond = models.IntegerField()
    transaction_persecond = models.SmallIntegerField()
    created_tmp_tables_persecond = models.SmallIntegerField()
    created_tmp_disk_tables_persecond = models.SmallIntegerField()
    created_tmp_files_persecond = models.SmallIntegerField()
    table_locks_immediate_persecond = models.IntegerField()
    table_locks_waited_persecond = models.SmallIntegerField()
    key_buffer_size = models.BigIntegerField()
    sort_buffer_size = models.IntegerField()
    join_buffer_size = models.IntegerField()
    key_blocks_not_flushed = models.IntegerField()
    key_blocks_unused = models.IntegerField()
    key_blocks_used = models.IntegerField()
    key_read_requests_persecond = models.IntegerField()
    key_reads_persecond = models.IntegerField()
    key_write_requests_persecond = models.IntegerField()
    key_writes_persecond = models.IntegerField()
    innodb_version = models.CharField(max_length=30)
    innodb_buffer_pool_instances = models.SmallIntegerField()
    innodb_buffer_pool_size = models.BigIntegerField()
    innodb_doublewrite = models.CharField(max_length=10)
    innodb_file_per_table = models.CharField(max_length=10)
    innodb_flush_log_at_trx_commit = models.IntegerField()
    innodb_flush_method = models.CharField(max_length=30)
    innodb_force_recovery = models.IntegerField()
    innodb_io_capacity = models.IntegerField()
    innodb_read_io_threads = models.IntegerField()
    innodb_write_io_threads = models.IntegerField()
    innodb_buffer_pool_pages_total = models.IntegerField()
    innodb_buffer_pool_pages_data = models.IntegerField()
    innodb_buffer_pool_pages_dirty = models.IntegerField()
    innodb_buffer_pool_pages_flushed = models.BigIntegerField()
    innodb_buffer_pool_pages_free = models.IntegerField()
    innodb_buffer_pool_pages_misc = models.IntegerField()
    innodb_page_size = models.IntegerField()
    innodb_pages_created = models.BigIntegerField()
    innodb_pages_read = models.BigIntegerField()
    innodb_pages_written = models.BigIntegerField()
    innodb_row_lock_current_waits = models.CharField(max_length=100)
    innodb_buffer_pool_pages_flushed_persecond = models.IntegerField()
    innodb_buffer_pool_read_requests_persecond = models.IntegerField()
    innodb_buffer_pool_reads_persecond = models.IntegerField()
    innodb_buffer_pool_write_requests_persecond = models.IntegerField()
    innodb_rows_read_persecond = models.IntegerField()
    innodb_rows_inserted_persecond = models.IntegerField()
    innodb_rows_updated_persecond = models.IntegerField()
    innodb_rows_deleted_persecond = models.IntegerField()
    query_cache_hitrate = models.CharField(max_length=10)
    thread_cache_hitrate = models.CharField(max_length=10)
    key_buffer_read_rate = models.CharField(max_length=10)
    key_buffer_write_rate = models.CharField(max_length=10)
    key_blocks_used_rate = models.CharField(max_length=10)
    created_tmp_disk_tables_rate = models.CharField(max_length=10)
    connections_usage_rate = models.CharField(max_length=10)
    open_files_usage_rate = models.CharField(max_length=10)
    open_tables_usage_rate = models.CharField(max_length=10)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mysql_status'


class MysqlStatusHistory(models.Model):
    server_id = models.SmallIntegerField()
    host = models.CharField(max_length=30)
    port = models.CharField(max_length=10)
    tags = models.CharField(max_length=50)
    connect = models.SmallIntegerField()
    role = models.CharField(max_length=30)
    uptime = models.IntegerField()
    version = models.CharField(max_length=50)
    max_connections = models.SmallIntegerField()
    max_connect_errors = models.SmallIntegerField()
    open_files_limit = models.IntegerField()
    open_files = models.SmallIntegerField()
    table_open_cache = models.SmallIntegerField()
    open_tables = models.SmallIntegerField()
    max_tmp_tables = models.SmallIntegerField()
    max_heap_table_size = models.IntegerField()
    max_allowed_packet = models.IntegerField()
    threads_connected = models.IntegerField()
    threads_running = models.IntegerField()
    threads_waits = models.IntegerField()
    threads_created = models.IntegerField()
    threads_cached = models.IntegerField()
    connections = models.IntegerField()
    aborted_clients = models.IntegerField()
    aborted_connects = models.IntegerField()
    connections_persecond = models.SmallIntegerField()
    bytes_received_persecond = models.IntegerField()
    bytes_sent_persecond = models.IntegerField()
    com_select_persecond = models.SmallIntegerField()
    com_insert_persecond = models.SmallIntegerField()
    com_update_persecond = models.SmallIntegerField()
    com_delete_persecond = models.SmallIntegerField()
    com_commit_persecond = models.SmallIntegerField()
    com_rollback_persecond = models.SmallIntegerField()
    questions_persecond = models.IntegerField()
    queries_persecond = models.IntegerField()
    transaction_persecond = models.SmallIntegerField()
    created_tmp_tables_persecond = models.SmallIntegerField()
    created_tmp_disk_tables_persecond = models.SmallIntegerField()
    created_tmp_files_persecond = models.SmallIntegerField()
    table_locks_immediate_persecond = models.IntegerField()
    table_locks_waited_persecond = models.SmallIntegerField()
    key_buffer_size = models.BigIntegerField()
    sort_buffer_size = models.IntegerField()
    join_buffer_size = models.IntegerField()
    key_blocks_not_flushed = models.IntegerField()
    key_blocks_unused = models.IntegerField()
    key_blocks_used = models.IntegerField()
    key_read_requests_persecond = models.IntegerField()
    key_reads_persecond = models.IntegerField()
    key_write_requests_persecond = models.IntegerField()
    key_writes_persecond = models.IntegerField()
    innodb_version = models.CharField(max_length=30)
    innodb_buffer_pool_instances = models.SmallIntegerField()
    innodb_buffer_pool_size = models.BigIntegerField()
    innodb_doublewrite = models.CharField(max_length=10)
    innodb_file_per_table = models.CharField(max_length=10)
    innodb_flush_log_at_trx_commit = models.IntegerField()
    innodb_flush_method = models.CharField(max_length=30)
    innodb_force_recovery = models.IntegerField()
    innodb_io_capacity = models.IntegerField()
    innodb_read_io_threads = models.IntegerField()
    innodb_write_io_threads = models.IntegerField()
    innodb_buffer_pool_pages_total = models.IntegerField()
    innodb_buffer_pool_pages_data = models.IntegerField()
    innodb_buffer_pool_pages_dirty = models.IntegerField()
    innodb_buffer_pool_pages_flushed = models.BigIntegerField()
    innodb_buffer_pool_pages_free = models.IntegerField()
    innodb_buffer_pool_pages_misc = models.IntegerField()
    innodb_page_size = models.IntegerField()
    innodb_pages_created = models.BigIntegerField()
    innodb_pages_read = models.BigIntegerField()
    innodb_pages_written = models.BigIntegerField()
    innodb_row_lock_current_waits = models.CharField(max_length=100)
    innodb_buffer_pool_pages_flushed_persecond = models.IntegerField()
    innodb_buffer_pool_read_requests_persecond = models.IntegerField()
    innodb_buffer_pool_reads_persecond = models.IntegerField()
    innodb_buffer_pool_write_requests_persecond = models.IntegerField()
    innodb_rows_read_persecond = models.IntegerField()
    innodb_rows_inserted_persecond = models.IntegerField()
    innodb_rows_updated_persecond = models.IntegerField()
    innodb_rows_deleted_persecond = models.IntegerField()
    query_cache_hitrate = models.CharField(max_length=10)
    thread_cache_hitrate = models.CharField(max_length=10)
    key_buffer_read_rate = models.CharField(max_length=10)
    key_buffer_write_rate = models.CharField(max_length=10)
    key_blocks_used_rate = models.CharField(max_length=10)
    created_tmp_disk_tables_rate = models.CharField(max_length=10)
    connections_usage_rate = models.CharField(max_length=10)
    open_files_usage_rate = models.CharField(max_length=10)
    open_tables_usage_rate = models.CharField(max_length=10)
    create_time = models.DateTimeField()
    ymdhi = models.BigIntegerField(db_column='YmdHi')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mysql_status_history'


class Options(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'options'


class OracleStatus(models.Model):
    server_id = models.SmallIntegerField()
    host = models.CharField(max_length=50)
    port = models.CharField(max_length=10)
    tags = models.CharField(max_length=100, blank=True, null=True)
    connect = models.IntegerField()
    instance_name = models.CharField(max_length=30)
    instance_role = models.CharField(max_length=50)
    instance_status = models.CharField(max_length=50)
    database_role = models.CharField(max_length=50)
    open_mode = models.CharField(max_length=30)
    protection_mode = models.CharField(max_length=30)
    host_name = models.CharField(max_length=50)
    database_status = models.CharField(max_length=30)
    startup_time = models.CharField(max_length=100)
    uptime = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    archiver = models.CharField(max_length=50)
    session_total = models.IntegerField()
    session_actives = models.SmallIntegerField()
    session_waits = models.SmallIntegerField()
    dg_stats = models.CharField(max_length=255)
    dg_delay = models.IntegerField()
    processes = models.IntegerField()
    session_logical_reads_persecond = models.IntegerField()
    physical_reads_persecond = models.IntegerField()
    physical_writes_persecond = models.IntegerField()
    physical_read_io_requests_persecond = models.IntegerField()
    physical_write_io_requests_persecond = models.IntegerField()
    db_block_changes_persecond = models.IntegerField()
    os_cpu_wait_time = models.IntegerField()
    logons_persecond = models.IntegerField()
    logons_current = models.IntegerField()
    opened_cursors_persecond = models.IntegerField()
    opened_cursors_current = models.IntegerField()
    user_commits_persecond = models.IntegerField()
    user_rollbacks_persecond = models.IntegerField()
    user_calls_persecond = models.IntegerField()
    db_block_gets_persecond = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oracle_status'


class OracleStatusHistory(models.Model):
    server_id = models.SmallIntegerField()
    host = models.CharField(max_length=50)
    port = models.CharField(max_length=10)
    tags = models.CharField(max_length=100, blank=True, null=True)
    connect = models.IntegerField()
    instance_name = models.CharField(max_length=30)
    instance_role = models.CharField(max_length=50)
    instance_status = models.CharField(max_length=50)
    database_role = models.CharField(max_length=50)
    open_mode = models.CharField(max_length=30)
    protection_mode = models.CharField(max_length=30)
    host_name = models.CharField(max_length=50)
    database_status = models.CharField(max_length=30)
    startup_time = models.CharField(max_length=100)
    uptime = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    archiver = models.CharField(max_length=50)
    session_total = models.IntegerField()
    session_actives = models.SmallIntegerField()
    session_waits = models.SmallIntegerField()
    dg_stats = models.CharField(max_length=255)
    dg_delay = models.IntegerField()
    processes = models.IntegerField()
    session_logical_reads_persecond = models.IntegerField()
    physical_reads_persecond = models.IntegerField()
    physical_writes_persecond = models.IntegerField()
    physical_read_io_requests_persecond = models.IntegerField()
    physical_write_io_requests_persecond = models.IntegerField()
    db_block_changes_persecond = models.IntegerField()
    os_cpu_wait_time = models.IntegerField()
    logons_persecond = models.IntegerField()
    logons_current = models.IntegerField()
    opened_cursors_persecond = models.IntegerField()
    opened_cursors_current = models.IntegerField()
    user_commits_persecond = models.IntegerField()
    user_rollbacks_persecond = models.IntegerField()
    user_calls_persecond = models.IntegerField()
    db_block_gets_persecond = models.IntegerField()
    create_time = models.DateTimeField()
    ymdhi = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'oracle_status_history'


class OracleTablespace(models.Model):
    server_id = models.SmallIntegerField()
    host = models.CharField(max_length=50)
    port = models.CharField(max_length=30)
    tags = models.CharField(max_length=50)
    tablespace_name = models.CharField(max_length=100)
    total_size = models.BigIntegerField()
    used_size = models.BigIntegerField()
    avail_size = models.BigIntegerField()
    used_rate = models.CharField(max_length=255)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oracle_tablespace'


class OracleTablespaceHistory(models.Model):
    server_id = models.SmallIntegerField()
    host = models.CharField(max_length=50)
    port = models.CharField(max_length=30)
    tags = models.CharField(max_length=50)
    tablespace_name = models.CharField(max_length=100)
    total_size = models.BigIntegerField()
    used_size = models.BigIntegerField()
    avail_size = models.BigIntegerField()
    used_rate = models.CharField(max_length=255)
    create_time = models.DateTimeField()
    ymdhi = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'oracle_tablespace_history'


class OsDisk(models.Model):
    ip = models.CharField(max_length=50)
    tags = models.CharField(max_length=100, blank=True, null=True)
    mounted = models.CharField(max_length=50)
    total_size = models.BigIntegerField()
    used_size = models.BigIntegerField()
    avail_size = models.BigIntegerField()
    used_rate = models.CharField(max_length=255)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'os_disk'


class OsDiskHistory(models.Model):
    ip = models.CharField(max_length=50)
    tags = models.CharField(max_length=100, blank=True, null=True)
    mounted = models.CharField(max_length=50)
    total_size = models.BigIntegerField()
    used_size = models.BigIntegerField()
    avail_size = models.BigIntegerField()
    used_rate = models.CharField(max_length=255)
    create_time = models.DateTimeField()
    ymdhi = models.BigIntegerField(db_column='YmdHi')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'os_disk_history'


class OsDiskio(models.Model):
    ip = models.CharField(max_length=50)
    tags = models.CharField(max_length=100, blank=True, null=True)
    fdisk = models.CharField(max_length=50)
    disk_io_reads = models.BigIntegerField()
    disk_io_writes = models.BigIntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'os_diskio'


class OsDiskioHistory(models.Model):
    ip = models.CharField(max_length=50)
    tags = models.CharField(max_length=100, blank=True, null=True)
    fdisk = models.CharField(max_length=50)
    disk_io_reads = models.BigIntegerField()
    disk_io_writes = models.BigIntegerField()
    create_time = models.DateTimeField()
    ymdhi = models.BigIntegerField(db_column='YmdHi')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'os_diskio_history'


class OsNet(models.Model):
    ip = models.CharField(max_length=50)
    tags = models.CharField(max_length=100, blank=True, null=True)
    if_descr = models.CharField(max_length=50)
    in_bytes = models.BigIntegerField()
    out_bytes = models.BigIntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'os_net'


class OsNetHistory(models.Model):
    ip = models.CharField(max_length=50)
    tags = models.CharField(max_length=100, blank=True, null=True)
    if_descr = models.CharField(max_length=50)
    in_bytes = models.BigIntegerField()
    out_bytes = models.BigIntegerField()
    create_time = models.DateTimeField()
    ymdhi = models.BigIntegerField(db_column='YmdHi')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'os_net_history'


class OsStatus(models.Model):
    ip = models.CharField(max_length=50)
    snmp = models.IntegerField()
    tags = models.CharField(max_length=100, blank=True, null=True)
    hostname = models.CharField(max_length=100)
    kernel = models.CharField(max_length=50)
    system_date = models.CharField(max_length=50)
    system_uptime = models.CharField(max_length=50)
    process = models.SmallIntegerField()
    load_1 = models.DecimalField(max_digits=4, decimal_places=2)
    load_5 = models.DecimalField(max_digits=4, decimal_places=2)
    load_15 = models.DecimalField(max_digits=4, decimal_places=2)
    cpu_user_time = models.IntegerField()
    cpu_system_time = models.IntegerField()
    cpu_idle_time = models.IntegerField()
    swap_total = models.IntegerField()
    swap_avail = models.IntegerField()
    mem_total = models.IntegerField()
    mem_used = models.IntegerField()
    mem_free = models.IntegerField()
    mem_shared = models.IntegerField()
    mem_buffered = models.IntegerField()
    mem_cached = models.IntegerField()
    mem_usage_rate = models.CharField(max_length=50)
    mem_available = models.CharField(max_length=50)
    disk_io_reads_total = models.IntegerField()
    disk_io_writes_total = models.IntegerField()
    net_in_bytes_total = models.BigIntegerField()
    net_out_bytes_total = models.BigIntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'os_status'


class OsStatusHistory(models.Model):
    ip = models.CharField(max_length=50)
    snmp = models.IntegerField()
    tags = models.CharField(max_length=100, blank=True, null=True)
    hostname = models.CharField(max_length=100)
    kernel = models.CharField(max_length=50)
    system_date = models.CharField(max_length=50)
    system_uptime = models.CharField(max_length=50)
    process = models.SmallIntegerField()
    load_1 = models.DecimalField(max_digits=4, decimal_places=2)
    load_5 = models.DecimalField(max_digits=4, decimal_places=2)
    load_15 = models.DecimalField(max_digits=4, decimal_places=2)
    cpu_user_time = models.IntegerField()
    cpu_system_time = models.IntegerField()
    cpu_idle_time = models.IntegerField()
    swap_total = models.IntegerField()
    swap_avail = models.IntegerField()
    mem_total = models.IntegerField()
    mem_used = models.IntegerField()
    mem_free = models.IntegerField()
    mem_shared = models.IntegerField()
    mem_buffered = models.IntegerField()
    mem_cached = models.IntegerField()
    mem_usage_rate = models.CharField(max_length=50)
    mem_available = models.CharField(max_length=50)
    disk_io_reads_total = models.IntegerField()
    disk_io_writes_total = models.IntegerField()
    net_in_bytes_total = models.BigIntegerField()
    net_out_bytes_total = models.BigIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    ymdhi = models.BigIntegerField(db_column='YmdHi')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'os_status_history'


class RedisReplication(models.Model):
    server_id = models.SmallIntegerField()
    tags = models.CharField(max_length=50)
    host = models.CharField(max_length=30, blank=True, null=True)
    port = models.SmallIntegerField(blank=True, null=True)
    role = models.CharField(max_length=20, blank=True, null=True)
    master_server_id = models.SmallIntegerField()
    master_host = models.CharField(max_length=20, blank=True, null=True)
    master_port = models.CharField(max_length=20, blank=True, null=True)
    master_link_status = models.CharField(max_length=20, blank=True, null=True)
    master_last_io_seconds_ago = models.CharField(max_length=20, blank=True, null=True)
    master_sync_in_progress = models.CharField(max_length=20, blank=True, null=True)
    slave_priority = models.CharField(max_length=20, blank=True, null=True)
    slave_read_only = models.CharField(max_length=20, blank=True, null=True)
    connected_slaves = models.SmallIntegerField(blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'redis_replication'


class RedisReplicationHistory(models.Model):
    server_id = models.SmallIntegerField()
    tags = models.CharField(max_length=50)
    host = models.CharField(max_length=20, blank=True, null=True)
    port = models.SmallIntegerField(blank=True, null=True)
    role = models.CharField(max_length=20, blank=True, null=True)
    master_server_id = models.SmallIntegerField()
    master_host = models.CharField(max_length=20, blank=True, null=True)
    master_port = models.CharField(max_length=20, blank=True, null=True)
    master_link_status = models.CharField(max_length=20, blank=True, null=True)
    master_last_io_seconds_ago = models.CharField(max_length=20, blank=True, null=True)
    master_sync_in_progress = models.CharField(max_length=20, blank=True, null=True)
    slave_priority = models.CharField(max_length=20, blank=True, null=True)
    slave_read_only = models.CharField(max_length=20, blank=True, null=True)
    connected_slaves = models.SmallIntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    ymdhi = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'redis_replication_history'


class RedisStatus(models.Model):
    server_id = models.SmallIntegerField()
    host = models.CharField(max_length=30)
    port = models.CharField(max_length=10)
    tags = models.CharField(max_length=50)
    connect = models.SmallIntegerField()
    redis_role = models.CharField(max_length=30)
    redis_version = models.CharField(max_length=50)
    redis_git_sha1 = models.CharField(max_length=255)
    redis_git_dirty = models.CharField(max_length=255)
    redis_mode = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    arch_bits = models.CharField(max_length=10)
    multiplexing_api = models.CharField(max_length=20)
    gcc_version = models.CharField(max_length=20)
    process_id = models.IntegerField()
    run_id = models.CharField(max_length=255)
    tcp_port = models.IntegerField()
    uptime_in_seconds = models.IntegerField()
    uptime_in_days = models.IntegerField()
    hz = models.IntegerField()
    lru_clock = models.BigIntegerField()
    connected_clients = models.SmallIntegerField()
    client_longest_output_list = models.SmallIntegerField()
    client_biggest_input_buf = models.SmallIntegerField()
    blocked_clients = models.SmallIntegerField()
    used_memory = models.BigIntegerField()
    used_memory_human = models.CharField(max_length=50)
    used_memory_rss = models.CharField(max_length=50)
    used_memory_peak = models.CharField(max_length=50)
    used_memory_peak_human = models.CharField(max_length=50)
    used_memory_lua = models.CharField(max_length=50)
    mem_fragmentation_ratio = models.CharField(max_length=50)
    mem_allocator = models.CharField(max_length=50)
    loading = models.SmallIntegerField()
    rdb_changes_since_last_save = models.SmallIntegerField()
    rdb_bgsave_in_progress = models.SmallIntegerField()
    rdb_last_save_time = models.BigIntegerField()
    rdb_last_bgsave_status = models.CharField(max_length=10)
    rdb_last_bgsave_time_sec = models.SmallIntegerField()
    rdb_current_bgsave_time_sec = models.SmallIntegerField()
    aof_enabled = models.SmallIntegerField()
    aof_rewrite_in_progress = models.SmallIntegerField()
    aof_rewrite_scheduled = models.SmallIntegerField()
    aof_last_rewrite_time_sec = models.SmallIntegerField()
    aof_current_rewrite_time_sec = models.SmallIntegerField()
    aof_last_bgrewrite_status = models.CharField(max_length=10)
    total_connections_received = models.BigIntegerField()
    total_commands_processed = models.BigIntegerField()
    current_commands_processed = models.SmallIntegerField()
    instantaneous_ops_per_sec = models.SmallIntegerField()
    rejected_connections = models.SmallIntegerField()
    expired_keys = models.IntegerField()
    evicted_keys = models.IntegerField()
    keyspace_hits = models.IntegerField()
    keyspace_misses = models.IntegerField()
    pubsub_channels = models.IntegerField()
    pubsub_patterns = models.IntegerField()
    latest_fork_usec = models.IntegerField()
    used_cpu_sys = models.DecimalField(max_digits=10, decimal_places=2)
    used_cpu_user = models.FloatField()
    used_cpu_sys_children = models.IntegerField()
    used_cpu_user_children = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'redis_status'


class RedisStatusHistory(models.Model):
    server_id = models.SmallIntegerField()
    host = models.CharField(max_length=30)
    port = models.CharField(max_length=10)
    tags = models.CharField(max_length=50)
    connect = models.SmallIntegerField()
    redis_role = models.CharField(max_length=30)
    redis_version = models.CharField(max_length=50)
    redis_git_sha1 = models.CharField(max_length=255)
    redis_git_dirty = models.CharField(max_length=255)
    redis_mode = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    arch_bits = models.CharField(max_length=10)
    multiplexing_api = models.CharField(max_length=20)
    gcc_version = models.CharField(max_length=20)
    process_id = models.IntegerField()
    run_id = models.CharField(max_length=255)
    tcp_port = models.IntegerField()
    uptime_in_seconds = models.IntegerField()
    uptime_in_days = models.IntegerField()
    hz = models.IntegerField()
    lru_clock = models.BigIntegerField()
    connected_clients = models.SmallIntegerField()
    client_longest_output_list = models.SmallIntegerField()
    client_biggest_input_buf = models.SmallIntegerField()
    blocked_clients = models.SmallIntegerField()
    used_memory = models.BigIntegerField()
    used_memory_human = models.CharField(max_length=50)
    used_memory_rss = models.CharField(max_length=50)
    used_memory_peak = models.CharField(max_length=50)
    used_memory_peak_human = models.CharField(max_length=50)
    used_memory_lua = models.CharField(max_length=50)
    mem_fragmentation_ratio = models.CharField(max_length=50)
    mem_allocator = models.CharField(max_length=50)
    loading = models.SmallIntegerField()
    rdb_changes_since_last_save = models.SmallIntegerField()
    rdb_bgsave_in_progress = models.SmallIntegerField()
    rdb_last_save_time = models.BigIntegerField()
    rdb_last_bgsave_status = models.CharField(max_length=10)
    rdb_last_bgsave_time_sec = models.SmallIntegerField()
    rdb_current_bgsave_time_sec = models.SmallIntegerField()
    aof_enabled = models.SmallIntegerField()
    aof_rewrite_in_progress = models.SmallIntegerField()
    aof_rewrite_scheduled = models.SmallIntegerField()
    aof_last_rewrite_time_sec = models.SmallIntegerField()
    aof_current_rewrite_time_sec = models.SmallIntegerField()
    aof_last_bgrewrite_status = models.CharField(max_length=10)
    total_connections_received = models.BigIntegerField()
    total_commands_processed = models.BigIntegerField()
    current_commands_processed = models.SmallIntegerField()
    instantaneous_ops_per_sec = models.SmallIntegerField()
    rejected_connections = models.SmallIntegerField()
    expired_keys = models.IntegerField()
    evicted_keys = models.IntegerField()
    keyspace_hits = models.IntegerField()
    keyspace_misses = models.IntegerField()
    pubsub_channels = models.IntegerField()
    pubsub_patterns = models.IntegerField()
    latest_fork_usec = models.IntegerField()
    used_cpu_sys = models.DecimalField(max_digits=10, decimal_places=2)
    used_cpu_user = models.FloatField()
    used_cpu_sys_children = models.IntegerField()
    used_cpu_user_children = models.IntegerField()
    create_time = models.DateTimeField()
    ymdhi = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'redis_status_history'
