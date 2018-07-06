# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Tick_1yr_1hr.tickopen'
        db.alter_column(u'joins_tick_1yr_1hr', 'tickopen', self.gf('django.db.models.fields.CharField')(max_length='12'))

        # Changing field 'Tick_1yr_1hr.tickhigh'
        db.alter_column(u'joins_tick_1yr_1hr', 'tickhigh', self.gf('django.db.models.fields.CharField')(max_length='12'))

        # Changing field 'Tick_1yr_1hr.tickclose'
        db.alter_column(u'joins_tick_1yr_1hr', 'tickclose', self.gf('django.db.models.fields.CharField')(max_length='12'))

        # Changing field 'Tick_1yr_1hr.ticklow'
        db.alter_column(u'joins_tick_1yr_1hr', 'ticklow', self.gf('django.db.models.fields.CharField')(max_length='12'))

    def backwards(self, orm):

        # Changing field 'Tick_1yr_1hr.tickopen'
        db.alter_column(u'joins_tick_1yr_1hr', 'tickopen', self.gf('django.db.models.fields.DecimalField')(max_digits='8', decimal_places='2'))

        # Changing field 'Tick_1yr_1hr.tickhigh'
        db.alter_column(u'joins_tick_1yr_1hr', 'tickhigh', self.gf('django.db.models.fields.DecimalField')(max_digits='8', decimal_places='2'))

        # Changing field 'Tick_1yr_1hr.tickclose'
        db.alter_column(u'joins_tick_1yr_1hr', 'tickclose', self.gf('django.db.models.fields.DecimalField')(max_digits='8', decimal_places='3'))

        # Changing field 'Tick_1yr_1hr.ticklow'
        db.alter_column(u'joins_tick_1yr_1hr', 'ticklow', self.gf('django.db.models.fields.DecimalField')(max_digits='8', decimal_places='2'))

    models = {
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
            'ticktimestamp': ('django.db.models.fields.DateTimeField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['joins']