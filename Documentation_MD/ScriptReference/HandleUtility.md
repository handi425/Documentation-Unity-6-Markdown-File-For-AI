[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# HandleUtility

class in UnityEditor

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

Helper functions for Scene View style 3D GUI.

These are mainly mathematical functions that assist in converting between the
3D Scene space and the 2D GUI. The functions are used in the construction of
the Unity Editor itself and so using them is a good way to make your own
[Handles](Handles.html) GUIs consistent with Unity's.

### Static Properties

[acceleration](HandleUtility-acceleration.html)| Get standard acceleration for
dragging values (Read Only).  
---|---  
[nearestControl](HandleUtility-nearestControl.html)| The controlID of the
nearest Handle to the mouse cursor.  
[niceMouseDelta](HandleUtility-niceMouseDelta.html)| Get nice mouse delta to
use for dragging a float value (Read Only).  
[niceMouseDeltaZoom](HandleUtility-niceMouseDeltaZoom.html)| Get nice mouse
delta to use for zooming (Read Only).  
  
### Static Methods

[AddControl](HandleUtility.AddControl.html)| Record a distance measurement
from a handle.  
---|---  
[AddDefaultControl](HandleUtility.AddDefaultControl.html)| Add the ID for a
default control. This will be picked if nothing else is.  
[CalcLineTranslation](HandleUtility.CalcLineTranslation.html)| Map a mouse
drag onto a movement along a line in 3D space.  
[ClosestPointToArc](HandleUtility.ClosestPointToArc.html)| Get the point on an
arc (in 3D space) which is closest to the current mouse position.  
[ClosestPointToDisc](HandleUtility.ClosestPointToDisc.html)| Get the point on
an disc (in 3D space) which is closest to the current mouse position.  
[ClosestPointToPolyLine](HandleUtility.ClosestPointToPolyLine.html)| Get the
point on a polyline (in 3D space) which is closest to the current mouse
position.  
[DecodeSelectionId](HandleUtility.DecodeSelectionId.html)| Translates a
Vector4 selectionId value retrieved from GPU into a single integer picking
index.  
[DistancePointBezier](HandleUtility.DistancePointBezier.html)| Calculate
distance between a point and a Bezier curve.  
[DistancePointLine](HandleUtility.DistancePointLine.html)| Calculate distance
between a point and a line.  
[DistancePointToLine](HandleUtility.DistancePointToLine.html)| Distance from a
point p in 2d to a line defined by two points a and b.  
[DistancePointToLineSegment](HandleUtility.DistancePointToLineSegment.html)|
Distance from a point p in 2d to a line segment defined by two points a and b.  
[DistanceToArc](HandleUtility.DistanceToArc.html)| Returns the distance in
pixels from the mouse pointer to a 3D section of a disc.  
[DistanceToCircle](HandleUtility.DistanceToCircle.html)| Returns the distance
in pixels from the mouse pointer to a camera facing circle.  
[DistanceToCone](HandleUtility.DistanceToCone.html)| Returns the distance in
pixels from the mouse pointer to a cone.  
[DistanceToCube](HandleUtility.DistanceToCube.html)| Returns the distance in
pixels from the mouse pointer to a cube.  
[DistanceToDisc](HandleUtility.DistanceToDisc.html)| Returns the distance in
pixels from the mouse pointer to a 3D disc.  
[DistanceToLine](HandleUtility.DistanceToLine.html)| Returns the distance in
pixels from the mouse pointer to a line.  
[DistanceToPolyLine](HandleUtility.DistanceToPolyLine.html)| Returns the
distance in pixels from the mouse pointer to a polyline.  
[DistanceToRectangle](HandleUtility.DistanceToRectangle.html)| Returns the
distance in pixels from the mouse pointer to a rectangle on screen.  
[EncodeSelectionId](HandleUtility.EncodeSelectionId.html)| Translates a single
integer picking index into a Vector4 selectionId value. The Vector4
selectionId is used to render the picking render textures during picking
rendering.  
[FindNearestVertex](HandleUtility.FindNearestVertex.html)| Returns the nearest
vertex to a guiPoint within a maximum radius of 50 pixels.  
[GetHandleSize](HandleUtility.GetHandleSize.html)| Get world space size of a
manipulator handle at given position.  
[GetOverlappingObjects](HandleUtility.GetOverlappingObjects.html)| Gets an
ordered list of objects that would be picked under the give mouse position.  
[GetPickingIncludeExcludeList](HandleUtility.GetPickingIncludeExcludeList.html)|
Gets the picking PickingIncludeExcludeList for the currently executing
BatchRendererGroup.OnPerformCulling callback.  
[GetSelectionOutlineIncludeExcludeList](HandleUtility.GetSelectionOutlineIncludeExcludeList.html)|
Gets the selection outline PickingIncludeExcludeList for the currently
executing BatchRendererGroup.OnPerformCulling callback.  
[GUIPointToScreenPixelCoordinate](HandleUtility.GUIPointToScreenPixelCoordinate.html)|
Converts a 2D GUI position to screen pixel coordinates.  
[GUIPointToWorldRay](HandleUtility.GUIPointToWorldRay.html)| Convert 2D GUI
position to a world space ray.  
[PickAllObjects](HandleUtility.PickAllObjects.html)| Creates a list of all
GameObjects under the specified position in screen coordinates.  
[PickGameObject](HandleUtility.PickGameObject.html)| Pick game object closest
to specified position.  
[PickRectObjects](HandleUtility.PickRectObjects.html)| Pick GameObjects that
lie within a specified screen rectangle.  
[PlaceObject](HandleUtility.PlaceObject.html)| Casts a ray against the loaded
scenes and returns the nearest intersected point on a collider.  
[PointOnLineParameter](HandleUtility.PointOnLineParameter.html)| Returns the
parameter for the projection of the point on the given line.  
[PopCamera](HandleUtility.PopCamera.html)| Retrieve all camera settings.  
[ProjectPointLine](HandleUtility.ProjectPointLine.html)| Project point onto a
line.  
[PushCamera](HandleUtility.PushCamera.html)| Store all camera settings.  
[RaySnap](HandleUtility.RaySnap.html)| Casts ray against the Scene and reports
whether an object lies in its path.  
[RegisterRenderPickingCallback](HandleUtility.RegisterRenderPickingCallback.html)|
Registers a callback to invoke when Unity renders for picking.  
[Repaint](HandleUtility.Repaint.html)| Repaint the current view.  
[UnregisterRenderPickingCallback](HandleUtility.UnregisterRenderPickingCallback.html)|
Unregisters the callback that was previously registered for custom picking
rendering.The method throws InvalidOperationException if you try to call it
inside render picking callbacks.  
[WorldPointToSizedRect](HandleUtility.WorldPointToSizedRect.html)| Calculate a
rectangle to display a 2D GUI element near a projected point in 3D space.  
[WorldToGUIPoint](HandleUtility.WorldToGUIPoint.html)| Convert a world space
point to a 2D GUI position.  
[WorldToGUIPointWithDepth](HandleUtility.WorldToGUIPointWithDepth.html)|
Convert a world space point to a 2D GUI position.  
  
### Events

[getAuthoringObjectForEntity](HandleUtility-getAuthoringObjectForEntity.html)|
The user-defined callback that Unity uses to retrieve the Unity Object
associated with a DOTS Entity.  
---|---  
[getEntitiesForAuthoringObject](HandleUtility-
getEntitiesForAuthoringObject.html)| The user-defined callback that Unity uses
to retrieve the DOTS Entity IDs associated with a Unity Object.  
[pickGameObjectCustomPasses](HandleUtility-pickGameObjectCustomPasses.html)|
Subscribe to this event to add additional picking objects to the
HandleUtility.PickGameObject method.  
[placeObjectCustomPasses](HandleUtility-placeObjectCustomPasses.html)|
Subscribe to this event to handle object placement in the SceneView.  
  
### Delegates

[PickGameObjectCallback](HandleUtility.PickGameObjectCallback.html)| This is
the method definition for pickGameObjectCustomPasses.  
---|---  
[PlaceObjectDelegate](HandleUtility.PlaceObjectDelegate.html)| This is the
method definition for placeObjectCustomPasses.  
[RenderPickingCallback](HandleUtility.RenderPickingCallback.html)| The
delegate type to use with RegisterRenderPickingCallback and
UnregisterRenderPickingCallback.  
[ResolvePickingCallback](HandleUtility.ResolvePickingCallback.html)| The
delegate type to return from RenderPickingCallback through the
RenderPickingResult.resolver member.  
[ResolvePickingWithWorldPositionCallback](HandleUtility.ResolvePickingWithWorldPositionCallback.html)|
The delegate type to return from RenderPickingCallback through the
RenderPickingResult.resolverWithWorldPos member, with the additional world
space position and depth information of where the click occurred.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

