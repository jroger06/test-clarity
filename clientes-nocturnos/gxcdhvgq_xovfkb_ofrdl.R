#!/usr/bin/Rscript

library(clarity)

# Optional (meaning that this function can be safely deleted)
check_prerequisites <- function(){
  #If in order to create the attribute, some prerequisites are needed
  #this is where all the checks should be included.
  #If you need to, overwrite the content of this function. If you don't,
  #just leave it as it is or delete it.

  # Do nothing
  return()
}

# Mandatory
build_table <- function(){
  #This is where all the build functionality goes. When you build a new attribute,
  #you need to replace most of the example code provided here with your own.

  # It is highly recommended that you use the R SDK provided by Clarity to
  # build queries or connect with services such as Hive or Impala.
  # The following example shows you how to do it:

  # Get output name based on class and env. The output name should always be
  # obtained like this, so you can reuse this line.
  outnam <- clarity_output_table_name()

  ####################################################################################
  # The following code is an example and can be deleted                              #
  ####################################################################################

  # Create your own queries here like this:
  sql <- paste('create table', outnam, '(PersonID int,LastName varchar(255))')

  # You can also use clarity to connect with Hive and Impala
  drop_table(outnam)
  do_hive(sql)

  # or call other functions to structure your code and make it cleaner
  dummy_function()

  TRUE
  ####################################################################################
}

# Example (meaning that this function can be safely deleted)
dummy_function <- function(){
  #This is a dummy function that illustrates that you can create as many functions as
  #you want, as long as you remember to call them from the check or build functions.
  #You can delete this function when you start building your own attribute.

  # Do nothing
  return()
}