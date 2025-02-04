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

#
[CapsuleBoundsHandle](IMGUI.Controls.CapsuleBoundsHandle.html).OnHandleChanged

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

## Declaration

protected [Bounds](Bounds.html)
OnHandleChanged([IMGUI.Controls.PrimitiveBoundsHandle.HandleDirection](IMGUI.Controls.PrimitiveBoundsHandle.HandleDirection.html)
handle, [Bounds](Bounds.html) boundsOnClick, [Bounds](Bounds.html) newBounds);

### Parameters

handle | The handle that was dragged.  
---|---  
boundsOnClick | The raw [Bounds](Bounds.html) for this instance's volume at the time the control handle was clicked.  
newBounds | The raw [Bounds](Bounds.html) for this instance's volume based on the updated handle position.  
  
### Returns

**Bounds** The bounds that should be applied to this instance, with any
necessary modifications applied.

### Description

A callback for when a control handle was dragged in the Scene.

This method ensures that the radius axes scale uniformly and that the
[height](IMGUI.Controls.CapsuleBoundsHandle-height.html) and
[radius](IMGUI.Controls.CapsuleBoundsHandle-radius.html) parameters cannot
fall outside their acceptable ranges relative to one another.  
  
The height control handles cannot be made smaller than the diameter. Enlarging
the diameter handles automatically increases the height if needed. The height
value at the time the control was clicked is preferred until the user releases
the control handle.

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

