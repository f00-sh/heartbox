# Heartbox — i3/sway colors
# class                 border              bground             text                indicator           child_border
client.focused          #E03818     #142238 #EDE6DE #B8C0C8   #E03818
client.focused_inactive #2A3548 #0A1528 #6E7A8A #2A3548 #2A3548
client.unfocused        #0A1528 #0A1528 #6E7A8A #0A1528 #0A1528
client.urgent           #E06028  #E06028     #0A1528 #E06028  #E06028
client.placeholder      #0A1528 #0A1528 #EDE6DE #0A1528 #0A1528
client.background       #0A1528

bar {
    colors {
        background #0A1528
        statusline #EDE6DE
        separator  #2A3548
        focused_workspace  #E03818 #E03818 #0A1528
        active_workspace   #4E1A22 #142238 #EDE6DE
        inactive_workspace #0A1528 #0A1528 #6E7A8A
        urgent_workspace   #E06028 #E06028 #0A1528
    }
}
