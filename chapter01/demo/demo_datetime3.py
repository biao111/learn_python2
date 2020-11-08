from datetime import datetime,timedelta

now_ = datetime.now()
now_before = now_ - timedelta(days=3,hours=36,minutes=12)
print(now_before)

now_after = now_ + timedelta(days=10)
print(now_after)