from traits.api import HasTraits, Str, Int

class Observer(HasTraits):
    first_name = Str
    last_name = Str
    affiliation = Str

    keck_nights = Int

obs = Observer()
obs.configure_traits()
