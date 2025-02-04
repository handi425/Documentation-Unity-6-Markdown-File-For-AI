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

#  [NavMeshLinkInstance](AI.NavMeshLinkInstance.html).owner

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

**Obsolete** owner has been deprecated. Use NavMesh.GetLinkOwner() and
NavMesh.SetLinkOwner() instead. public Object owner;

### Description

Get or set the owning Object.

If the instance is not valid, setting the owner has no effect and getting it
returns null.  
Use this property to reference the component that created the link, or more
generally, any object that contains useful information about this specific
link active in the navigation system. The owner is null for any new link
instance created with [NavMesh.AddLink](AI.NavMesh.AddLink.html). You can, at
any time, assign any Object to this property and retrieve that reference
later.  
When the link instance is [removed](NavMeshLinkInstance.Remove.html) the owner
property returns null once again.  
  
Additional resources: [OffMeshLinkData.owner](AI.OffMeshLinkData-owner.html),
[NavMesh.GetLinkOwner](AI.NavMesh.GetLinkOwner.html),
[NavMesh.SetLinkOwner](AI.NavMesh.SetLinkOwner.html).

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

