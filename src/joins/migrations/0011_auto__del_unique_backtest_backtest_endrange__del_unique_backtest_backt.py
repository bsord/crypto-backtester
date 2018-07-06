# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Backtest', fields ['ref_id']
        db.delete_unique(u'joins_backtest', ['ref_id'])

        # Removing unique constraint on 'Backtest', fields ['backtest_startrange']
        db.delete_unique(u'joins_backtest', ['backtest_startrange'])

        # Removing unique constraint on 'Backtest', fields ['backtest_endrange']
        db.delete_unique(u'joins_backtest', ['backtest_endrange'])


    def backwards(self, orm):
        # Adding unique constraint on 'Backtest', fields ['backtest_endrange']
        db.create_unique(u'joins_backtest', ['backtest_endrange'])

        # Adding unique constraint on 'Backtest', fields ['backtest_startrange']
        db.create_unique(u'joins_backtest', ['backtest_startrange'])

        # Adding unique constraint on 'Backtest', fields ['ref_id']
        db.create_unique(u'joins_backtest', ['ref_id'])


    models = {
        u'joins.backtest': {
            'Meta': {'object_name': 'Backtest'},
            'backtest_endrange': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'max_length': '120'}),
            'backtest_id': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'unique': 'True', 'max_length': '120'}),
            'backtest_interval': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'max_length': '120'}),
            'backtest_startrange': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'max_length': '120'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ref_id': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'max_length': '120'})
        },
        u'joins.join': {
            'Meta': {'unique_together': "(('email', 'ref_id'),)", 'object_name': 'Join'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'filepath': ('django.db.models.fields.CharField', [], {'default': "'default.py'", 'max_length': '120'}),
            'friend': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'referral'", 'null': 'True', 'to': u"orm['joins.Join']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'max_length': '120'}),
            'ref_id': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'unique': 'True', 'max_length': '120'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'joins.tick_1yr_1hr': {
            'Meta': {'object_name': 'Tick_1yr_1hr'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tickclose': ('django.db.models.fields.CharField', [], {'max_length': "'12'"}),
            'tickhigh': ('django.db.models.fields.CharField', [], {'max_length': "'12'"}),
            'ticklow': ('django.db.models.fields.CharField', [], {'max_length': "'12'"}),
            'tickopen': ('django.db.models.fields.CharField', [], {'max_length': "'12'"}),
            'ticktimestamp': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['joins']