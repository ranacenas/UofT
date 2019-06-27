from django import forms
from django.conf import settings
import requests
from decouple import config
import psycopg2
#from config1 import config2
import os
import string 
from django.core.validators import MinLengthValidator

#API Key


class CourseForm(forms.Form):
    code = forms.CharField(max_length=8, validators=[MinLengthValidator(8)])


    #params = config2()
    def search(self):
        """User inputs a course code and returns a dictionary"""
        course = self.cleaned_data['code']
      
        return course

    def c(self, campus, br):
      #for local dev
        db1 = 'uoftpre'
        user = config('USER')
        pw = config('PASSWORD')
        host = config('HOST')
        port = config('PORT')
        conn = psycopg2.connect(dbname = db1, user = user, password = pw, host = host, port=port)

      #heroku dev
      # DATABASE_URL = os.environ['DATABASE_URL']
      # conn = psycopg2.connect(DATABASE_URL, sslmode='require')

        cur = conn.cursor()
        cur2 = conn.cursor()
        sql = """SELECT code FROM allofuoft WHERE pre ILIKE '%{code}%' AND campus LIKE '{campus}' AND br LIKE '{br}'"""
        #sql2 = """SELECT coursename FROM allofuoft WHERE pre ILIKE '%{code}%' AND campus = '{campus}'"""
        new = sql.format(code=self, campus=campus, br=br)

        #new2 = sql2.format(code=self, campus=campus)
        cur.execute(new)
        #cur2.execute(new2)

        y = (cur.fetchall())
        #z = (cur2.fetchall())

        dic = {}

        dic['codee'] = y
        #dic['cnamee'] = z
        #cur.execute(new2)
        #z = (cur.fetchall())

        #dic['name'] = z
        cur.close()
        #cur2.close()
        
        #you = [list(i) for i in y]
        return dic
      


    

    def catch_rel(self):
        """type(self) = list
        
        returns a list with strings containing the Codes. 
        This function is usually used after the check function 
        (see below)
        
        catch_rel(['Completion', 'of', 'BIO325H1F']
        => ['BIO325H1F'] """
        Codes = ['H1', 'H3', 'H5', 'Y']
        
        catch = [course for code in Codes for course in self if code in course]
        return catch



    
    def check(self):
        """type(self) = str
        generates a new list
        
        check(['MATA36H3F and BIOA01H3F', 'Completion of CSC411H1F/CSC404H1F'])
        => ['MATA36H3', 'BIOA01H3', 'CSC411H1', 'CSC404H1F']"""
        
        L1_pre = self.replace("/", " ").split()
        # stripchars = ['[](),;']
        # for c in stripchars:
        #   s = L1_pre.replace(c, " ")
        strip_and = [code for code in L1_pre if code != "and"]
        strip_or = [code for code in strip_and if code != "or"]
        strip_charac = [s.strip("[") for s in strip_or]
        strip_charac = [s.strip("]") for s in strip_charac]
        strip_charac = [s.strip(")") for s in strip_charac]
        strip_charac = [s.strip("(") for s in strip_charac]
        strip_charac = [s.strip("/") for s in strip_charac]
        strip_charac = [s.strip("/(") for s in strip_charac]
        strip_charac = [s.strip(")/") for s in strip_charac]
        strip_charac = [s.strip(",") for s in strip_charac]
        strip_charac = [s.strip(";") for s in strip_charac]
        strip_charac = [s.strip("(70%") for s in strip_charac]
        

        L1_pre = strip_charac
        
        return L1_pre
 
class CampusForm(forms.Form):
    campus_choice = [('%', 'All'),
                     ('St. George', 'St. George'),
                     ('Scarborough', 'Scarborough'),
                     ('Mississauga', 'Mississauga')]
    campus = forms.ChoiceField(choices=campus_choice, label="campus")

    def search(self):
        """User inputs a course code and returns a dictionary"""
        campus = self.cleaned_data['campus']

        return campus

class BrForm(forms.Form):
    br_choice = [('%', 'All'),
                ('All', 'UTSG - No Breadth Requirements'),
                ("Creative and Cultural Representations", "UTSG - Creative and Cultural Representations"),
                ("Thought Belief and Behaviour", "UTSG - Thought, Belief, and Behaviour"),
                ("Society and Its Institutions", "UTSG - Society and Its Institutions"),
                ("Living Things and Their Environment", "UTSG - Living Things and Their Environment"),
                ("The Physical and Mathematical Universes", "UTSG - The Physical and Mathematical Universes"),
                ("Arts, Literature & Language", "UTSC - Arts, Literature & Language"),
                ("History, Philosophy & Cultural Studies", "UTSC - History, Philosophy & Cultural Studies"),
                ("Social & Behavioural Sciences", "UTSC - Social & Behavioural Sciences"),
                ("Natural Sciences","UTSC - Natural Sciences"),
                ("Quantitative Reasoning", "UTSC - Quantitative Reasoning"),
                ("Humanities", "UTM - Humanities"),
                ("Social Science", "UTM - Social Science"),
                ("Science", "UTM - Science")]

    br = forms.ChoiceField(choices=br_choice, label="Breadth/Distribution Requirement")

    def search(self):
        """User inputs a course code and returns a dictionary"""
        br = self.cleaned_data['br']

        return br




