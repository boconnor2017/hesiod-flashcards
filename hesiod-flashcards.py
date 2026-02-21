# Import Hesiod libraries
from hesiod import lib_general as libgen
from hesiod import lib_json as libjson
from hesiod import lib_logs_and_headers as liblog 
from hesiod import lib_paramiko as libpko 

# Import Standard Python libraries
import os
import sys
import subprocess

# Import json configuration parameters
env_json_str = libjson.populate_var_from_json_file("json", "lab_environment.json")
env_json_py = libjson.load_json_variable(env_json_str)
this_script_name = os.path.basename(__file__)
logfile_name = env_json_py["logs"][this_script_name]

# Hesiod Header and Log init
liblog.hesiod_print_header()
liblog.hesiod_log_header(logfile_name)
err = "Successfully imported Hesiod python libraries."
liblog.write_to_logs(err, logfile_name)
err = "Succesfully initialized logs to "+logfile_name
liblog.write_to_logs(err, logfile_name)
err = ""
liblog.write_to_logs(err, logfile_name)

# Local Functions
def main():
    score = 0
    f=0 
    while f < len(env_json_py["flashcards"]):
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
        print("Question "+str(f+1))
        print(env_json_py["flashcards"][f]["Question"])
        c=0
        while c < len(env_json_py["flashcards"][0]["Choices"]):
            print(env_json_py["flashcards"][f]["Choices"][c])
            c=c+1
        print("")
        promptanswer = input("Answer: ")
        promptanswer = promptanswer.upper()
        if promptanswer == env_json_py["flashcards"][f]["Answer"]:
            print("Correct!")
            print("")
            print("")
            score = score+1
        else:
            print("Incorrect. The correct answer is "+env_json_py["flashcards"][f]["Answer"])
            print("")
            print("")
        f=f+1
    
    print("Your final score is "+str(score)+" out of "+str(len(env_json_py["flashcards"])))
    perc_score = (score/len(env_json_py["flashcards"]))*100
    print(str(score)+"/"+str(len(env_json_py["flashcards"]))+" is "+str(perc_score)+"%")
    print("")
    min_score = 80
    if perc_score > min_score:
        print("Congratulations! You passed!")
    else:
        print("To pass you need a minimum of "+str(min_score)+". You failed.")

main()