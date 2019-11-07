#!/bin/bash                                                                                                                                                                                                   
# ##########################################################################                           
# Author: Guannan Ma                                                                                              
# Brief:  Upload cup to pypi                                                                                             
#                                                                                                      
# Returns:                                                                                             
#   succ: 0                                                                                            
#   fail: not 0                                                                                        
# ##########################################################################   
rm -rf ./build ./output ./*.egg-info
python setup.py sdist
twine upload  ./output/dist/*.tar.gz
