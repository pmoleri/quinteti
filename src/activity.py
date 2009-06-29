from sugar.activity.activity import ActivityToolbox
from olpcgames import activity
from gettext import gettext as _

#SERVICE = "org.laptop.HelloMesh"
#IFACE = SERVICE
#PATH = "/org/laptop/HelloMesh"

# PyGameActivity: http://www.vrplumber.com/sugar-docs/olpcgames.activity.html
class Quinteti(activity.PyGameActivity):
    """Set up Quin-te-ti activity."""
    game_name = 'run'
    game_title = _('Quin-te-ti')
    game_size = None
