from imhotep.tools import Tool
from collections import defaultdict
import json
import os
import logging

log = logging.getLogger(__name__)


class FoodCritic(Tool):

    def invoke(self,
               dirname,
               filenames=set(),
               config_file=None,
               file_list=None):
        retval = defaultdict(lambda: defaultdict(list))
        if file_list is None:
            cmd = "find %s/cookbooks -type d -maxdepth 1 ! -path %s/cookbooks xargs foodcritic" % (dirname, dirname)
        else:
            cmd = "foodcritic %s" % (" ".join(file_list))
        log.debug("Command: %s", cmd)
        try:
            output = self.executor(cmd)
            for line in output.split('\n'):
                rule, message, file_name, line_number = line.split(':')
                file_name = file_name.lstrip()
                file_name = file_name.replace(dirname, "")[1:]
                message = "[%s](http://acrmp.github.io/foodcritic/#%s): %s" % (rule, rule, message)
                retval[file_name][line_number].append(message)
        except:
            pass
        return retval
