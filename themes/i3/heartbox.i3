# Heartbox — i3/sway colors
# class                 border              bground             text                indicator           child_border
client.focused          #E5141A     #3D2F2D #E8E4DC #C2C8CC   #E5141A
client.focused_inactive #3D2F2D #191413 #7A656A #3D2F2D #3D2F2D
client.unfocused        #191413 #191413 #7A656A #191413 #191413
client.urgent           #EA5638  #EA5638     #191413 #EA5638  #EA5638
client.placeholder      #191413 #191413 #E8E4DC #191413 #191413
client.background       #191413

bar {
    colors {
        background #191413
        statusline #E8E4DC
        separator  #3D2F2D
        focused_workspace  #E5141A #E5141A #191413
        active_workspace   #4B1006 #3D2F2D #E8E4DC
        inactive_workspace #191413 #191413 #7A656A
        urgent_workspace   #EA5638 #EA5638 #191413
    }
}
