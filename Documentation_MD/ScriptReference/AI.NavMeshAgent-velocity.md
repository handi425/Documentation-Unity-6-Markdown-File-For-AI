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

#  [NavMeshAgent](AI.NavMeshAgent.html).velocity

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

public [Vector3](Vector3.html) velocity;

### Description

Access the current velocity of the [NavMeshAgent](AI.NavMeshAgent.html)
component, or set a velocity to control the agent manually.

Reading the variable will return the current velocity of the agent based on
the crowd simulation.  
  
Setting the variable will override the simulation (including: moving towards
destination, collision avoidance, and acceleration control) and command the
NavMesh Agent to move using the specific velocity directly. When the agent is
controlled using a velocity, its movement is still constrained on the NavMesh.  
  
Setting the velocity directly, can be used for implementing player characters,
which are moving on NavMesh and affecting the rest of the simulated crowd. In
addition, setting priority to high (a small value is higher priority), will
make other simulated agents to avoid the player controlled agent even more
eagerly.  
  
It is recommended to set the velocity each frame when controlling the agent
manually, and if releasing the control to the simulation, set the velocity to
zero. If agent’s velocity is set to some value and then stopped updating it,
the simulation will pick up from there and the agent will slowly decelerate
(assuming no destination is set).  
  
Note that reading the velocity will always return value from the simulation.
If you set the value, the effect will show up in the next update. Since the
returned velocity comes from the simulation (including avoidance and collision
handling), it can be different than the one you set.  
  
The velocity is specified in distance units per second (same as physics), and
represented in global coordinate system.

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

