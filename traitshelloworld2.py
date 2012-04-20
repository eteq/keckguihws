from __future__ import division
from traits.api import HasTraits, Str, Int, Float, on_trait_change

class Observer(HasTraits):
    first_name = Str
    last_name = Str
    affiliation = Str

    keck_nights = Int
    papers = Int
    keck_efficiency = Float
    
    @on_trait_change('papers,keck_nights')
    def _update_eff(self,obj, name, new):
        self.keck_efficiency = self.papers/self.keck_nights
obs = Observer()
obs.configure_traits()
