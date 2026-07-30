# Heartbox — i3/sway colors
# class                 border              bground             text                indicator           child_border
client.focused          #B82E18     #1C1617 #EDE6DE #B8BEC2   #B82E18
client.focused_inactive #3A3232 #090909 #8A7874 #3A3232 #3A3232
client.unfocused        #090909 #090909 #8A7874 #090909 #090909
client.urgent           #C45A20  #C45A20     #090909 #C45A20  #C45A20
client.placeholder      #090909 #090909 #EDE6DE #090909 #090909
client.background       #090909

bar {
    colors {
        background #090909
        statusline #EDE6DE
        separator  #3A3232
        focused_workspace  #B82E18 #B82E18 #090909
        active_workspace   #56180A #1C1617 #EDE6DE
        inactive_workspace #090909 #090909 #8A7874
        urgent_workspace   #C45A20 #C45A20 #090909
    }
}
