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

#  [PhysicsJobOptions2D](PhysicsJobOptions2D.html).islandSolverCostThreshold

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

public int islandSolverCostThreshold;

### Description

The minimum threshold cost of all bodies, contacts and joints in an island
during discrete island solving.

The discrete island solver generates "islands", which are bodies connected
together by contacts. These contact islands are solved together as they all
potentially affect each other when moving. The first stage is generating the
contact islands. When a contact island has been created, it can then be
evaluated in a job. However, executing lots of small contact islands each as a
job can lead to lots of jobs, and can be very inefficient. To reduce the
number of contact islands processed by each job, each job island has a cost
associated with it. A job island's cost is automatically calculated by summing
the cost of the island's bodies, contacts and joints. Each of these has its
own scaling property,
[islandSolverBodyCostScale](PhysicsJobOptions2D-islandSolverBodyCostScale.html),
[islandSolverContactCostScale](PhysicsJobOptions2D-islandSolverContactCostScale.html)
and
[islandSolverJointCostScale](PhysicsJobOptions2D-islandSolverJointCostScale.html)
respectively. The island is only processed by a job if the total cost of the
island is above the
[islandSolverCostThreshold](PhysicsJobOptions2D-islandSolverCostThreshold.html).  
  
Increasing the cost threshold will increase the number of islands solved in
each job. Depending on the number and size of contact islands, this allows you
to control the efficiency of discrete island solving.

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

