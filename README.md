#Project Remez
Decent external explination of the project; http://www.boost.org/doc/libs/1_46_1/libs/math/doc/sf_and_dist/html/math_toolkit/backgrounders/remez.html
Try using this form of notation; http://en.wikipedia.org/wiki/CamelCase
The video an ex-student had made; https://www.youtube.com/watch?v=f02mC61_RAo

#If you need ideas on what to work with; check the issues tab.

Some guidelines for using github; in order to prevent errors when merging code,
that usually occurs when two coders work in the same area of the code,
we need to work branch by branch. This means that for each feature we add
we should introduce it by pushing in a new branch. 

The easiest way to go about this is to create a new branch to the main repository,
and ultimatly on the more advanced level branch on the branch.
Before merging the new code you must check so that on your side the repository is up to date,
by syncing the upper-level-branch/master.

The buttomline is; dont work on the same lines or branches as someone else.

#FlowChart of how the typical worksituation could look like.

(1) Update your local version of 'master', by syncing in the GIU : (2) Create a new Branch, from the master,
with an appropriate name : (3) Code what you should code, and one feature per branch, DO NOT TOUCH ANY OTHER PARTS OF THE CODE 
: (4) Commit the changes in the GIU application, and sync : (5) Create a Pull Request on the website : (6) Wait for feedback,
and ultimatly we want to merge several pull requests at a time, to avoid complications.
