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

#  [NavMesh](AI.NavMesh.html).IsLinkOccupied

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

public static bool
IsLinkOccupied([AI.NavMeshLinkInstance](AI.NavMeshLinkInstance.html) handle);

### Parameters

handle | The link instance whose state to query.  
---|---  
  
### Returns

**bool** True if an agent is currently traversing the link, otherwise false.

### Description

Determines whether or not a NavMesh agent is currently using this link.

Use this method to determine if your NavMesh agent can move onto the specified
NavMesh link instance. Only one NavMesh agent can traverse a NavMesh link
instance at any one time, so your agent can't move onto a NavMesh link
instance that is already occupied. A NavMesh link instance is occupied when
any NavMesh agent moves onto the link as part of the path the agent has
calculated to the [destination](AI.NavMeshAgent-destination.html). When the
agent moves off of the link, either automatically or through a call to
[NavMeshAgent.CompleteOffMeshLink](AI.NavMeshAgent.CompleteOffMeshLink.html),
the link instance is no longer occupied.  
  
This method is available as of 2023.2.  
  
Additional resources: [NavMeshAgent.isOnOffMeshLink](AI.NavMeshAgent-
isOnOffMeshLink.html).

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

