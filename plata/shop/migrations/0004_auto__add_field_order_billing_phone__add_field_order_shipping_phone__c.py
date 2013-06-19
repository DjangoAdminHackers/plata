# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Order.billing_phone'
        db.add_column(u'shop_order', 'billing_phone', self.gf('django.db.models.fields.CharField')(default='', max_length=50), keep_default=False)

        # Adding field 'Order.shipping_phone'
        db.add_column(u'shop_order', 'shipping_phone', self.gf('django.db.models.fields.CharField')(default='', max_length=50), keep_default=False)

        # Changing field 'Order.language_code'
        db.alter_column(u'shop_order', 'language_code', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True))

        # Changing field 'Order.shipping_same_as_billing'
        db.alter_column(u'shop_order', 'shipping_same_as_billing', self.gf('django.db.models.fields.BooleanField')(blank=True))

        # Changing field 'OrderItem.product'
        db.alter_column(u'shop_orderitem', 'product_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['zai_products.ProductVariant'], null=True, blank=True))

        # Changing field 'OrderItem.tax_class'
        db.alter_column(u'shop_orderitem', 'tax_class_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.TaxClass'], null=True, blank=True))

        # Changing field 'OrderItem.is_sale'
        db.alter_column(u'shop_orderitem', 'is_sale', self.gf('django.db.models.fields.BooleanField')(blank=True))


    def backwards(self, orm):
        
        # Deleting field 'Order.billing_phone'
        db.delete_column(u'shop_order', 'billing_phone')

        # Deleting field 'Order.shipping_phone'
        db.delete_column(u'shop_order', 'shipping_phone')

        # Changing field 'Order.language_code'
        db.alter_column(u'shop_order', 'language_code', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Order.shipping_same_as_billing'
        db.alter_column(u'shop_order', 'shipping_same_as_billing', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'OrderItem.product'
        db.alter_column(u'shop_orderitem', 'product_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simple.Product'], null=True, on_delete=models.SET_NULL, blank=True))

        # Changing field 'OrderItem.tax_class'
        db.alter_column(u'shop_orderitem', 'tax_class_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.TaxClass'], null=True, on_delete=models.SET_NULL, blank=True))

        # Changing field 'OrderItem.is_sale'
        db.alter_column(u'shop_orderitem', 'is_sale', self.gf('django.db.models.fields.BooleanField')())


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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 19, 9, 20, 24, 668353)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 19, 9, 20, 24, 667575)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'shop.order': {
            'Meta': {'object_name': 'Order'},
            '_order_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'billing_address': ('django.db.models.fields.TextField', [], {}),
            'billing_city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'billing_company': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'billing_country': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'billing_first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'billing_last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'billing_phone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'billing_zip_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'confirmed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'data': ('plata.fields.JSONField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items_discount': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '18', 'decimal_places': '10'}),
            'items_subtotal': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '18', 'decimal_places': '10'}),
            'items_tax': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '18', 'decimal_places': '10'}),
            'language_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'paid': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '18', 'decimal_places': '10'}),
            'shipping_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'shipping_city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'shipping_company': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'shipping_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '18', 'decimal_places': '10', 'blank': 'True'}),
            'shipping_country': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'shipping_discount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '18', 'decimal_places': '10', 'blank': 'True'}),
            'shipping_first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'shipping_last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'shipping_method': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'shipping_phone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'shipping_same_as_billing': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'shipping_tax': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '18', 'decimal_places': '10'}),
            'shipping_zip_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10'}),
            'total': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '18', 'decimal_places': '10'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'orders'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'shop.orderitem': {
            'Meta': {'unique_together': "(('order', 'product'),)", 'object_name': 'OrderItem'},
            '_line_item_discount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '18', 'decimal_places': '10', 'blank': 'True'}),
            '_line_item_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '18', 'decimal_places': '10'}),
            '_line_item_tax': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '18', 'decimal_places': '10'}),
            '_unit_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '18', 'decimal_places': '10'}),
            '_unit_tax': ('django.db.models.fields.DecimalField', [], {'max_digits': '18', 'decimal_places': '10'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'data': ('plata.fields.JSONField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_sale': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['shop.Order']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['zai_products.ProductVariant']", 'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'tax_class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.TaxClass']", 'null': 'True', 'blank': 'True'}),
            'tax_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        u'shop.orderpayment': {
            'Meta': {'object_name': 'OrderPayment'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'authorized': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'data': ('plata.fields.JSONField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'payments'", 'to': u"orm['shop.Order']"}),
            'payment_method': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'payment_module': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'payment_module_key': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'shop.orderstatus': {
            'Meta': {'object_name': 'OrderStatus'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statuses'", 'to': u"orm['shop.Order']"}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '20'})
        },
        u'shop.taxclass': {
            'Meta': {'object_name': 'TaxClass'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        u'zai_products.product': {
            'Meta': {'object_name': 'Product'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        u'zai_products.productvariant': {
            'Meta': {'object_name': 'ProductVariant'},
            '_unit_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '18', 'decimal_places': '10'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'grip': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['zai_products.Product']"}),
            'tax_class': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['shop.TaxClass']"}),
            'tax_included': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['shop']
