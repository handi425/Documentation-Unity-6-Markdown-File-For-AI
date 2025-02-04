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

#  [Camera](Camera.html).eventMask

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

[Switch to Manual](../Manual/class-Camera.html "Go to Camera Component in the
Manual")

public int eventMask;

### Description

Mask to select which layers can trigger events on the camera.

Just as the camera's `cullingMask` determines if the camera is able to see the
[GameObject](GameObject.html), the event mask determines whether the
[GameObject](GameObject.html) is able to receive mouse events. Only objects
visible by the camera and whose `layerMask` overlaps with the camera's
`eventMask` will be able to receive OnMouseXXX events. Setting this mask to
zero will improve performance and is recommended if you don't use OnMouseXXX
events. See [Layers](../Manual/Layers.html) for more information.  
  
Additional resources:
[MonoBehaviour.OnMouseEnter](MonoBehaviour.OnMouseEnter.html),
[MonoBehaviour.OnMouseExit](MonoBehaviour.OnMouseExit.html),
[MonoBehaviour.OnMouseOver](MonoBehaviour.OnMouseOver.html),
[MonoBehaviour.OnMouseDown](MonoBehaviour.OnMouseDown.html),
[MonoBehaviour.OnMouseOver](MonoBehaviour.OnMouseOver.html),
[MonoBehaviour.OnMouseUp](MonoBehaviour.OnMouseUp.html),
[MonoBehaviour.OnMouseDrag](MonoBehaviour.OnMouseDrag.html),
[MonoBehaviour.OnMouseUpAsButton](MonoBehaviour.OnMouseUpAsButton.html).

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

