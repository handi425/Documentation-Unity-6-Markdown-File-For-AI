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

#  [GlobalObjectId](GlobalObjectId.html).targetPrefabId

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

public ulong targetPrefabId;

### Description

The ID of the prefab instance that contains the referenced object.

Adding a new prefab instance to a scene creates a new instance of every object
the prefab contains, including every GameObject. The GameObject inside a
prefab instance doesn't have its own stable local file ID and a single prefab
can be instantiated multiple times in a scene. Therefore, to reliably identify
a GameObject that's part of a prefab requires both the local file ID of the
original version of the GameObject (GameObject.targetObjectId) and the ID of
the particular prefab instance it belongs to (@@targetPrefabId@).  
  
For more information on creating prefab instances, refer to [Creating
Prefabs](../Manual/CreatingPrefabs.html) in the Manual.  
  
The `targetPrefabId` constitutes the `{p}` element in the string
representation of a `GlobalObjectId`, the format of which is:  
  
`GlobalObjectId_V1-{i}-{a}-{l}-{p}`  
  
Additional resources:
[PrefabUtility.IsPartOfAnyPrefab](PrefabUtility.IsPartOfAnyPrefab.html)

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

