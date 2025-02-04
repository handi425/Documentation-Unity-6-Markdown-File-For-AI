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

# CustomSampler

class in UnityEngine.Profiling

/

Inherits from:[Profiling.Sampler](Profiling.Sampler.html)

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Custom CPU Profiler label used for profiling arbitrary code blocks.

Use CustomSampler to measure execution time of script code blocks. Produced
information is displayed in the [CPU Profiler](../Manual/ProfilerCPU.html) and
can be captured with [Recorder](Profiling.Recorder.html).  
Using CustomSampler is more efficient than using
[Profiler.BeginSample](Profiling.Profiler.BeginSample.html) to profile your
code. This is because CustomSamplers that have been created in advance have
very low [Begin](Profiling.CustomSampler.Begin.html) call overhead compared to
[Profiler.BeginSample](Profiling.Profiler.BeginSample.html).

    
    
    using UnityEngine;
    using UnityEngine.Profiling;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        [CustomSampler](Profiling.CustomSampler.html) sampler;
        void Start()
        {
            sampler = [CustomSampler.Create](Profiling.CustomSampler.Create.html)("MyCustomSampler");
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            sampler.Begin();
            // do something that takes a lot of time
            sampler.End();
        }
    }
    

CustomSampler.Begin is conditionally compiled away using ConditionalAttribute.
Thus it will have zero overhead, when it is deployed in non-Development Build.  
  
Additional resources: [Sampler](Profiling.Sampler.html),
[CustomSampler.Create](Profiling.CustomSampler.Create.html),
[CustomSampler.Begin](Profiling.CustomSampler.Begin.html).

### Public Methods

[Begin](Profiling.CustomSampler.Begin.html)| Begin profiling a piece of code
with a custom label defined by this instance of CustomSampler.  
---|---  
[End](Profiling.CustomSampler.End.html)| End profiling a piece of code with a
custom label.  
  
### Static Methods

[Create](Profiling.CustomSampler.Create.html)| Creates a new CustomSampler for
profiling parts of your code.  
---|---  
  
### Inherited Members

### Properties

[isValid](Profiling.Sampler-isValid.html)| Returns true if Sampler is valid.
(Read Only)  
---|---  
[name](Profiling.Sampler-name.html)| Sampler name. (Read Only)  
  
### Public Methods

[GetRecorder](Profiling.Sampler.GetRecorder.html)| Returns Recorder associated
with the Sampler.  
---|---  
  
### Static Methods

[Get](Profiling.Sampler.Get.html)| Returns Sampler object for the specific CPU
Profiler label.  
---|---  
[GetNames](Profiling.Sampler.GetNames.html)| Returns number and names of all
registered Profiler labels.  
  
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

