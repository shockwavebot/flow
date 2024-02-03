# Concepts 

Terminology:
- Flow - tool for composing and executing shell scripts in test-like manner
- Step - specific indenpendent action that can be executed sequentally or in parallel with some other step
  - Setup - conditional requirement for each step that is done before actual step execution starts
  - Teardown -  conditional post-action after each step, can be used for managing resources for that step, processing results etc.
- Project (Scenario) - flow of steps, ordered list with ability to specify what is run in parallel and what is run sequentally, also can have setup and teardown
- Config files - 
- Variable - Any variable that can be defined in any file and overriden in any other file
- Step - specific indenpendent action that can be executed sequentally or in parallel with some other step 
- Test - calling specific project with customised variables 

## Files 

### Config file
### Rules file 
### Build file 

## Stages

### Build

- Expensive and time consuming process - many projects/tests can share and reuse one build
- Creates a dir tree with execution products(results) 


### Run 

- During run we can initiate a new build or use existing one 

```
Scenario: 

setup 

kobaz 1
kobaz 2, kobaz3 
kobaz 4 

teardown 
```
