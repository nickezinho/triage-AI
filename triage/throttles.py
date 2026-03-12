from rest_framework.throttling import AnonRateThrottle

class TriageRateThrottle(AnonRateThrottle):
    rate = '3/day'