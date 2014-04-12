# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Recepient'
        db.create_table(u'onedollarpayments_recepient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('stripe_toke', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'onedollarpayments', ['Recepient'])

        # Adding model 'Sender'
        db.create_table(u'onedollarpayments_sender', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('stripe_toke', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'onedollarpayments', ['Sender'])

        # Adding model 'Request'
        db.create_table(u'onedollarpayments_request', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('recepient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onedollarpayments.Recepient'])),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onedollarpayments.Sender'])),
            ('stripe_toke', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'onedollarpayments', ['Request'])


    def backwards(self, orm):
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
            'stripe_toke': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'onedollarpayments.request': {
            'Meta': {'object_name': 'Request'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recepient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onedollarpayments.Recepient']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onedollarpayments.Sender']"}),
            'stripe_toke': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'onedollarpayments.sender': {
            'Meta': {'object_name': 'Sender'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stripe_toke': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['onedollarpayments']