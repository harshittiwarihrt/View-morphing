#############################################################################
# Generated by PAGE version 4.14
# in conjunction with Tcl version 8.6
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(active_menu_fg) #000000
}

#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top37
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top37
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    set site_3_0 $base.can38
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top37 {base} {
    if {$base == ""} {
        set base .top37
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#d9d9d9} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x450+428+145
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1370 749
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "View Morphing"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    canvas $top.can38 \
        -background {#d9d9d9} -borderwidth 2 -closeenough 1.0 -height 453 \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -relief ridge -selectbackground {#c4c4c4} \
        -selectforeground black -width 313 
    vTcl:DefineAlias "$top.can38" "Canvas1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.can38
    entry $site_3_0.ent40 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent40" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab38 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Image 1} 
    vTcl:DefineAlias "$site_3_0.lab38" "Label1" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but39 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command button1comm \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {Select Image} 
    vTcl:DefineAlias "$site_3_0.but39" "Button1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab39 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Image 2} 
    vTcl:DefineAlias "$site_3_0.lab39" "Label2" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent41 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent41" "Entry2" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but42 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text {Select Image} 
    vTcl:DefineAlias "$site_3_0.but42" "Button2" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but38 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text {Start Processing} 
    vTcl:DefineAlias "$site_3_0.but38" "Button3" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.ent40 \
        -in $site_3_0 -x 30 -y 90 -width 184 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab38 \
        -in $site_3_0 -x 30 -y 60 -anchor nw -bordermode ignore 
    place $site_3_0.but39 \
        -in $site_3_0 -x 230 -y 90 -anchor nw -bordermode ignore 
    place $site_3_0.lab39 \
        -in $site_3_0 -x 30 -y 160 -width 48 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent41 \
        -in $site_3_0 -x 30 -y 190 -width 184 -height 20 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but42 \
        -in $site_3_0 -x 230 -y 190 -width 78 -height 24 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but38 \
        -in $site_3_0 -x 140 -y 310 -anchor nw -bordermode ignore 
    canvas $top.can39 \
        -background {#d9d9d9} -borderwidth 2 -closeenough 1.0 -height 453 \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -relief ridge -selectbackground {#c4c4c4} \
        -selectforeground black -width 303 
    vTcl:DefineAlias "$top.can39" "Canvas2" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.can38 \
        -in $top -x -10 -y 0 -width 313 -relwidth 0 -height 453 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.can39 \
        -in $top -x 300 -y 0 -width 303 -relwidth 0 -height 453 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top37 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

