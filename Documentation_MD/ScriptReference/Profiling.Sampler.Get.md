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

#  [Sampler](Profiling.Sampler.html).Get

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

public static [Profiling.Sampler](Profiling.Sampler.html) Get(string name);

### Parameters

name | Profiler Sampler name.  
---|---  
  
### Returns

**Sampler** [Sampler](Profiling.Sampler.html) object which represents specific
profiler label.

### Description

Returns [Sampler](Profiling.Sampler.html) object for the specific CPU Profiler
label.

You can use this function to get a Sampler associated with a built-in or
custom label. The _name_ parameter is the same you can see in Hierarchy view
of the [Profiler Window](../Manual/ProfilerCPU.html). If label with the
specified _name_ parameter does not exist or not available in the Player, an
invalid Sampler object will be returned. You can use
[Sampler.isValid](Profiling.Sampler-isValid.html) to verify if Sampler is
valid.

    
    
    using UnityEngine;
    using UnityEngine.Profiling;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        [Sampler](Profiling.Sampler.html) sampler;
        void Start()
        {
            sampler = [Sampler.Get](Profiling.Sampler.Get.html)("BehaviourUpdate");
        }
    }
    

**Get** can be used to obtain any existing Sampler including custom Sampler.
Return value is always Sampler type and can not be casted to CustomSampler.  
  
**Note:** At the moment all built-in counters are available only in the Editor
and Development Players. **Get** in non-Development Players returns invalid
Sampler.  
  
Additional resources: [Sampler](Profiling.Sampler.html),
[Sampler.isValid](Profiling.Sampler-isValid.html), [CPU Usage
Profiler](../Manual/ProfilerCPU.html).

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

