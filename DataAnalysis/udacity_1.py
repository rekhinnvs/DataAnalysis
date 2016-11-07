import unicodecsv


def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)


enrollments = read_csv('/home/rekhin/Rexo/Develop/Works/pythonWorks/DataAnalysis/dataset/enrollments.csv')
daily_engagement = read_csv('/home/rekhin/Rexo/Develop/Works/pythonWorks/DataAnalysis/dataset/daily_engagement.csv')
project_submissions = read_csv('/home/rekhin/Rexo/Develop/Works/pythonWorks/DataAnalysis/dataset/project_submissions.csv')

### For each of these three tables, find the number of rows in the table and
### the number of unique students in the table. To find the number of unique
### students, you might want to create a set of the account keys in each table.

print "Unique Student Enrollments"
#print enrollments[0]
unique_students = set()  # Replace this with your code
for reader in enrollments:
    unique_students.add(reader['account_key'])
    #print reader['account_key']
enrollment_num_rows = len(enrollments)  # Replace this with your code
enrollment_num_unique_student = len(unique_students)
print enrollment_num_rows
print enrollment_num_unique_student

print "Daily Engagements"
#print daily_engagement[len(daily_engagement)-1]
unique_student_engagement = set()
for reader in daily_engagement:
    unique_students.add(reader['acct'])  # Replace this with your code
    reader['account_key'] = reader['acct']
    del[reader['acct']]
unique_students_engagement = len(unique_students)
engagement_num_rows = len(daily_engagement)  # Replace this with your code
print engagement_num_rows
print unique_students_engagement

print "Project Submissions"
#print project_submissions[len(project_submissions)-1]
unique_students = set()
for reader in project_submissions:
    unique_students.add(reader['account_key'])
submission_num_rows = len(project_submissions)  # Replace this with your code
submission_num_unique_students = len(unique_students)  # Replace this with your code
print submission_num_rows
print submission_num_unique_students


def find_surprice():
    for read_enrolment in enrollments:
        if read_enrolment['account_key'] not in unique_student_engagement:
            print read_enrolment
            break
find_surprice()



