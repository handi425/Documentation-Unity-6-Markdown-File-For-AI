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
[GameObjectUtility](GameObjectUtility.html).ModifyMaskIfGameObjectIsHiddenForPrefabModeInContext

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

public static ulong ModifyMaskIfGameObjectIsHiddenForPrefabModeInContext(ulong
sceneCullingMask, [GameObject](GameObject.html) gameObject);

### Parameters

sceneCullingMask | The scene culling mask intended to be used with the custom renderer.  
---|---  
gameObject | The GameObject associated with the custom renderer.  
  
### Returns

**ulong** If the GameObject is hidden for Prefab Mode in Context, a modified
scene culling mask is returned. If it's not hidden, then the input scene
culling mask is returned.

### Description

Use this method if a custom scene culling mask is needed for renderers that
should be shown or hidden in a Scene view when Prefab Mode in Context is
active.

When entering Prefab Mode in Context for a Prefab Asset the Prefab instance in
the Main Stage is hidden. Use this method to ensure that any custom renderers
associated with a given GameObject are hidden in the same Scene views if that
GameObject is part of a hidden Prefab instance.

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

