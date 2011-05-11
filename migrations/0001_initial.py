# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Address'
        db.create_table('phonebook_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('entry', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['phonebook.Entry'], unique=True)),
        ))
        db.send_create_signal('phonebook', ['Address'])

        # Adding model 'Entry'
        db.create_table('phonebook_entry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('phonebook', ['Entry'])


    def backwards(self, orm):
        
        # Deleting model 'Address'
        db.delete_table('phonebook_address')

        # Deleting model 'Entry'
        db.delete_table('phonebook_entry')


    models = {
        'phonebook.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'entry': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['phonebook.Entry']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'phonebook.entry': {
            'Meta': {'ordering': "['last_name', 'first_name']", 'object_name': 'Entry'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['phonebook']
