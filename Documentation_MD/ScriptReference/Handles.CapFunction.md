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

#  [Handles](Handles.html).CapFunction

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

public delegate void CapFunction(int controlID, [Vector3](Vector3.html)
position, [Quaternion](Quaternion.html) rotation, float size,
[EventType](EventType.html) eventType);

### Parameters

controlID | The control ID for the handle.  
---|---  
position | The position of the handle in the space of [Handles.matrix](Handles-matrix.html).  
rotation | The rotation of the handle in the space of [Handles.matrix](Handles-matrix.html).  
size | The size of the handle in world-space units.  
eventType | Event type for the handle to act upon. By design it handles [EventType.Layout](EventType.Layout.html) and [EventType.Repaint](EventType.Repaint.html) events.  
  
### Description

The function to use for drawing the handle e.g. Handles.RectangleCap.

Custom CapFunction has two responsibilities:

  1. For [EventType.Layout](EventType.Layout.html) event, call [HandleUtility.AddControl](HandleUtility.AddControl.html) to inform Unity about the distance of the handle from mouse position.
  2. For [EventType.Repaint](EventType.Repaint.html) event, render the actual handle.

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

