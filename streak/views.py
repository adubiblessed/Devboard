# from django.shortcuts import render
# from django.utils import timezone
# from datetime import timedelta

# from .models import Streak
# # Create your views here.


# def update_user_streak(user):
#     today = timezone.now().date()
#     streak, created = Streak.objects.get_or_create(user=user)

#     if streak.last_activity is None:
#         # First time ever
#         streak.streak_count = 1
#     else:
#         days_since_last = (today - streak.last_activity).days

#         if days_since_last == 1:
#             # Consecutive day - increment streak
#             streak.streak_count += 1
#         elif days_since_last > 1:
#             # Missed a day - reset streak
#             streak.streak_count = 1
#         # if days_since_last == 0, same day - do nothing

#     streak.last_activity = today
#     streak.save()

# def create_note_view(request):
#     if request.method == 'POST':
#         # ... your note creation logic

#         # Update streak
#         update_user_streak(request.user)

#         # redirect or render response
