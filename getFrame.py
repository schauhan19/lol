import requests                                                                                                                                                                               
import subprocess                                                                                                                                                                             
                                                                                                                                                                                              
channel = 'tsm_dyrus'                                                                                                                                                                           
                                                                                                                                                                                              
r = requests.get('http://usher.justin.tv/find/%s.json?type=any' % (channel))                                                                                                                  
result = r.json()[0]                                                                                                                                                                          
                                                                                                                                                                                              
command = 'rtmpdump --swfUrl http://www.justin.tv/widgets/live_embed_player.swf --jtv \'%s\' --live -r %s/%s --stop 1 | avconv -i - -s 1920x1080 -vframes 1 file.png' % (result['token'], result['connect'], result['play'])                                                                                                                                                                  
                                                                                                                                                                                              
subprocess.call(command, shell=True) 