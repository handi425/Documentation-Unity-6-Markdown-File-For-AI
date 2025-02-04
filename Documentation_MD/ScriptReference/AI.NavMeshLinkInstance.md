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

# NavMeshLinkInstance

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

Represents a link available for pathfinding.

You obtain a valid object when you call
[NavMesh.AddLink](AI.NavMesh.AddLink.html) to create one specific link in the
navigation system. Conversely, you need to pass it into
[NavMesh.RemoveLink](AI.NavMesh.RemoveLink.html) to remove that instance of
the link from the system. Use this object to check or modify the state of the
link instance by calling the following methods:
[NavMesh.IsLinkValid](AI.NavMesh.IsLinkValid.html),
[NavMesh.IsLinkOccupied](AI.NavMesh.IsLinkOccupied.html),
[NavMesh.IsLinkActive](AI.NavMesh.IsLinkActive.html),
[NavMesh.SetLinkActive](AI.NavMesh.SetLinkActive.html),
[NavMesh.GetLinkOwner](AI.NavMesh.GetLinkOwner.html) and
[NavMesh.SetLinkOwner](AI.NavMesh.SetLinkOwner.html).  
  
Empty objects created when you instantiate this struct do not represent any
link that exists in the navigation system. The
[NavMesh.IsLinkValid](AI.NavMesh.IsLinkValid.html) and
[NavMesh.IsLinkActive](AI.NavMesh.IsLinkActive.html) methods return a value of
`false` for objects created in this manner.  

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

