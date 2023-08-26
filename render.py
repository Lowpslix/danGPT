import re

import streamlit as st

bot_msg_container_html_template = """
<div style='background-color: #FFFFFF; padding: 10px; border-radius: 5px; margin-bottom: 10px; display: flex'>
    <div style="width: 20%; display: flex; justify-content: center">
        <img src="https://www.fuqua.duke.edu/shared/images/pics/fac_staff/mkt/fs_dandan.jpg" style="max-height: 50px; max-width: 50px; border-radius: 50%;">
    </div>
    <div style="width: 80%;">
        $MSG
    </div>
</div>
"""

user_msg_container_html_template = """
<div style='background-color: #FFFFFF; padding: 10px; border-radius: 5px; margin-bottom: 10px; display: flex'>
    <div style="width: 78%">
        $MSG
    </div>
    <div style="width: 20%; margin-left: auto; display: flex; justify-content: center;">
        <img src="https://www.maddisoncreative.co.uk/wp-content/uploads/2022/11/ape-7020995_1280.png" style="max-width: 50px; max-height: 50px; float: right; border-radius: 50%;">
    </div>    
</div>
"""
