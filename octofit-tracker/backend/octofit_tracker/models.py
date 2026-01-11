from djongo import models

class User(models.Model):
	_id = models.ObjectIdField()
	name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	team = models.CharField(max_length=50)
	class Meta:
		db_table = 'users'

class Team(models.Model):
	_id = models.ObjectIdField()
	name = models.CharField(max_length=50, unique=True)
	members = models.JSONField()
	class Meta:
		db_table = 'teams'

class Activity(models.Model):
	_id = models.ObjectIdField()
	user = models.CharField(max_length=100)
	activity = models.CharField(max_length=100)
	duration = models.IntegerField()
	class Meta:
		db_table = 'activities'

class Leaderboard(models.Model):
	_id = models.ObjectIdField()
	team = models.CharField(max_length=50)
	points = models.IntegerField()
	class Meta:
		db_table = 'leaderboard'

class Workout(models.Model):
	_id = models.ObjectIdField()
	name = models.CharField(max_length=100)
	suggested_for = models.JSONField()
	class Meta:
		db_table = 'workouts'
