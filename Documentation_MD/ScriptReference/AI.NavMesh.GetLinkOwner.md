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

#  [NavMesh](AI.NavMesh.html).GetLinkOwner

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

public static Object
GetLinkOwner([AI.NavMeshLinkInstance](AI.NavMeshLinkInstance.html) handle);

### Parameters

handle | The identifier of the link instance whose owner needs to be retrieved.  
---|---  
  
### Returns

**Object** The object that was passed into
[SetLinkOwner](AI.NavMesh.SetLinkOwner.html) for the specified link instance.  
Returns `null` when no owner object has been assigned or when the link
instance is not valid.

### Description

Gets the object, if any, that is associated with the link instance.

Use this method to obtain a reference to the component that created the link,
or more generally, to any object that contains useful information about this
specific link that is active in the navigation system. We refer to that object
as the "owner". The owner is null for any new link instance created with
[AddLink](AI.NavMesh.AddLink.html). Therefore you need to first call
[SetLinkOwner](AI.NavMesh.SetLinkOwner.html) in order to retrieve the same
object later. This "owner" is also referenced by the
[OffMeshLinkData.owner](AI.OffMeshLinkData-owner.html) property when you query
for the next link on a NavMesh agent's path.  
When the link instance is [removed](NavMeshLinkInstance.Remove.html) the owner
property returns null once again.  
  
Additional resources: [OffMeshLinkData.owner](AI.OffMeshLinkData-owner.html).

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

