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

# NavMeshLinkData

struct in UnityEngine.AI

/

Implemented in:[UnityEngine.AIModule](UnityEngine.AIModule.html)

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

### Description

Used for runtime manipulation of links connecting polygons of the NavMesh.

A typical use case is to connect different navigation meshes. Use the
[NavMesh.AddLink](AI.NavMesh.AddLink.html) method to instantiate a link with
these properties in the navigation system. The [NavMesh
Link](https://docs.unity3d.com/Packages/com.unity.ai.navigation@2.0/manual/NavMeshLink.html)
component creates its runtime data in this way.

### Properties

[agentTypeID](AI.NavMeshLinkData-agentTypeID.html)| Specifies which agent type
this link is available for.  
---|---  
[area](AI.NavMeshLinkData-area.html)| Area type of the link.  
[bidirectional](AI.NavMeshLinkData-bidirectional.html)| If true, the link can
be traversed in both directions, otherwise only from start to end position.  
[costModifier](AI.NavMeshLinkData-costModifier.html)| If positive, overrides
the pathfinder cost to traverse the link.  
[endPosition](AI.NavMeshLinkData-endPosition.html)| End position of the link.  
[startPosition](AI.NavMeshLinkData-startPosition.html)| Start position of the
link.  
[width](AI.NavMeshLinkData-width.html)| If positive, the link will be
rectangle aligned along the line from start to end.  
  
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

