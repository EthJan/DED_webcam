import gi
import subprocess
from gi.repository import Gtk, GdkX11, Gdk

# Load the Glade file
builder = Gtk.Builder()
builder.add_from_file("my_ui.glade")
#builder.add_from_file("/home/operator/tmc/python/images/tormach_mill_ui.glade")


# Get the main window and drawing area
window = builder.get_object("window1")
#window =builder.get_object("main_window")
drawing_area = builder.get_object("drawingarea1")

# Show the window
window.show_all()

# Get the XID of the drawing area
xid = drawing_area.get_window().get_xid()

# Run mplayer with the XID embedded in the drawing area
command = "mplayer tv:// -tv driver=v4l2:device=/dev/video0 -wid %d" % xid
subprocess.Popen(command, shell=True)

# Start the GTK main loop
Gtk.main()
