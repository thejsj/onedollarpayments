# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Request.paid'
        db.add_column(u'onedollarpayments_request', 'paid',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Request.paid'
        db.delete_column(u'onedollarpayments_request', 'paid')


    models = {
        u'onedollarpayments.recepient': {
            'Meta': {'object_name': 'Recepient'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stripe_token': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'onedollarpayments.request': {
            'Meta': {'object_name': 'Request'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '65', 'decimal_places': '2'}),
            'recepient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onedollarpayments.Recepient']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onedollarpayments.Sender']"})
        },
        u'onedollarpayments.sender': {
            'Meta': {'object_name': 'Sender'},
            'bank_account_number': ('django.db.models.fields.IntegerField', [], {'default': 'None'}),
            'bank_routing_number': ('django.db.models.fields.IntegerField', [], {'default': 'None'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['onedollarpayments']