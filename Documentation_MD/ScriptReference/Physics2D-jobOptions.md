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

#  [Physics2D](Physics2D.html).jobOptions

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

public static [PhysicsJobOptions2D](PhysicsJobOptions2D.html) jobOptions;

### Description

A set of options that control how physics operates when using the job system
to multithread the physics simulation.

Multithreaded physics is currently an experimental feature. As such, many
options are exposed that allow performance configuration that may not be
available when the feature moves out of experimental status.  
  
A physics simulation executes in the following discrete stages:  
  
• Find New Contacts  
• Contact Collision  
• Discrete Solver (Clear Island Flags -> Discrete Island Traversal -> Discrete
Island Solver -> Synchronize Fixtures -> Find New Contacts)  
• Continuous Solver (Clear Island Flags > Continuous Island Traversal ->
Discrete Island Solver -> Synchronize Fixtures -> Find New Contacts)  
• Clear Body Forces  
• Update Trigger Contacts  
  
These stages execute in the order given above. Each stage is run as a job
"task". Each task executes sub job tasks, which are shown in parenthesis
above. When executing a job, physics simulation may process bodies, contacts,
joints, and so on, across multiple job threads. You can task each of these
threads with executing a specific number of items, such as bodies, contacts
and joints. Many of the options provided here allow you to control the minimum
number of items assigned to each job. Raising the minimum can reduce the
number of jobs required. This is because running a lot of jobs, each
processing only a few items, is usually not very efficient. The default
settings provide a decent performance to job balance, however you are free to
experiment.  
  
Additionally, prior to the simulation being run,
[Rigidbody2D](Rigidbody2D.html) interpolation/extrapolation poses are stored
ready for per-frame interpolation/extrapolation. These are also executed using
the job system and are controlled here.

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

