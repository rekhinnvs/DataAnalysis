import unicodecsv

enrollments_filename = 'enrollments.csv'

## Longer version of code (replaced with shorter, equivalent version below)

# enrollments = []
# f = open(enrollments_filename, 'rb')
# reader = unicodecsv.DictReader(f)
# for row in reader:
#     enrollments.append(row)
# f.close()

with open(enrollments_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)

engagement_filename = '/dataset/daily_engagement.csv'
submissions_filename = '/dataset/project_submissions.csv'
enrollments_filename = '/dataset/enrollments.csv'

with open(engagement_filename, 'rb') as file:
    reader = unicodecsv.DictReader(file)
    daily_engagement = list(reader)
    #print len(daily_engagement)
    #print(daily_engagement[0])  # Replace this with your code
    unique_engagement_student = set()
    for engagement_key in daily_engagement:
        engagement_key['account_key'] = engagement_key['acct']
        del engagement_key['acct']
    for student in daily_engagement:
        unique_engagement_student.add(student['account_key'])
    print daily_engagement[0]
    print "Total Unique Engagments ",len(unique_engagement_student)

with open(enrollments_filename,'rb') as file:
    reader = unicodecsv.DictReader(file)
    total_enrollment = list(reader)
    unique_enrollments = set()
    for student in total_enrollment:
        unique_enrollments.add(student['account_key'])
    print "Total Unique Enrolement" ,len(unique_enrollments)


with open(submissions_filename, 'rb') as file:
    reader = unicodecsv.DictReader(file)
    project_submissions = list(reader)
    #print(project_submissions[0])

def read_csv(filename):
    with open(filename,'rb') as file:
        reader = unicodecsv.DictReader(file)
        return list(reader)

enrollments = read_csv(enrollments_filename)
project_submissions = read_csv(submissions_filename)
daily_engagement = read_csv(enrollments_filename)

1640
1302

136240
1237

3642
743