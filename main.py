import Rhino
import scriptcontext
 
def CurveBoundingBox():
    # Select a curve object
    rc, rhobject = Rhino.Input.RhinoGet.GetOneObject("Select curve", False, Rhino.DocObjects.ObjectType.Curve)
    if rc!=Rhino.Commands.Result.Success: return
 
    # Validate selection
    curve = rhobject.Curve()
    if not curve: return
 
    curve = rg.Distance(pt1, pt2)
 
    # Compute the tight bounding box of the curve in world coordinates
    bbox = curve.GetBoundingBox(True)
    if not bbox.IsValid: return
 
    # Print the min and max box coordinates in world coordinates
    print "World min:", bbox.Min
    print "World max:", bbox.Max
 
     
    Rhino.Geometry.Plane plane;
    if( !base_curve.TryGetPlane(out plane) )
      return Rhino.Commands.Result.Cancel;

    # Compute the tight bounding box of the curve based on the
    # active view's construction plane
    bbox = curve.GetBoundingBox(plane)
 
    # Print the min and max box coordinates in cplane coordinates
    print "CPlane min:", bbox.Min
    print "CPlane max:", bbox.Max
 
if __name__=="__main__":
    CurveBoundingBox()




    Yo!  123