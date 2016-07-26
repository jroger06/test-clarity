#!/usr/bin/env python

"""gzcjxeyv_ooip_kllyozf generator."""

# Import all the modules you need here:
import clarity


class MyAttribute(clarity.ClarityAttribute):
    # Optional (meaning that this function can be safely deleted)
    def check(self):
        """
        If in order to create the attribute, some prerrequisites are needed
        this is where all the checks should be included.
        If you need to, overwrite the content of this function. If you don't,
        just leave it as it is, or delete it.
        """
        # Do nothing
        pass

    # Mandatory
    def build(self):
        """
        This is where all the build functionality goes. When you build a new attribute,
        you need to replace most of the example code provided here with your own.
        """

        # It is highly recommended that you use the python SDK provided by Clarity to
        # build queries, log messages or connect with services such as Hive or Impala.
        # The following example shows you how to do it:

        # Get output name based on class and env. The output name should always be
        # obtained like this, so yuo can reuse this line.
        output_name = self.clarity_output_name()

        ####################################################################################
        # The following code is an example and can be deleted                              #
        ####################################################################################

        # Create your own queries here like this:
        creator_query = "create table {} (PersonID int,LastName varchar(255))".format(
            output_name
        )

        # and log messages using the clarity logger:
        self.clarity.logger.debug(
            "Build attribute {}. Create table with name {}.".format(
                self.source_file, output_name)
        )

        # you can also use clarity to connect with Hive and Impala
        self.clarity.drop_table(output_name)
        self.clarity.do_hive(creator_query)

        # or call other functions to structure your code and make it cleaner
        self.dummy_function()

        ####################################################################################

    # Example (meaning that this function can be safely deleted)
    def dummy_function(self):
        """
        This is a dummy function that illustrates that you can create as many functions as
        you want, as long as you remember to call them from the check or build functions.
        You can delete this function when you start building your own attribute.
        """
        # Do nothing
        pass


if __name__ == "__main__":
    attr = MyAttribute()
