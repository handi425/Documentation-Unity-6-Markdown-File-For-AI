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

#  [OffMeshLinkData](AI.OffMeshLinkData.html).owner

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

public Object owner;

### Description

Get the object used to create the NavMesh link represented by the data in this
struct.

If the link has been instantiated by a call to
[NavMesh.AddLink](AI.NavMesh.AddLink.html) then this property returns the
object that might have been associated to that instance with a call to
[NavMesh.SetLinkOwner](AI.NavMesh.SetLinkOwner.html). If that link instance
has no owner assigned to it then this property returns null.  
If the link was instantiated by an OffMeshLink component then the owner
returns a reference to that component.  
To effectively use this property in your scripts you need to determine the
exact type of the returned object. To do that cast the object to the types
that you use in your project to create NavMesh links.  
For automatically-generated Jump or Drop links, this property returns null.  
  
Additional resources: [NavMesh.SetLinkOwner](AI.NavMesh.SetLinkOwner.html).

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

