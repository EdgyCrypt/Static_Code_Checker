# Static_Code_Checker

## PROJECT CHARTER

Static_Code_Checker is a system used to help students check their own code and professors to grade a system. It takes input, output and an executable file and compares the two outputs. 

### ABSTRACT


Authors:
- Matt Brown
- Will Fitzgerald
- Jake Gadaleta
- Nick Hertzog

#### [Contents](###Contents)

1. [Project Summary](###Project%20Summary)
2. [Team](###Team)
3. [Scope](###Scope)

    3.1. [Goals and Objectives](####Goals%20and%20Objectives)

    3.2. [Deliverables](####Deliverables)

    3.3. [Stakeholders](####Stakeholders)

    3.4. [Out-Of-Scope](####Out-Of-Scope)

4. [Success Measurement](###Success%20Measurement)
5. [Signatures](###Signatures)
6. [Appendix A - Glossary](###Appendix%20A)

### Project Summary

Grading code is a very time-consuming task. We aim to make this easier for both students and professors alike. Students armed with an input and output file will test their code against their professors expected outputs giving them the difference so they can correct prior to submission. For professors, the application will run and test a student's code and provided information on whether or not the inputs match.


### Team

| Name           | Primary Role | Secondary Role | Tertiary Role |
|----------------|--------------|----------------|---------------|
| Matt Brown     |Designer      |Programmer      |               |
| Will Fitzgerald|Commenter     |Dev Ops         |Programmer     |
| Jake Gadaleta  |Supreme Leader|Dev Ops         |Programmer     |
| Nick Hertzog   |Programmer    |Designer        |Dev Ops        |

### Scope

The scope of this project is to provide a deliverable file that a user can run locally on their machine. This software is not an IDE but does have similar features to an IDE. A user should be able to import their code and edit it within the software. The software will be able to compile Python and Java code. The user's code will be tested with a set of inputs designated within a file and tested to see if the user's output matches the desired output.

#### Goals and Objectives

This product will include:

- A grading system
- The ability for students to edit code in the app
- Editable input files that feed input to the users
- Editable output files that check outputs against 
- Code compellation of the Java Programing Language
- Code compellation of the Python (c) Programming Language



#### Deliverables

All listed functions as either:
    - An easy to run executable file
    - A pip install-able package

#### Stakeholders


| Role | Interest / Impact |
|------|--------------------|
| Students      | To test their code against those of their professors                   |
| Professors    | Test and auto grade assignments from students                          |
| Interviewees  | Quickly compare answers to given questions with no IDE support         |

#### Out-Of-Scope

This product will not include

| Risk/Constraint/Assumption Title | Explanation |
|-------------------------------------------------------|------------------------------------------------------------------------|
| No support for Code completion for any available programing language  | It's expensive and unreasonable for a 3 month long project             |
|  No support Code Linting or Control                               | We aim to edit raw text, this is not an IDE and should not be treated as such|
| This is NOT a web app                                 | The application can result in security flaws as users will be able to pass commands into the system |
| This application will not have all the answers        | This is not the be-all end all in coding education it is mearly a tool|

### Success Measurement

Static_Code_Checker will measure its success by the complexation of a stable version of the application that can easily be opened by the most technologically illiterate people. Distributed with github and possibly hosted on [PyPi](https://pypi.org/).

Another measurement would be a seal of approval by the DeSales University Computer Science Department

### Signatures

The signatures of the people below document approval of the formal Project Charter.  The project manager is empowered by this charter to proceed with the project as outlined in the charter.


#### Customer

| Name | Signature | Date |
|------|-----------|------|
|      |           |      |
|      |           |      |
|      |           |      |

#### Project Manager

| Name | Signature | Date |
|------|-----------|------|
|      |           |      |
|      |           |      |
|      |           |      |

#### Team Members

| Name | Signature | Date |
|------|-----------|------|
|      |           |      |
|      |           |      |
|      |           |      |

### Appendix A



### Additional Notes

For user setup information please refer to the [README](README.md)

For usage information please read [User Guide](USER_GUIDE.md)

For developer setup please refer to [DEV](DEV.md)
