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
               linter_configs=set()):
        retval = defaultdict(lambda: defaultdict(list))
        if len(filenames) == 0:
            cmd = "find %s/cookbooks -type d -maxdepth 1 ! -path %s/cookbooks | xargs foodcritic" % (dirname, dirname)
        else:
            if 'cookbooks' not in filenames:
                return retval
            filenames = ["%s/%s" % (dirname, "/".join(filename.split('/')[:2])) for filename in filenames]
            filnames = list(set(filenames))
            cmd = "foodcritic %s" % (" ".join(filenames))
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
