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

# Handles

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

Custom 3D GUI controls and drawing in the Scene view.

Handles are the 3D controls that Unity uses to manipulate items in the Scene
view. There are a number of built-in Handle GUIs, such as the familiar tools
to position, scale and rotate an object via the Transform component. However,
it is also possible to define your own Handle GUIs to use with custom
component editors. Such GUIs can be a very useful way to edit procedurally-
generated Scene content, "invisible" items and groups of related objects, such
as waypoints and location markers.  
  
You can also supplement the 3D Handle GUI in the Scene with 2D buttons and
other controls overlaid on the Scene view. This is done by enclosing standard
Unity GUI calls in a [Handles.BeginGUI](Handles.BeginGUI.html) and
[Handles.EndGUI](Handles.EndGUI.html) pair within the
[Editor.OnSceneGUI](Editor.OnSceneGUI.html) function. You can use
[HandleUtility.GUIPointToWorldRay](HandleUtility.GUIPointToWorldRay.html) and
[HandleUtility.WorldToGUIPoint](HandleUtility.WorldToGUIPoint.html) to convert
coordinates between 2D GUI and 3D world coordinates.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public float value = 7.0f;
    }  
      
    // A tiny custom editor for ExampleScript component
    [[CustomEditor](CustomEditor.html)(typeof(ExampleScript))]
    public class ExampleEditor : [Editor](Editor.html)
    {
        // Custom in-scene UI for when ExampleScript
        // component is selected.
        public void OnSceneGUI()
        {
            var t = target as ExampleScript;
            var tr = t.transform;
            var pos = tr.position;
            // display an orange disc where the object is
            var color = new [Color](Color.html)(1, 0.8f, 0.4f, 1);
            [Handles.color](Handles-color.html) = color;
            [Handles.DrawWireDisc](Handles.DrawWireDisc.html)(pos, tr.up, 1.0f);
            // display object "value" in scene
            [GUI.color](GUI-color.html) = color;
            [Handles.Label](Handles.Label.html)(pos, t.value.ToString("F1"));
        }
    }
    

![](../StaticFiles/ScriptRefImages/HandlesExample.png).

### Static Properties

[centerColor](Handles-centerColor.html)| Color to use for handles that
represent the center of something.  
---|---  
[color](Handles-color.html)| Sets the color of handles. Color is a persistent
state and affects any handles drawn after it is set. Use DrawingScope to set
the color for a block of handles without affecting the color of other handles.  
[elementColor](Handles-elementColor.html)| The default color of objects in an
Edit Mode.  
[elementPreselectionColor](Handles-elementPreselectionColor.html)| Color to
use to highlight an unselected object currently under the mouse pointer in a
custom Edit Mode.  
[elementSelectionColor](Handles-elementSelectionColor.html)| The color of
selected objects in a Edit Mode.  
[inverseMatrix](Handles-inverseMatrix.html)| The inverse of the matrix for all
handle operations.  
[lighting](Handles-lighting.html)| Are handles lit?  
[lineThickness](Handles-lineThickness.html)| Retrieves the user preference
setting that controls the thickness of tool handle lines. (Read Only)  
[matrix](Handles-matrix.html)| Matrix for all handle operations. This is used
by functions in HandleUtility and Handles to transform controls.  
[preselectionColor](Handles-preselectionColor.html)| Color to use to highlight
an unselected handle currently under the mouse pointer.  
[secondaryColor](Handles-secondaryColor.html)| Soft color to use for for
general things.  
[selectedColor](Handles-selectedColor.html)| Color to use for the currently
active handle.  
[UIColliderHandleColor](Handles.UIColliderHandleColor.html)| Color to use for
the Unity UI's padding visualization.  
[xAxisColor](Handles-xAxisColor.html)| Color to use for handles that
manipulates the X coordinate of something.  
[yAxisColor](Handles-yAxisColor.html)| Color to use for handles that
manipulates the Y coordinate of something.  
[zAxisColor](Handles-zAxisColor.html)| Color to use for handles that
manipulates the Z coordinate of something.  
[zTest](Handles-zTest.html)| zTest of the handles.  
  
### Properties

[currentCamera](Handles-currentCamera.html)| Gets or sets the camera that is
currently rendering.  
---|---  
  
### Static Methods

[ArrowHandleCap](Handles.ArrowHandleCap.html)| Draw an arrow like those used
by the move tool.  
---|---  
[BeginGUI](Handles.BeginGUI.html)| Begin a 2D GUI block inside the 3D handle
GUI.  
[Button](Handles.Button.html)| Make a 3D Button.  
[CircleHandleCap](Handles.CircleHandleCap.html)| Draw a circle handle. Pass
this into handle functions.  
[ClearCamera](Handles.ClearCamera.html)| Clears the camera.  
[ConeHandleCap](Handles.ConeHandleCap.html)| Draw a cone handle. Pass this
into handle functions.  
[CubeHandleCap](Handles.CubeHandleCap.html)| Draw a cube handle. Pass this
into handle functions.  
[CylinderHandleCap](Handles.CylinderHandleCap.html)| Draw a cylinder handle.
Pass this into handle functions.  
[Disc](Handles.Disc.html)| Make a 3D disc that can be dragged with the mouse.  
[DotHandleCap](Handles.DotHandleCap.html)| Draw a dot handle. Pass this into
handle functions.  
[DrawAAConvexPolygon](Handles.DrawAAConvexPolygon.html)| Draw anti-aliased
convex polygon specified with point array.  
[DrawAAPolyLine](Handles.DrawAAPolyLine.html)| Draw anti-aliased line
specified with point array and width.  
[DrawBezier](Handles.DrawBezier.html)| Draw textured bezier line through start
and end points with the given tangents.  
[DrawCamera](Handles.DrawCamera.html)| Draws a camera inside a rectangle.  
[DrawDottedLine](Handles.DrawDottedLine.html)| Draw a dotted line from p1 to
p2.  
[DrawDottedLines](Handles.DrawDottedLines.html)| Draw a list of dotted line
segments.  
[DrawGizmos](Handles.DrawGizmos.html)| Draw the Gizmos for the specified
camera.  
[DrawLine](Handles.DrawLine.html)| Draws a line from p1 to p2.  
[DrawLines](Handles.DrawLines.html)| Draw a list of line segments.  
[DrawOutline](Handles.DrawOutline.html)| Draws an outline around the specified
GameObjects in the Scene View.  
[DrawPolyLine](Handles.DrawPolyLine.html)| Draw a line going through the list
of points.  
[DrawSelectionFrame](Handles.DrawSelectionFrame.html)| Creates a square at a
position and rotation with a specified size.  
[DrawSolidArc](Handles.DrawSolidArc.html)| Draw a circular sector (pie piece)
in 3D space.  
[DrawSolidDisc](Handles.DrawSolidDisc.html)| Draw a solid flat disc in 3D
space.  
[DrawSolidRectangleWithOutline](Handles.DrawSolidRectangleWithOutline.html)|
Draw a solid outlined rectangle in 3D space.  
[DrawTexture3DSDF](Handles.DrawTexture3DSDF.html)| Draws a 3D texture using
Signed Distance Field rendering mode in 3D space.  
[DrawTexture3DSlice](Handles.DrawTexture3DSlice.html)| Draws a 3D texture
using Slice rendering mode in 3D space.  
[DrawTexture3DVolume](Handles.DrawTexture3DVolume.html)| Draws a 3D texture
using Volume rendering mode in 3D space.  
[DrawWireArc](Handles.DrawWireArc.html)| Draws a circular arc in 3D space.  
[DrawWireCube](Handles.DrawWireCube.html)| Draw a wireframe box with center
and size.  
[DrawWireDisc](Handles.DrawWireDisc.html)| Draws the outline of a flat disc in
3D space.  
[EndGUI](Handles.EndGUI.html)| End a 2D GUI block and get back to the 3D
handle GUI.  
[FreeMoveHandle](Handles.FreeMoveHandle.html)| Make an unconstrained movement
handle.  
[FreeRotateHandle](Handles.FreeRotateHandle.html)| Make an unconstrained
rotation handle.  
[GetMainGameViewSize](Handles.GetMainGameViewSize.html)| Get the width and
height of the main game view.  
[Label](Handles.Label.html)| Creates a text label for a handle that is
positioned in 3D space.  
[MakeBezierPoints](Handles.MakeBezierPoints.html)| Retuns an array of points
to representing the bezier curve.  
[PositionHandle](Handles.PositionHandle.html)| Make a position handle.  
[RadiusHandle](Handles.RadiusHandle.html)| Make a Scene view radius handle.  
[RectangleHandleCap](Handles.RectangleHandleCap.html)| Draw a rectangle
handle. Pass this into handle functions.  
[RotationHandle](Handles.RotationHandle.html)| Make a Scene view rotation
handle.  
[ScaleHandle](Handles.ScaleHandle.html)| Make a Scene view scale handle.  
[ScaleSlider](Handles.ScaleSlider.html)| Make a directional scale slider.  
[ScaleValueHandle](Handles.ScaleValueHandle.html)| Make a 3D handle that
scales a single float.  
[SetCamera](Handles.SetCamera.html)| Set the current camera so all Handles and
Gizmos are draw with its settings.  
[ShouldRenderGizmos](Handles.ShouldRenderGizmos.html)| Determines whether or
not to draw Gizmos.  
[Slider](Handles.Slider.html)| Make a 3D slider that moves along one axis.  
[Slider2D](Handles.Slider2D.html)| Make a 3D slider that moves along a plane
defined by two axes.  
[SnapToGrid](Handles.SnapToGrid.html)| Rounds each Transform.position or
Vector3 to the closest multiple of EditorSnapSettings.gridSize.  
[SnapValue](Handles.SnapValue.html)| Rounds value to the closest multiple of
snap if snapping is active. Note that snap can only be positive.  
[SphereHandleCap](Handles.SphereHandleCap.html)| Draw a sphere handle. Pass
this into handle functions.  
[TransformHandle](Handles.TransformHandle.html)| Creates a transform handle.  
  
### Delegates

[CapFunction](Handles.CapFunction.html)| The function to use for drawing the
handle e.g. Handles.RectangleCap.  
---|---  
[SizeFunction](Handles.SizeFunction.html)| A delegate type for getting a
handle's size based on its current position.  
  
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

