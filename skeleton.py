#skeleton of code

|--htdocs_base
|--phpmyadmin_base
|--switcher_log
|--switcher.py
|--projects

#switcher.py

#function switcher(newprojectname):
    #go to switcher log
    #find site_name
    #look for site_name in /opt/lampp
    #look for activated site in switcher.py
    #if site name isn't in switcher.py:
        #throw an error
    #if it is there:
        # ask if user wants to make a backup of website
            #if yes, copy the whole shebang to somewhere
        
        # rename /opt/lampp/htdocs to opt/lampp/htdocs_oldprojectname
        # rename /opt/lampp/phpmyadmin to opt/lampp/phpmyadmin_oldprojectname
        # rename /opt/lampp/htdocs_newprojectname to htdocs
        # do the same thing but for the php 
        # if things went well:
            #print success!
        # else
            #state that there was an error, and tell how the user can restore to a backup. 

#switcher_log

    #should be some sort of dictionary file or something
    #[projectname | projectsize | activated? ]




