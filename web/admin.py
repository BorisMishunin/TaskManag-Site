from django.contrib import admin
from web.models import comments, projects, tasks, tasks_files, users_param, positions

admin.site.register(comments)
admin.site.register(projects)
admin.site.register(tasks)
admin.site.register(tasks_files)
admin.site.register(users_param)
admin.site.register(positions)



