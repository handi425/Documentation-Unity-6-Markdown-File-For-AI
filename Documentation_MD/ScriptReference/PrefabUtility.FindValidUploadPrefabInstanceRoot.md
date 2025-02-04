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

#  [PrefabUtility](PrefabUtility.html).FindValidUploadPrefabInstanceRoot

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

**Obsolete** FindValidUploadPrefabInstanceRoot is deprecated, please use
GetOutermostPrefabInstanceRoot instead.

## Declaration

public static [GameObject](GameObject.html)
FindValidUploadPrefabInstanceRoot([GameObject](GameObject.html) target);

### Parameters

target | GameObject to process.  
---|---  
  
### Returns

**GameObject** Return the root game object of the Prefab Asset.

### Description

Returns the root GameObject of the Prefab instance if that root Prefab
instance is a parent of the Prefab.

A Prefab internally consists of a Prefab object and the list of objects used
for the Prefab. The Prefab object has a reference to the root GameObject.
Also, if the Prefab is an instance, it contains a reference to the Prefab
Asset it was created from and a list of the overrides (if any) on the
instance.  
  
This works in the same way as
PrefabUtility.FindRootGameObjectWithSameParentPrefab but it will return the
root GameObject of the Prefab Asset. This is useful if you have a disconnected
Prefab instance object and you want to know the root game object of the Prefab
Asset which it used to be connected to.

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

