import settings

OPENID_REDIRECT_NEXT = '/accounts/openid/done/'

OPENID_SREG = {"requred": "nickname, email, fullname",
               "optional":"postcode, country",
               "policy_url": ""}

#example should be something more like the real thing, i think
OPENID_AX = [{"type_uri": "http://axschema.org/contact/email",
              "count": 1,
              "required": True,
              "alias": "email"},
             {"type_uri": "http://axschema.org/schema/fullname",
              "count":1 ,
              "required": False,
              "alias": "fname"}]

OPENID_AX_PROVIDER_MAP = {'Google': {'email': 'http://axschema.org/contact/email',
                                     'firstname': 'http://axschema.org/namePerson/first',
                                     'lastname': 'http://axschema.org/namePerson/last'},
                          'Default': {'email': 'http://axschema.org/contact/email',
                                      'fullname': 'http://axschema.org/namePerson',
                                      'nickname': 'http://axschema.org/namePerson/friendly'}
                          }

if settings.DEBUG:
    TWITTER_CONSUMER_KEY = 'PqoYQezQY5iXM0TmzPFOw'
    TWITTER_CONSUMER_SECRET = 's69v6PqByE71vP6S0usfk4j6e5MeUyeNkCWCQm3vwrA'

    FACEBOOK_APP_ID = '141364582585691'
    FACEBOOK_API_KEY = '841275542085a002d1077c5347ce389f'
    FACEBOOK_SECRET_KEY = 'b40ac404919fb2150a87b5462749ec91'

    LINKEDIN_CONSUMER_KEY = ''
    LINKEDIN_CONSUMER_SECRET = ''
else:
    TWITTER_CONSUMER_KEY = 'ni1HGsMNz2uar9Y9H9eiQ'
    TWITTER_CONSUMER_SECRET = 'nL96wXkMikKK8FNoOU4RaRcoR0v7cMveP7TjJHJg'

    FACEBOOK_APP_ID = '151052074945727'
    FACEBOOK_API_KEY = '2aa8960b27cfe0b769d739326f4e545e'
    FACEBOOK_SECRET_KEY = 'cb0b2cf55244af72861403e3078231bd'

    LINKEDIN_CONSUMER_KEY = 'Me-21YpxKgwuc2LQ3wVYB-fAD3rJEgGajZzJYLYx7_wMBBQOTlIltZtpMJMXAeW5'
    LINKEDIN_CONSUMER_SECRET = 'CdwLcIXThkx_heAmq8GYyTT6u2_8TFVEVlHKZGUo-fWP8Cm4qRrfAAvdyQ3MxYN7'

## if any of this information is desired for your app
FACEBOOK_EXTENDED_PERMISSIONS = (
    #'publish_stream',
    #'create_event',
    #'rsvp_event',
    #'sms',
    #'offline_access',
    #'email',
    #'read_stream',
    #'user_about_me',
    #'user_activites',
    #'user_birthday',
    #'user_education_history',
    #'user_events',
    #'user_groups',
    #'user_hometown',
    #'user_interests',
    #'user_likes',
    #'user_location',
    #'user_notes',
    #'user_online_presence',
    #'user_photo_video_tags',
    #'user_photos',
    #'user_relationships',
    #'user_religion_politics',
    #'user_status',
    #'user_videos',
    #'user_website',
    #'user_work_history',
    #'read_friendlists',
    #'read_requests',
    #'friend_about_me',
    #'friend_activites',
    #'friend_birthday',
    #'friend_education_history',
    #'friend_events',
    #'friend_groups',
    #'friend_hometown',
    #'friend_interests',
    #'friend_likes',
    #'friend_location',
    #'friend_notes',
    #'friend_online_presence',
    #'friend_photo_video_tags',
    #'friend_photos',
    #'friend_relationships',
    #'friend_religion_politics',
    #'friend_status',
    #'friend_videos',
    #'friend_website',
    #'friend_work_history',
)


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'socialauth.auth_backends.OpenIdBackend',
    'socialauth.auth_backends.TwitterBackend',
    'socialauth.auth_backends.FacebookBackend',
    'socialauth.auth_backends.LinkedInBackend',
)
