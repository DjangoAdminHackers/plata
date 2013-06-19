# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Contact.billing_phone'
        db.add_column(u'contact_contact', 'billing_phone', self.gf('django.db.models.fields.CharField')(default='', max_length=50), keep_default=False)

        # Adding field 'Contact.shipping_phone'
        db.add_column(u'contact_contact', 'shipping_phone', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True), keep_default=False)

        # Changing field 'Contact.shipping_same_as_billing'
        db.alter_column(u'contact_contact', 'shipping_same_as_billing', self.gf('django.db.models.fields.BooleanField')(blank=True))


    def backwards(self, orm):
        
        # Deleting field 'Contact.billing_phone'
        db.delete_column(u'contact_contact', 'billing_phone')

        # Deleting field 'Contact.shipping_phone'
        db.delete_column(u'contact_contact', 'shipping_phone')

        # Changing field 'Contact.shipping_same_as_billing'
        db.alter_column(u'contact_contact', 'shipping_same_as_billing', self.gf('django.db.models.fields.BooleanField')())


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 19, 9, 33, 2, 92679)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 19, 9, 33, 2, 91878)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contact.contact': {
            'Meta': {'object_name': 'Contact'},
            'billing_address': ('django.db.models.fields.TextField', [], {}),
            'billing_city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'billing_company': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'billing_country': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'billing_first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'billing_last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'billing_phone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'billing_zip_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'shipping_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'shipping_city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'shipping_company': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'shipping_country': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'shipping_first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'shipping_last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'shipping_phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'shipping_same_as_billing': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'shipping_zip_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'contactuser'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['contact']
