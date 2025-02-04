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

#
[ScriptableCullingParameters](Rendering.ScriptableCullingParameters.html).maximumPortalCullingJobs

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

public int maximumPortalCullingJobs;

### Description

This parameter controls how many active jobs contribute to occlusion culling.

The value must be in the range of 1 to 16. The default value is 6. The best
amount of jobs depends on your scene.  
  
When the culling system performs culling in the scene, it can divide the area
on the screen into a grid. Each job handles a cell in the grid.  
  
The higher the job count, the more cells are in the grid and the smaller they
are. If you have more jobs with smaller workloads, Unity performs better by
culling faster.  
  
**Note:** Each job has some overhead, so adding more jobs does not always
increase performance. It takes a little effort to start a
[thread](../Manual/JobSystemOverview#multithreading.html) and join the
results. If your performance is low, try adjusting this value to a lower
number.  
  
Additional resources:
[ScriptableCullingParameters.cullingJobsLowerLimit](Rendering.ScriptableCullingParameters-
cullingJobsLowerLimit.html),
[ScriptableCullingParameters.cullingJobsUpperLimit](Rendering.ScriptableCullingParameters-
cullingJobsUpperLimit.html).

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

