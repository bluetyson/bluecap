"""
Copyright (C) 2019, Monash University, Geoscience Australia
Copyright (C) 2018, Stuart Walsh 

Bluecap is released under the Apache License, Version 2.0 (the "License");
you may not use this software except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

The project uses third party components which may have different licenses. 
Please refer to individual components for more details.

"""

import subprocess
import os

def GetGitSha():
   fileDir = os.path.dirname(os.path.abspath(__file__))
   cmd = "cd " +fileDir + "; git rev-parse --short HEAD"
   print cmd
   returned_value = subprocess.check_output(cmd,shell="True")
   returned_value = returned_value.strip(' \n\t')
   
   return returned_value
 



  