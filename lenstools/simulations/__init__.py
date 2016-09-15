"""

.. module:: simulations 
	:platform: Unix
	:synopsis: This module handles the book keeping of simulation sets map names, cosmological parameters, etc... It also provides an API to interact with Gadget2 snapshots and a prototype ray tracing engine


.. moduleauthor:: Andrea Petri <apetri@phys.columbia.edu>


"""

from .design import Design
from .igs1 import IGS1
from .cfhtemu1 import CFHTemu1,CFHTcov
from .raytracing import Plane,DensityPlane,PotentialPlane,RayTracer
from .nicaea import NicaeaSettings,Nicaea

from .gadget2 import Gadget2Snapshot,Gadget2SnapshotDE,Gadget2SnapshotPipe
from .fastpm import FastPMSnapshot

snapshot_allowed = {

"Gadget2Snapshot" : "Basic handling of Gadget2 snapshots",
"Gadget2SnapshotDE" : "Handle Gadget2 snapshots with Dark Energy information in the header",
"Gadget2SnapshotPipe" : "Use this handler if you plan to combine N-body simulations and plane generation via named pipes",
"FastPMSnapshot" : "Handle N-body snapshots generated by FastPM"

}