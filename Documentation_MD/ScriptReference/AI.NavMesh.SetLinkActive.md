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

#  [NavMesh](AI.NavMesh.html).SetLinkActive

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

public static void
SetLinkActive([AI.NavMeshLinkInstance](AI.NavMeshLinkInstance.html) handle,
bool value);

### Parameters

handle | The link instance whose active state to modify.  
---|---  
value | Whether agents can plan paths through, and traverse, the link. When the value is true, agents can plan paths through, and traverse, the link. Otherwise, no paths can use the link instance.  
  
### Description

Activates or deactivates the link instance. An active link instance can be
traversed by agents and used to plan paths, but a deactivated link cannot.

This method changes the state of the link instance immediately. Any path that
you [calculate](AI.NavMesh.CalculatePath.html) afterwards takes into account
the new state of the link. When you disable the link instance any paths that
have already been calculated through it get a [status](AI.NavMeshPath-
status.html) value of [invalid](AI.NavMeshPathStatus.PathInvalid.html).  
You can call this method at any time to deactivate the link and prevent agents
from moving through a section of the game level, for example through a door
that connects two rooms. Conversely, you can activate the link and allow the
agents to move between the respective game level sections.  
Deactivated links remain connected to the NavMesh surfaces and they do not
need to find the connection points again when they are reactivated.  
Any link instance created with the [AddLink](AI.NavMesh.AddLink.html) method
is active by default.  
  
This method is available as of 2023.2.  
  
Additional resources: [IsLinkActive](AI.NavMesh.IsLinkActive.html).

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

