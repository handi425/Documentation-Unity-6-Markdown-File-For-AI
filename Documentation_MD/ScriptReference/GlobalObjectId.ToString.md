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

#  [GlobalObjectId](GlobalObjectId.html).ToString

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

public string ToString();

### Returns

**string** The string representation of the `GlobalObjectId`.

### Description

Obtains the string representation of the unique object identifier.

The string representation of a `GlobalObjectId` can be serialized, then used
at a later time to re-initialize a `GlobalObjectID` struct.  
  
The format of the string representation of the ID is
`GlobalObjectId_V1-{i}-{a}-{l}-{p}`, where:

  * `{i}` is the identifier type represented by an integer (0 = Null, 1 = Imported Asset, 2 = Scene Object, 3 = Source Asset).
  * `{a}` is the asset GUID. This is a globally unique identifier that Unity assigns to every newly discovered asset. For more information, refer to [Asset Metadata](../Manual/AssetMetadata.html) in the Manual.
  * `{l}` is the local file ID of the object. For objects inside a prefab instance, this ID is the local file ID of the original source object that is part of the prefab. For more information, refer to [GlobalObjectId.targetObjectId](GlobalObjectId-targetObjectId.html).
  * `{p}` is the local file ID of the prefab instance of the object. If the object isn't part of a prefab instance, then `{p}` is `0`.

**Note** : Actual local file IDs are signed 64-bit values and can be negative.
But in a `GlobalObjectId`, these values are cast to
[GlobalObjectId.targetObjectId](GlobalObjectId-targetObjectId.html), which is
an unsigned 64-bit value (`ulong`). Therefore, a negative local file ID will
lose its sign when saved to a `GlobalObjectId` and you should not rely on the
value of `targetObjectId`, or the `{l}` element from the string representation
of a GlobalObjectID, to find an object.  
  
Additional resources: [GlobalObjectId.TryParse](GlobalObjectId.TryParse.html)

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

