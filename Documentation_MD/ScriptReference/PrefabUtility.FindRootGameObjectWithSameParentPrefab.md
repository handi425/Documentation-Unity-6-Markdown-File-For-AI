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

**Method group is Obsolete**  

#  [PrefabUtility](PrefabUtility.html).FindRootGameObjectWithSameParentPrefab

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

**Obsolete** FindRootGameObjectWithSameParentPrefab is deprecated, please use
GetOutermostPrefabInstanceRoot instead.

## Declaration

public static [GameObject](GameObject.html)
FindRootGameObjectWithSameParentPrefab([GameObject](GameObject.html) target);

### Parameters

target | The GameObject to use in the search.  
---|---  
  
### Returns

**GameObject** The GameObject at the root of the Prefab.

### Description

Retrieves the topmost GameObject that has the same Prefab parent as `target`.

A Prefab internally consists of a Prefab object and the list of objects used
for the Prefab. The Prefab object has a reference to the root GameObject.
Also, if the Prefab is an instance, it contains a reference to the Prefab
Asset it was created from and a list of the overrides (if any) on the
instance.  
  
This method only returns a valid result when a Prefab instance, or a
GameObject that has been disconnected from a Prefab is used.  
  
The method finds the Transform associated with the supplied target GameObject.
It checks the parents of the Transform tree as long as the Transform was
instantiated from the same Prefab Asset. Once it reaches the Transform that
matches the Transform on the root GameObject of the Prefab Asset, it will stop
and return the GameObject instance.  
  
This method is similar to PrefabUtility.FindPrefabRoot but it also works if
the Prefab instance has been disconnected. This is useful if you have a
disconnected Prefab instance and you want to reconnect it to the Prefab Asset.

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

