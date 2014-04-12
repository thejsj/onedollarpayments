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
            ('stripe_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('livemode', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('used', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'onedollarpayments', ['StripeToken'])

        # Adding model 'Recepient'
        db.create_table(u'onedollarpayments_recepient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('stripe_token', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onedollarpayments.StripeToken'], null=True, blank=True)),
        ))
        db.send_create_signal(u'onedollarpayments', ['Recepient'])

        # Adding model 'Sender'
        db.create_table(u'onedollarpayments_sender', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('bank_routing_number', self.gf('django.db.models.fields.IntegerField')(default=None)),
            ('bank_account_number', self.gf('django.db.models.fields.IntegerField')(default=None)),
        ))
        db.send_create_signal(u'onedollarpayments', ['Sender'])

        # Adding model 'Request'
        db.create_table(u'onedollarpayments_request', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('recepient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onedollarpayments.Recepient'])),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onedollarpayments.Sender'])),
            ('quantity', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=65, decimal_places=2)),
            ('paid', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'onedollarpayments', ['Request'])


    def backwards(self, orm):
        # Deleting model 'StripeToken'
        db.delete_table(u'onedollarpayments_stripetoken')

        # Deleting model 'Recepient'
        db.delete_table(u'onedollarpayments_recepient')

        # Deleting model 'Sender'
        db.delete_table(u'onedollarpayments_sender')

        # Deleting model 'Request'
        db.delete_table(u'onedollarpayments_request')


    models = {
        u'onedollarpayments.recepient': {
            'Meta': {'object_name': 'Recepient'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stripe_token': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onedollarpayments.StripeToken']", 'null': 'True', 'blank': 'True'})
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
            'created': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'livemode': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stripe_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['onedollarpayments']