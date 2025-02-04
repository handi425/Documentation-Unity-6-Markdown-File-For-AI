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

#  [ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html).CopyTo

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

public int CopyTo(ProfilerRecorderSample* dest, int destSize, bool reset);

### Parameters

dest | Pointer to the destination samples array.  
---|---  
destSize | Destination samples array size.  
reset | Reset ProfilerRecorder.  
  
### Returns

**int** Returns the count of the copied elements.

### Description

Copies collected samples to the destination array.

    
    
    using Unity.Profiling;  
      
    public class ExampleScript
    {
        static double GetRecorderFrameAverage([ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html) recorder)
        {
            var samplesCount = recorder.Capacity;
            if (samplesCount == 0)
                return 0;  
      
            double r = 0;
            unsafe
            {
                var samples = stackalloc [ProfilerRecorderSample](Unity.Profiling.ProfilerRecorderSample.html)[samplesCount];
                recorder.CopyTo(samples, samplesCount);
                for (var i = 0; i < samplesCount; ++i)
                    r += samples[i].Value;
                r /= samplesCount;
            }  
      
            return r;
        }
    }
    

* * *

## Declaration

public void CopyTo(List<ProfilerRecorderSample> outSamples, bool reset);

### Parameters

outSamples | Destination list.  
---|---  
reset | Reset ProfilerRecorder.  
  
### Description

Copies all collected samples to the destination list.

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

