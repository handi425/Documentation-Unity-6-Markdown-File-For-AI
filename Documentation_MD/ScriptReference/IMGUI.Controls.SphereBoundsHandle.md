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

# SphereBoundsHandle

class in UnityEditor.IMGUI.Controls

/

Inherits
from:[IMGUI.Controls.PrimitiveBoundsHandle](IMGUI.Controls.PrimitiveBoundsHandle.html)

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

A compound handle to edit a sphere-shaped bounding volume in the Scene view.

A sphere volume is defined by only a
[radius](IMGUI.Controls.SphereBoundsHandle-radius.html) parameter, and so
dragging a handle will always scale the volume uniformly.  
  
![](../StaticFiles/ScriptRefImages/SphereBoundsHandle.png) _2D and 3D
SphereBoundsHandle in the Scene View._  
  
Additional resources:
[PrimitiveBoundsHandle](IMGUI.Controls.PrimitiveBoundsHandle.html).

### Properties

[radius](IMGUI.Controls.SphereBoundsHandle-radius.html)| Returns or specifies
the radius of the sphere bounding volume.  
---|---  
  
### Constructors

[SphereBoundsHandle](IMGUI.Controls.SphereBoundsHandle-ctor.html)| Create a
new instance of the SphereBoundsHandle class.  
---|---  
  
### Protected Methods

[DrawWireframe](IMGUI.Controls.SphereBoundsHandle.DrawWireframe.html)| Draw a
wireframe sphere for this instance.  
---|---  
[OnHandleChanged](IMGUI.Controls.SphereBoundsHandle.OnHandleChanged.html)| A
callback for when a control handle was dragged in the Scene.  
  
### Inherited Members

### Properties

[axes](IMGUI.Controls.PrimitiveBoundsHandle-axes.html)| Flags specifying which
axes should display control handles.  
---|---  
[center](IMGUI.Controls.PrimitiveBoundsHandle-center.html)| Returns or
specifies the center of the bounding volume for the handle.  
[handleColor](IMGUI.Controls.PrimitiveBoundsHandle-handleColor.html)| Returns
or specifies the color of the control handles.  
[midpointHandleDrawFunction](IMGUI.Controls.PrimitiveBoundsHandle-
midpointHandleDrawFunction.html)| An optional CapFunction to use when
displaying the control handles. Defaults to Handles.DotHandleCap if no value
is specified.  
[midpointHandleSizeFunction](IMGUI.Controls.PrimitiveBoundsHandle-
midpointHandleSizeFunction.html)| The SizeFunction to specify how large the
midpoint control handles should be.  
[wireframeColor](IMGUI.Controls.PrimitiveBoundsHandle-wireframeColor.html)|
Returns or specifies the color of the wireframe shape.  
  
### Public Methods

[DrawHandle](IMGUI.Controls.PrimitiveBoundsHandle.DrawHandle.html)| A function
to display this instance in the current handle camera using its current
configuration.  
---|---  
[SetColor](IMGUI.Controls.PrimitiveBoundsHandle.SetColor.html)| Sets
handleColor and wireframeColor to the same value.  
  
### Protected Methods

[GetSize](IMGUI.Controls.PrimitiveBoundsHandle.GetSize.html)| Gets the current
size of the bounding volume for this instance.  
---|---  
[IsAxisEnabled](IMGUI.Controls.PrimitiveBoundsHandle.IsAxisEnabled.html)| Gets
a value indicating whether the specified axis is enabled for the current
instance.  
[SetSize](IMGUI.Controls.PrimitiveBoundsHandle.SetSize.html)| Sets the current
size of the bounding volume for this instance.  
  
### Static Methods

[DefaultMidpointHandleSizeFunction](IMGUI.Controls.PrimitiveBoundsHandle.DefaultMidpointHandleSizeFunction.html)|
A SizeFunction that returns a fixed screen-space size.  
---|---  
  
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

