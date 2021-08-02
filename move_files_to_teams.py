import os
import shutil

t1 = [123534,122868,121550,120897,120101]
t2 = [120904,124990,121938,123900,124133]
t3 = [121243,122431,122084,122263]
t4 = [124059,121104,128079,121804,122061]
t5 = [123295,123525,123673,122152,123864]

students = [t1, t2, t3, t4, t5]

files = os.listdir('.')

# Remove empty folder
for afile in files:
   #check that the file is a directory
   if os.path.isdir(afile):
      #remove directory, only empty directory can be removed, which is our intention
      try:
         os.rmdir(afile)
      except OSError:
         pass

# Create Team Folder
for i in range(1, 6):
   filename = "Team " + str(i)
   if not os.path.exists (filename):
      os.mkdir(filename)

# Copy folder
count = 1
for tt in students:
    for t in tt:
        t = str(t)
        t = "Student " + t
        if os.path.exists(t):
            desc = 'Team ' + str(count) + '/' + t + '/'
            print (desc)
            if not os.path.exists(desc):
                shutil.copytree(t, desc)

        # remove student folder
        if os.path.exists(t):
            shutil.rmtree(t)

    count += 1
