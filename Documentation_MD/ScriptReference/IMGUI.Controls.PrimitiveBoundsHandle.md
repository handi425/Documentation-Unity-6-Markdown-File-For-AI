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

# PrimitiveBoundsHandle

class in UnityEditor.IMGUI.Controls

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

Base class for a compound handle to edit a bounding volume in the Scene view.

This class allows you to display a shape with up to six control handles for
simultaneously editing the size and center of a bounding volume. Dragging on
any one control handle will expand the volume along the control handle's axis.
All classes that inherit from this class also gain the following modifier keys
while a control handle is being dragged:  
  
• **Alt** : Pin the [center](IMGUI.Controls.PrimitiveBoundsHandle-center.html)
of the volume to its location at the time the control handle was clicked and
grow the size in both directions along the control handle's axis of movement.  
• **Shift** : Uniformly scale the volume along all enabled
[axes](IMGUI.Controls.PrimitiveBoundsHandle-axes.html) in proportion to its
size at the time the control handle was clicked.  
  
The handle rendered by this class's
[DrawHandle](IMGUI.Controls.PrimitiveBoundsHandle.DrawHandle.html) method is
affected by global state in the [Handles](Handles.html) class, such as
[Handles.matrix](Handles-matrix.html) and [Handles.color](Handles-color.html).  
  
Additional resources: [Editor.OnSceneGUI](Editor.OnSceneGUI.html),
[Handles.SetCamera](Handles.SetCamera.html).

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
  
### Constructors

[PrimitiveBoundsHandle](IMGUI.Controls.PrimitiveBoundsHandle-ctor.html)|
Create a new instance of the PrimitiveBoundsHandle class.  
---|---  
  
### Public Methods

[DrawHandle](IMGUI.Controls.PrimitiveBoundsHandle.DrawHandle.html)| A function
to display this instance in the current handle camera using its current
configuration.  
---|---  
[SetColor](IMGUI.Controls.PrimitiveBoundsHandle.SetColor.html)| Sets
handleColor and wireframeColor to the same value.  
  
### Protected Methods

[DrawWireframe](IMGUI.Controls.PrimitiveBoundsHandle.DrawWireframe.html)| Draw
a wireframe shape for this instance. Subclasses must implement this method.  
---|---  
[GetSize](IMGUI.Controls.PrimitiveBoundsHandle.GetSize.html)| Gets the current
size of the bounding volume for this instance.  
[IsAxisEnabled](IMGUI.Controls.PrimitiveBoundsHandle.IsAxisEnabled.html)| Gets
a value indicating whether the specified axis is enabled for the current
instance.  
[OnHandleChanged](IMGUI.Controls.PrimitiveBoundsHandle.OnHandleChanged.html)|
A callback for when a control handle was dragged in the Scene.  
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

