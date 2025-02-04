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

#  [HandleUtility](HandleUtility.html).PlaceObject

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

public static bool PlaceObject([Vector2](Vector2.html) guiPosition, out
[Vector3](Vector3.html) position, out [Vector3](Vector3.html) normal);

### Parameters

guiPosition | The GUI position in the [SceneView](SceneView.html). You can pass Event.current.mousePosition to this parameter in most cases.  
---|---  
position | Returns the nearest intersected point to a ray cast from the mouse position into the scene.  
normal | Returns the normal of the nearest intersected point to a ray cast from the mouse position into the scene.  
  
### Returns

**bool** Returns true if the raycast intersected something in the scene;
otherwise, false.

### Description

Casts a ray against the loaded scenes and returns the nearest intersected
point on a collider.

Use this method to match the behavior of drag and drop in the
[SceneView](SceneView.html).  
  
[PlaceObject](HandleUtility.PlaceObject.html) also queries any delegates
registered to [placeObjectCustomPasses](HandleUtility-
placeObjectCustomPasses.html) when determining the nearest point.

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

