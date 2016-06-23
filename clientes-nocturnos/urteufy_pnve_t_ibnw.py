#!/usr/bin/env python

"""urteufy_pnve_t_ibnw generator."""

import clarity


class MyAttribute(clarity.ClarityAttribute):

    def build(self):
        # Get output name based on class and env.
        output_name = self.clarity_output_name()

        # Create build sql
        creator_query = "create table {} (PersonID int,LastName varchar(255))".format(
            output_name
        )

        self.clarity.logger.debug(
            "Build attribute {}. Create table with name {}.".format(
                self.source_file, output_name)
        )

        # Drop table here.
        self.clarity.drop_table(output_name)

        # Do hive.
        self.clarity.do_hive(creator_query)


if __name__ == "__main__":

    attr = MyAttribute()
