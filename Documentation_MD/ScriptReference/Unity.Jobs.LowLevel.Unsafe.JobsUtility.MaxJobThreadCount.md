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
[JobsUtility](Unity.Jobs.LowLevel.Unsafe.JobsUtility.html).MaxJobThreadCount

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

public static int MaxJobThreadCount;

### Description

The maximum number of job threads that the job system can create.

This maximum is the maximum number of threads that the job can system support.
However, the maximum number of job worker threads that the job system creates
is lower because the job system doesn't create more job worker threads than
logical CPU cores on the target hardware. This value is useful for compile
time constants, however when used for creating buffers it might be larger than
what you need. If you want to allocate a buffer that can be subdivided evenly
between job worker threads, use the runtime constant that
[JobsUtility.ThreadIndexCount](Unity.Jobs.LowLevel.Unsafe.JobsUtility.ThreadIndexCount.html)
returns. SA: Unity.Jobs.LowLevel.Unsafe.JobsUtility.ThreadIndexCount

    
    
    using UnityEngine;  
      
    public class JobWorkerExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            // Sets worker count thread to 1
            [Unity.Jobs.LowLevel.Unsafe.JobsUtility.JobWorkerCount](Unity.Jobs.LowLevel.Unsafe.JobsUtility.JobWorkerCount.html) = 1;
            // Sets worker count thread to 4
            [Unity.Jobs.LowLevel.Unsafe.JobsUtility.JobWorkerCount](Unity.Jobs.LowLevel.Unsafe.JobsUtility.JobWorkerCount.html) = 4;
            // Reads the value of JobWorkerCount and outputs it to the Unity log
            [Debug.Log](Debug.Log.html)("${ [Unity.Jobs.LowLevel.Unsafe.JobsUtility.JobWorkerCount](Unity.Jobs.LowLevel.Unsafe.JobsUtility.JobWorkerCount.html)}");  
      
        }
    }
    

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

