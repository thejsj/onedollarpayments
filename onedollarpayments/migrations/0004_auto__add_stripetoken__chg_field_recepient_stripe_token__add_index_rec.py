# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StripeToken'
        db.create_table(u'onedollarpayments_stripetoken', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stripe_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('livemode', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.IntegerField')(default=None, blank=True)),
            ('used', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'onedollarpayments', ['StripeToken'])


        # Renaming column for 'Recepient.stripe_token' to match new field type.
        db.rename_column(u'onedollarpayments_recepient', 'stripe_token', 'stripe_token_id')
        # Changing field 'Recepient.stripe_token'
        db.alter_column(u'onedollarpayments_recepient', 'stripe_token_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onedollarpayments.StripeToken']))
        # Adding index on 'Recepient', fields ['stripe_token']
        db.create_index(u'onedollarpayments_recepient', ['stripe_token_id'])


    def backwards(self, orm):
        # Removing index on 'Recepient', fields ['stripe_token']
        db.delete_index(u'onedollarpayments_recepient', ['stripe_token_id'])

        # Deleting model 'StripeToken'
        db.delete_table(u'onedollarpayments_stripetoken')


        # Renaming column for 'Recepient.stripe_token' to match new field type.
        db.rename_column(u'onedollarpayments_recepient', 'stripe_token_id', 'stripe_token')
        # Changing field 'Recepient.stripe_token'
        db.alter_column(u'onedollarpayments_recepient', 'stripe_token', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        u'onedollarpayments.recepient': {
            'Meta': {'object_name': 'Recepient'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stripe_token': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onedollarpayments.StripeToken']"})
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
        },
        u'onedollarpayments.stripetoken': {
            'Meta': {'object_name': 'StripeToken'},
            'created': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'livemode': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stripe_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['onedollarpayments']