# Heartbox — i3/sway colors
# class                 border              bground             text                indicator           child_border
client.focused          #E02030     #2C1F22 #F4EBE0 #B8C0C8   #E02030
client.focused_inactive #4A3A3E #1A1214 #8A6E78 #4A3A3E #4A3A3E
client.unfocused        #1A1214 #1A1214 #8A6E78 #1A1214 #1A1214
client.urgent           #E8924A  #E8924A     #1A1214 #E8924A  #E8924A
client.placeholder      #1A1214 #1A1214 #F4EBE0 #1A1214 #1A1214
client.background       #1A1214

bar {
    colors {
        background #1A1214
        statusline #F4EBE0
        separator  #4A3A3E
        focused_workspace  #E02030 #E02030 #1A1214
        active_workspace   #3A2428 #2C1F22 #F4EBE0
        inactive_workspace #1A1214 #1A1214 #8A6E78
        urgent_workspace   #E8924A #E8924A #1A1214
    }
}
