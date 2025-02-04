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

#  [PrefabUtility](PrefabUtility.html).GetOutermostPrefabInstanceRoot

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

public static [GameObject](GameObject.html)
GetOutermostPrefabInstanceRoot([Object](Object.html) componentOrGameObject);

### Parameters

componentOrGameObject | The object to check. Must be a component or GameObject.  
---|---  
  
### Returns

**GameObject** The outermost Prefab instance root.

### Description

Retrieves the GameObject that is the root of the outermost Prefab instance the
object is part of.

The method will search up the parents in the Transform hierarchy until it
finds the root of a Prefab instance which is not an applied nested Prefab
inside another Prefab.  
  
If the method finds a Prefab instance root which is an added GameObject to
another Prefab instance, it will return that root, since it it not an applied
nested Prefab root.  
  
The method will return null if the given object is not part of a Prefab
instance. This includes GameObjects or components that have been added and not
applied to a Prefab instance.  
  
![](../StaticFiles/ScriptRefImages/PrefabInstanceRoots.png)  
_Overview of which objects are Prefab instance roots._  
  
In the editor, outermost Prefab instance roots have the Overrides dropdown,
whereas other Prefab instance roots don’t.  
  
Additional resources:
[GetNearestPrefabInstanceRoot](PrefabUtility.GetNearestPrefabInstanceRoot.html).

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

