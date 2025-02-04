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

#  [GlobalObjectId](GlobalObjectId.html).targetObjectId

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

public ulong targetObjectId;

### Description

The local file ID of the referenced object.

This is the ID that uniquely identifies each individual object in an asset
file. For objects that are not part of a prefab, this is sufficient to
identify the object. For more information on asset files and meta data, refer
to [ Asset Metadata](../Manual/AssetMetadata.html) in the Manual.  
  
For a GameObject that's part of a prefab, the `targetObjectId` alone is not
sufficient to identify the object because additional instances of the object
are created for every instance of the prefab in the scene. To identify such
objects unambiguously, the ID of the prefab instance they belong to is also
required. For more information, refer to
[GlobalObjectId.targetPrefabId](GlobalObjectId-targetPrefabId.html).  
  
The `targetObjectId` constitutes the `{l}` element in the string
representation of a `GlobalObjectId`, the format of which is:  
  
@@GlobalObjectId_V1-{i}-{a}-{l}-{p  
  
**Note** : Actual local file IDs are signed 64-bit values and can be negative.
But in a `GlobalObjectId`, these values are cast to `targetObjectId`, which is
an unsigned 64-bit value (`ulong`). Therefore, a negative local file ID will
lose its sign when saved to a `GlobalObjectId` and you should not rely on the
value of `targetObjectId`, or the `{l}` element from the string representation
of a GlobalObjectID, to find an object.  
  
Additional resources:
[AssetDatabase.TryGetGUIDAndLocalFileIdentifier](AssetDatabase.TryGetGUIDAndLocalFileIdentifier.html)

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

