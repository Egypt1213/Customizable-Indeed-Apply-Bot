# bot settings you can change -- options listed to the right
job_posting_age = '1'  # all, 1, 3, 7, 14 (these are days)
job_posting_type = 'all'  # all, full-time, contract, part-time, internship, temporary
job_posting_experience = 'all'  # all, entry, mid, senior
job_posting_distance = '25'  # default 5, 10, 15, 25, 50, 100 (these are miles)

# change these to your information
account_email = ''  # your indeed email
account_password = ''  # your indeed password
job_titles = ['python developer',]  # separate job titles must be in quotations separated by a comma
job_location = '30340'  # job zip

# apply personal answers
add_address = 'xxxx'
add_phone = 'xxxxx'
add_website = 'www.indeed.com'
add_city = 'pompano beach'
add_postal = '33069'
add_state = 'FLorida'
add_github = ''
add_valid_cert = 'no'
add_university = 'university of michagin'
add_linkedin = 'www.linkedin.com'
add_personalwebsite = 'www.me.com'
add_stateresident = 'yes'  # yes, no -- are you a state resident
add_sponsorship = 'no'  # yes, no -- will you need work sponsorship
add_relocate = 'yes'  # yes, no -- resident of ga or willing to relocate
add_workauthorized = 'yes'  # yes, no -- authorized to work in us
add_citizen = 'yes'  # yes, no -- us citizen
add_education = 'Associate'  # other, highschool, associate, bachelor, master, doctorate -- education level
add_leadershipdevelopment = '5'  # years
add_salary = '60k'
add_gender = 'male' # male, female, decline
add_veteran = 'no' # yes, no, decline -- veteran status
add_disability = 'no' # yes, no, decline -- disability status
add_commute = 'no' # yes, no, decline -- commute status
add_valid_cert = ''
default_unknown_multi = 'no'

# language experience years

add_java = '1'
add_aws = '0.5'
add_python = '4'
add_analysis = '2'
add_django = '1'
add_php = '5'
add_react = '0'
add_node = '0'
add_angular = '0'
add_javascript = '3'
ad_orm = '0'
add_sdet = '0'
add_selenium = '0'
add_testautomation = '0'
add_webdevyears = '10'
add_programming = '2'
add_default_experience = '1'
# don't change these - you break it you buy it
base_url = 'https://indeed.com'
login_url = 'https://secure.indeed.com/account/login?hl=en_US&co=US&continue=https%3A%2F%2Fwww.indeed.com%2F&tmpl=desktop&service=my&from=gnav-util-homepage'
page_timeout = 30
long_timeout = 300
job_urls = []

date_posted = {
    'all': '',
    '1': '&fromage=1',
    '3': '&fromage=3',
    '7': '&fromage=7',
    '14': '&fromage=14'
}

job_type = {
    'all': '',
    'full-time': '&jt=fulltime',
    'contract': '&jt=contract',
    'part-time': '&jt=parttime',
    'internship': '&jt=internship',
    'temporary': '&jt=temporary'
}

experience_level = {
    'all': '',
    'entry': '&explvl=entry_level',
    'mid': '&explvl=mid_level',
    'senior': '&explvl=senior_level'
}

job_distance = {
    'default': '',
    '5': '&radius=5',
    '10': '&radius=10',
    '15': '&radius=15',
    '25': '&radius=25',
    '50': '&radius=50',
    '100': '&radius=100'
}

apply_veteranoptions = {
    'no' : 'i am not',
    'yes' : 'i identify as one',
    'decline' : "i don't wish"
}

apply_disabilityoptions = {
    'no' : 'no',
    'yes' : 'yes',
    'decline' : "i don't wish"
}